"""Measured audio/picture evidence for the L004 manual review (run after assemble + delivery).

Produces qc/media-review.json plus frames taken from the FINAL captioned MP4:
- one frame at the midpoint of each of the 36 delivered SRT cues (9 contact sheets),
- opening, opening→lesson fade, and one scene→scene fade.
Audio: per-scene lag and correlation between the master's audio and this lesson's own
scene narration files, the opening audio against the shared opening source, and the
quietest 50 ms inside every scene (a music bed would keep that floor high).

These are machine measurements to support, not replace, looking and listening.

    ./portable-runtime.sh python authoring/l004/media_review.py
"""
from pathlib import Path
import json
import subprocess

import numpy as np
from PIL import Image

R = Path(__file__).resolve().parents[2]
E = R / 'episodes/academy/l004-network-relay'
MASTER = E / 'output/l004-network-relay-master.mp4'
ZH = E / 'output/l004-network-relay-zh-TW.mp4'
SR = 48000


def pcm(path, start=None, dur=None):
    cmd = ['ffmpeg', '-v', 'error']
    if start is not None: cmd += ['-ss', f'{start:.6f}']
    if dur is not None: cmd += ['-t', f'{dur:.6f}']
    cmd += ['-i', str(path), '-vn', '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-']
    return np.frombuffer(subprocess.run(cmd, check=True, capture_output=True).stdout, dtype=np.float32).astype(np.float64)


def lag_and_corr(a, b, max_lag=int(0.25 * SR)):
    """Lag (samples) of a relative to b maximising correlation, searched within ±max_lag."""
    n = min(len(a), len(b)) - 2 * max_lag
    ref = b[max_lag:max_lag + n]
    best = (-2.0, 0)
    step = 8
    for lag in list(range(-max_lag, max_lag + 1, step)):
        seg = a[max_lag + lag:max_lag + lag + n]
        c = float(np.dot(seg, ref) / (np.linalg.norm(seg) * np.linalg.norm(ref) + 1e-12))
        if c > best[0]: best = (c, lag)
    for lag in range(best[1] - step, best[1] + step + 1):
        seg = a[max_lag + lag:max_lag + lag + n]
        c = float(np.dot(seg, ref) / (np.linalg.norm(seg) * np.linalg.norm(ref) + 1e-12))
        if c > best[0]: best = (c, lag)
    return best[1], best[0]


def frame(t, out, size=(960, 540)):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.3f}', '-i', str(ZH), '-frames:v', '1',
                          '-vf', f'scale={size[0]}:{size[1]}', '-pix_fmt', 'rgb24', '-f', 'rawvideo', '-'],
                         check=True, capture_output=True).stdout
    im = Image.frombytes('RGB', size, raw)
    if out: im.save(out)
    return im


def seconds(t):
    h, m, rest = t.split(':'); s, ms = rest.split(',')
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def main():
    timing = json.loads((E / 'production/timing.json').read_text(encoding='utf-8'))
    assembly = json.loads((E / 'qc/assembly.json').read_text(encoding='utf-8'))
    intro = float(assembly['opening']['seconds'])
    frames = E / 'qc/video-frames'; frames.mkdir(parents=True, exist_ok=True)

    # --- audio: scene narration vs master, floor level, opening vs source
    scenes, cursor = [], intro
    for s in timing['scenes']:
        dur = 12.0
        a = pcm(MASTER, cursor - 0.25, dur + 0.5)
        b = pcm(E / s['audio'], 0, dur)
        b = np.concatenate([np.zeros(int(0.25 * SR)), b, np.zeros(int(0.25 * SR))])
        lag, corr = lag_and_corr(a, b, max_lag=int(0.2 * SR))
        whole = pcm(MASTER, cursor, s['duration'])
        win = int(0.05 * SR)
        rms = np.sqrt(np.mean(whole[:len(whole) // win * win].reshape(-1, win) ** 2, axis=1))
        scenes.append({'slide': s['slide'], 'start': round(cursor, 3), 'lagMs': round(1000 * lag / SR, 2),
                       'correlation': round(corr, 6),
                       'quietest50msDbfs': round(20 * np.log10(max(rms.min(), 1e-9)), 1),
                       'loudest50msDbfs': round(20 * np.log10(rms.max()), 1)})
        cursor += s['duration']
    opening = R / 'assets/opening/開場影片-v2.mp4'
    lag, corr = lag_and_corr(np.concatenate([np.zeros(int(0.2 * SR)), pcm(MASTER, 5, 30)]),
                             np.concatenate([np.zeros(int(0.2 * SR)), pcm(opening, 5, 30)]), max_lag=int(0.15 * SR))
    tail = pcm(MASTER, cursor - 0.3, 5)

    # --- picture: every delivered cue, from the captioned file
    blocks = [b.splitlines() for b in (E / 'subtitles/zh-TW.srt').read_text(encoding='utf-8').strip().split('\n\n')]
    cues = [(seconds(b[1].split(' --> ')[0]), seconds(b[1].split(' --> ')[1])) for b in blocks]
    assert len(cues) == 36
    shots = [frame((a + b) / 2, None) for a, b in cues]
    for k in range(9):
        sheet = Image.new('RGB', (1920, 1080))
        for j in range(4):
            sheet.paste(shots[k * 4 + j], ((j % 2) * 960, (j // 2) * 540))
        sheet.save(frames / f'cues_{k * 4 + 1:02d}-{k * 4 + 4:02d}.jpg', quality=88)
    frame(30.0, frames / 'opening.png')
    frame(intro + 0.27, frames / 'opening-transition.png')
    boundary = intro + sum(s['duration'] for s in timing['scenes'][:6])
    frame(boundary + 0.27, frames / 'scene-06-07-transition.png')
    frame(cursor - 1.0, frames / 'final-second.png')

    report = {
        'method': 'ffmpeg-decoded 48 kHz mono; normalised cross-correlation of 12 s per scene (±200 ms search); '
                  '50 ms RMS windows over each full scene; frames decoded from the captioned MP4',
        'openingSeconds': intro,
        'openingVsSource': {'lagMs': round(1000 * lag / SR, 2), 'correlation': round(corr, 6), 'window': '5–35 s'},
        'scenes': scenes,
        'maxAbsLagMs': max(abs(x['lagMs']) for x in scenes),
        'minCorrelation': min(x['correlation'] for x in scenes),
        'highestQuietFloorDbfs': max(x['quietest50msDbfs'] for x in scenes),
        'audioAfterLastSceneDbfs': round(20 * np.log10(max(float(np.sqrt(np.mean(tail ** 2))), 1e-9)), 1) if len(tail) else None,
        'cueFrames': {'count': len(shots), 'sheets': sorted(p.name for p in frames.glob('cues_*.jpg'))},
        'limits': 'correlation and noise floor indicate that scene audio is this lesson\'s narration with no added bed; '
                  'they do not judge pronunciation or tone',
    }
    (E / 'qc/media-review.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'scenes'}, ensure_ascii=False, indent=1))
    for x in scenes: print(x)


if __name__ == '__main__':
    main()
