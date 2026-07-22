#!/usr/bin/env python3
"""Run deterministic delivery checks for the full remake."""

from __future__ import annotations

import argparse
import json
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


def probe(path: Path) -> dict:
    result = subprocess.run([
        "ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path),
    ], check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", required=True)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[2]
    ep = (root / args.episode).resolve()
    manifest = json.loads((ep / "production/manifest.json").read_text(encoding="utf-8"))
    timing = json.loads((ep / "production/timing.json").read_text(encoding="utf-8"))
    count = manifest["slideCount"]
    checks: list[dict] = []

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append({"name": name, "pass": bool(ok), "detail": detail})

    slides = sorted((ep / "assets/slides").glob("slide_*.png"))
    audio = sorted((ep / "audio").glob("slide_*.mp3"))
    check("slide_count", len(slides) == count, f"{len(slides)}/{count}")
    check("audio_count", len(audio) == count, f"{len(audio)}/{count}")
    check("slide_dimensions", all(Image.open(p).size == (1920, 1080) for p in slides), "all 1920x1080")
    check("timing_count", len(timing["scenes"]) == count, f"{len(timing['scenes'])}/{count}")
    check("new_tts", (ep / "production/tts-manifest.json").stat().st_size > 1000, manifest["tts"]["engine"])

    subtitles = (ep / "subtitles/zh-TW.srt").read_text(encoding="utf-8")
    check("subtitle_cues", subtitles.count(" --> ") == 36, f"{subtitles.count(' --> ')}/36")
    check("font_exists", (root / "assets/fonts/NotoSansCJKtc-Regular.otf").stat().st_size > 1_000_000, "Noto Sans CJK TC")

    deck = ep / "production/presentation/ep01-computer-inside.pptx"
    with zipfile.ZipFile(deck) as archive:
        slide_xml = [n for n in archive.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml")]
        note_xml = [n for n in archive.namelist() if n.startswith("ppt/notesSlides/notesSlide") and n.endswith(".xml")]
    check("pptx_slides", len(slide_xml) == count, f"{len(slide_xml)}/{count}")
    check("pptx_notes", len(note_xml) == count, f"{len(note_xml)}/{count}")

    music = ep / "music/data-kitchen-loop.wav"
    music_info = probe(music)
    check("original_music", 31.5 <= float(music_info["format"]["duration"]) <= 32.5, f"{float(music_info['format']['duration']):.2f}s")

    cutouts = sorted((root / "assets/characters/cutouts").glob("*.png"))
    alpha_ok = all(Image.open(p).convert("RGBA").getpixel((0, 0))[3] == 0 for p in cutouts)
    check("ip_character_alpha", len(cutouts) >= 4 and alpha_ok, f"{len(cutouts)} XiNew poses")

    video = ep / "output/ep01-computer-inside-zh-TW.mp4"
    info = probe(video)
    streams = info["streams"]
    video_stream = next(s for s in streams if s["codec_type"] == "video")
    audio_stream = next(s for s in streams if s["codec_type"] == "audio")
    check("video_codec", video_stream["codec_name"] == "h264", video_stream["codec_name"])
    check("audio_codec", audio_stream["codec_name"] == "aac", audio_stream["codec_name"])
    check("audio_sample_rate", audio_stream.get("sample_rate") == "48000", f"{audio_stream.get('sample_rate')} Hz")
    check("video_dimensions", (video_stream["width"], video_stream["height"]) == (1920, 1080), f"{video_stream['width']}x{video_stream['height']}")
    final_duration = float(info["format"]["duration"])
    check("duration", abs(final_duration - timing["sourceDuration"]) < 2.0, f"{final_duration:.2f}s")
    check("github_file_size", video.stat().st_size < 100 * 1024 * 1024, f"{video.stat().st_size / 1024 / 1024:.1f} MiB")

    decode = subprocess.run(["ffmpeg", "-v", "error", "-i", str(video), "-f", "null", "-"], capture_output=True, text=True)
    check("decode_test", decode.returncode == 0 and not decode.stderr.strip(), decode.stderr.strip() or "0 errors")

    report = {
        "episode": manifest["episode"],
        "version": "full-remake-v2",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "pass": all(c["pass"] for c in checks),
        "checks": checks,
    }
    qc = ep / "qc"
    qc.mkdir(parents=True, exist_ok=True)
    (qc / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        f"# {manifest['episode']} 完整重製驗收報告", "",
        f"總結果：**{'PASS' if report['pass'] else 'FAIL'}**", "",
        "| 檢查 | 結果 | 詳情 |", "|---|---:|---|",
    ]
    lines += [f"| `{c['name']}` | {'PASS' if c['pass'] else 'FAIL'} | {c['detail']} |" for c in checks]
    lines += ["", f"產生時間：{report['generatedAt']}", ""]
    (qc / "report.md").write_text("\n".join(lines), encoding="utf-8")
    print("PASS" if report["pass"] else "FAIL")
    raise SystemExit(0 if report["pass"] else 1)


if __name__ == "__main__":
    main()
