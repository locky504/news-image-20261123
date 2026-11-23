#!/usr/bin/env python3
"""Draw the front page for make.fun news-image-20261123.

Renders the verified world headlines of Monday 23 November 2026 as a
one-page newspaper front page (1024x1024 PNG) and writes it to
entry.png beside this file. Run once, locally:

    python3 draw.py

The drawing is fully deterministic: fixed headlines, fixed fonts, fixed
layout, no clock, no randomness, no network. The entry point the
grader runs is main.ts (Node), which copies the finished entry.png to
/output/entry.png byte for byte.

Headlines were verified on 23 November 2026 against SCMP, Arab News,
The Manila Times and The Economic Times (all dated 23 November 2026);
only headline-level facts are used, and no casualty or damage figures
are given.
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
MARGIN = 36
CONTENT_W = W - 2 * MARGIN

PAPER = (248, 244, 233)   # warm newsprint
INK = (20, 20, 20)
RED = (163, 30, 30)       # kicker accent
GREY = (90, 86, 78)
BLUE = (28, 68, 110)      # globe / sea accent

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)   # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)            # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)     # noqa: E731


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap; returns a list of lines that fit max_width."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, max_width, fill, leading):
    lines = wrap(draw, text, fnt, max_width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, x1, y, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def draw_globe(draw, cx, cy, r):
    """Simple line globe: circle, meridians, equator."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=BLUE, width=3)
    draw.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r],
                 outline=BLUE, width=2)
    draw.line([(cx - r, cy), (cx + r, cy)], fill=BLUE, width=2)
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2],
             start=200, end=340, fill=BLUE, width=2)
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2],
             start=20, end=160, fill=BLUE, width=2)


def draw_planet(draw, cx, cy, r):
    """Small cratered planet (Mercury) with an orbit ring."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                 fill=(196, 178, 150), outline=INK, width=2)
    for dx, dy, cr in [(-r // 3, -r // 4, 7), (r // 4, r // 5, 9),
                       (r // 10, -r // 2, 5), (-r // 5, r // 3, 6)]:
        draw.ellipse([cx + dx - cr, cy + dy - cr, cx + dx + cr, cy + dy + cr],
                     outline=GREY, width=2)
    draw.ellipse([cx - r - 16, cy - 10, cx + r + 16, cy + 10],
                 outline=RED, width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    x0, x1 = MARGIN, W - MARGIN

    # ---- Masthead -----------------------------------------------------
    rule(d, x0, x1, 30, 3)
    d.text((W // 2, 44), "THE WORLD TODAY", font=SERIF_B(84),
           fill=INK, anchor="ma")
    rule(d, x0, x1, 142, 2)
    d.text((x0, 152), "MONDAY, 23 NOVEMBER 2026", font=SANS_B(20),
           fill=INK, anchor="la")
    d.text((x1, 152), "THE WORLD IN ONE PAGE", font=SANS_B(20),
           fill=INK, anchor="ra")
    rule(d, x0, x1, 182, 1)

    # ---- Lead story ---------------------------------------------------
    y = 196
    d.text((x0, y), "CLIMATE  \u00b7  TURKEY", font=SANS_B(22), fill=RED)
    y += 34
    y = draw_wrapped(
        d, x0, y, "Climate Talks Collapse As Nations Fail To Agree",
        SERIF_B(44), CONTENT_W - 150, INK, 50)
    # globe sits to the right of the headline block
    draw_globe(d, x1 - 62, 268, 58)
    y += 4
    y = draw_wrapped(
        d, x0, y,
        "Nearly 200 countries end the COP31 summit in Turkey without a "
        "climate declaration, split over fossil fuels, as the UN chief "
        "warns there is \u2018no ambiguity in the science\u2019.",
        SANS(22), CONTENT_W, INK, 28)
    rule(d, x0, x1, y + 14, 2)

    # ---- 2 x 2 grid ----------------------------------------------------
    col_w = (CONTENT_W - 24) // 2
    grid = [
        ("POLITICS  \u00b7  WASHINGTON",
         "Democrats Clinch 258-Seat House Majority",
         "Democrats win at least 258 seats in the House, their largest "
         "majority since 1992."),
        ("SHIPPING  \u00b7  GULF",
         "Tankers Struck Near Strait Of Hormuz",
         "More tankers are hit in and near the strait over the weekend, "
         "in the sharpest run of attacks on shipping there since the war "
         "began."),
        ("LIBYA  \u00b7  MEDITERRANEAN",
         "Sea Drones Hit Russian Warship In Libya",
         "Suspected Ukrainian sea drones strike a Russian corvette at "
         "the Benghazi naval base; Libyan officials say the ship is "
         "severely damaged."),
        ("UKRAINE  \u00b7  KYIV",
         "Russian Strikes Hit Kyiv Region",
         "Russian strikes hit the Kyiv region, Ukraine says, in the "
         "latest round of attacks on the capital\u2019s region."),
    ]
    gy = y + 22
    row_h = 200
    for i, (kicker, headline, dek) in enumerate(grid):
        col = i % 2
        row = i // 2
        cx = x0 + col * (col_w + 24)
        cy = gy + row * row_h
        d.text((cx, cy), kicker, font=SANS_B(18), fill=RED)
        cy = draw_wrapped(d, cx, cy + 26, headline, SERIF_B(28),
                          col_w, INK, 33)
        draw_wrapped(d, cx, cy + 4, dek, SANS(19), col_w, INK, 24)
    # vertical divider between the two columns
    mid_x = x0 + col_w + 12
    d.line([(mid_x, gy), (mid_x, gy + 2 * row_h - 12)], fill=GREY, width=1)

    # ---- Bottom band ---------------------------------------------------
    by = gy + 2 * row_h + 2
    rule(d, x0, x1, by, 2)
    by += 12
    d.text((x0, by), "SPACE  \u00b7  MERCURY", font=SANS_B(20), fill=RED)
    by += 26
    d.text((x0, by), "BepiColombo Enters Orbit Around Mercury",
           font=SERIF_B(32), fill=INK)
    by += 40
    draw_wrapped(
        d, x0, by,
        "After an eight-year journey, the European-Japanese spacecraft "
        "enters orbit around Mercury \u2014 only the second mission ever "
        "to do so.",
        SANS(20), CONTENT_W - 150, INK, 26)
    draw_planet(d, x1 - 62, by + 22, 46)
    by += 62

    # ---- Footer --------------------------------------------------------
    rule(d, x0, x1, 984, 1)
    d.text((W // 2, 992),
           "Headlines verified from SCMP, Arab News, The Manila Times "
           "and The Economic Times  \u00b7  23 November 2026",
           font=SANS(15), fill=GREY, anchor="ma")

    assert by < 984, f"layout overflow: bottom band ends at {by}"
    img.save(OUT, format="PNG")
    size = os.path.getsize(OUT)
    print(f"wrote {OUT} ({size} bytes, {W}x{H})")
    assert size <= 1048576, "entry.png exceeds 1 MiB"


if __name__ == "__main__":
    main()
