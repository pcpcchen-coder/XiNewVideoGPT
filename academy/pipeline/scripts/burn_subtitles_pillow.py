#!/usr/bin/env python3
"""Burn SRT subtitles without relying on FFmpeg's optional libass filter."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


@dataclass
class Cue:
    start: float
    end: float
    text: str


def run(cmd: list[str]) -> str:
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout.strip()


def parse_srt_time(value: str) -> float:
    h, m, rest = value.split(":")
    s, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def parse_srt(path: Path) -> list[Cue]:
    blocks = re.split(r"\n\s*\n", path.read_text(encoding="utf-8-sig").strip())
    cues: list[Cue] = []
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) < 3 or "-->" not in lines[1]:
            continue
        start, end = [part.strip() for part in lines[1].split("-->")]
        cues.append(Cue(parse_srt_time(start), parse_srt_time(end), " ".join(lines[2:])))
    return cues


def video_info(path: Path) -> tuple[int, int, float, int]:
    data = json.loads(run([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height,r_frame_rate,nb_frames",
        "-of", "json", str(path),
    ]))
    stream = data["streams"][0]
    numerator, denominator = stream["r_frame_rate"].split("/")
    fps = float(numerator) / float(denominator)
    frames = int(stream.get("nb_frames") or round(float(run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=nw=1:nk=1", str(path),
    ])) * fps))
    return int(stream["width"]), int(stream["height"]), fps, frames


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    tokens = list(text)
    lines: list[str] = []
    line = ""
    for token in tokens:
        candidate = line + token
        if draw.textbbox((0, 0), candidate, font=font, stroke_width=2)[2] <= max_width or not line:
            line = candidate
            continue
        lines.append(line)
        line = token
    if line:
        lines.append(line)
    return lines


def draw_subtitle(frame: Image.Image, text: str, font: ImageFont.FreeTypeFont) -> None:
    overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    width, height = frame.size
    lines = wrap_text(draw, text, font, int(width * 0.78))
    line_height = int(font.size * 1.35)
    text_height = line_height * len(lines)
    pad_x = 30
    pad_y = 18
    box_width = max(draw.textbbox((0, 0), line, font=font, stroke_width=2)[2] for line in lines) + pad_x * 2
    box_height = text_height + pad_y * 2
    x0 = (width - box_width) // 2
    y0 = height - box_height - 38
    draw.rounded_rectangle(
        (x0, y0, x0 + box_width, y0 + box_height),
        radius=10,
        fill=(16, 24, 32, 205),
    )
    y = y0 + pad_y
    for line in lines:
        line_width = draw.textbbox((0, 0), line, font=font, stroke_width=2)[2]
        draw.text(
            ((width - line_width) // 2, y),
            line,
            font=font,
            fill=(255, 255, 255, 255),
            stroke_width=2,
            stroke_fill=(16, 24, 32, 255),
        )
        y += line_height
    frame.alpha_composite(overlay)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--srt", required=True)
    parser.add_argument("--font", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    source = Path(args.input)
    srt = Path(args.srt)
    font_path = Path(args.font)
    output = Path(args.output)
    width, height, fps, total_frames = video_info(source)
    font = ImageFont.truetype(str(font_path), 42)
    cues = parse_srt(srt)

    decoder = subprocess.Popen([
        "ffmpeg", "-v", "error", "-i", str(source),
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-",
    ], stdout=subprocess.PIPE)
    encoder = subprocess.Popen([
        "ffmpeg", "-y", "-v", "error",
        "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{width}x{height}", "-r", f"{fps:.6f}", "-i", "-",
        "-i", str(source), "-map", "0:v", "-map", "1:a:0",
        "-c:v", "libx264", "-preset", "fast", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "copy", "-movflags", "+faststart", str(output),
    ], stdin=subprocess.PIPE)

    assert decoder.stdout is not None
    assert encoder.stdin is not None
    frame_size = width * height * 3
    cue_index = 0
    cached_cue = -1
    cached_overlay = None
    try:
        for frame_number in range(total_frames):
            raw = decoder.stdout.read(frame_size)
            if len(raw) != frame_size:
                break
            timestamp = frame_number / fps
            while cue_index < len(cues) and cues[cue_index].end < timestamp:
                cue_index += 1
            frame = Image.frombytes("RGB", (width, height), raw).convert("RGBA")
            if cue_index < len(cues) and cues[cue_index].start <= timestamp <= cues[cue_index].end:
                if cached_cue != cue_index:
                    cached_overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
                    draw_subtitle(cached_overlay, cues[cue_index].text, font)
                    cached_cue = cue_index
                frame.alpha_composite(cached_overlay)
            encoder.stdin.write(frame.tobytes())
            if frame_number and frame_number % 900 == 0:
                print(f"burned {frame_number}/{total_frames} frames", file=sys.stderr)
    finally:
        decoder.stdout.close()
        encoder.stdin.close()
        decoder.wait()
        encoder.wait()
    if encoder.returncode != 0:
        raise SystemExit(encoder.returncode)


if __name__ == "__main__":
    main()
