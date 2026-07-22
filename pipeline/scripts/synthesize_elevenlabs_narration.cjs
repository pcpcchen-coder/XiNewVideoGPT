#!/usr/bin/env node
"use strict";

const crypto = require("node:crypto");
const fs = require("node:fs");
const https = require("node:https");
const os = require("node:os");
const path = require("node:path");
const { spawnSync } = require("node:child_process");

const DEFAULT_VOICE_ID = "fQj4gJSexpu8RDE2Ii5m";
const DEFAULT_MODEL_ID = "eleven_multilingual_v2";

function run(command, args) {
  const result = spawnSync(command, args, { encoding: "utf8" });
  if (result.status !== 0) {
    throw new Error(`${command} failed:\n${result.stderr || result.stdout}`);
  }
  return result.stdout.trim();
}

function duration(file) {
  return Number(run("ffprobe", [
    "-v", "error", "-show_entries", "format=duration",
    "-of", "default=nw=1:nk=1", file,
  ]));
}

function sha256(file) {
  return crypto.createHash("sha256").update(fs.readFileSync(file)).digest("hex");
}

function srtTime(seconds) {
  const ms = Math.max(0, Math.round(seconds * 1000));
  const h = Math.floor(ms / 3600000);
  const m = Math.floor((ms % 3600000) / 60000);
  const s = Math.floor((ms % 60000) / 1000);
  const r = ms % 1000;
  return `${String(h).padStart(2, "0")}:${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")},${String(r).padStart(3, "0")}`;
}

function sentenceText(sentence) {
  return sentence.tts || sentence.text;
}

function requestAudio({ apiKey, voiceId, modelId, text, previousText, nextText }) {
  return new Promise((resolve, reject) => {
    const payload = {
      text,
      model_id: modelId,
      voice_settings: {
        stability: 0.7,
        similarity_boost: 0.82,
        style: 0,
        use_speaker_boost: true,
        speed: 0.95,
      },
    };
    if (previousText) payload.previous_text = previousText;
    if (nextText) payload.next_text = nextText;

    const body = JSON.stringify(payload);
    const req = https.request({
      hostname: "api.elevenlabs.io",
      path: `/v1/text-to-speech/${voiceId}`,
      method: "POST",
      headers: {
        Accept: "audio/mpeg",
        "Content-Type": "application/json",
        "Content-Length": Buffer.byteLength(body),
        "xi-api-key": apiKey,
      },
    }, (res) => {
      const chunks = [];
      res.on("data", (chunk) => chunks.push(chunk));
      res.on("end", () => {
        const data = Buffer.concat(chunks);
        if (res.statusCode !== 200) {
          reject(new Error(`ElevenLabs HTTP ${res.statusCode}: ${data.toString("utf8").slice(0, 500)}`));
          return;
        }
        resolve(data);
      });
    });
    req.on("error", reject);
    req.setTimeout(120000, () => req.destroy(new Error("ElevenLabs request timed out after 120s")));
    req.write(body);
    req.end();
  });
}

function flatten(narration) {
  const items = [];
  for (const scene of narration) {
    for (const sentence of scene.sentences) {
      items.push({ scene, sentence, text: sentenceText(sentence) });
    }
  }
  return items;
}

