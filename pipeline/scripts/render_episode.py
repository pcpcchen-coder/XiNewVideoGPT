#!/usr/bin/env python3
"""Render XiNew-branded slides, thumbnail, and contact sheet."""

from __future__ import annotations

import argparse
import json
import math
import shutil
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


W, H = 1920, 1080
NAVY = (4, 18, 34)
NAVY_2 = (7, 31, 55)
BLUE = (25, 130, 196)
GOLD = (255, 193, 47)
WHITE = (247, 247, 248)
MUTED = (168, 184, 201)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def background() -> Image.Image:
    im = Image.new("RGB", (W, H), NAVY)
    px = im.load()
    for y in range(H):
        t = y / (H - 1)
        for x in range(W):
            glow = max(0.0, 1.0 - math.hypot((x - 1450) / 1200, (y - 350) / 850))
            px[x, y] = (
                int(NAVY[0] * (1 - t) + NAVY_2[0] * t + glow * 3),
                int(NAVY[1] * (1 - t) + NAVY_2[1] * t + glow * 12),
                int(NAVY[2] * (1 - t) + NAVY_2[2] * t + glow * 20),
            )
    d = ImageDraw.Draw(im, "RGBA")
    for y in (110, 930):
        d.line((48, y, W - 48, y), fill=(*BLUE, 90), width=2)
    for row in range(4):
        y = 180 + row * 170
        d.line((1420, y, 1510, y, 1545, y + 35, 1770, y + 35), fill=(*BLUE, 42), width=3)
        for x in (1420, 1770):
            d.ellipse((x - 5, y - 5, x + 5, y + 5), fill=(*BLUE, 90))
    return im


def fit_inside(im: Image.Image, size: tuple[int, int]) -> Image.Image:
    copy = im.copy()
    copy.thumbnail(size, Image.Resampling.LANCZOS)
    return copy


