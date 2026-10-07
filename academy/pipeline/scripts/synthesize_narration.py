#!/usr/bin/env python3
"""Synthesize EP10 narration sentence-by-sentence with the series voice.

Mirrors the XiNewVideoGPT pipeline: per-sentence synthesis -> warm voice
mastering chain -> per-scene concat -> loudnorm -> timing.json + source SRT.
Voice: zh-TW-YunJheNeural (the toolkit-designated Chen XiNew voice).
"""
from __future__ import annotations

import asyncio
import edge_tts
import edge_tts.communicate
import os
import ssl
# Extend trust with the current environment CA; certificate verification stays enabled.
_ca_bundle = os.environ.get("XINEW_CA_BUNDLE") or ssl.get_default_verify_paths().cafile
if _ca_bundle:
    edge_tts.communicate._SSL_CTX.load_verify_locations(_ca_bundle)
# aiohttp ignores HTTPS_PROXY unless told; pass the environment's proxy explicitly.
# A proxy that denies speech.platform.bing.com (403) is a policy block: report it, do not route around it.
_PROXY = os.environ.get("XINEW_TTS_PROXY") or os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy") or None
import hashlib
import argparse
import tempfile
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument("--episode", required=True)
args = parser.parse_args()
EP = (ROOT / args.episode).resolve()

VOICE = "zh-TW-YunJheNeural"
_work = tempfile.TemporaryDirectory(prefix="xinew-tts-")
WORK = Path(_work.name)


def run(cmd: list[str]) -> str:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"{cmd[0]} failed:\n{r.stderr or r.stdout}")
    return r.stdout.strip()


def duration(path: Path) -> float:
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                      "-of", "default=nw=1:nk=1", str(path)]))


def srt_time(seconds: float) -> str:
    ms = max(0, round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, r = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{r:03d}"


def synthesize(text: str, out: Path) -> None:
    for attempt in range(1, 5):
        try:
            asyncio.run(edge_tts.Communicate(text, VOICE, proxy=_PROXY).save(str(out)))
            if out.exists() and out.stat().st_size > 2000:
                return
        except Exception:
            if attempt == 4:
                raise
        print(f"  retry {attempt}: {text[:16]}...", flush=True)
    raise RuntimeError(f"TTS failed for: {text}")


def main() -> None:
    manifest = json.loads((EP / "production/manifest.json").read_text(encoding="utf-8"))
    if manifest["tts"]["voice"] != VOICE:
        raise ValueError("Profile requires zh-TW-YunJheNeural")
    narration = json.loads((EP / "production/narration.json").read_text(encoding="utf-8"))
    audio_dir = EP / "audio"; audio_dir.mkdir(exist_ok=True)
    sub_dir = EP / "subtitles"; sub_dir.mkdir(exist_ok=True)

    scenes = []
    source_srt: list[str] = []
    global_time = 0.0
    sub_idx = 1

    for scene in narration:
        sentence_files = []
        sentence_timings = []
        scene_time = 0.0
        for i, sentence in enumerate(scene["sentences"]):
            stem = f"s{scene['slide']:02d}-{i + 1:02d}"
            raw = WORK / f"{stem}-raw.mp3"
            warm = WORK / f"{stem}.wav"
            spoken = sentence.get("tts") or sentence["text"]
            if not raw.exists():
                synthesize(spoken, raw)
            run(["ffmpeg", "-y", "-v", "error", "-i", str(raw), "-af",
                 "adelay=140,highpass=f=85,lowpass=f=8800,"
                 "equalizer=f=170:t=q:w=1:g=2.5,equalizer=f=2600:t=q:w=1.2:g=1.2,"
                 "aecho=0.8:0.35:28:0.035,acompressor=threshold=0.16:ratio=2.3:attack=18:release=180,"
                 "alimiter=limit=0.92,apad=pad_dur=0.34",
                 "-ar", "44100", "-ac", "1", str(warm)])
            d = duration(warm)
            sentence_files.append(warm)
            sentence_timings.append({"text": sentence["text"], "start": scene_time,
                                     "end": scene_time + d - 0.18})
            source_srt += [str(sub_idx),
                           f"{srt_time(global_time + scene_time)} --> {srt_time(global_time + scene_time + d - 0.18)}",
                           sentence["text"], ""]
            sub_idx += 1
            scene_time += d
            print(f"  s{scene['slide']:02d}-{i + 1:02d} {d:5.2f}s {sentence['text'][:20]}", flush=True)

        concat = WORK / f"slide-{scene['slide']:02d}.txt"
        concat.write_text("".join(f"file '{f}'\n" for f in sentence_files), encoding="utf-8")
        temp_out = WORK / f"slide_{scene['slide']:02d}.mp3"
        out = audio_dir / f"slide_{scene['slide']:02d}.mp3"
        run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(concat),
             "-af", "loudnorm=I=-18:TP=-2:LRA=7", "-c:a", "libmp3lame", "-b:a", "160k", str(temp_out)])
        import shutil
        for attempt in range(3):
            shutil.copyfile(temp_out, out)
            if out.stat().st_size > 10_000 and duration(out) > 1:
                break
        scene_duration = duration(out)
        scenes.append({"slide": scene["slide"], "title": scene["title"], "duration": scene_duration,
                       "sentences": sentence_timings, "audio": f"audio/slide_{scene['slide']:02d}.mp3",
                       "sha256": hashlib.sha256(out.read_bytes()).hexdigest()})
        global_time += scene_duration
        print(f"scene {scene['slide']:02d}: {scene_duration:.2f}s", flush=True)

    (sub_dir / "zh-TW-source.srt").write_text("\n".join(source_srt) + "\n", encoding="utf-8")
    (EP / "production/timing.json").write_text(json.dumps(
        {"version": 1, "sourceDuration": global_time, "scenes": scenes},
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (EP / "production/tts-manifest.json").write_text(json.dumps({
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "narrationSha256": hashlib.sha256((EP / "production/narration.json").read_bytes()).hexdigest(),
        "engine": manifest["tts"]["engine"], "voice": manifest["tts"]["voice"],
        "persona": manifest["tts"]["persona"], "rate": "+0%",
        "pitch": "+0Hz",
        "packageVersion": edge_tts.__version__,
        "method": "Traditional Chinese text -> edge-tts zh-TW-YunJheNeural -> warm voice mastering",
        "scenes": [{"slide": s["slide"], "duration": s["duration"], "audio": s["audio"],
                    "sha256": s["sha256"]} for s in scenes],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Synthesized {len(scenes)} scenes ({global_time:.2f}s).")


if __name__ == "__main__":
    sys.exit(main())
