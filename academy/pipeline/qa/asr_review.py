"""Machine listening check for an academy episode (NOT a human listening review).

Cuts the audio of the final captioned MP4 at every cue of the delivered full-program
SRT, transcribes each clip with a local faster-whisper model and compares it with the
cue text. A clip that matches its own cue shows that the spoken sentence is present
and sits inside that cue's time window (audio/caption sync), for all 36 cues.

Optional tooling, not part of the series pipeline:
    python -m venv /path/asr && /path/asr/bin/pip install faster-whisper zhconv
    /path/asr/bin/python pipeline/qa/asr_review.py --episode episodes/academy/<slug> --model /path/to/faster-whisper-small

The model directory must already exist locally; nothing is downloaded here. Only the
finished public audio is processed, locally. ASR mistakes on names/acronyms are expected;
low scores are prompts for a human to listen, not proof of a defect.
"""
from pathlib import Path
import argparse
import difflib
import json
import re
import subprocess
import tempfile
import wave

import numpy as np

R = Path(__file__).resolve().parents[2]


def seconds(t):
    h, m, rest = t.split(':'); s, ms = rest.split(',')
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def norm(text):
    import zhconv
    text = zhconv.convert(text, 'zh-hans').lower()
    return re.sub(r'[^0-9a-z一-鿿]', '', text)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--model', required=True, type=Path)
    p.add_argument('--episode', required=True, type=Path)
    args = p.parse_args()
    E = (R / args.episode).resolve()
    if not args.model.is_dir():
        raise SystemExit('Supply an existing local model directory; no implicit download')
    from faster_whisper import WhisperModel
    engine = WhisperModel(str(args.model.resolve()), device='cpu', compute_type='int8', local_files_only=True)
    video = E / 'output' / f'{E.name}-zh-TW.mp4'
    blocks = [b.splitlines() for b in (E / 'subtitles/zh-TW.srt').read_text(encoding='utf-8').strip().split('\n\n')]
    cues = [(seconds(b[1].split(' --> ')[0]), seconds(b[1].split(' --> ')[1]), ' '.join(b[2:])) for b in blocks]
    assert len(cues) == 36
    rows = []
    with tempfile.TemporaryDirectory(prefix='xinew-asr-') as t:
        for i, (start, end, text) in enumerate(cues, 1):
            clip = Path(t) / f'cue{i:02d}.wav'
            subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{start:.3f}', '-to', f'{end + 0.18:.3f}', '-i', str(video),
                            '-vn', '-ac', '1', '-ar', '16000', '-c:a', 'pcm_s16le', str(clip)], check=True)
            with wave.open(str(clip)) as w:  # decode here; avoids PyAV version differences
                audio = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
            segments, _ = engine.transcribe(audio, language='zh', beam_size=5, vad_filter=False,
                                            condition_on_previous_text=False, initial_prompt='以下是繁體中文的教學旁白。')
            heard = ''.join(s.text for s in segments).strip()
            a, b = norm(text), norm(heard)
            ratio = difflib.SequenceMatcher(None, a, b).ratio()
            rows.append({'cue': i, 'slide': (i - 1) // 3 + 1, 'start': start, 'end': end, 'text': text, 'heard': heard,
                         'similarity': round(ratio, 3), 'headMatch': a[:4] == b[:4], 'tailMatch': a[-4:] == b[-4:]})
            print(f"{i:02d} {ratio:.2f} {heard}", flush=True)
    report = {
        'method': 'faster-whisper (local, CPU int8) on audio cut from the final captioned MP4 at each delivered SRT cue; '
                  'simplified/traditional and punctuation normalised before comparison',
        'model': args.model.name, 'video': video.name, 'cues': len(rows),
        'minSimilarity': min(r['similarity'] for r in rows),
        'meanSimilarity': round(sum(r['similarity'] for r in rows) / len(rows), 3),
        'below0_80': [r['cue'] for r in rows if r['similarity'] < 0.80],
        'limits': 'machine transcription, not human listening; cannot judge tone, naturalness, or subtle mispronunciation',
        'rows': rows}
    (E / 'qc/asr-review.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print({k: v for k, v in report.items() if k != 'rows'})


if __name__ == '__main__':
    main()