def rounded_paste(base: Image.Image, src: Image.Image, box: tuple[int, int, int, int], radius: int = 28) -> None:
    x, y, w, h = box
    fitted = fit_inside(src.convert("RGB"), (w, h))
    panel = Image.new("RGB", (w, h), WHITE)
    panel.paste(fitted, ((w - fitted.width) // 2, (h - fitted.height) // 2))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w, h), radius=radius, fill=255)
    glow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow, "RGBA")
    gd.rounded_rectangle((x - 10, y - 10, x + w + 10, y + h + 10), radius=radius + 8, fill=(*BLUE, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(18))
    base.paste(glow, (0, 0), glow)
    base.paste(panel, (x, y), mask)
    ImageDraw.Draw(base, "RGBA").rounded_rectangle((x, y, x + w, y + h), radius=radius, outline=(*BLUE, 175), width=4)


def alpha_crop(im: Image.Image) -> Image.Image:
    rgba = im.convert("RGBA")
    box = rgba.getchannel("A").getbbox()
    if not box:
        raise ValueError("Character cutout has no visible pixels")
    return rgba.crop(box)


def safe_save(im: Image.Image, out: Path, **kwargs) -> None:
    """Write through /tmp and verify; some mounted workspaces truncate large PNG writes."""
    out.parent.mkdir(parents=True, exist_ok=True)
    suffix = out.suffix or ".png"
    for attempt in range(1, 4):
        with tempfile.NamedTemporaryFile(prefix="xinew-", suffix=suffix, dir="/tmp", delete=False) as fh:
            temp = Path(fh.name)
        try:
            im.save(temp, **kwargs)
            with Image.open(temp) as probe:
                probe.verify()
            shutil.copyfile(temp, out)
            with Image.open(out) as probe:
                probe.verify()
            return
        except (OSError, SyntaxError):
            if attempt == 3:
                raise
        finally:
            temp.unlink(missing_ok=True)


def add_character(base: Image.Image, cutout: Image.Image, pose: str) -> None:
    char = alpha_crop(cutout)
    target_h = 850 if pose != "pointer" else 800
    char = char.resize((round(char.width * target_h / char.height), target_h), Image.Resampling.LANCZOS)
    x = W - char.width - 35
    if pose == "pointer":
        x = W - char.width + 20
    y = 942 - char.height
    shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    alpha = char.getchannel("A").filter(ImageFilter.GaussianBlur(18))
    shade = Image.new("RGBA", char.size, (0, 0, 0, 125))
    shade.putalpha(alpha)
    shadow.paste(shade, (x + 14, y + 18), shade)
    base.paste(shadow, (0, 0), shadow)
    base.paste(char, (x, y), char)


def header(draw: ImageDraw.ImageDraw, cjk: Path, n: int, title: str) -> None:
    draw.text((64, 35), "CHEN", font=font(cjk, 34), fill=WHITE)
    draw.text((190, 35), "XiNew", font=font(cjk, 34), fill=GOLD)
    draw.text((310, 45), "TECH CLASS", font=font(cjk, 18), fill=MUTED)
    draw.rounded_rectangle((1550, 36, 1848, 88), radius=22, outline=(*GOLD, 210), width=2, fill=(3, 14, 27, 190))
    draw.text((1574, 49), f"EP01  ·  {n:02d}/10", font=font(cjk, 20), fill=GOLD)
    draw.text((64, 956), title, font=font(cjk, 23), fill=MUTED)
    draw.text((1728, 956), "XINEW SAYS", font=font(cjk, 19), fill=GOLD)


def render_slide(source: Path, cutout: Path, out: Path, cjk: Path, n: int, title: str, pose: str) -> None:
    canvas = background()
    rounded_paste(canvas, Image.open(source), (58, 142, 1325, 745))
    add_character(canvas, Image.open(cutout), pose)
    header(ImageDraw.Draw(canvas, "RGBA"), cjk, n, title)
    safe_save(canvas, out, optimize=True)


def thumbnail(source: Path, cutout: Path, out: Path, cjk: Path) -> None:
    canvas = background().resize((1280, 720), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas, "RGBA")
    draw.rounded_rectangle((42, 34, 210, 80), radius=20, fill=(*GOLD, 235))
    draw.text((65, 44), "EP01", font=font(cjk, 23), fill=NAVY)
    draw.text((54, 118), "電腦裡面", font=font(cjk, 73), fill=WHITE)
    draw.text((54, 208), "有什麼？", font=font(cjk, 86), fill=GOLD)
    draw.text((58, 325), "從廚房比喻看懂五大單元", font=font(cjk, 29), fill=WHITE)
    draw.line((58, 382, 670, 382), fill=(*BLUE, 220), width=4)
    src = Image.open(source).convert("RGB").resize((520, 293), Image.Resampling.LANCZOS)
    src = src.filter(ImageFilter.GaussianBlur(0.25))
    rounded_paste(canvas, src, (58, 410, 520, 260), radius=18)
    char = alpha_crop(Image.open(cutout))
    h = 650
    char = char.resize((round(char.width * h / char.height), h), Image.Resampling.LANCZOS)
    canvas.paste(char, (1280 - char.width + 20, 75), char)
    draw = ImageDraw.Draw(canvas, "RGBA")
    draw.text((1000, 646), "CHEN XiNew", font=font(cjk, 24), fill=WHITE)
    safe_save(canvas, out, quality=92, optimize=True)


def contact_sheet(slides: list[Path], out: Path, cjk: Path) -> None:
    thumb_w, thumb_h = 480, 270
    sheet = Image.new("RGB", (thumb_w * 2 + 60, thumb_h * 5 + 120), NAVY)
    d = ImageDraw.Draw(sheet)
    d.text((30, 22), "S01E01 · CONTACT SHEET", font=font(cjk, 30), fill=GOLD)
    for i, path in enumerate(slides):
        im = Image.open(path).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = 30 + (i % 2) * thumb_w
        y = 90 + (i // 2) * thumb_h
        sheet.paste(im, (x, y))
        d.rectangle((x, y, x + 52, y + 34), fill=NAVY)
        d.text((x + 9, y + 5), f"{i + 1:02d}", font=font(cjk, 18), fill=GOLD)
    safe_save(sheet, out, quality=88, optimize=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", required=True)
    args = ap.parse_args()
    root = repo_root()
    ep = (root / args.episode).resolve()
    manifest = json.loads((ep / "production/manifest.json").read_text(encoding="utf-8"))
    cjk = root / "assets/fonts/NotoSansCJKtc-Regular.otf"
    pose_paths = {
        "open-palms": root / "assets/characters/cutouts/xinew-open-palms.png",
        "pointer": root / "assets/characters/cutouts/xinew-pointer.png",
        "point-up": root / "assets/characters/cutouts/xinew-point-up.png",
        "thumbs-up": root / "assets/characters/cutouts/xinew-thumbs-up.png",
    }
    outputs: list[Path] = []
    for n, pose in enumerate(manifest["poses"], 1):
        out = ep / f"assets/slides/slide_{n:02d}.png"
        render_slide(
            ep / f"production/source_slides/slide_{n:02d}.png",
            pose_paths[pose], out, cjk, n, manifest["title"], pose,
        )
        outputs.append(out)
    thumbnail(
        ep / "production/source_slides/slide_01.png",
        pose_paths["point-up"], ep / "output/thumbnail.jpg", cjk,
    )
    contact_sheet(outputs, ep / "qc/contact-sheet.jpg", cjk)
    print(f"Rendered {len(outputs)} slides for {manifest['episode']}")


if __name__ == "__main__":
    main()