async function main() {
  const epArg = process.argv[2];
  if (!epArg) throw new Error("Usage: synthesize_elevenlabs_narration.cjs <episode-path>");

  const apiKey = process.env.ELEVENLABS_API_KEY;
  if (!apiKey) throw new Error("ELEVENLABS_API_KEY is required");

  const root = path.resolve(__dirname, "../..");
  const ep = path.resolve(root, epArg);
  const manifestPath = path.join(ep, "production/manifest.json");
  const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
  const narration = JSON.parse(fs.readFileSync(path.join(ep, "production/narration.json"), "utf8"));
  const audioDir = path.join(ep, "audio");
  const subtitleDir = path.join(ep, "subtitles");
  fs.mkdirSync(audioDir, { recursive: true });
  fs.mkdirSync(subtitleDir, { recursive: true });

  const voiceId = process.env.ELEVENLABS_VOICE_ID || manifest.tts.voiceId || DEFAULT_VOICE_ID;
  const modelId = process.env.ELEVENLABS_MODEL_ID || manifest.tts.model || DEFAULT_MODEL_ID;
  const work = fs.mkdtempSync(path.join(os.tmpdir(), "xinew-elevenlabs-"));
  const allSentences = flatten(narration);
  const scenes = [];
  const sourceSrt = [];
  let globalTime = 0;
  let subtitleIndex = 1;
  let sentenceIndex = 0;

  for (const scene of narration) {
    const sentenceFiles = [];
    const sentenceTimings = [];
    let sceneTime = 0;

    for (let i = 0; i < scene.sentences.length; i += 1) {
      const item = allSentences[sentenceIndex];
      const previous = allSentences[sentenceIndex - 1]?.text;
      const next = allSentences[sentenceIndex + 1]?.text;
      const stem = `s${String(scene.slide).padStart(2, "0")}-${String(i + 1).padStart(2, "0")}`;
      const raw = path.join(work, `${stem}-raw.mp3`);
      const warm = path.join(work, `${stem}.mp3`);

      console.log(`[${String(scene.slide).padStart(2, "0")}.${i + 1}] ${item.text}`);
      const audio = await requestAudio({
        apiKey,
        voiceId,
        modelId,
        text: item.text,
        previousText: previous,
        nextText: next,
      });
      fs.writeFileSync(raw, audio);
      run("ffmpeg", [
        "-y", "-v", "error", "-i", raw,
        "-af", "highpass=f=70,lowpass=f=12000,acompressor=threshold=0.18:ratio=1.7:attack=12:release=160,alimiter=limit=0.94,apad=pad_dur=0.22",
        "-ar", "44100", "-ac", "1", "-c:a", "libmp3lame", "-b:a", "192k", warm,
      ]);

      const d = duration(warm);
      sentenceFiles.push(warm);
      sentenceTimings.push({
        text: item.sentence.text,
        start: sceneTime,
        end: sceneTime + d - 0.08,
      });
      sourceSrt.push(
        String(subtitleIndex++),
        `${srtTime(globalTime + sceneTime)} --> ${srtTime(globalTime + sceneTime + d - 0.08)}`,
        item.sentence.text,
        "",
      );
      sceneTime += d;
      sentenceIndex += 1;
    }

    const concatFile = path.join(work, `slide-${String(scene.slide).padStart(2, "0")}.txt`);
    fs.writeFileSync(concatFile, sentenceFiles.map((f) => `file '${f}'`).join("\n") + "\n");
    const output = path.join(audioDir, `slide_${String(scene.slide).padStart(2, "0")}.mp3`);
    run("ffmpeg", [
      "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", concatFile,
      "-af", "loudnorm=I=-18:TP=-2:LRA=7", "-c:a", "libmp3lame", "-b:a", "192k", output,
    ]);
    const sceneDuration = duration(output);
    scenes.push({
      slide: scene.slide,
      title: scene.title,
      duration: sceneDuration,
      sentences: sentenceTimings,
      audio: path.relative(ep, output),
      sha256: sha256(output),
    });
    globalTime += sceneDuration;
  }

  fs.writeFileSync(path.join(subtitleDir, "zh-TW-source.srt"), sourceSrt.join("\n") + "\n");
  fs.writeFileSync(path.join(ep, "production/timing.json"), JSON.stringify({
    version: 1,
    sourceDuration: globalTime,
    scenes,
  }, null, 2) + "\n");
  fs.writeFileSync(path.join(ep, "production/tts-manifest.json"), JSON.stringify({
    generatedAt: new Date().toISOString(),
    engine: "ElevenLabs",
    voice: "George F",
    voiceId,
    model: modelId,
    persona: manifest.tts.persona || "warm AI rhino lecturer",
    method: "Original narration.json sentences -> ElevenLabs George F voice -> per-slide normalized MP3",
    scenes: scenes.map(({ slide, duration: d, audio, sha256: hash }) => ({ slide, duration: d, audio, sha256: hash })),
  }, null, 2) + "\n");

  manifest.tts = {
    ...manifest.tts,
    engine: "ElevenLabs",
    voice: "George F",
    voiceId,
    model: modelId,
  };
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + "\n");
  console.log(`Synthesized ${scenes.length} scenes (${globalTime.toFixed(2)}s) with ElevenLabs George F.`);
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
