"""Contact sheets for looking at a lesson: slides (4 per sheet), print pack pages, special video frames.

Review aid only; writes JPEGs to --out (use a scratch folder, nothing here is a deliverable).

    ./portable-runtime.sh python pipeline/qa/review_sheets.py --episode episodes/academy/<slug> --out /tmp/review [--what slides|print|special]
"""
from pathlib import Path
import argparse
import subprocess
import tempfile

from PIL import Image

R = Path(__file__).resolve().parents[2]


def grid(images, out, cell=(960, 540), cols=2):
    rows = (len(images) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * cell[0], rows * cell[1]), 'gray')
    for j, im in enumerate(images):
        sheet.paste(im.convert('RGB').resize(cell), ((j % cols) * cell[0], (j // cols) * cell[1]))
    sheet.save(out, quality=90)
    print(out)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--episode', required=True, type=Path)
    p.add_argument('--out', required=True, type=Path)
    p.add_argument('--what', default='slides', choices=['slides', 'print', 'special'])
    a = p.parse_args()
    E = (R / a.episode).resolve()
    a.out.mkdir(parents=True, exist_ok=True)
    tag = E.name.split('-')[0]
    if a.what == 'slides':
        files = sorted((E / 'assets/slides').glob('slide_*.png'))
        assert len(files) == 12
        for k in range(0, 12, 4):
            grid([Image.open(f) for f in files[k:k + 4]], a.out / f'{tag}-slides-{k // 4 + 1}.jpg')
    elif a.what == 'print':
        pdf = next((E / 'classroom').glob('*/*.pdf'))
        with tempfile.TemporaryDirectory() as t:
            subprocess.run(['pdftoppm', '-r', '100', '-png', str(pdf), f'{t}/p'], check=True)
            pages = [Image.open(f).copy() for f in sorted(Path(t).glob('p*.png'))]
        for k in range(0, len(pages), 2):
            grid(pages[k:k + 2], a.out / f'{tag}-print-{k // 2 + 1}.jpg', cell=(827, 1169), cols=2)
    else:
        v = E / 'qc/video-frames'
        grid([Image.open(v / n) for n in ('opening.png', 'opening-transition.png', 'scene-06-07-transition.png', 'final-second.png')],
             a.out / f'{tag}-special.jpg')


if __name__ == '__main__':
    main()
