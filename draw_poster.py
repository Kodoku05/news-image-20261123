#!/usr/bin/env python3
"""Draw the news-image-20261123 poster: a newspaper front page for
Monday 23 November 2026 with 50 verified stories. Deterministic output:
fixed text, flat colours, no timestamps, no randomness, no network.
Saves entry.png (1024x1024, <= 1 MiB) in the repo root."""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

import stories as S

W, H = 1024, 1024
MARGIN = 28
CONTENT_W = W - 2 * MARGIN

PAPER = (248, 244, 234)
INK = (17, 24, 39)
NAVY = (14, 42, 71)
NAVY_LIGHT = (31, 68, 110)
RED = (193, 39, 45)
RED_DARK = (150, 25, 32)
MUTED = (107, 114, 128)
RULE = (201, 194, 178)
SKY = (188, 214, 232)
SEA = (46, 111, 160)
GREEN = (46, 125, 70)
SAND = (232, 214, 170)
WHITE = (255, 255, 255)
GOLD = (212, 160, 32)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
REG = os.path.join(FONT_DIR, "DejaVuSans.ttf")


def font(path, size):
    return ImageFont.truetype(path, int(round(size)))


def text_w(draw, text, fnt):
    return draw.textlength(text, font=fnt)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap by measured width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if text_w(draw, trial, fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_one_line(draw, text, fnt_path, size, max_w, min_size=8.5):
    """Shrink font until the text fits on one line; returns (font, text).
    If it still does not fit at min_size, truncate with an ellipsis."""
    size = float(size)
    while size > min_size:
        fnt = font(fnt_path, size)
        if text_w(draw, text, fnt) <= max_w:
            return fnt, text
        size -= 0.5
    fnt = font(fnt_path, min_size)
    if text_w(draw, text, fnt) <= max_w:
        return fnt, text
    while text and text_w(draw, text + "\u2026", fnt) > max_w:
        text = text[:-1].rstrip()
    return fnt, text + "\u2026"


def draw_flag(draw, x, y, w, h, stripes):
    """A small vertical-pole flag with horizontal stripes."""
    draw.line([(x, y), (x, y + h + 14)], fill=INK, width=2)
    for i, colour in enumerate(stripes):
        sh = h / len(stripes)
        draw.rectangle([x + 2, y + i * sh, x + 2 + w, y + (i + 1) * sh],
                       fill=colour)


# ---------------------------------------------------------------- icons
def icon_ship(draw, x, y, s, colour=NAVY):
    draw.polygon([(x, y + s * 0.55), (x + s, y + s * 0.55),
                  (x + s * 0.85, y + s * 0.9), (x + s * 0.15, y + s * 0.9)],
                 fill=colour)
    draw.rectangle([x + s * 0.42, y + s * 0.1, x + s * 0.58, y + s * 0.55],
                   fill=colour)
    draw.rectangle([x + s * 0.2, y + s * 0.3, x + s * 0.8, y + s * 0.45],
                   fill=colour)


def icon_drone(draw, x, y, s, colour=INK):
    draw.ellipse([x, y, x + s * 0.25, y + s * 0.25], fill=colour)
    draw.ellipse([x + s * 0.75, y, x + s, y + s * 0.25], fill=colour)
    draw.ellipse([x, y + s * 0.75, x + s * 0.25, y + s], fill=colour)
    draw.ellipse([x + s * 0.75, y + s * 0.75, x + s, y + s], fill=colour)
    draw.rectangle([x + s * 0.35, y + s * 0.35, x + s * 0.65, y + s * 0.65],
                   fill=colour)


def icon_flame(draw, x, y, s, colour=RED):
    draw.polygon([(x + s * 0.5, y), (x + s * 0.85, y + s * 0.45),
                  (x + s, y + s * 0.7), (x + s * 0.7, y + s),
                  (x + s * 0.3, y + s), (x, y + s * 0.7),
                  (x + s * 0.15, y + s * 0.45)], fill=colour)
    draw.ellipse([x + s * 0.35, y + s * 0.55, x + s * 0.65, y + s * 0.85],
                 fill=GOLD)


def icon_trophy(draw, x, y, s, colour=GOLD):
    draw.polygon([(x + s * 0.2, y), (x + s * 0.8, y),
                  (x + s * 0.7, y + s * 0.55), (x + s * 0.3, y + s * 0.55)],
                 fill=colour)
    draw.arc([x, y + s * 0.1, x + s * 0.3, y + s * 0.45], 90, 270,
             fill=colour, width=2)
    draw.arc([x + s * 0.7, y + s * 0.1, x + s, y + s * 0.45], 270, 90,
             fill=colour, width=2)
    draw.rectangle([x + s * 0.42, y + s * 0.55, x + s * 0.58, y + s * 0.8],
                   fill=colour)
    draw.rectangle([x + s * 0.3, y + s * 0.8, x + s * 0.7, y + s * 0.92],
                   fill=colour)


def icon_chip(draw, x, y, s, colour=NAVY):
    draw.rectangle([x + s * 0.2, y + s * 0.2, x + s * 0.8, y + s * 0.8],
                   fill=colour)
    draw.rectangle([x + s * 0.4, y + s * 0.4, x + s * 0.6, y + s * 0.6],
                   fill=PAPER)
    for i in range(3):
        t = y + s * (0.3 + i * 0.2)
        draw.line([(x, t), (x + s * 0.2, t)], fill=colour, width=2)
        draw.line([(x + s * 0.8, t), (x + s, t)], fill=colour, width=2)


def icon_plane(draw, x, y, s, colour=NAVY_LIGHT):
    draw.polygon([(x + s * 0.5, y), (x + s * 0.65, y + s * 0.4),
                  (x + s, y + s * 0.55), (x + s * 0.62, y + s * 0.6),
                  (x + s * 0.55, y + s * 0.95), (x + s * 0.45, y + s * 0.95),
                  (x + s * 0.38, y + s * 0.6), (x, y + s * 0.55),
                  (x + s * 0.35, y + s * 0.4)], fill=colour)


def icon_note(draw, x, y, s, colour=INK):
    draw.ellipse([x + s * 0.05, y + s * 0.7, x + s * 0.35, y + s * 0.95],
                 fill=colour)
    draw.rectangle([x + s * 0.3, y + s * 0.1, x + s * 0.38, y + s * 0.8],
                   fill=colour)
    draw.polygon([(x + s * 0.3, y + s * 0.1), (x + s * 0.85, y + s * 0.25),
                  (x + s * 0.85, y + s * 0.38), (x + s * 0.38, y + s * 0.25)],
                 fill=colour)


def icon_cross(draw, x, y, s, colour=RED):
    draw.rectangle([x + s * 0.4, y, x + s * 0.6, y + s], fill=colour)
    draw.rectangle([x, y + s * 0.4, x + s, y + s * 0.6], fill=colour)


def icon_megaphone(draw, x, y, s, colour=RED):
    draw.polygon([(x + s * 0.1, y + s * 0.35), (x + s * 0.9, y + s * 0.1),
                  (x + s * 0.9, y + s * 0.9), (x + s * 0.1, y + s * 0.65)],
                 fill=colour)
    draw.rectangle([x, y + s * 0.35, x + s * 0.18, y + s * 0.75],
                   fill=colour)


def icon_cap(draw, x, y, s, colour=NAVY):
    draw.polygon([(x + s * 0.5, y + s * 0.1), (x + s, y + s * 0.4),
                  (x + s * 0.5, y + s * 0.7), (x, y + s * 0.4)], fill=colour)
    draw.line([(x + s * 0.5, y + s * 0.55), (x + s * 0.5, y + s * 0.9)],
              fill=colour, width=2)
    draw.line([(x + s * 0.25, y + s * 0.9), (x + s * 0.75, y + s * 0.9)],
              fill=colour, width=2)


def icon_magnifier(draw, x, y, s, colour=INK):
    draw.ellipse([x, y, x + s * 0.7, y + s * 0.7], outline=colour, width=3)
    draw.line([(x + s * 0.55, y + s * 0.55), (x + s, y + s)],
              fill=colour, width=3)


def icon_flag(draw, x, y, s, colour=GREEN):
    draw.line([(x + s * 0.2, y), (x + s * 0.2, y + s)], fill=INK, width=2)
    draw.polygon([(x + s * 0.2, y), (x + s * 0.95, y + s * 0.18),
                  (x + s * 0.2, y + s * 0.4)], fill=colour)


# Spot icons for a dozen grid stories, keyed by grid index (0-based).
SPOT_ICONS = {
    0: icon_ship,       # Sparta II
    1: icon_drone,      # Kyiv flats
    8: icon_flame,      # Indonesia factory fire
    9: icon_megaphone,  # Lisbon march
    10: icon_flag,      # Nepal PM
    11: icon_cap,       # S. Korea minister
    13: icon_trophy,    # India 720/9
    14: icon_magnifier, # FBI breach
    15: icon_chip,      # NVIDIA chips
    17: icon_cross,     # Gaza insulin
    22: icon_plane,     # Delta delays
    23: icon_note,      # Miley Cyrus
}


# ------------------------------------------------------- lead illustrations
def draw_climate_scene(draw, x0, y0, x1, y1):
    """COP31 summit scene: sky, sun, hills, globe, flags, podium."""
    draw.rectangle([x0, y0, x1, y1], fill=SKY)
    draw.ellipse([x1 - 52, y0 + 8, x1 - 14, y0 + 46], fill=GOLD)
    draw.polygon([(x0, y1), (x0 + (x1 - x0) * 0.35, y0 + 62),
                  (x0 + (x1 - x0) * 0.7, y1)], fill=GREEN)
    draw.polygon([(x0 + (x1 - x0) * 0.45, y1),
                  (x0 + (x1 - x0) * 0.8, y0 + 78), (x1, y1)], fill=(58, 140, 82))
    # globe
    cx, cy, r = x0 + 62, y0 + 62, 30
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SEA)
    draw.ellipse([cx - r * 0.45, cy - r * 0.8, cx + r * 0.2, cy - r * 0.1],
                 fill=GREEN)
    draw.ellipse([cx - r * 0.1, cy + r * 0.25, cx + r * 0.55, cy + r * 0.8],
                 fill=GREEN)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=INK, width=2)
    # flags
    draw_flag(draw, x0 + 150, y0 + 22, 34, 16, [RED, WHITE, RED])
    draw_flag(draw, x0 + 196, y0 + 22, 34, 16, [NAVY, WHITE, GOLD])
    draw_flag(draw, x0 + 242, y0 + 22, 34, 16, [GREEN, WHITE, GREEN])
    # podium with COP31
    draw.rectangle([x0 + 150, y1 - 46, x1 - 16, y1], fill=NAVY)
    draw.rectangle([x0 + 150, y1 - 46, x1 - 16, y1 - 38], fill=RED)
    fnt = font(BOLD, 15)
    draw.text((x0 + 168, y1 - 34), "COP31", font=fnt, fill=WHITE)
    draw.rectangle([x0, y0, x1, y1], outline=INK, width=2)


