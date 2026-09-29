#!/usr/bin/env python3
"""Generate the 6 procedural visuals for EP10 (XiNew style: navy + cyan/orange glow)."""
from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[2]
EP = ROOT / "episodes/season-01/ep10-ai-and-our-future"
VIS = EP / "assets/visuals"
VIS.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
CYAN = (70, 200, 255)
BLUE = (25, 130, 196)
ORANGE = (255, 193, 47)
WHITE = (247, 247, 248)
GRAY = (168, 184, 201)
PANEL = (10, 24, 40)
NAVY_TOP = (7, 24, 44)
NAVY_BOT = (3, 12, 24)
GREEN = (120, 220, 140)
RED = (255, 110, 90)
PURPLE = (190, 140, 255)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_CJK = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.truetype(FONT_BOLD, size)


def cjk(size: int) -> ImageFont.FreeTypeFont:
    return font(FONT_CJK, size)


def base_canvas() -> Image.Image:
    img = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        c = tuple(int(NAVY_TOP[i] * (1 - t) + NAVY_BOT[i] * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    return img


def glow(img: Image.Image, draw_fn, blur: int = 16) -> None:
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    draw_fn(d)
    img.alpha_composite(layer.filter(ImageFilter.GaussianBlur(blur)))
    img.alpha_composite(layer)


def rrect(d: ImageDraw.ImageDraw, box, r, **kw):
    d.rounded_rectangle(box, radius=r, **kw)


def floor_grid(d: ImageDraw.ImageDraw, y_start: int = 900):
    for i in range(9):
        y = y_start + i * 22
        d.line([(0, y), (W, y)], fill=(*BLUE, 60 - i * 5), width=2)
    for x in range(0, W, 160):
        d.line([(x, y_start), (x - 260, H)], fill=(*BLUE, 34), width=2)
        d.line([(x, y_start), (x + 260, H)], fill=(*BLUE, 34), width=2)


def save(img: Image.Image, name: str):
    img.save(VIS / name)
    print("saved", name)


def ctext(d, xy, s, size, fill, anchor="mm"):
    d.text(xy, s, font=cjk(size), fill=fill, anchor=anchor)


def bolt(dd, cx, cy, s, col):
    """Lightning bolt centered at cx,cy with height s."""
    pts = [(cx + 0.10 * s, cy - 0.50 * s), (cx - 0.28 * s, cy + 0.08 * s),
           (cx - 0.02 * s, cy + 0.08 * s), (cx - 0.10 * s, cy + 0.50 * s),
           (cx + 0.28 * s, cy - 0.08 * s), (cx + 0.02 * s, cy - 0.08 * s)]
    dd.polygon(pts, fill=(*col, 255))


def chip(dd, cx, cy, w, h, label, size, col):
    rrect(dd, [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], 18,
          fill=(16, 34, 54, 255), outline=(*col, 255), width=4)
    f = cjk(size)
    dd.text((cx, cy), label, font=f, fill=(*col, 255), anchor="mm")


# ---------------------------------------------------------- 1 cover hero: sunrise horizon (slide 1)
def future_hero():
    img = base_canvas()
    d = ImageDraw.Draw(img)
    floor_grid(d, 900)

    cx, cy, r = 1120, 470, 300

    # stars above the horizon
    rng = random.Random(10)
    for _ in range(46):
        x = rng.randint(40, W - 40)
        y = rng.randint(50, 380)
        rr = rng.choice((2, 3, 4))
        col = rng.choice((CYAN, ORANGE, WHITE))
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=(*col, rng.randint(120, 220)))

    # sunrise glow rays
    def rays(dd):
        for i in range(20):
            ang = 180 + i * (180 / 19)
            x1 = cx + (r + 18) * math.cos(math.radians(ang))
            y1 = cy + (r + 18) * math.sin(math.radians(ang))
            x2 = cx + (r + 64) * math.cos(math.radians(ang))
            y2 = cy + (r + 64) * math.sin(math.radians(ang))
            dd.line([(x1, y1), (x2, y2)], fill=(*ORANGE, 120), width=5)
    glow(img, rays, 8)

    # sun disc
    glow(img, lambda dd: dd.ellipse([cx - r, cy - r, cx + r, cy + r],
         fill=(60, 40, 12, 255), outline=(*ORANGE, 255), width=8), 14)
    d.ellipse([cx - r + 30, cy - r + 30, cx + r - 30, cy + r - 30], fill=(16, 34, 54, 255))
    glow(img, lambda dd: bolt(dd, cx, cy - 30, 240, ORANGE), 10)
    ctext(d, (cx, cy + 150), "未來", 72, (*ORANGE, 255))

    # horizon road leading to the sun
    d.polygon([(cx - 60, 770), (cx + 60, 770), (cx + 330, 1080), (cx - 330, 1080)],
              fill=(10, 24, 40, 255), outline=(*BLUE, 200))
    for i in range(5):
        y = 800 + i * 58
        half = 10 + i * 8
        d.line([(cx - half, y), (cx + half, y)], fill=(*CYAN, 190), width=6)

    # orbiting chips
    for label, ang, col in (("日常", 205, CYAN), ("幫手", 285, ORANGE), ("你當家", 335, GREEN)):
        px = cx + (r + 12) * math.cos(math.radians(ang))
        py = cy + (r + 12) * math.sin(math.radians(ang))
        glow(img, lambda dd, p=(px, py), l=label, c=col: chip(dd, p[0], p[1], 168, 76, l, 32, c), 8)

    # hanging dots
    d2 = ImageDraw.Draw(img)
    for i in range(16):
        x = 60 + i * 120
        d2.line([(x, 0), (x, 40 + (i % 5) * 12)], fill=(*BLUE, 90), width=3)
        d2.ellipse([x - 8, 40 + (i % 5) * 12, x + 8, 56 + (i % 5) * 12], fill=(*ORANGE, 200))
    save(img, "future-hero.png")


# ---------------------------------------------------------- 2 full-bleed: a day with AI (slide 3)
def day_map():
    img = base_canvas()
    d = ImageDraw.Draw(img)
    floor_grid(d, 900)

    # timeline
    ty = 560
    glow(img, lambda dd: dd.line([(200, ty), (1620, ty)], fill=(*BLUE, 255), width=10), 8)
    for x in range(200, 1621, 71):
        d.ellipse([x - 6, ty - 6, x + 6, ty + 6], fill=(*CYAN, 200))

    def alarm(dd, cx, cy):
        dd.ellipse([cx - 70, cy - 70, cx + 70, cy + 70], outline=(*ORANGE, 255), width=8)
        dd.line([(cx, cy), (cx, cy - 42)], fill=(*ORANGE, 255), width=8)
        dd.line([(cx, cy), (cx + 30, cy + 18)], fill=(*ORANGE, 255), width=8)
        dd.arc([cx - 96, cy - 104, cx - 24, cy - 32], 200, 340, fill=(*ORANGE, 255), width=8)
        dd.arc([cx + 24, cy - 104, cx + 96, cy - 32], 200, 340, fill=(*ORANGE, 255), width=8)

    def book(dd, cx, cy):
        dd.polygon([(cx, cy - 50), (cx - 90, cy - 76), (cx - 90, cy + 44), (cx, cy + 70)],
                   fill=(16, 34, 54, 255), outline=(*CYAN, 255))
        dd.polygon([(cx, cy - 50), (cx + 90, cy - 76), (cx + 90, cy + 44), (cx, cy + 70)],
                   fill=(16, 34, 54, 255), outline=(*CYAN, 255))
        dd.line([(cx, cy - 50), (cx, cy + 70)], fill=(*CYAN, 255), width=5)

    def moon(dd, cx, cy):
        dd.ellipse([cx - 66, cy - 66, cx + 66, cy + 66], fill=(*PURPLE, 255))
        dd.ellipse([cx - 30, cy - 82, cx + 90, cy + 50], fill=(*NAVY_TOP, 255))

    nodes = [(420, "早上", alarm, ORANGE, "幫你排好行程"),
             (910, "下午", book, CYAN, "練英文・找資料"),
             (1400, "晚上", moon, PURPLE, "明天記得帶傘")]
    for cx, label, icon, col, cap in nodes:
        d.line([(cx, ty), (cx, ty - 60)], fill=(*col, 255), width=6)
        glow(img, lambda dd, c=cx, i=icon: i(dd, c, ty - 170), 8)
        chip(d, cx, ty + 70, 150, 68, label, 34, col)
        ctext(d, (cx, 790), cap, 32, (*col, 255))
    save(img, "day-map.png")


# ---------------------------------------------------------- 3 bullets visual: agent task list (slide 4)
def agent_tasks():
    img = base_canvas()
    d = ImageDraw.Draw(img)

    # task panel
    glow(img, lambda dd: rrect(dd, [130, 330, 830, 800], 24, fill=(16, 34, 54, 255),
         outline=(*BLUE, 255), width=5), 8)
    ctext(d, (480, 410), "數位小幫手　任務單", 38, (*WHITE, 255))
    d.line([(170, 452), (790, 452)], fill=(*BLUE, 160), width=3)

    items = [("訂機票", CYAN), ("排行程", ORANGE), ("訂餐廳", GREEN)]
    for i, (label, col) in enumerate(items):
        y = 540 + i * 86
        d.rounded_rectangle([190, y - 28, 246, y + 28], radius=9, outline=(*col, 255), width=5)
        d.line([(200, y), (212, y + 14)], fill=(*col, 255), width=7)
        d.line([(212, y + 14), (236, y - 14)], fill=(*col, 255), width=7)
        d.text((280, y), label, font=cjk(36), fill=(*WHITE, 255), anchor="lm")
        d.line([(460, y), (740, y)], fill=(*col, 120), width=4)
        ctext(d, (740, y - 24), "OK", 26, (*col, 255), anchor="rm")

    # green done stamp
    stamp = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(stamp)
    sd.rounded_rectangle([540, 706, 800, 782], radius=14, outline=(*GREEN, 255), width=6)
    sd.text((670, 744), "全部辦好！", font=cjk(36), fill=(*GREEN, 255), anchor="mm")
    stamp = stamp.rotate(-8, center=(670, 744), resample=Image.BICUBIC)
    img.alpha_composite(stamp)
    save(img, "agent-tasks.png")


# ---------------------------------------------------------- 4 bullets visual: you are the director (slide 7)
def creative_director():
    img = base_canvas()
    d = ImageDraw.Draw(img)

    # director chair (backrest + seat + splayed legs)
    def chair(dd):
        cx = 330
        dd.rounded_rectangle([cx - 110, 420, cx + 110, 470], radius=10, fill=(16, 34, 54, 255),
                             outline=(*ORANGE, 255), width=5)
        dd.line([(cx - 96, 470), (cx - 96, 560)], fill=(*ORANGE, 255), width=8)
        dd.line([(cx + 96, 470), (cx + 96, 560)], fill=(*ORANGE, 255), width=8)
        dd.rounded_rectangle([cx - 110, 540, cx + 110, 580], radius=10, fill=(16, 34, 54, 255),
                             outline=(*ORANGE, 255), width=5)
        dd.line([(cx - 100, 580), (cx - 150, 800)], fill=(*ORANGE, 255), width=10)
        dd.line([(cx + 100, 580), (cx + 150, 800)], fill=(*ORANGE, 255), width=10)
        dd.line([(cx - 96, 580), (cx - 20, 800)], fill=(*ORANGE, 255), width=8)
        dd.line([(cx + 96, 580), (cx + 20, 800)], fill=(*ORANGE, 255), width=8)
        dd.line([(cx - 120, 700), (cx + 120, 700)], fill=(*ORANGE, 255), width=7)
    glow(img, chair, 8)
    ctext(d, (330, 445), "導演", 30, (*ORANGE, 255))

    # clapperboard
    def clap(dd):
        dd.rounded_rectangle([560, 360, 860, 470], radius=10, fill=(16, 34, 54, 255),
                             outline=(*CYAN, 255), width=5)
        dd.polygon([(560, 360), (570, 320), (880, 340), (860, 360)], fill=(16, 34, 54, 255),
                   outline=(*CYAN, 255))
        for i in range(4):
            x = 590 + i * 70
            dd.line([(x, 326), (x + 36, 352)], fill=(*CYAN, 255), width=6)
    glow(img, clap, 8)
    ctext(d, (710, 415), "你做決定", 32, (*CYAN, 255))

    # palette with AI brush
    def palette(dd):
        cx, cy = 700, 640
        dd.ellipse([cx - 110, cy - 90, cx + 110, cy + 90], fill=(16, 34, 54, 255),
                   outline=(*PURPLE, 255), width=5)
        for ang, col in ((30, ORANGE), (110, CYAN), (190, GREEN), (270, RED)):
            px = cx + 62 * math.cos(math.radians(ang))
            py = cy + 52 * math.sin(math.radians(ang))
            dd.ellipse([px - 16, py - 16, px + 16, py + 16], fill=(*col, 255))
    glow(img, palette, 8)
    glow(img, lambda dd: (dd.line([(790, 560), (880, 470)], fill=(*WHITE, 255), width=10),
         dd.polygon([(872, 452), (906, 438), (896, 474)], fill=(*PURPLE, 255))), 6)
    ctext(d, (700, 760), "AI 畫筆，你喊「開拍」", 30, (*WHITE, 255))
    save(img, "creative-director.png")


# ---------------------------------------------------------- 5 full-bleed: personal tutor paths (slide 8)
def tutor_map():
    img = base_canvas()
    d = ImageDraw.Draw(img)
    floor_grid(d, 900)

    # goal flag top-right
    def flag(dd):
        dd.line([(1620, 260), (1620, 470)], fill=(*ORANGE, 255), width=10)
        dd.polygon([(1620, 260), (1750, 300), (1620, 350)], fill=(*ORANGE, 255))
    glow(img, flag, 10)
    ctext(d, (1620, 510), "學會了！", 36, (*ORANGE, 255))

    # three student paths
    paths = [
        ("小文", CYAN, 610, [(380, 610), (560, 640), (760, 660), (980, 560), (1200, 520), (1400, 430), (1600, 380)]),
        ("小武", GREEN, 700, [(380, 700), (600, 560), (820, 480), (1040, 470), (1260, 400), (1440, 360), (1600, 340)]),
        ("小梅", PURPLE, 790, [(380, 790), (540, 760), (720, 710), (900, 690), (1120, 610), (1340, 530), (1600, 420)]),
    ]
    for name, col, sy, pts in paths:
        glow(img, lambda dd, p=pts, c=col: dd.line(p, fill=(*c, 255), width=8, joint="curve"), 6)
        for px, py in pts[1:-1:2]:
            d.ellipse([px - 12, py - 12, px + 12, py + 12], fill=(*col, 255))
        d.ellipse([pts[0][0] - 40, pts[0][1] - 40, pts[0][0] + 40, pts[0][1] + 40],
                  fill=(16, 34, 54, 255), outline=(*col, 255), width=5)
        ctext(d, pts[0], name, 28, (*col, 255))

    ctext(d, (660, 430), "卡在哪，從哪教", 34, (*WHITE, 255))
    ctext(d, (960, 790), "每個人走自己的路，都到得了", 30, (*WHITE, 255))
    save(img, "tutor-map.png")


# ---------------------------------------------------------- 6 four-cards overlay: you hold the wheel (slide 10)
def drive_wheel():
    img = base_canvas()
    d = ImageDraw.Draw(img)

    # steering wheel
    cx, cy, r = 560, 460, 200
    glow(img, lambda dd: dd.ellipse([cx - r, cy - r, cx + r, cy + r],
         outline=(*ORANGE, 255), width=18), 10)
    def spokes(dd):
        dd.line([(cx, cy), (cx, cy - r + 20)], fill=(*ORANGE, 255), width=12)
        dd.line([(cx, cy), (cx - r + 34, cy + r - 92)], fill=(*ORANGE, 255), width=12)
        dd.line([(cx, cy), (cx + r - 34, cy + r - 92)], fill=(*ORANGE, 255), width=12)
        dd.ellipse([cx - 42, cy - 42, cx + 42, cy + 42], fill=(16, 34, 54, 255),
                   outline=(*ORANGE, 255), width=6)
    glow(img, spokes, 6)
    ctext(d, (cx, cy), "你", 44, (*ORANGE, 255))

    # dashboard LEDs: four actions
    acts = [("好奇", CYAN), ("提問", ORANGE), ("查證", GREEN), ("負責", PURPLE)]
    for i, (label, col) in enumerate(acts):
        x = 1060 + (i % 2) * 260
        y = 330 + (i // 2) * 150
        glow(img, lambda dd, b=[x - 110, y - 56, x + 110, y + 56], c=col: rrect(dd, b, 18,
             fill=(16, 34, 54, 255), outline=(*c, 255), width=4), 6)
        d.ellipse([x - 88, y - 14, x - 60, y + 14], fill=(*col, 255))
        d.text((x - 40, y), label, font=cjk(34), fill=(*WHITE, 255), anchor="lm")
    ctext(d, (1190, 592), "方向盤在你手上", 34, (*ORANGE, 255))
    save(img, "drive-wheel.png")


if __name__ == "__main__":
    future_hero()
    day_map()
    agent_tasks()
    creative_director()
    tutor_map()
    drive_wheel()
