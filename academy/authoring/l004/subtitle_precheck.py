"""Pre-TTS caption layout check for L004 (no audio needed, no timing claimed).

Burns every narration sentence onto its own rendered slide with the exact libass
style used by pipeline/scripts/assemble_episode.py, then measures where the caption
lands and whether it touches slide content. It does NOT replace the post-assembly
check of the real captioned video; timings are unknown until TTS runs.

    ./portable-runtime.sh python authoring/l004/subtitle_precheck.py
"""
from pathlib import Path
import json
import subprocess
import tempfile

import numpy as np
from PIL import Image

R = Path(__file__).resolve().parents[2]
E = R / 'episodes/academy/l004-network-relay'
STYLE = ("FontName=Noto Sans CJK TC,FontSize=16,Bold=1,PrimaryColour=&H00FFFFFF,"
         "OutlineColour=&H7A000000,BackColour=&H7A000000,BorderStyle=1,Outline=1.2,"
         "Shadow=0,Alignment=2,MarginV=20,MarginL=24,MarginR=24")
_ASSEMBLER = (R / 'pipeline/scripts/assemble_episode.py').read_text(encoding='utf-8')
for _part in ('"FontName=Noto Sans CJK TC,FontSize=16,Bold=1,PrimaryColour=&H00FFFFFF,"',
              '"OutlineColour=&H7A000000,BackColour=&H7A000000,BorderStyle=1,Outline=1.2,"',
              '"Shadow=0,Alignment=2,MarginV=20,MarginL=24,MarginR=24"'):
    assert _part in _ASSEMBLER and _part.strip('"') in STYLE, 'burn style changed in assembler'


def frame(cmd):
    raw = subprocess.run(cmd, check=True, capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.uint8).reshape(1080, 1920, 3).astype(np.int16)


def main():
    narration = json.loads((E / 'production/narration.json').read_text(encoding='utf-8'))
    results, keep = [], E / 'qc/subtitle-precheck'
    keep.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='xinew-subcheck-') as t:
        t = Path(t)
        for scene in narration:
            png = E / f"assets/slides/slide_{scene['slide']:02d}.png"
            base = ['ffmpeg', '-v', 'error', '-loop', '1', '-i', str(png), '-frames:v', '1']
            tail = ['-pix_fmt', 'rgb24', '-f', 'rawvideo', '-']
            clean = frame([*base, '-vf', 'scale=1920:1080,format=rgb24', *tail])
            for i, sentence in enumerate(scene['sentences'], 1):
                srt = t / f"s{scene['slide']:02d}-{i}.srt"
                srt.write_text(f"1\n00:00:00,000 --> 00:00:05,000\n{sentence['text']}\n", encoding='utf-8')
                vf = f"scale=1920:1080,subtitles='{srt}':fontsdir='{R}/assets/fonts':force_style='{STYLE}',format=rgb24"
                burned = frame([*base, '-vf', vf, *tail])
                diff = np.abs(burned - clean).sum(axis=2) > 24
                ys, xs = np.where(diff)
                assert len(ys), ('caption not rendered', scene['slide'], i)
                top, bottom, left, right = int(ys.min()), int(ys.max()), int(xs.min()), int(xs.max())
                # Slide content inside the caption band: pixels far from the dark background.
                band = clean[top:bottom + 1]
                bright = (band.max(axis=2) > 110)
                content_px = int(bright.sum())
                lines = 1 if bottom - top < 90 else 2 if bottom - top < 170 else 3
                results.append({'slide': scene['slide'], 'sentence': i, 'chars': len(sentence['text']),
                                'top': top, 'bottom': bottom, 'left': left, 'right': right, 'lines': lines,
                                'slideContentPixelsUnderCaption': content_px})
                if i == 1 or lines > 2 or content_px:
                    Image.fromarray(burned.astype(np.uint8)).resize((960, 540)).save(keep / f"slide_{scene['slide']:02d}_s{i}.png")
    summary = {
        'method': 'each of 36 sentences burned on its own slide PNG with the assembler libass style; bbox from pixel diff',
        'burnStyle': STYLE, 'cues': len(results),
        'topMin': min(x['top'] for x in results), 'bottomMax': max(x['bottom'] for x in results),
        'leftMin': min(x['left'] for x in results), 'rightMax': max(x['right'] for x in results),
        'maxLines': max(x['lines'] for x in results),
        'cuesTouchingSlideContent': [f"{x['slide']}-{x['sentence']}" for x in results if x['slideContentPixelsUnderCaption']],
        'limits': 'static pre-check only; real cue timing, fades and the final captioned MP4 are unchecked until TTS/assembly',
        'results': results}
    summary['passed'] = (summary['cues'] == 36 and summary['maxLines'] <= 2 and summary['leftMin'] >= 24
                         and summary['rightMax'] <= 1896 and summary['bottomMax'] <= 1040
                         and not summary['cuesTouchingSlideContent'])
    (E / 'qc/subtitle-precheck.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print({k: v for k, v in summary.items() if k != 'results'})
    if not summary['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
