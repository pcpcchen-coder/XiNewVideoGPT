#!/usr/bin/env python3
"""Create delivery thumbnail and contact sheet from the final deck renders."""

from __future__ import annotations

import argparse
import json
import math
import shutil
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def safe_save(im: Image.Image, out: Path, **kwargs) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(prefix="xinew-", suffix=out.suffix, dir="/tmp", delete=False) as fh:
        temp = Path(fh.name)
    try:
        im.save(temp, **kwargs)
        with Image.open(temp) as probe:
            probe.verify()
        shutil.copyfile(temp, out)
    finally:
        temp.unlink(missing_ok=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", required=True)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[2]
    ep = (root / args.episode).resolve()
    manifest = json.loads((ep / "production/manifest.json").read_text(encoding="utf-8"))
    slides = [ep / f"assets/slides/slide_{n:02d}.png" for n in range(1, manifest["slideCount"] + 1)]
    missing = [str(p) for p in slides if not p.exists()]
    if missing:
        raise FileNotFoundError(f"Missing deck renders: {missing}")

    hero = Image.open(slides[0]).convert("RGB").resize((1280, 720), Image.Resampling.LANCZOS)
    safe_save(hero, ep / "output/thumbnail.jpg", quality=92, optimize=True)

    thumb_w, thumb_h = 480, 270
    columns = 3
    rows = math.ceil(len(slides) / columns)
    sheet = Image.new("RGB", (thumb_w * columns + 80, thumb_h * rows + 130), (4, 18, 34))
    draw = ImageDraw.Draw(sheet)
    font_path = root / "assets/fonts/NotoSansCJKtc-Regular.otf"
    title_font = ImageFont.truetype(str(font_path), 30)
    number_font = ImageFont.truetype(str(font_path), 18)
    draw.text((35, 25), "S01E01 完整重製 · CONTACT SHEET", font=title_font, fill=(255, 193, 47))
    for i, slide_path in enumerate(slides):
        image = Image.open(slide_path).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = 35 + (i % columns) * thumb_w
        y = 90 + (i // columns) * thumb_h
        sheet.paste(image, (x, y))
        draw.rectangle((x, y, x + 54, y + 34), fill=(4, 18, 34))
        draw.text((x + 10, y + 5), f"{i + 1:02d}", font=number_font, fill=(255, 193, 47))
    safe_save(sheet, ep / "qc/contact-sheet.jpg", quality=90, optimize=True)
    print(f"Prepared thumbnail and {len(slides)}-slide contact sheet.")


if __name__ == "__main__":
    main()
