#!/usr/bin/env python3
"""Run deterministic delivery checks and write JSON/Markdown reports."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


def probe(path: Path) -> dict:
    p = subprocess.run(
        ["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)],
        check=True, capture_output=True, text=True,
    )
    return json.loads(p.stdout)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", required=True)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[2]
    ep = (root / args.episode).resolve()
    manifest = json.loads((ep / "production/manifest.json").read_text(encoding="utf-8"))
    n = manifest["slideCount"]
    checks: list[dict] = []

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append({"name": name, "pass": bool(ok), "detail": detail})

    slides = sorted((ep / "assets/slides").glob("slide_*.png"))
    audio = sorted((ep / "audio").glob("slide_*.mp3"))
    check("slide_count", len(slides) == n, f"{len(slides)}/{n}")
    check("audio_count", len(audio) == n, f"{len(audio)}/{n}")
    check("subtitle_exists", (ep / "subtitles/zh-TW.srt").stat().st_size > 100, "zh-TW.srt")
    check("font_exists", (root / "assets/fonts/NotoSansCJKtc-Regular.otf").stat().st_size > 1_000_000, "Noto Sans CJK TC")
    check("slide_dimensions", all(Image.open(p).size == (1920, 1080) for p in slides), "all 1920x1080")

    cutouts = sorted((root / "assets/characters/cutouts").glob("*.png"))
    alpha_ok = True
    for p in cutouts:
        im = Image.open(p).convert("RGBA")
        alpha_ok &= im.getpixel((0, 0))[3] == 0 and im.getchannel("A").getbbox() is not None
    check("character_alpha", len(cutouts) >= 4 and alpha_ok, f"{len(cutouts)} reusable poses")

    video = ep / "output/ep01-computer-inside-zh-TW.mp4"
    info = probe(video)
    streams = info["streams"]
    vs = next(s for s in streams if s["codec_type"] == "video")
    aud = next(s for s in streams if s["codec_type"] == "audio")
    check("video_codec", vs["codec_name"] == "h264", vs["codec_name"])
    check("audio_codec", aud["codec_name"] == "aac", aud["codec_name"])
    check("video_dimensions", (vs["width"], vs["height"]) == (1920, 1080), f"{vs['width']}x{vs['height']}")
    check("duration", float(info["format"]["duration"]) > 180, f"{float(info['format']['duration']):.2f}s")
    check("github_file_size", video.stat().st_size < 100 * 1024 * 1024, f"{video.stat().st_size / 1024 / 1024:.1f} MiB")

    decode = subprocess.run(["ffmpeg", "-v", "error", "-i", str(video), "-f", "null", "-"], capture_output=True, text=True)
    check("decode_test", decode.returncode == 0 and not decode.stderr.strip(), decode.stderr.strip() or "0 errors")

    report = {
        "episode": manifest["episode"],
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "pass": all(c["pass"] for c in checks),
        "checks": checks,
    }
    qc = ep / "qc"
    qc.mkdir(parents=True, exist_ok=True)
    (qc / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [f"# {manifest['episode']} 驗收報告", "", f"總結果：**{'PASS' if report['pass'] else 'FAIL'}**", "", "| 檢查 | 結果 | 詳情 |", "|---|---:|---|"]
    lines += [f"| `{c['name']}` | {'PASS' if c['pass'] else 'FAIL'} | {c['detail']} |" for c in checks]
    lines += ["", f"產生時間：{report['generatedAt']}", ""]
    (qc / "report.md").write_text("\n".join(lines), encoding="utf-8")
    print("PASS" if report["pass"] else "FAIL")
    raise SystemExit(0 if report["pass"] else 1)


if __name__ == "__main__":
    main()

