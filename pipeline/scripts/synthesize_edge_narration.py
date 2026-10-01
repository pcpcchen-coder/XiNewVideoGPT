#!/usr/bin/env python3
"""Synthesize sentence-level Traditional Chinese narration with Microsoft Edge TTS."""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import subprocess
import sys
import tempfile
import wave
from datetime import datetime, timezone
from pathlib import Path

import edge_tts


SAMPLE_RATE = 48_000
SENTENCE_GAP_SECONDS = 0.22


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def probe_duration(path: Path) -> float:
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


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def srt_time(seconds: float) -> str:
    milliseconds = max(0, round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


async def save_sentence(
    text: str,
    output: Path,
    *,
    voice: str,
    rate: str,
    pitch: str,
    volume: str,
) -> None:
    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            communicate = edge_tts.Communicate(
                text=text,
                voice=voice,
                rate=rate,
                pitch=pitch,
                volume=volume,
            )
            await communicate.save(str(output))
            if output.stat().st_size < 500:
                raise RuntimeError(f"Edge TTS returned a short file for: {text}")
            return
        except Exception as exc:  # network service retry
            last_error = exc
            if attempt < 3:
                await asyncio.sleep(attempt * 1.5)
    raise RuntimeError(f"Edge TTS failed after three attempts: {text}") from last_error


async def synthesize_scene(
    scene: dict,
    scene_index: int,
    temp_dir: Path,
    *,
    voice: str,
    rate: str,
    pitch: str,
    volume: str,
) -> list[Path]:
    outputs: list[Path] = []
    for sentence_index, sentence in enumerate(scene["sentences"], start=1):
        output = temp_dir / f"scene_{scene_index:02d}_sentence_{sentence_index:02d}.mp3"
        await save_sentence(
            sentence.get("tts", sentence["text"]),
            output,
            voice=voice,
            rate=rate,
            pitch=pitch,
            volume=volume,
        )
        outputs.append(output)
    return outputs


def combine_scene(sentence_mp3s: list[Path], output: Path) -> tuple[list[tuple[float, float]], float]:
    wavs: list[Path] = []
    for source in sentence_mp3s:
        wav_path = source.with_suffix(".wav")
        run(
            [
                "ffmpeg",
                "-y",
                "-v",
                "error",
                "-i",
                str(source),
                "-ar",
                str(SAMPLE_RATE),
                "-ac",
                "1",
                "-c:a",
                "pcm_s16le",
                str(wav_path),
            ]
        )
        wavs.append(wav_path)

    pcm_parts: list[bytes] = []
    timings: list[tuple[float, float]] = []
    cursor_frames = 0
    silence_frames = round(SENTENCE_GAP_SECONDS * SAMPLE_RATE)
    silence = b"\x00\x00" * silence_frames
    for index, wav_path in enumerate(wavs):
        with wave.open(str(wav_path), "rb") as source:
            if source.getframerate() != SAMPLE_RATE or source.getnchannels() != 1 or source.getsampwidth() != 2:
                raise RuntimeError(f"Unexpected PCM format: {wav_path}")
            frames = source.getnframes()
            start = cursor_frames / SAMPLE_RATE
            pcm_parts.append(source.readframes(frames))
            cursor_frames += frames
            end = cursor_frames / SAMPLE_RATE
            timings.append((start, end))
            if index < len(wavs) - 1:
                pcm_parts.append(silence)
                cursor_frames += silence_frames

    combined_wav = output.with_suffix(".wav")
    with wave.open(str(combined_wav), "wb") as target:
        target.setnchannels(1)
        target.setsampwidth(2)
        target.setframerate(SAMPLE_RATE)
        for part in pcm_parts:
            target.writeframes(part)
    run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-i",
            str(combined_wav),
            "-af",
            "highpass=f=55,lowpass=f=14500,loudnorm=I=-17:TP=-2:LRA=8",
            "-ar",
            str(SAMPLE_RATE),
            "-ac",
            "1",
            "-c:a",
            "libmp3lame",
            "-b:a",
            "160k",
            str(output),
        ]
    )
    combined_wav.unlink(missing_ok=True)
    return timings, probe_duration(output)