def draw_tanker_icon(draw, x0, y0, s):
    """Small tanker convoy icon for lead 2."""
    draw.rectangle([x0, y0, x0 + s, y0 + s], fill=SKY)
    draw.rectangle([x0, y0 + s * 0.62, x0 + s, y0 + s], fill=SEA)
    icon_ship(draw, x0 + s * 0.08, y0 + s * 0.18, s * 0.84, RED_DARK)
    draw.rectangle([x0, y0, x0 + s, y0 + s], outline=INK, width=2)


def draw_dome_icon(draw, x0, y0, s):
    """Small US Capitol dome icon for lead 3."""
    draw.rectangle([x0, y0, x0 + s, y0 + s], fill=PAPER)
    draw.rectangle([x0 + s * 0.1, y0 + s * 0.72, x0 + s * 0.9, y0 + s * 0.8],
                   fill=NAVY)
    draw.rectangle([x0 + s * 0.2, y0 + s * 0.62, x0 + s * 0.8, y0 + s * 0.72],
                   fill=NAVY)
    draw.pieslice([x0 + s * 0.3, y0 + s * 0.22, x0 + s * 0.7, y0 + s * 0.66],
                  180, 360, fill=NAVY)
    draw.rectangle([x0 + s * 0.47, y0 + s * 0.1, x0 + s * 0.53, y0 + s * 0.26],
                   fill=NAVY)
    draw.ellipse([x0 + s * 0.43, y0 + s * 0.05, x0 + s * 0.57, y0 + s * 0.17],
                 fill=GOLD)
    draw.rectangle([x0, y0, x0 + s, y0 + s], outline=INK, width=2)


