#!/usr/bin/env python3
"""Assemble an authored episode: user opening video + manifest-defined static scenes, narration only.

Same contract as EP05: opening video conformed to 1080p30, static slide
clips (no camera motion), fade-only transitions, NO background music under
the slides, two-step loudnorm to -16 LUFS, zh-TW subtitles shifted by intro.
"""
from __future__ import annotations

import sys
import argparse
import tempfile
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument("--episode", required=True)
args = parser.parse_args()
EP = (ROOT / args.episode).resolve()
_work = tempfile.TemporaryDirectory(prefix="xinew-assemble-")
WORK = Path(_work.name)

FPS = 30
OPENING_SRC = str(ROOT / "assets/opening/開場影片-v2.mp4")



def run(cmd: list[str]) -> str:
    if cmd[0] == "ffmpeg":
        # Bound decoder/encoder threads for this 8 GiB cloud environment.
        if "-i" in cmd:
            bounded = [cmd[0], "-filter_complex_threads", "1", "-filter_threads", "2"]
            for arg in cmd[1:-1]:
                if arg == "-i": bounded.extend(["-threads", "2"])
                bounded.append(arg)
            cmd = [*bounded, "-threads", "4", cmd[-1]]
        else:
            cmd = [cmd[0], "-filter_complex_threads", "1", *cmd[1:]]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"failed: {' '.join(cmd[:3])}...\n{r.stderr[-2500:]}")
    return r.stdout.strip()


def duration(path: Path) -> float:
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                      "-of", "default=nw=1:nk=1", str(path)]))


def static_clip(img: str, dur: float, out: Path) -> None:
    """Static shot — no camera motion, no temporal noise."""
    vf = ("scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
          "format=yuv420p,setsar=1,eq=contrast=1.015:brightness=0.003:saturation=1.03,"
          "vignette=angle=PI/4.8:dither=0")
    run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-i", img,
         "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
         "-vf", vf, "-t", f"{dur:.3f}", "-r", str(FPS), "-c:v", "libx264",
         "-preset", "veryfast", "-crf", "17", "-c:a", "aac", "-shortest", str(out)])


def scene_clip(slide: int, dur: float, out: Path) -> None:
    static_clip(str(EP / f"assets/slides/slide_{slide:02d}.png"), dur, out)


