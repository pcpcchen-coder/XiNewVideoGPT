#!/usr/bin/env python3
"""Animate slides, mix the lesson, prepend the XiNew theme montage, and add captions."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


TRANSITIONS = ["fade"]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=nw=1:nk=1",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
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


def build_animated_lesson(
    episode: Path,
    manifest: dict,
    timing: dict,
    clips: Path,
) -> Path:
    count = manifest["slideCount"]
    fps = manifest["video"]["fps"]
    transition = manifest["transitionSeconds"]
    scene_durations: list[float] = []
    pipeline_mtime = Path(__file__).stat().st_mtime

    for n in range(1, count + 1):
        slide = episode / f"assets/slides/slide_{n:02d}.png"
        audio = episode / f"audio/slide_{n:02d}.mp3"
        clip = clips / f"animated_{n:02d}.mp4"
        seconds = duration(audio)
        scene_durations.append(seconds)
        if clip.exists() and clip.stat().st_mtime >= max(
            slide.stat().st_mtime,
            audio.stat().st_mtime,
            pipeline_mtime,
        ):
            continue
        vf = (
            f"scale=1920:1080:flags=lanczos,setsar=1,fps={fps},format=yuv420p"
        )
        run(
            [
                "ffmpeg",
                "-y",
                "-v",
                "error",
                "-loop",
                "1",
                "-framerate",
                str(fps),
                "-i",
                str(slide),
                "-i",
                str(audio),
                "-vf",
                vf,
                "-t",
                f"{seconds:.3f}",
                "-c:v",
                "libx264",
                "-preset",
                "veryfast",
                "-crf",
                "22",
                "-c:a",
                "aac",
                "-b:a",
                "160k",
                "-ar",
                "48000",
                "-ac",
                "2",
                "-shortest",
                str(clip),
            ]
        )

    animated_speech = clips / f"{manifest['slug']}-animated-speech.mp4"
    inputs: list[str] = []
    for n in range(1, count + 1):
        inputs += ["-i", str(clips / f"animated_{n:02d}.mp4")]
    filters: list[str] = []
    for i in range(count):
        pad = f",tpad=stop_mode=clone:stop_duration={transition:.3f}" if i < count - 1 else ""
        filters.append(f"[{i}:v]settb=AVTB,setpts=PTS-STARTPTS{pad}[v{i}]")
        filters.append(f"[{i}:a]aresample=48000,asetpts=PTS-STARTPTS[a{i}]")
    video_label = "v0"
    elapsed = scene_durations[0]
    for i in range(1, count):
        next_label = f"vx{i}"
        transition_name = TRANSITIONS[(i - 1) % len(TRANSITIONS)]
        filters.append(
            f"[{video_label}][v{i}]"
            f"xfade=transition={transition_name}:duration={transition:.3f}:offset={elapsed:.3f}"
            f"[{next_label}]"
        )
        video_label = next_label
        elapsed += scene_durations[i]
    audio_inputs = "".join(f"[a{i}]" for i in range(count))
    filters.append(f"{audio_inputs}concat=n={count}:v=0:a=1[aout]")
    run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            *inputs,
            "-filter_complex",
            ";".join(filters),
            "-map",
            f"[{video_label}]",
            "-map",
            "[aout]",
            "-c:v",
            "libx264",
            "-preset",
            "fast",
            "-crf",
            "22",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-ar",
            "48000",
            "-movflags",
            "+faststart",
            str(animated_speech),
        ]
    )
    expected = sum(scene["duration"] for scene in timing["scenes"])
    if abs(duration(animated_speech) - expected) > 1.5:
        raise RuntimeError("Animated lesson duration no longer matches TTS timing.")
    return animated_speech


def prepare_voice_only_lesson(speech: Path, output: Path) -> None:
    seconds = duration(speech)
    run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-i",
            str(speech),
            "-filter:a",
            "loudnorm=I=-16:TP=-1.5:LRA=9",
            "-map",
            "0:v",
            "-map",
            "0:a",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-ar",
            "48000",
            "-t",
            f"{seconds:.3f}",
            "-movflags",
            "+faststart",
            str(output),
        ]
    )


def build_opening_montage(
    root: Path,
    episode: Path,
    manifest: dict,
    clips: Path,
) -> Path:
    theme = episode / manifest["openingTheme"]["file"]
    theme_seconds = duration(theme)
    fps = manifest["video"]["fps"]
    images = [
        root / "assets/xinew-brand-identity.png",
        root / "assets/characters/xinew-key-visual.png",
        episode / "assets/slides/slide_01.png",
        root / "assets/characters/xinew-turnaround.png",
        episode / "assets/slides/slide_12.png",
    ]
    if not all(image.exists() for image in images):
        missing = [str(image) for image in images if not image.exists()]
        raise FileNotFoundError(f"Opening montage images are missing: {missing}")
    segment_seconds = theme_seconds / len(images)
    montage_clips: list[Path] = []
    for index, image in enumerate(images, start=1):
        clip = clips / f"opening_{index:02d}.mp4"
        montage_clips.append(clip)
        vf = (
            "scale=1920:1080:force_original_aspect_ratio=decrease,"
            "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=0x031426,"
            f"setsar=1,fps={fps},"
            f"fade=t=in:st=0:d=0.8,fade=t=out:st={max(0, segment_seconds - 0.8):.3f}:d=0.8,"
            "format=yuv420p"
        )
        run(
            [
                "ffmpeg",
                "-y",
                "-v",
                "error",
                "-loop",
                "1",
                "-framerate",
                str(fps),
                "-i",
                str(image),
                "-vf",
                vf,
                "-t",
                f"{segment_seconds:.3f}",
                "-an",
                "-c:v",
                "libx264",
                "-preset",
                "veryfast",
                "-crf",
                "22",
                str(clip),
            ]
        )
    concat_list = clips / "opening-concat.txt"
    concat_list.write_text(
        "\n".join(f"file '{clip.as_posix()}'" for clip in montage_clips) + "\n",
        encoding="utf-8",
    )
    opening = clips / f"{manifest['slug']}-opening-theme.mp4"
    run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-i",
            str(theme),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-ar",
            "48000",
            "-ac",
            "2",
            "-t",
            f"{theme_seconds:.3f}",
            "-movflags",
            "+faststart",
            str(opening),
        ]
    )
    return opening


def burn_lesson_captions(root: Path, lesson: Path, srt: Path, output: Path) -> None:
    fonts = root / "assets/fonts"
    style = (
        "FontName=Noto Sans CJK TC,FontSize=18,PrimaryColour=&H00FFFFFF,"
        "OutlineColour=&H00101820,BackColour=&HC0101820,BorderStyle=3,"
        "Outline=1,Shadow=0,MarginV=34,Alignment=2"
    )
    subtitle_filter = (
        f"subtitles=filename='{srt.as_posix()}':fontsdir='{fonts.as_posix()}':"
        f"force_style='{style}'"
    )
    try:
        run(
            [
                "ffmpeg",
                "-y",
                "-v",
                "error",
                "-i",
                str(lesson),
                "-vf",
                subtitle_filter,
                "-c:v",
                "libx264",
                "-preset",
                "fast",
                "-crf",
                "21",
                "-c:a",
                "copy",
                "-movflags",
                "+faststart",
                str(output),
            ]
        )
    except subprocess.CalledProcessError:
        run(
            [
                sys.executable,
                str(root / "pipeline/scripts/burn_subtitles_pillow.py"),
                "--input",
                str(lesson),
                "--srt",
                str(srt),
                "--font",
                str(fonts / "NotoSansCJKtc-Regular.otf"),
                "--output",
                str(output),
            ]
        )


def concatenate_program(opening: Path, lesson: Path, output: Path) -> None:
    run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-i",
            str(opening),
            "-i",
            str(lesson),
            "-filter_complex",
            "[0:v]settb=AVTB,setpts=PTS-STARTPTS[v0];"
            "[1:v]settb=AVTB,setpts=PTS-STARTPTS[v1];"
            "[v0][v1]concat=n=2:v=1:a=0[v];"
            "[0:a]aresample=48000,asetpts=PTS-STARTPTS[a0];"
            "[1:a]aresample=48000,asetpts=PTS-STARTPTS[a1];"
            "[a0][a1]concat=n=2:v=0:a=1[a]",
            "-map",
            "[v]",
            "-map",
            "[a]",
            "-c:v",
            "libx264",
            "-preset",
            "fast",
            "-crf",
            "23",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-ar",
            "48000",
            "-movflags",
            "+faststart",
            str(output),
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episode", required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    episode = (root / args.episode).resolve()
    manifest = json.loads((episode / "production/manifest.json").read_text(encoding="utf-8"))
    timing = json.loads((episode / "production/timing.json").read_text(encoding="utf-8"))
    clips = episode / "qc/clips"
    output_dir = episode / "output"
    subtitle_dir = episode / "subtitles"
    clips.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    subtitle_dir.mkdir(parents=True, exist_ok=True)

    print("1/6 Animating the twelve lesson scenes.", flush=True)
    speech = build_animated_lesson(episode, manifest, timing, clips)
    lesson = output_dir / manifest["output"]["lesson"]
    print("2/6 Preparing the voice-only Edge-TTS lesson track.", flush=True)
    prepare_voice_only_lesson(speech, lesson)
    final_srt = subtitle_dir / "zh-TW.srt"
    write_final_srt(timing, final_srt)
    captioned_lesson = clips / f"{manifest['slug']}-lesson-captioned.mp4"
    print("3/6 Burning sentence-level Traditional Chinese captions.", flush=True)
    burn_lesson_captions(root, lesson, final_srt, captioned_lesson)
    print("4/6 Building the full-length XiNew opening-theme montage.", flush=True)
    opening = build_opening_montage(root, episode, manifest, clips)
    master = output_dir / manifest["output"]["master"]
    captioned = output_dir / manifest["output"]["captioned"]
    print("5/6 Prepending the opening theme to the clean lesson master.", flush=True)
    concatenate_program(opening, lesson, master)
    print("6/6 Prepending the opening theme to the captioned lesson.", flush=True)
    concatenate_program(opening, captioned_lesson, captioned)
    print(captioned)


if __name__ == "__main__":
    main()