def draw_car_icon(draw, x0, y0, s):
    """Small race-car icon for lead 4."""
    draw.rectangle([x0, y0, x0 + s, y0 + s], fill=NAVY)
    draw.polygon([(x0 + s * 0.1, y0 + s * 0.55), (x0 + s * 0.3, y0 + s * 0.4),
                  (x0 + s * 0.65, y0 + s * 0.4), (x0 + s * 0.9, y0 + s * 0.55),
                  (x0 + s * 0.9, y0 + s * 0.7), (x0 + s * 0.1, y0 + s * 0.7)],
                 fill=RED)
    draw.ellipse([x0 + s * 0.2, y0 + s * 0.62, x0 + s * 0.36, y0 + s * 0.78],
                 fill=INK)
    draw.ellipse([x0 + s * 0.64, y0 + s * 0.62, x0 + s * 0.8, y0 + s * 0.78],
                 fill=INK)
    for i in range(4):
        xx = x0 + s * 0.08 + i * s * 0.06
        draw.rectangle([xx, y0 + s * 0.1, xx + s * 0.03, y0 + s * 0.22],
                       fill=WHITE if i % 2 == 0 else INK)
    draw.rectangle([x0, y0, x0 + s, y0 + s], outline=INK, width=2)


LEAD_ICONS = [draw_tanker_icon, draw_dome_icon, draw_car_icon]