async def main_async() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("episode")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    episode = (root / args.episode).resolve()
    manifest = json.loads((episode / "production/manifest.json").read_text(encoding="utf-8"))
    narration = json.loads((episode / "production/narration.json").read_text(encoding="utf-8"))
    tts = manifest["tts"]
    voice = tts["voice"]
    if voice != "zh-TW-YunJheNeural":
        raise ValueError(f"This production requires zh-TW-YunJheNeural, got {voice}")

    audio_dir = episode / "audio"
    subtitle_dir = episode / "subtitles"
    audio_dir.mkdir(parents=True, exist_ok=True)
    subtitle_dir.mkdir(parents=True, exist_ok=True)
    timing_scenes: list[dict] = []
    tts_scenes: list[dict] = []
    absolute_cursor = 0.0
    srt_lines: list[str] = []
    cue_index = 1

    with tempfile.TemporaryDirectory(prefix="xinew-edge-tts-") as temp_name:
        temp_dir = Path(temp_name)
        for scene_index, scene in enumerate(narration, start=1):
            print(f"Edge TTS {scene_index:02d}/{len(narration):02d}: {scene['title']}", flush=True)
            sentence_mp3s = await synthesize_scene(
                scene,
                scene_index,
                temp_dir,
                voice=voice,
                rate=tts["rate"],
                pitch=tts["pitch"],
                volume=tts["volume"],
            )
            output = audio_dir / f"slide_{scene_index:02d}.mp3"
            sentence_timings, scene_duration = combine_scene(sentence_mp3s, output)
            sentence_records: list[dict] = []
            for sentence, (start, end) in zip(scene["sentences"], sentence_timings, strict=True):
                sentence_records.append({"text": sentence["text"], "start": round(start, 3), "end": round(end, 3)})
                srt_lines.extend(
                    [
                        str(cue_index),
                        f"{srt_time(absolute_cursor + start)} --> {srt_time(absolute_cursor + end)}",
                        sentence["text"],
                        "",
                    ]
                )
                cue_index += 1
            timing_scenes.append(
                {
                    "slide": scene_index,
                    "title": scene["title"],
                    "duration": round(scene_duration, 3),
                    "sentences": sentence_records,
                }
            )
            tts_scenes.append(
                {
                    "slide": scene_index,
                    "file": output.relative_to(episode).as_posix(),
                    "duration": round(scene_duration, 3),
                    "sha256": sha256(output),
                    "bytes": output.stat().st_size,
                    "sentences": [
                        {
                            "displayText": sentence["text"],
                            "spokenText": sentence.get("tts", sentence["text"]),
                        }
                        for sentence in scene["sentences"]
                    ],
                }
            )
            absolute_cursor += scene_duration

    timing = {
        "episode": manifest["episode"],
        "engine": tts["engine"],
        "voice": voice,
        "sourceDuration": round(absolute_cursor, 3),
        "sentenceGapSeconds": SENTENCE_GAP_SECONDS,
        "scenes": timing_scenes,
    }
    tts_manifest = {
        "episode": manifest["episode"],
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "engine": tts["engine"],
        "package": f"edge-tts {getattr(edge_tts, '__version__', 'unknown')}",
        "voice": voice,
        "locale": tts["locale"],
        "rate": tts["rate"],
        "pitch": tts["pitch"],
        "volume": tts["volume"],
        "sampleRate": SAMPLE_RATE,
        "scenes": tts_scenes,
    }
    (episode / "production/timing.json").write_text(
        json.dumps(timing, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (episode / "production/tts-manifest.json").write_text(
        json.dumps(tts_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (subtitle_dir / "zh-TW-source.srt").write_text("\n".join(srt_lines) + "\n", encoding="utf-8")
    print(f"Prepared {len(narration)} scenes / {cue_index - 1} sentence cues with {voice}.")


def main() -> None:
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        sys.exit(130)


if __name__ == "__main__":
    main()
