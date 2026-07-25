#!/usr/bin/env python3
"""Generate the episode's original ambient loop with FFmpeg oscillators."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


CHORDS = [
    (130.81, 155.56, 196.00, 261.63),  # C minor
    (103.83, 130.81, 155.56, 207.65),  # A-flat major 7 color
    (87.31, 130.81, 155.56, 196.00),   # F minor 9 color
    (98.00, 146.83, 174.61, 233.08),   # G suspended color
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", required=True)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[2]
    ep = (root / args.episode).resolve()
    manifest = json.loads((ep / "production/manifest.json").read_text(encoding="utf-8"))
    out_dir = ep / "music"
    out_dir.mkdir(parents=True, exist_ok=True)
    music = manifest["music"]
    declared = Path(music["file"])
    out = ep / declared
    if out.parent != out_dir:
        raise ValueError(f"Music output must stay inside {out_dir}: {declared}")

    inputs: list[str] = []
    for chord in CHORDS:
        pad = "+".join(f"sin(2*PI*{freq}*t)" for freq in chord)
        bell = f"sin(2*PI*{chord[-1] * 2}*t)*exp(-5*(t-2*floor(t/2)))"
        expr = f"0.019*({pad})+0.010*({bell})"
        inputs += ["-f", "lavfi", "-i", f"aevalsrc={expr}:s=44100:d=8"]

    concat_inputs = "".join(f"[{n}:a]" for n in range(len(CHORDS)))
    filter_graph = (
        f"{concat_inputs}concat=n={len(CHORDS)}:v=0:a=1,"
        "highpass=f=55,lowpass=f=6200,aecho=0.8:0.45:160:0.08,"
        "loudnorm=I=-29:TP=-5:LRA=5,afade=t=in:st=0:d=1.2,afade=t=out:st=31:d=1[out]"
    )
    subprocess.run([
        "ffmpeg", "-y", "-v", "error", *inputs,
        "-filter_complex", filter_graph, "-map", "[out]", "-ar", "44100", "-ac", "2", str(out),
    ], check=True)
    (out_dir / "GENERATED-MUSIC.md").write_text(
        f"# {music['title']}\n\n"
        f"本集原創背景音樂，{music['bpm']} BPM、32 秒無人聲科技氛圍循環。"
        "由 `pipeline/scripts/generate_music.py` 以正弦振盪器、和弦進行與 FFmpeg 效果器程式化產生，"
        "不含外部取樣或第三方音樂。影片混音時會在旁白出現時自動降低音量。\n",
        encoding="utf-8",
    )
    print(out)


if __name__ == "__main__":
    main()