# ------------------------------------------------------------- dotted map
# Coarse land rectangles as (x0, y0, x1, y1) fractions of the map area.
LAND = [
    (0.05, 0.10, 0.30, 0.45),   # North America
    (0.28, 0.55, 0.38, 0.85),   # South America
    (0.44, 0.08, 0.62, 0.42),   # Europe / Africa top
    (0.47, 0.42, 0.58, 0.75),   # Africa
    (0.60, 0.10, 0.82, 0.45),   # Asia
    (0.66, 0.48, 0.78, 0.62),   # SE Asia / Indonesia
    (0.82, 0.62, 0.95, 0.82),   # Australia
]


def draw_dotted_map(draw, x0, y0, x1, y1):
    step = 7
    for gx in range(x0, x1, step):
        for gy in range(y0, y1, step):
            fx = (gx - x0) / max(1, x1 - x0)
            fy = (gy - y0) / max(1, y1 - y0)
            on_land = any(ax <= fx <= bx and ay <= fy <= by
                          for ax, ay, bx, by in LAND)
            r = 1.6 if on_land else 1.1
            draw.ellipse([gx - r, gy - r, gx + r, gy + r],
                         fill=NAVY if on_land else (196, 190, 175))
    for num, _label, fx, fy in S.MAP_PINS:
        px, py = x0 + fx * (x1 - x0), y0 + fy * (y1 - y0)
        draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED,
                     outline=WHITE, width=1)
        fnt = font(BOLD, 10)
        tw = text_w(draw, str(num), fnt)
        draw.text((px - tw / 2, py - 7), str(num), font=fnt, fill=WHITE)


