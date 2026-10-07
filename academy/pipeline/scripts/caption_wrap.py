"""Line breaks for burned-in zh-TW captions (opt-in: manifest renderOptions.captionLineBreak = "kinsoku").

libass balances long CJK cues by character count, so a second line can start with
「，」「、」「；」 or cut a word in half. This module decides the break before libass
sees the cue: one line when it fits, otherwise two lines, breaking after punctuation
(sentence punctuation before the list comma) when that keeps both lines reasonable,
never before closing punctuation, never after an opening bracket and never inside a
Latin/number run.

Only the burned picture uses these breaks. The delivered SRT keeps one line per cue.
Widths are estimated in em (full-width = 1); pipeline/qa/subtitle_precheck.py renders
every cue with libass and fails when the rendered line count differs from the plan.
"""
from __future__ import annotations

import unicodedata

# 1920 px frame, libass margins 24+24 of PlayResX 384 -> 1680 px; the burn style renders
# a full-width glyph about 41.4 px wide, so 40 full-width characters fit on one line.
LINE_LIMIT_EM = 40.0
NO_LINE_START = set("，。、；：？！）」』》〉】〕…—～％,.;:?!)]}%")
NO_LINE_END = set("（「『《〈【〔([{")
BREAK_AFTER = set("，。、；：？！,;:?!")
STRONG_BREAK = set("，。；：？！;:?!")  # preferred over the list comma 「、」
MIN_SHARE = 0.25  # a punctuation break must leave each line at least this share of the cue


def width_em(text: str) -> float:
    total = 0.0
    for ch in text:
        if ch == " ":
            total += 0.3
        elif unicodedata.east_asian_width(ch) in ("W", "F", "A"):
            total += 1.0
        else:
            total += 0.56
    return total


def _latin(ch: str) -> bool:
    return ch.isascii() and not ch.isspace()


def _allowed(text: str, i: int) -> bool:
    left, right = text[i - 1], text[i]
    if right in NO_LINE_START or left in NO_LINE_END:
        return False
    if _latin(left) and _latin(right) and left not in BREAK_AFTER:
        return False
    return True


def wrap_caption(text: str, limit: float = LINE_LIMIT_EM) -> list[str]:
    """Return one or two display lines for a single-line cue."""
    text = " ".join(text.split())
    total = width_em(text)
    if total <= limit:
        return [text]
    options = []
    for i in range(1, len(text)):
        if not _allowed(text, i):
            continue
        a, b = text[:i].rstrip(), text[i:].lstrip()
        wa, wb = width_em(a), width_em(b)
        if not a or not b or wa > limit or wb > limit:
            continue
        options.append((abs(wa - wb), i, a, b, wa, wb))
    if not options:
        raise ValueError(f"Caption cannot be laid out in two lines of {limit:g} em: {text}")
    fair = [o for o in options if min(o[4], o[5]) >= MIN_SHARE * total]
    strong = [o for o in fair if o[2][-1] in STRONG_BREAK]
    weak = [o for o in fair if o[2][-1] in BREAK_AFTER]
    _, _, a, b, _, _ = min(strong or weak or options)
    return [a, b]
