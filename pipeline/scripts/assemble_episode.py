#!/usr/bin/env python3
"""Animate deck renders, add transitions/music, and burn Traditional Chinese subtitles."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


TRANSITIONS = ["fade", "smoothleft", "circleopen", "wipeup", "dissolve", "slideleft"]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def duration(path: Path) -> float:
    result = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=nw=1:nk=1", str(path),
    ], check=True, capture_output=True, text=True)
    return float(result.stdout.strip())


def srt_time(seconds: float) -> str:
    milliseconds = max(0, round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def write_final_srt(timing: dict, output: Path) -> None:
    lines: list[str] = []
    index = 1
    scene_start = 0.0
    for scene in timing["scenes"]:
        for sentence in scene["sentences"]:
            lines += [
                str(index),
                f"{srt_time(scene_start + sentence['start'])} --> {srt_time(scene_start + sentence['end'])}",
                sentence["text"],
                "",
            ]
            index += 1
        scene_start += scene["duration"]
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", required=True)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[2]
    ep = (root / args.episode).resolve()
    manifest = json.loads((ep / "production/manifest.json").read_text(encoding="utf-8"))
    timing = json.loads((ep / "production/timing.json").read_text(encoding="utf-8"))
    count = manifest["slideCount"]
    fps = manifest["video"]["fps"]
    transition = manifest["transitionSeconds"]
    clips = ep / "qc/clips"
    clips.mkdir(parents=True, exist_ok=True)
    scene_durations: list[float] = []

    for n in range(1, count + 1):
        slide = ep / f"assets/slides/slide_{n:02d}.png"
        audio = ep / f"audio/slide_{n:02d}.mp3"
        clip = clips / f"animated_{n:02d}.mp4"
        seconds = duration(audio)
        scene_durations.append(seconds)
        if clip.exists() and clip.stat().st_mtime >= max(slide.stat().st_mtime, audio.stat().st_mtime):
            continue
        frames = max(1, round(seconds * fps))
        x_anchor = [0.15, 0.50, 0.82][(n - 1) % 3]
        y_anchor = [0.28, 0.52][(n - 1) % 2]
        vf = (
            "zoompan="
            "z='min(zoom+0.000045,1.028)':"
            f"x='(iw-iw/zoom)*{x_anchor}':y='(ih-ih/zoom)*{y_anchor}':"
            f"d={frames}:s=1920x1080:fps={fps},"
            "drawbox=x=0:y='mod(t*115,ih)':w=iw:h=3:color=0x46c8ff@0.045:t=fill,"
            "vignette=PI/5,format=yuv420p"
        )
        run([
            "ffmpeg", "-y", "-v", "error", "-loop", "1", "-framerate", str(fps), "-i", str(slide),
            "-i", str(audio), "-vf", vf, "-t", f"{seconds:.3f}",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "21",
            "-c:a", "aac", "-b:a", "160k", "-ar", "44100", "-ac", "2",
            "-shortest", str(clip),
        ])

    animated_speech = clips / "ep01-animated-speech.mp4"
    inputs: list[str] = []
    for n in range(1, count + 1):
        inputs += ["-i", str(clips / f"animated_{n:02d}.mp4")]

    filters: list[str] = []
    for i in range(count):
        pad = f",tpad=stop_mode=clone:stop_duration={transition:.3f}" if i < count - 1 else ""
        filters.append(f"[{i}:v]settb=AVTB,setpts=PTS-STARTPTS{pad}[v{i}]")
        filters.append(f"[{i}:a]aresample=44100,asetpts=PTS-STARTPTS[a{i}]")
    video_label = "v0"
    elapsed = scene_durations[0]
    for i in range(1, count):
        next_label = f"vx{i}"
        transition_name = TRANSITIONS[(i - 1) % len(TRANSITIONS)]
        filters.append(
            f"[{video_label}][v{i}]xfade=transition={transition_name}:duration={transition:.3f}:offset={elapsed:.3f}[{next_label}]"
        )
        video_label = next_label
        elapsed += scene_durations[i]
    audio_inputs = "".join(f"[a{i}]" for i in range(count))
    filters.append(f"{audio_inputs}concat=n={count}:v=0:a=1[aout]")
    run([
        "ffmpeg", "-y", "-v", "error", *inputs,
        "-filter_complex", ";".join(filters),
        "-map", f"[{video_label}]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "21",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(animated_speech),
    ])

    output = ep / "output"
    output.mkdir(parents=True, exist_ok=True)
    master = output / "ep01-computer-inside-master.mp4"
    final_seconds = duration(animated_speech)
    music = ep / "music/data-kitchen-loop.wav"
    music_fade = max(0.0, final_seconds - 2.0)
    run([
        "ffmpeg", "-y", "-v", "error", "-i", str(animated_speech), "-stream_loop", "-1", "-i", str(music),
        "-filter_complex",
        f"[1:a]atrim=0:{final_seconds:.3f},asetpts=PTS-STARTPTS,volume=0.82,"
        f"afade=t=in:st=0:d=1.5,afade=t=out:st={music_fade:.3f}:d=2[music];"
        "[music][0:a]sidechaincompress=threshold=0.028:ratio=7:attack=25:release=420[ducked];"
        "[0:a][ducked]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=9[mix]",
        "-map", "0:v", "-map", "[mix]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-ar", "48000", "-t", f"{final_seconds:.3f}", "-movflags", "+faststart", str(master),
    ])

    final_srt = ep / "subtitles/zh-TW.srt"
    write_final_srt(timing, final_srt)
    fonts = root / "assets/fonts"
    style = (
        "FontName=Noto Sans CJK TC,FontSize=18,PrimaryColour=&H00FFFFFF,"
        "OutlineColour=&H00101820,BackColour=&HC0101820,BorderStyle=3,"
        "Outline=1,Shadow=0,MarginV=34,Alignment=2"
    )
    subtitle_filter = f"subtitles=filename='{final_srt.as_posix()}':fontsdir='{fonts.as_posix()}':force_style='{style}'"
    captioned = output / "ep01-computer-inside-zh-TW.mp4"
    run([
        "ffmpeg", "-y", "-v", "error", "-i", str(master), "-vf", subtitle_filter,
        "-c:v", "libx264", "-preset", "fast", "-crf", "20", "-c:a", "copy",
        "-movflags", "+faststart", str(captioned),
    ])
    print(captioned)


if __name__ == "__main__":
    main()