def srt_time(seconds: float) -> str:
    ms = max(0, round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, r = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{r:03d}"


def main() -> None:
    print("Preparing opening and scene clips", flush=True)
    (EP / "output").mkdir(exist_ok=True)
    manifest = json.loads((EP / "production/manifest.json").read_text(encoding="utf-8"))
    timing = json.loads((EP / "production/timing.json").read_text(encoding="utf-8"))
    transition_seconds = manifest["transitionSeconds"]
    scenes = timing["scenes"]

    # 1) clips: user-provided opening (conformed to 1080p30) + manifest-defined static scenes
    intro_clip = WORK / "clip-00.mp4"
    if not intro_clip.exists():
        run(["ffmpeg", "-y", "-v", "error", "-i", OPENING_SRC,
             "-vf", "scale=1920:1080:flags=lanczos,fps=30,format=yuv420p,setsar=1",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "17",
             "-ar", "48000", "-ac", "2", "-c:a", "aac", "-b:a", "192k", str(intro_clip)])

    intro_len = duration(intro_clip)
    clips = [intro_clip]
    durations = [duration(intro_clip)]
    for scene in scenes:
        print(f"Scene {scene['slide']:02d}/{len(scenes)}", flush=True)
        dur = scene["duration"]
        clip = WORK / f"clip-{scene['slide']:02d}.mp4"
        if not clip.exists():
            scene_clip(scene["slide"], dur, clip)
        clips.append(clip); durations.append(dur)

    # 2) pad all but last with freeze tail, then fade-only xfade chain
    print("Joining static scenes with gentle fades", flush=True)
    animated = WORK / "animated.mp4"
    if not animated.exists():
        padded = []
        for i, clip in enumerate(clips):
            out = WORK / f"pad-{i:02d}.mp4"
            if i < len(clips) - 1:
                run(["ffmpeg", "-y", "-v", "error", "-i", str(clip), "-vf",
                     f"tpad=stop_mode=clone:stop_duration={transition_seconds}",
                     "-c:v", "libx264", "-preset", "veryfast", "-crf", "17",
                     "-c:a", "copy", str(out)])
            else:
                shutil.copyfile(clip, out)
            padded.append(out)

        transitions = ["fade"] * 13  # gentle fades only, no motion transitions
        fc, last, elapsed = [], "0:v", 0.0
        for i in range(len(padded) - 1):
            offset = durations[i] if i == 0 else elapsed + durations[i]
            fc.append(f"[{last}][{i + 1}:v]xfade=transition={transitions[i % len(transitions)]}:"
                      f"duration={transition_seconds}:offset={offset:.3f}[v{i + 1}]")
            last = f"v{i + 1}"; elapsed = offset
        fc.append(f"[{last}]format=yuv420p,setsar=1[vout]")
        run(["ffmpeg", "-y", "-v", "error", *sum([["-i", str(c)] for c in padded], []),
             "-filter_complex", ";".join(fc), "-map", "[vout]", "-c:v", "libx264",
             "-preset", "medium", "-crf", "16", str(animated)])

    # 3) audio: opening video's own theme-song audio + scene narration (NO BGM)
    print("Assembling narration and mastering audio", flush=True)
    parts = [intro_clip] + [EP / s["audio"] for s in scenes]
    base_audio = WORK / "base-audio.m4a"
    ins = sum([["-i", str(p)] for p in parts], [])
    fc_in = "".join(f"[{i}:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
                    f"apad,atrim=duration={durations[i]:.9f},asetpts=PTS-STARTPTS[a{i}];"
                    for i in range(len(parts)))
    fc_in += "".join(f"[a{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=0:a=1[aout]"
    run(["ffmpeg", "-y", "-v", "error", *ins, "-filter_complex", fc_in,
         "-map", "[aout]", "-c:a", "aac", "-b:a", "192k", str(base_audio)])

    # 4) no background music under slides — narration only (per spec)
    mixed = base_audio

    # 5) Measured mastering: target -16 LUFS, accepted -18 to -14; preserve source waveform when feasible.
    normed = WORK / "normed.wav"
    analysis = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(mixed), "-af",
        "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
        capture_output=True, text=True, check=True)
    stats = json.loads(analysis.stderr[analysis.stderr.rfind("{"):])
    gain = min(-16 - float(stats["input_i"]), -1.5 - float(stats["input_tp"]) - .1)
    predicted = float(stats["input_i"]) + gain
    if -18 <= predicted <= -14:
        norm_filter = f"volume={gain:.6f}dB"
        norm_method = "measured constant gain; source waveform and peak headroom preserved"
    else:
        norm_filter = ("loudnorm=I=-16:TP=-1.5:LRA=11:linear=true:"
            f"measured_I={stats['input_i']}:measured_TP={stats['input_tp']}:"
            f"measured_LRA={stats['input_lra']}:measured_thresh={stats['input_thresh']}:offset={stats['target_offset']}")
        norm_method = "two-pass loudnorm"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(mixed),
         "-af", norm_filter, "-c:a", "pcm_s16le", str(normed)])
    (EP / "qc/loudness-normalization.json").write_text(json.dumps({
        "method": norm_method, "analysis": stats, "secondPassFilter": norm_filter,
        "predictedIntegratedLUFS": predicted, "requestedRangeLUFS": [-18, -14]}, indent=2) + "\n")
    master = EP / "output" / f"{EP.name}-master.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(animated), "-i", str(normed),
         "-map", "0:v", "-map", "1:a", "-ar", "48000", "-ac", "2",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(master)])

    # 6) zh-TW subtitle shifted by intro length, burned copy
    print("Writing full-program subtitles and captioned video", flush=True)
    src_srt = (EP / "subtitles/zh-TW-source.srt").read_text(encoding="utf-8").strip().split("\n\n")
    cues = []
    for block in src_srt:
        lines = block.splitlines()
        if len(lines) < 3: continue
        idx, rng, text = lines[0], lines[1], " ".join(lines[2:])
        st, en = rng.split(" --> ")
        def parse(t: str) -> float:
            h, m, rest = t.split(":"); s, ms = rest.split(",")
            return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
        cues.append(f"{len(cues) + 1}\n{srt_time(parse(st) + intro_len)} --> "
                    f"{srt_time(parse(en) + intro_len)}\n{text}\n")
    (EP / "subtitles/zh-TW.srt").write_text("\n".join(cues) + "\n", encoding="utf-8")

    style = ("FontName=Noto Sans CJK TC,FontSize=14,Bold=1,PrimaryColour=&H00FFFFFF,"
             "OutlineColour=&H7A000000,BackColour=&H7A000000,BorderStyle=1,Outline=1.2,"
             "Shadow=0,Alignment=2,MarginV=18,MarginL=24,MarginR=24")
    zh = EP / "output" / f"{EP.name}-zh-TW.mp4"
    filters = run(["ffmpeg", "-hide_banner", "-filters"])
    if " subtitles " in filters:
        run(["ffmpeg", "-y", "-v", "error", "-i", str(master), "-vf",
             f"subtitles='{EP}/subtitles/zh-TW.srt':fontsdir='{ROOT}/assets/fonts':force_style='{style}'",
             "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-c:a", "copy", str(zh)])
    else:
        run([sys.executable, str(ROOT / "pipeline/scripts/burn_subtitles_pillow.py"),
             "--input", str(master), "--srt", str(EP / "subtitles/zh-TW.srt"),
             "--font", str(ROOT / "assets/fonts/NotoSansCJKtc-Regular.otf"), "--output", str(zh)])


    # 7) thumbnail + contact sheet
    import time
    for attempt in range(6):
        try:
            shutil.copyfile(EP / "assets/slides/slide_01.png", EP / "output/thumbnail.png")
            if (EP / "output/thumbnail.png").stat().st_size > 10000:
                break
        except OSError:
            time.sleep(1)
    frames_dir = WORK / "frames"; frames_dir.mkdir(exist_ok=True)
    run(["ffmpeg", "-y", "-v", "error", "-i", str(master), "-vf",
         "fps=1/20,scale=480:270", str(frames_dir / "f%03d.png")])
    from PIL import Image
    files = sorted(frames_dir.glob("f*.png"))[:14]
    cols = 4; rows = (len(files) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 480, rows * 270), (4, 18, 34))
    for i, f in enumerate(files):
        sheet.paste(Image.open(f), ((i % cols) * 480, (i // cols) * 270))
    sheet.save(EP / "output/contact-sheet.png")

    (EP / "qc").mkdir(exist_ok=True)
    (EP / "qc/assembly.json").write_text(json.dumps({
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "version": "opening v2 (native 1080p30) + static scenes, narration only",
        "scenes": len(scenes),
        "opening": {"file": OPENING_SRC, "seconds": durations[0],
                    "note": "User-supplied opening v2; duration measured during this build"},
        "backgroundMusic": "none — narration only under slides",
        "animated": str(animated), "master": str(master), "zh": str(zh),
        "masterDuration": duration(master), "loudnessNormalization": norm_method,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("master:", master, f"{duration(master):.2f}s")


if __name__ == "__main__":
    main()
