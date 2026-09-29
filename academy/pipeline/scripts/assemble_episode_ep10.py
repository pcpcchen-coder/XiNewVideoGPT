#!/usr/bin/env python3
"""Assemble EP10: user opening video + 12 static scenes, narration only.

Same contract as EP05: opening video conformed to 1080p30, static slide
clips (no camera motion), fade-only transitions, NO background music under
the slides, two-step loudnorm to -16 LUFS, zh-TW subtitles shifted by intro.
"""
from __future__ import annotations

import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EP = ROOT / "episodes/season-01/ep10-ai-and-our-future"
WORK = Path("/tmp/ep10-assemble"); WORK.mkdir(parents=True, exist_ok=True)

FPS = 30
OPENING_SRC = "/mnt/agents/output/XiNewVideoGPT/assets/opening/開場影片-v2.mp4"
INTRO_LEN = 60.267  # opening v2 duration (ffprobe: 60.266667s, native 1080p30)


def run(cmd: list[str]) -> str:
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
          "vignette=PI/4.8")
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
    manifest = json.loads((EP / "production/manifest.json").read_text(encoding="utf-8"))
    timing = json.loads((EP / "production/timing.json").read_text(encoding="utf-8"))
    transition_seconds = manifest["transitionSeconds"]
    scenes = timing["scenes"]

    # 1) clips: user-provided opening (conformed to 1080p30) + 12 static scenes
    intro_clip = WORK / "clip-00.mp4"
    if not intro_clip.exists():
        run(["ffmpeg", "-y", "-v", "error", "-i", OPENING_SRC,
             "-vf", "scale=1920:1080:flags=lanczos,fps=30,format=yuv420p,setsar=1",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "17",
             "-ar", "48000", "-ac", "2", "-c:a", "aac", "-b:a", "192k", str(intro_clip)])

    clips = [intro_clip]
    durations = [duration(intro_clip)]
    for scene in scenes:
        dur = scene["duration"]
        clip = WORK / f"clip-{scene['slide']:02d}.mp4"
        if not clip.exists():
            scene_clip(scene["slide"], dur, clip)
        clips.append(clip); durations.append(dur)

    # 2) pad all but last with freeze tail, then fade-only xfade chain
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
    parts = [intro_clip] + [EP / s["audio"] for s in scenes]
    base_audio = WORK / "base-audio.m4a"
    ins = sum([["-i", str(p)] for p in parts], [])
    fc_in = "".join(f"[{i}:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo[a{i}];"
                    for i in range(len(parts)))
    fc_in += "".join(f"[a{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=0:a=1[aout]"
    run(["ffmpeg", "-y", "-v", "error", *ins, "-filter_complex", fc_in,
         "-map", "[aout]", "-c:a", "aac", "-b:a", "192k", str(base_audio)])

    # 4) no background music under slides — narration only (per spec)
    mixed = base_audio

    # 5) master + loudness target -16 LUFS (two-step to dodge loudnorm reinit bug)
    normed = WORK / "normed.wav"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(mixed),
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:a", "pcm_s16le", str(normed)])
    master = EP / "output/ep10-ai-and-our-future-master.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(animated), "-i", str(normed),
         "-map", "0:v", "-map", "1:a", "-ar", "48000", "-ac", "2",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(master)])

    # 6) zh-TW subtitle shifted by intro length, burned copy
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
        cues.append(f"{len(cues) + 1}\n{srt_time(parse(st) + INTRO_LEN)} --> "
                    f"{srt_time(parse(en) + INTRO_LEN)}\n{text}\n")
    (EP / "subtitles/zh-TW.srt").write_text("\n".join(cues) + "\n", encoding="utf-8")

    style = ("FontName=Noto Sans CJK TC,FontSize=14,Bold=1,PrimaryColour=&H00FFFFFF,"
             "OutlineColour=&H7A000000,BackColour=&H7A000000,BorderStyle=1,Outline=1.2,"
             "Shadow=0,Alignment=2,MarginV=60,MarginL=110,MarginR=110")
    zh = EP / "output/ep10-ai-and-our-future-zh-TW.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(master), "-vf",
         f"subtitles='{EP}/subtitles/zh-TW.srt':force_style='{style}'",
         "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-c:a", "copy", str(zh)])

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
                    "note": "new theme-song animation v2 supplied by user, native 1080p30, audio correlates 0.988 with 犀牛角亮起來短版"},
        "backgroundMusic": "none — narration only under slides",
        "animated": str(animated), "master": str(master), "zh": str(zh),
        "masterDuration": duration(master),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("master:", master, f"{duration(master):.2f}s")


if __name__ == "__main__":
    main()
