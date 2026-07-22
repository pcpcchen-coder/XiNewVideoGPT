#!/usr/bin/env node
"use strict";

const crypto = require("node:crypto");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const { spawnSync } = require("node:child_process");
const meSpeak = require("mespeak");
const { pinyin } = require("pinyin-pro");

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

function copyVerified(source, target) {
  for (let attempt = 1; attempt <= 3; attempt += 1) {
    fs.copyFileSync(source, target);
    try {
      if (fs.statSync(target).size > 10_000 && duration(target) > 1) return;
    } catch (_) {
      // Retry mounted-workspace copies that were truncated during transfer.
    }
  }
  throw new Error(`Could not safely copy ${source} to ${target}`);
}

function spokenPinyin(text) {
  return pinyin(text, { toneType: "num", type: "array" })
    .join(" ")
    .replaceAll("，", ",")
    .replaceAll("。", ".")
    .replaceAll("：", ":")
    .replaceAll("；", ";")
    .replaceAll("？", "?")
    .replaceAll("！", "!");
}

function srtTime(seconds) {
  const ms = Math.max(0, Math.round(seconds * 1000));
  const h = Math.floor(ms / 3600000);
  const m = Math.floor((ms % 3600000) / 60000);
  const s = Math.floor((ms % 60000) / 1000);
  const r = ms % 1000;
  return `${String(h).padStart(2, "0")}:${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")},${String(r).padStart(3, "0")}`;
}

function main() {
  const epArg = process.argv[2];
  if (!epArg) throw new Error("Usage: synthesize_narration.cjs <episode-path>");
  const root = path.resolve(__dirname, "../..");
  const ep = path.resolve(root, epArg);
  const manifest = JSON.parse(fs.readFileSync(path.join(ep, "production/manifest.json"), "utf8"));
  const narration = JSON.parse(fs.readFileSync(path.join(ep, "production/narration.json"), "utf8"));
  const audioDir = path.join(ep, "audio");
  const subtitleDir = path.join(ep, "subtitles");
  fs.mkdirSync(audioDir, { recursive: true });
  fs.mkdirSync(subtitleDir, { recursive: true });

  meSpeak.loadConfig(require("mespeak/src/mespeak_config.json"));
  meSpeak.loadVoice(require("mespeak/voices/zh.json"));

  const work = fs.mkdtempSync(path.join(os.tmpdir(), "xinew-tts-"));
  const scenes = [];
  const sourceSrt = [];
  let globalTime = 0;
  let subtitleIndex = 1;

  for (const scene of narration) {
    const sentenceFiles = [];
    const sentenceTimings = [];
    let sceneTime = 0;

    for (let i = 0; i < scene.sentences.length; i += 1) {
      const sentence = scene.sentences[i];
      const stem = `s${String(scene.slide).padStart(2, "0")}-${String(i + 1).padStart(2, "0")}`;
      const raw = path.join(work, `${stem}-raw.wav`);
      const warm = path.join(work, `${stem}.wav`);
      const phonetic = spokenPinyin(sentence.tts || sentence.text);
      const wav = meSpeak.speak(phonetic, {
        rawdata: "buffer",
        speed: manifest.tts.speed,
        pitch: manifest.tts.pitch,
        amplitude: 92,
        wordgap: 2,
      });
      fs.writeFileSync(raw, wav);
      run("ffmpeg", [
        "-y", "-v", "error", "-i", raw,
        "-af",
        "adelay=140,highpass=f=85,lowpass=f=8800," +
          "equalizer=f=170:t=q:w=1:g=2.5,equalizer=f=2600:t=q:w=1.2:g=1.2," +
          "aecho=0.8:0.35:28:0.035,acompressor=threshold=0.16:ratio=2.3:attack=18:release=180," +
          "alimiter=limit=0.92,apad=pad_dur=0.34",
        "-ar", "44100", "-ac", "1", warm,
      ]);
      const d = duration(warm);
      sentenceFiles.push(warm);
      sentenceTimings.push({
        text: sentence.text,
        start: sceneTime,
        end: sceneTime + d - 0.18,
      });
      sourceSrt.push(
        String(subtitleIndex++),
        `${srtTime(globalTime + sceneTime)} --> ${srtTime(globalTime + sceneTime + d - 0.18)}`,
        sentence.text,
        "",
      );
      sceneTime += d;
    }

    const concatFile = path.join(work, `slide-${String(scene.slide).padStart(2, "0")}.txt`);
    fs.writeFileSync(concatFile, sentenceFiles.map((f) => `file '${f}'`).join("\n") + "\n");
    const tempOutput = path.join(work, `slide_${String(scene.slide).padStart(2, "0")}.mp3`);
    const output = path.join(audioDir, `slide_${String(scene.slide).padStart(2, "0")}.mp3`);
    run("ffmpeg", [
      "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", concatFile,
      "-af", "loudnorm=I=-18:TP=-2:LRA=7", "-c:a", "libmp3lame", "-b:a", "160k", tempOutput,
    ]);
    copyVerified(tempOutput, output);
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
    engine: manifest.tts.engine,
    voice: manifest.tts.voice,
    persona: manifest.tts.persona,
    speed: manifest.tts.speed,
    pitch: manifest.tts.pitch,
    method: "Traditional Chinese text -> numbered pinyin -> offline eSpeak waveform -> warm voice mastering",
    scenes: scenes.map(({ slide, duration: d, audio, sha256: hash }) => ({ slide, duration: d, audio, sha256: hash })),
  }, null, 2) + "\n");
  console.log(`Synthesized ${scenes.length} scenes (${globalTime.toFixed(2)}s) with offline TTS.`);
}

main();