# ------------------------------------------------------------------- main
def main():
    n_stories = S.story_count()
    n_regions = S.region_count()
    n_fields = S.field_count()
    print(f"stories={n_stories} regions={n_regions} fields={n_fields}")
    assert n_stories == 50, "must be exactly 50 stories"
    assert len(S.GRID) == 46 and len(S.LEADS) == 4

    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # ---- masthead band (0-80): name, date, story counts
    draw.rectangle([0, 0, W, 80], fill=NAVY)
    f_name = font(BOLD, 54)
    tw = text_w(draw, S.MASTHEAD_NAME, f_name)
    draw.text(((W - tw) / 2, 4), S.MASTHEAD_NAME, font=f_name, fill=WHITE)
    f_date = font(BOLD, 22)
    tw = text_w(draw, S.MASTHEAD_DATE, f_date)
    draw.text(((W - tw) / 2, 58), S.MASTHEAD_DATE, font=f_date, fill=GOLD)
    f_count = font(BOLD, 13)
    count_line = (f"{n_stories} STORIES \u00b7 {n_regions} REGIONS \u00b7 "
                  f"{n_fields} FIELDS")
    tw = text_w(draw, count_line, f_count)
    draw.text((W - MARGIN - tw, 60), count_line, font=f_count, fill=WHITE)

    # ---- lead story (84-244): text left, climate scene right
    y = 84
    lead = S.LEADS[0]
    text_x = MARGIN
    text_wd = 620
    ill_x0, ill_x1 = MARGIN + text_wd + 16, W - MARGIN
    f_kick = font(BOLD, 14)
    draw.text((text_x, y), "CLIMATE \u00b7 COP31 \u00b7 ANTALYA",
              font=f_kick, fill=RED)
    f_lead = font(BOLD, 36)
    ly = y + 22
    for line in wrap(draw, lead["headline"], f_lead, text_wd):
        draw.text((text_x, ly), line, font=f_lead, fill=INK)
        ly += 44
    f_deck = font(REG, 17)
    for line in wrap(draw, lead["deck"], f_deck, text_wd):
        draw.text((text_x, ly), line, font=f_deck, fill=INK)
        ly += 21
    f_src = font(BOLD, 12)
    draw.text((text_x, ly + 2), f"[{lead['source']}]", font=f_src,
              fill=MUTED)
    draw_climate_scene(draw, ill_x0, y, ill_x1, y + 156)
    draw.line([(MARGIN, 252), (W - MARGIN, 252)], fill=RULE, width=2)

    # ---- leads 2-4 as stacked rows (260-392): icon, headline, deck
    y = 260
    for idx, story in enumerate(S.LEADS[1:]):
        icon = LEAD_ICONS[idx]
        icon(draw, MARGIN, y, 40)
        tx = MARGIN + 52
        twd = W - MARGIN - tx
        hl, ht = fit_one_line(draw, story["headline"], BOLD, 19, twd, 15)
        draw.text((tx, y - 2), ht, font=hl, fill=INK)
        f_src11 = font(BOLD, 11)
        src_text = f"[{story['source']}]"
        sw = text_w(draw, src_text, f_src11) + 10
        dk, dt = fit_one_line(draw, story["deck"], REG, 13, twd - sw, 11)
        draw.text((tx, y + 21), dt, font=dk, fill=INK)
        draw.text((tx + twd - text_w(draw, src_text, f_src11), y + 21),
                  src_text, font=f_src11, fill=MUTED)
        y += 44
    draw.line([(MARGIN, 396), (W - MARGIN, 396)], fill=RULE, width=2)

    # ---- explainer box (396-430)
    y = 398
    draw.rectangle([MARGIN, y, MARGIN + 6, y + 30], fill=RED)
    f_lab = font(BOLD, 13)
    label = S.EXPLAINER["label"] + ": "
    draw.text((MARGIN + 14, y), label, font=f_lab, fill=RED_DARK)
    f_exp = font(REG, 14)
    lx = MARGIN + 14 + text_w(draw, label, f_lab)
    lines = wrap(draw, S.EXPLAINER["text"], f_exp, W - MARGIN - lx)
    for i, line in enumerate(lines[:2]):
        draw.text((lx if i == 0 else MARGIN + 14, y + i * 17), line,
                  font=f_exp, fill=INK)
    draw.line([(MARGIN, 434), (W - MARGIN, 434)], fill=RULE, width=2)

    # ---- timeline strip (438-474): label + events on two lines
    y = 440
    f_tl = font(BOLD, 11)
    tl_label = "HOW THE WEEKEND UNFOLDED \u2014 UTC: "
    draw.text((MARGIN, y), tl_label, font=f_tl, fill=NAVY)
    f_ev = font(REG, 11)
    short_events = [
        "SAT 18:00 IRGC strikes Bahrain",
        "SAT EVE Java factory fire",
        "SUN 07:00 Verstappen wins Vegas GP",
        "SUN PM COP31 collapses",
        "SUN EVE Democrats seal 258",
        "MON 00:00 Java search resumes",
    ]
    line1 = "  \u00b7  ".join(short_events[:2])
    line2 = "  \u00b7  ".join(short_events[2:])
    draw.text((MARGIN + text_w(draw, tl_label, f_tl), y), line1,
              font=f_ev, fill=INK)
    draw.text((MARGIN, y + 13), line2, font=f_ev, fill=INK)
    draw.line([(MARGIN, 474), (W - MARGIN, 474)], fill=RULE, width=2)

    # ---- grid (478-920): 3 columns, 16 rows of 27px
    gy0, gy1 = 478, 920
    cols = 3
    col_gap = 16
    col_w = (CONTENT_W - (cols - 1) * col_gap) // cols
    rows = (len(S.GRID) + cols - 1) // cols
    row_h = (gy1 - gy0) // rows
    f_grid_h = 12.5
    f_grid_d = 9.5
    for idx, (headline, deck, source, _region, _field) in enumerate(S.GRID):
        col, row = idx % cols, idx // cols
        gx = MARGIN + col * (col_w + col_gap)
        gy = gy0 + row * row_h
        icon = SPOT_ICONS.get(idx)
        hx = gx
        if icon is not None:
            icon(draw, gx, gy + 1, 13)
            hx = gx + 18
        hw = col_w - (hx - gx)
        hf, ht = fit_one_line(draw, headline, BOLD, f_grid_h, hw, 9)
        draw.text((hx, gy), ht, font=hf, fill=INK)
        f_gsrc = font(BOLD, 9)
        gsrc = f"[{source}]"
        gsw = text_w(draw, gsrc, f_gsrc) + 4
        df, dt = fit_one_line(draw, deck, REG, f_grid_d, hw - gsw, 8)
        draw.text((hx, gy + 14), dt, font=df, fill=MUTED)
        draw.text((hx + hw - text_w(draw, gsrc, f_gsrc), gy + 14), gsrc,
                  font=f_gsrc, fill=RED_DARK)
    draw.line([(MARGIN, 924), (W - MARGIN, 924)], fill=RULE, width=2)

    # ---- map + date check row (930-1006)
    y = 930
    map_x0, map_x1 = MARGIN, MARGIN + 470
    f_sec = font(BOLD, 12)
    draw.text((map_x0, y), "WHERE IT HAPPENED", font=f_sec, fill=NAVY)
    draw_dotted_map(draw, map_x0, y + 16, map_x1, y + 62)
    legend = "  ".join(f"{n} {lab}" for n, lab, _fx, _fy in S.MAP_PINS)
    lf, lt = fit_one_line(draw, legend, REG, 9, map_x1 - map_x0, 8)
    draw.text((map_x0, y + 64), lt, font=lf, fill=MUTED)

    dc_x0 = map_x1 + 20
    draw.text((dc_x0, y), "DATE CHECK \u2014 LEFT OUT AS OLDER NEWS",
              font=f_sec, fill=RED_DARK)
    f_dc = font(REG, 10)
    dc_lines = []
    for name, date in S.DATE_CHECK:
        dc_lines.append(f"{name} \u2014 {date}")
    dc_text = "  \u00b7  ".join(dc_lines)
    for i, line in enumerate(wrap(draw, dc_text, f_dc,
                                  W - MARGIN - dc_x0)[:3]):
        draw.text((dc_x0, y + 16 + i * 13), line, font=f_dc, fill=INK)

    # ---- footer strip (1010-1022)
    f_foot = font(REG, 11)
    ff, ft = fit_one_line(draw, S.FOOTER, REG, 11, CONTENT_W, 9)
    draw.text((MARGIN, 1010), ft, font=ff, fill=MUTED)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out, optimize=True)
    size = os.path.getsize(out)
    print(f"saved {out} {img.size[0]}x{img.size[1]} {size} bytes")
    if size > 1048576:
        print("ERROR: entry.png over 1 MiB", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
