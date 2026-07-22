#!/usr/bin/env python3
"""Assemble per-slide audio/video and burn Traditional Chinese subtitles."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def duration(path: Path) -> float:
    p = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        check=True, capture_output=True, text=True,
    )
    return float(p.stdout.strip())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", required=True)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[2]
    ep = (root / args.episode).resolve()
    manifest = json.loads((ep / "production/manifest.json").read_text(encoding="utf-8"))
    clips = ep / "qc/clips"
    clips.mkdir(parents=True, exist_ok=True)

    for n in range(1, manifest["slideCount"] + 1):
        slide = ep / f"assets/slides/slide_{n:02d}.png"
        audio = ep / f"audio/slide_{n:02d}.mp3"
        clip = clips / f"clip_{n:02d}.mp4"
        if clip.exists() and clip.stat().st_mtime >= max(slide.stat().st_mtime, audio.stat().st_mtime):
            continue
        seconds = duration(audio) + 0.35
        frames = max(1, round(seconds * manifest["video"]["fps"]))
        vf = (
            "zoompan="
            "z='min(zoom+0.00010,1.025)':"
            "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=1920x1080:fps={manifest['video']['fps']},format=yuv420p"
        )
        run([
            "ffmpeg", "-y", "-v", "error", "-loop", "1", "-i", str(slide), "-i", str(audio),
            "-vf", vf, "-t", f"{seconds:.3f}", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
            "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2", "-shortest", str(clip),
        ])

    concat = clips / "concat.txt"
    concat.write_text("\n".join(f"file '{(clips / f'clip_{n:02d}.mp4').as_posix()}'" for n in range(1, manifest["slideCount"] + 1)) + "\n", encoding="utf-8")
    master = ep / "output/ep01-computer-inside-master.mp4"
    captioned = ep / "output/ep01-computer-inside-zh-TW.mp4"
    master.parent.mkdir(parents=True, exist_ok=True)
    newest_clip = max((clips / f"clip_{n:02d}.mp4").stat().st_mtime for n in range(1, manifest["slideCount"] + 1))
    if not master.exists() or master.stat().st_mtime < newest_clip:
        run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", "-movflags", "+faststart", str(master)])

    srt = ep / "subtitles/zh-TW.srt"
    fonts = root / "assets/fonts"
    style = (
        "FontName=Noto Sans CJK TC,FontSize=18,PrimaryColour=&H00FFFFFF,"
        "OutlineColour=&H00101820,BackColour=&HC0101820,BorderStyle=3,"
        "Outline=1,Shadow=0,MarginV=32,Alignment=2"
    )
    vf = f"subtitles=filename='{srt.as_posix()}':fontsdir='{fonts.as_posix()}':force_style='{style}'"
    run([
        "ffmpeg", "-y", "-v", "error", "-i", str(master), "-vf", vf,
        "-c:v", "libx264", "-preset", "medium", "-crf", "19",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
        "-movflags", "+faststart", str(captioned),
    ])
    print(captioned)


if __name__ == "__main__":
    main()
