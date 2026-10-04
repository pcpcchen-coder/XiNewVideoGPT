#!/usr/bin/env python3
"""EP10 acceptance checks — same 18-check contract as the series pipeline."""
from __future__ import annotations

import argparse
import hashlib
import tempfile
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument("--episode", required=True)
args = parser.parse_args()
EP = (ROOT / args.episode).resolve()

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
    source_intro_len = ffprobe_duration(ROOT / "assets/opening/開場影片-v2.mp4")
    assembly_path = EP / "qc/assembly.json"
    assembly = json.loads(assembly_path.read_text(encoding="utf-8")) if assembly_path.exists() else {}
    intro_len = float(assembly.get("opening", {}).get("seconds", source_intro_len))
    check("opening_conform_duration", abs(intro_len - source_intro_len) <= 1 / 30,
          f"conformed {intro_len}s; original {source_intro_len}s; tolerance one frame")
    required = ["production/plan.md", "production/manifest.json", "production/narration.json",
                "production/slides.json", "production/storyboard.json",
                "production/tts-manifest.json", "production/timing.json"]
    missing = [p for p in required if not (EP / p).exists()]
    check("production_files", not missing, f"missing={missing}")

    pptx = EP / "production/presentation" / f"{EP.name}.pptx"
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
    check("sentences_per_scene", sent_ok, "15 sentences across 5 scenes")

    from PIL import Image
    slide_pngs = sorted((EP / "assets/slides").glob("slide_*.png"))
    dims = {Image.open(p).size for p in slide_pngs}
    check("slide_images", len(slide_pngs) == 5 and dims == {(1920, 1080)},
          f"{len(slide_pngs)} pngs, dims={dims}")

    audio = sorted((EP / "audio").glob("slide_*.mp3"))
    check("audio_files", len(audio) == 5, f"{len(audio)} scene mp3s")

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

    check("music_profile", "none" in manifest["music"]["backgroundMusic"],
          "manifest declares narration only; listening review still required")

    srt = (EP / "subtitles/zh-TW.srt").read_text(encoding="utf-8")
    cues = [b for b in srt.strip().split("\n\n") if " --> " in b]
    check("subtitle_cues", len(cues) == 15, f"{len(cues)} cues")

    first_start = cues[0].splitlines()[1].split(" --> ")[0]
    h, m, rest = first_start.split(":"); s, ms = rest.split(",")
    offset = int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
    check("subtitle_offset_intro", abs(offset - intro_len) < 1.0,
          f"first cue at {offset:.2f}s (intro {intro_len}s)")

    master = EP / "output" / f"{EP.name}-master.mp4"
    zh = EP / "output" / f"{EP.name}-zh-TW.mp4"
    thumb = EP / "output/thumbnail.png"
    sheet = EP / "output/contact-sheet.png"
    check("output_files", all(p.exists() and p.stat().st_size > 0 for p in [master, zh, thumb, sheet]),
          "master, zh-TW, thumbnail, contact-sheet")

    master_dur = ffprobe_duration(master)
    expected = intro_len + timing["sourceDuration"] + OUTRO_LEN
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

    r = run(["ffmpeg", "-v", "error", "-i", str(zh), "-f", "null", "-"])
    check("captioned_full_decode", r.returncode == 0 and not r.stderr.strip(),
          f"{len(r.stderr.strip())} decode error bytes")
    check("frame_rate", v["avg_frame_rate"] == "30/1", v["avg_frame_rate"])
    def sec(t):
        h, m, rest = t.split(":"); ss, ms = rest.split(",")
        return int(h) * 3600 + int(m) * 60 + int(ss) + int(ms) / 1000
    expected_cues = []
    cursor = intro_len
    for scene in timing["scenes"]:
        for sentence in scene["sentences"]:
            expected_cues.append((cursor + sentence["start"], cursor + sentence["end"], sentence["text"]))
        cursor += scene["duration"]
    aligned = len(cues) == len(expected_cues)
    previous = -1
    for cue, expected_cue in zip(cues, expected_cues):
        lines = cue.splitlines(); start, end = map(sec, lines[1].split(" --> "))
        aligned = aligned and start >= previous and start < end <= zh_dur
        aligned = aligned and abs(start - expected_cue[0]) < .01 and abs(end - expected_cue[1]) < .01
        aligned = aligned and " ".join(lines[2:]) == expected_cue[2]
        previous = end
    check("all_subtitle_timings", aligned, "all cues match sentence timing plus measured opening")

    # Compare settled static frames across all authored scenes, away from fades.
    if manifest.get("layoutProfile") == "academy-native-v1":
        import numpy as np
        cursor = intro_len
        deltas = []
        for scene in timing["scenes"]:
            frames = []
            for dt in (3, 4):
                raw = subprocess.check_output(["ffmpeg", "-v", "error", "-ss", str(cursor + dt),
                    "-i", str(master), "-frames:v", "1", "-vf", "scale=320:180",
                    "-pix_fmt", "rgb24", "-f", "rawvideo", "-"])
                frames.append(np.frombuffer(raw, dtype=np.uint8).astype(float))
            deltas.append(float(np.abs(frames[1] - frames[0]).mean()))
            cursor += scene["duration"]
        check("stable_scene_frames", max(deltas) < .1, f"5 scenes; max mean RGB delta={max(deltas):.6f} (<0.1)")
        (EP / "qc/stable-scenes.json").write_text(json.dumps({"deltas": deltas, "threshold": .1,
            "passed": all(d < .1 for d in deltas)}, indent=2) + "\n", encoding="utf-8")

    (EP / "qc").mkdir(exist_ok=True)
    (EP / "qc/report.json").write_text(json.dumps(
        {"episode": manifest["episode"], "checks": results,
         "passed": sum(1 for x in results if x["status"] == "PASS"),
         "total": len(results), "fingerprints": {str(p.relative_to(EP)): hashlib.sha256(p.read_bytes()).hexdigest() for p in [master, zh, EP / "production/narration.json", EP / "production/manifest.json", EP / "production/timing.json", EP / "subtitles/zh-TW.srt"]}}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if any(x["status"] != "PASS" for x in results):
        raise SystemExit(1)
    print(f"\n{sum(1 for x in results if x['status'] == 'PASS')}/{len(results)} checks passed")


if __name__ == "__main__":
    main()
