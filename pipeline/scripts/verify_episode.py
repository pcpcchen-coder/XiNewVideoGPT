#!/usr/bin/env python3
"""Run deterministic delivery checks for a XiNew teaching episode."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


def probe(path: Path) -> dict:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def media_duration(path: Path) -> float:
    return float(probe(path)["format"]["duration"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episode", required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    episode = (root / args.episode).resolve()
    manifest = json.loads((episode / "production/manifest.json").read_text(encoding="utf-8"))
    timing = json.loads((episode / "production/timing.json").read_text(encoding="utf-8"))
    tts_manifest = json.loads((episode / "production/tts-manifest.json").read_text(encoding="utf-8"))
    count = manifest["slideCount"]
    sentence_count = manifest["sentenceCount"]
    checks: list[dict] = []

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append({"name": name, "pass": bool(ok), "detail": detail})

    slides = sorted((episode / "assets/slides").glob("slide_*.png"))
    audio = sorted((episode / "audio").glob("slide_*.mp3"))
    check("slide_count", len(slides) == count, f"{len(slides)}/{count}")
    check("audio_count", len(audio) == count, f"{len(audio)}/{count}")
    check(
        "slide_dimensions",
        all(Image.open(path).size == (1920, 1080) for path in slides),
        "all 1920x1080",
    )
    check("timing_count", len(timing["scenes"]) == count, f"{len(timing['scenes'])}/{count}")
    check(
        "edge_tts_voice",
        tts_manifest["engine"] == "Microsoft Edge TTS"
        and tts_manifest["voice"] == "zh-TW-YunJheNeural"
        and len(tts_manifest["scenes"]) == count,
        f"{tts_manifest['engine']} / {tts_manifest['voice']}",
    )
    check(
        "tts_hashes",
        all(re.fullmatch(r"[0-9a-f]{64}", scene["sha256"]) for scene in tts_manifest["scenes"]),
        f"{len(tts_manifest['scenes'])} SHA-256 records",
    )

    subtitles = (episode / "subtitles/zh-TW.srt").read_text(encoding="utf-8")
    cue_count = subtitles.count(" --> ")
    check("subtitle_cues", cue_count == sentence_count, f"{cue_count}/{sentence_count}")
    check(
        "font_exists",
        (root / "assets/fonts/NotoSansCJKtc-Regular.otf").stat().st_size > 1_000_000,
        "Noto Sans CJK TC",
    )

    deck = episode / "production/presentation" / manifest["output"]["deck"]
    with zipfile.ZipFile(deck) as archive:
        names = archive.namelist()
        slide_xml = [
            name
            for name in names
            if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)
        ]
        note_xml = [
            name
            for name in names
            if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", name)
        ]
        notes_with_sources = sum(b"[Sources]" in archive.read(name) for name in note_xml)
        empty_placeholders = sum(
            len(
                re.findall(
                    rb"<p:ph(?:\s[^>]*)?/>|<p:ph(?:\s[^>]*)?></p:ph>",
                    archive.read(name),
                )
            )
            for name in slide_xml
        )
    check("pptx_slides", len(slide_xml) == count, f"{len(slide_xml)}/{count}")
    check(
        "pptx_notes_sources",
        len(note_xml) == count and notes_with_sources == count,
        f"{len(note_xml)} notes / {notes_with_sources} with sources",
    )
    check("pptx_empty_placeholders", empty_placeholders == 0, f"{empty_placeholders} empty")

    music = episode / manifest["music"]["file"]
    music_seconds = media_duration(music)
    check("original_music", 31.5 <= music_seconds <= 32.5, f"{music_seconds:.2f}s")
    theme = episode / manifest["openingTheme"]["file"]
    theme_info = probe(theme)
    theme_seconds = float(theme_info["format"]["duration"])
    theme_audio = [stream for stream in theme_info["streams"] if stream["codec_type"] == "audio"]
    check(
        "opening_theme",
        119.0 <= theme_seconds <= 121.0 and bool(theme_audio),
        f"{manifest['openingTheme']['title']} / {theme_seconds:.2f}s",
    )

    cutouts = sorted((root / "assets/characters/cutouts").glob("*.png"))
    alpha_ok = all(Image.open(path).convert("RGBA").getpixel((0, 0))[3] == 0 for path in cutouts)
    check("ip_character_alpha", len(cutouts) >= 4 and alpha_ok, f"{len(cutouts)} XiNew poses")

    lesson = episode / "output" / manifest["output"]["lesson"]
    lesson_seconds = media_duration(lesson)
    check(
        "lesson_duration",
        abs(lesson_seconds - timing["sourceDuration"]) < 2.0,
        f"{lesson_seconds:.2f}s / timing {timing['sourceDuration']:.2f}s",
    )
    video = episode / "output" / manifest["output"]["captioned"]
    info = probe(video)
    streams = info["streams"]
    video_stream = next(stream for stream in streams if stream["codec_type"] == "video")
    audio_stream = next(stream for stream in streams if stream["codec_type"] == "audio")
    check("video_codec", video_stream["codec_name"] == "h264", video_stream["codec_name"])
    check("audio_codec", audio_stream["codec_name"] == "aac", audio_stream["codec_name"])
    check(
        "audio_sample_rate",
        audio_stream.get("sample_rate") == "48000",
        f"{audio_stream.get('sample_rate')} Hz",
    )
    check(
        "video_dimensions",
        (video_stream["width"], video_stream["height"]) == (1920, 1080),
        f"{video_stream['width']}x{video_stream['height']}",
    )
    final_duration = float(info["format"]["duration"])
    expected_duration = theme_seconds + timing["sourceDuration"]
    check(
        "full_duration",
        abs(final_duration - expected_duration) < 2.5,
        f"{final_duration:.2f}s / expected {expected_duration:.2f}s",
    )
    check(
        "github_file_size",
        video.stat().st_size < 100 * 1024 * 1024,
        f"{video.stat().st_size / 1024 / 1024:.1f} MiB",
    )

    decode = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(video), "-f", "null", "-"],
        capture_output=True,
        text=True,
    )
    check(
        "decode_test",
        decode.returncode == 0 and not decode.stderr.strip(),
        decode.stderr.strip() or "0 errors",
    )

    report = {
        "episode": manifest["episode"],
        "version": "ip-lecturer-edge-tts-theme-v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "pass": all(item["pass"] for item in checks),
        "checks": checks,
    }
    qc = episode / "qc"
    qc.mkdir(parents=True, exist_ok=True)
    (qc / "report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        f"# {manifest['episode']} 完整製作驗收報告",
        "",
        f"總結果：**{'PASS' if report['pass'] else 'FAIL'}**",
        "",
        "| 檢查 | 結果 | 詳情 |",
        "|---|---:|---|",
    ]
    lines += [
        f"| `{item['name']}` | {'PASS' if item['pass'] else 'FAIL'} | {item['detail']} |"
        for item in checks
    ]
    lines += ["", f"產生時間：{report['generatedAt']}", ""]
    (qc / "report.md").write_text("\n".join(lines), encoding="utf-8")
    print("PASS" if report["pass"] else "FAIL")
    raise SystemExit(0 if report["pass"] else 1)


if __name__ == "__main__":
    main()
