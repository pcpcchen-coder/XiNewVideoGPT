#!/usr/bin/env python3
"""EP10 acceptance checks — same 18-check contract as the series pipeline."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EP = ROOT / "episodes/season-01/ep10-ai-and-our-future"
INTRO_LEN = 60.0  # user-provided opening video
OUTRO_LEN = 0.0

results: list[dict] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append({"check": name, "status": "PASS" if ok else "FAIL", "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


def ffprobe_duration(path: Path) -> float:
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", str(path)])
    return float(r.stdout.strip())


def main() -> None:
    required = ["production/plan.md", "production/manifest.json", "production/narration.json",
                "production/slides.json", "production/storyboard.json",
                "production/tts-manifest.json", "production/timing.json"]
    missing = [p for p in required if not (EP / p).exists()]
    check("production_files", not missing, f"missing={missing}")

    pptx = EP / "production/presentation/ep10-ai-and-our-future.pptx"
    check("pptx_exists", pptx.exists() and pptx.stat().st_size > 100_000,
          f"{pptx.stat().st_size if pptx.exists() else 0} bytes")

    manifest = json.loads((EP / "production/manifest.json").read_text(encoding="utf-8"))
    narration = json.loads((EP / "production/narration.json").read_text(encoding="utf-8"))
    timing = json.loads((EP / "production/timing.json").read_text(encoding="utf-8"))
    slides = json.loads((EP / "production/slides.json").read_text(encoding="utf-8"))
    storyboard = json.loads((EP / "production/storyboard.json").read_text(encoding="utf-8"))

    check("slide_count", len(slides) == manifest["slideCount"] == len(narration) == len(storyboard),
          f"slides={len(slides)} narration={len(narration)} storyboard={len(storyboard)}")

    sent_ok = all(len(s["sentences"]) == 3 for s in narration)
    check("sentences_per_scene", sent_ok, "36 sentences across 12 scenes")

    from PIL import Image
    slide_pngs = sorted((EP / "assets/slides").glob("slide_*.png"))
    dims = {Image.open(p).size for p in slide_pngs}
    check("slide_images", len(slide_pngs) == 12 and dims == {(1920, 1080)},
          f"{len(slide_pngs)} pngs, dims={dims}")

    audio = sorted((EP / "audio").glob("slide_*.mp3"))
    check("audio_files", len(audio) == 12, f"{len(audio)} scene mp3s")

    dur_sum = sum(ffprobe_duration(p) for p in audio)
    check("audio_duration_matches_timing", abs(dur_sum - timing["sourceDuration"]) < 1.0,
          f"sum={dur_sum:.2f}s timing={timing['sourceDuration']:.2f}s")

    silent = []
    for p in audio:
        r = run(["ffmpeg", "-i", str(p), "-af", "volumedetect", "-f", "null", "-"])
        if "mean_volume: -91.0 dB" in r.stderr or "max_volume: -91.0 dB" in r.stderr:
            silent.append(p.name)
        if "mean_volume: -inf" in r.stderr:
            silent.append(p.name)
    check("audio_non_silent", not silent, f"silent={silent}")

    kitchen = EP / "music/data-kitchen-loop.wav"
    theme = EP / "music/theme-song-1min.m4a"
    check("music_files", kitchen.exists() and theme.exists(),
          "Data Kitchen loop + theme song present")

    srt = (EP / "subtitles/zh-TW.srt").read_text(encoding="utf-8")
    cues = [b for b in srt.strip().split("\n\n") if " --> " in b]
    check("subtitle_cues", len(cues) == 36, f"{len(cues)} cues")

    first_start = cues[0].splitlines()[1].split(" --> ")[0]
    h, m, rest = first_start.split(":"); s, ms = rest.split(",")
    offset = int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
    check("subtitle_offset_intro", abs(offset - INTRO_LEN) < 1.0,
          f"first cue at {offset:.2f}s (intro {INTRO_LEN}s)")

    master = EP / "output/ep10-ai-and-our-future-master.mp4"
    zh = EP / "output/ep10-ai-and-our-future-zh-TW.mp4"
    thumb = EP / "output/thumbnail.png"
    sheet = EP / "output/contact-sheet.png"
    check("output_files", all(p.exists() and p.stat().st_size > 0 for p in [master, zh, thumb, sheet]),
          "master, zh-TW, thumbnail, contact-sheet")

    master_dur = ffprobe_duration(master)
    expected = INTRO_LEN + timing["sourceDuration"] + OUTRO_LEN + manifest["transitionSeconds"]
    check("duration", abs(master_dur - expected) < 2.0, f"{master_dur:.2f}s vs expected {expected:.2f}s")

    zh_dur = ffprobe_duration(zh)
    check("zh_burned_copy", abs(zh_dur - master_dur) < 0.5 and zh.stat().st_size != master.stat().st_size,
          f"zh {zh_dur:.2f}s, subtitles burned")

    r = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
             "stream=codec_name,width,height,avg_frame_rate", "-of", "json", str(master)])
    v = json.loads(r.stdout)["streams"][0]
    check("video_format", v["codec_name"] == "h264" and (v["width"], v["height"]) == (1920, 1080),
          f"{v['codec_name']} {v['width']}x{v['height']} @{v['avg_frame_rate']}")

    r = run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries",
             "stream=codec_name,sample_rate,channels", "-of", "json", str(master)])
    a = json.loads(r.stdout)["streams"][0]
    check("audio_format", a["codec_name"] == "aac" and a["sample_rate"] == "48000" and a["channels"] == 2,
          f"{a['codec_name']} {a['sample_rate']}Hz x{a['channels']}")

    r = run(["ffmpeg", "-v", "error", "-i", str(master), "-f", "null", "-"])
    check("full_decode", r.returncode == 0 and not r.stderr.strip(),
          f"{len(r.stderr.strip())} decode error bytes")

    r = run(["ffmpeg", "-i", str(master), "-af", "ebur128", "-f", "null", "-"])
    loud = [l for l in r.stderr.splitlines() if "I:" in l and "LUFS" in l]
    i_lufs = float(loud[-1].split("I:")[1].split("LUFS")[0].strip()) if loud else -99.0
    check("loudness", -18.0 <= i_lufs <= -14.0, f"integrated {i_lufs} LUFS")

    (EP / "qc").mkdir(exist_ok=True)
    (EP / "qc/report.json").write_text(json.dumps(
        {"episode": manifest["episode"], "checks": results,
         "passed": sum(1 for x in results if x["status"] == "PASS"),
         "total": len(results)}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n{sum(1 for x in results if x['status'] == 'PASS')}/{len(results)} checks passed")


if __name__ == "__main__":
    main()
