#!/usr/bin/env python3
"""Image a la une : la banniere bleue de la serie article-*.png du site.

Reprend au pixel pres la charte des visuels existants : fond #5174B4,
banderole blanche, titre coupe au deux-points, ligne 1 bleue, ligne 2 noire.

    python generate_featured_image.py --titre "..." --out image.png
"""
import os
import re
import sys
import argparse
import unicodedata
from PIL import Image, ImageDraw, ImageFont


CANVAS = (940, 575)
BG = (81, 116, 180)          # #5174B4 — fond
BANNER = (255, 255, 255)     # banderole
INK_TOP = (81, 116, 180)     # ligne 1 : même bleu que le fond
INK_BOTTOM = (0, 0, 0)       # ligne 2 : noir
RADIUS = 24
CAP_HEIGHT = 32              # hauteur de capitale visée, par ligne
PREF_MIN_CAP = 26            # au-dessus : on garde la mise en page d'origine (2 lignes)
MIN_CAP = 22                 # en dessous, le titre devient illisible en vignette
MAX_LINES = 3                # les titres longs passent sur 3 lignes, pas en minuscule
PAD_X = 28                   # marge latérale texte → bord de banderole
PAD_TOP = 25
PAD_BOTTOM = 30
LINE_GAP = 27                # espace entre le bas de L1 et le haut de L2
MAX_BANNER_RATIO = 0.90      # la banderole ne dépasse pas 90 % de la largeur

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\segoeuib.ttf",   # Segoe UI Bold
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\verdanab.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]



def clean_title(raw):
    """Décode les entités HTML et normalise les espaces/apostrophes."""
    t = html.unescape(raw)
    t = t.replace("\u2019", "'").replace("\u00a0", " ")
    return re.sub(r"\s+", " ", t).strip()


def split_title(title):
    """Découpe le titre en 2 lignes, à la manière des images d'origine.

    Priorité au « : » (la ponctuation reste sur la ligne 1), sinon on équilibre
    les mots pour que les deux lignes aient une longueur proche.
    """
    if ":" in title:
        a, b = title.split(":", 1)
        a, b = a.strip(), b.strip()
        if a and b:
            return a + " :", b

    for sep in (" — ", " – ", " - "):
        if sep in title:
            a, b = title.split(sep, 1)
            if a.strip() and b.strip():
                return a.strip(), b.strip()

    words = title.split()
    if len(words) < 2:
        return title, ""
    # point de coupe qui minimise l'écart de longueur entre les 2 lignes
    best, best_delta = 1, None
    for i in range(1, len(words)):
        a = " ".join(words[:i])
        b = " ".join(words[i:])
        delta = abs(len(a) - len(b))
        if best_delta is None or delta < best_delta:
            best, best_delta = i, delta
    return " ".join(words[:best]), " ".join(words[best:])


def pick_font():
    for p in FONT_CANDIDATES:
        if os.path.exists(p):
            return p
    sys.exit("❌ Aucune police grasse trouvée (voir FONT_CANDIDATES).")


def font_for_cap(path, cap_px):
    """Retourne la police dont la hauteur de capitale vaut ~cap_px."""
    size = int(cap_px / 0.70) or 1
    for _ in range(24):
        f = ImageFont.truetype(path, size)
        box = f.getbbox("H")
        cap = box[3] - box[1]
        if cap == cap_px:
            return f
        size += 1 if cap < cap_px else -1
        if size < 6:
            break
    return ImageFont.truetype(path, max(size, 6))


def text_width(draw, text, font):
    if not text:
        return 0
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0]


def wrap(draw, text, font, max_w):
    """Découpe `text` en lignes ne dépassant pas `max_w` pixels."""
    if not text:
        return []
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if not cur or text_width(draw, trial, font) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def balanced(draw, text, font, n):
    """Répartit `text` sur `n` lignes de largeurs aussi proches que possible.

    Évite les orphelins que produit un retour à la ligne gourmand
    (« AUGMENTER SA VISIBILITÉ WEB EN » / « 2026 : »).
    """
    words = text.split()
    if n <= 1 or len(words) <= n:
        return [text] if n <= 1 else words
    best = None
    for cuts in itertools.combinations(range(1, len(words)), n - 1):
        idx = (0,) + cuts + (len(words),)
        lines = [" ".join(words[idx[i]:idx[i + 1]]) for i in range(n)]
        widths = [text_width(draw, l, font) for l in lines]
        key = (max(widths), sum(w * w for w in widths))
        if best is None or key < best[0]:
            best = (key, lines)
    return best[1]


def make_image(title, dest):
    """Rend l'image de mise en avant et l'écrit dans `dest`."""
    part1, part2 = split_title(clean_title(title))
    part1, part2 = part1.upper(), part2.upper()

    font_path = pick_font()
    img = Image.new("RGB", CANVAS, BG)
    draw = ImageDraw.Draw(img)
    max_text_w = CANVAS[0] * MAX_BANNER_RATIO - 2 * PAD_X
    layout = None

    # 1. mise en page d'origine : une ligne par partie, texte le plus grand possible
    for cap in range(CAP_HEIGHT, PREF_MIN_CAP - 1, -1):
        font = font_for_cap(font_path, cap)
        if (text_width(draw, part1, font) <= max_text_w
                and text_width(draw, part2, font) <= max_text_w):
            layout = (cap, font, [part1], [part2] if part2 else [])
            break

    # 2. titre trop long : jusqu'à 3 lignes, réparties de façon équilibrée
    if layout is None:
        for cap in range(CAP_HEIGHT, MIN_CAP - 1, -1):
            font = font_for_cap(font_path, cap)
            n1 = len(wrap(draw, part1, font, max_text_w))
            n2 = len(wrap(draw, part2, font, max_text_w)) if part2 else 0
            if n1 + n2 <= MAX_LINES:
                layout = (cap, font,
                          balanced(draw, part1, font, n1),
                          balanced(draw, part2, font, n2) if n2 else [])
                break

    # 3. dernier recours : titre exceptionnellement long
    if layout is None:
        font = font_for_cap(font_path, MIN_CAP)
        layout = (MIN_CAP, font,
                  wrap(draw, part1, font, max_text_w),
                  wrap(draw, part2, font, max_text_w))

    cap, font, top, bottom = layout
    lines = [(t, INK_TOP) for t in top] + [(t, INK_BOTTOM) for t in bottom]
    gap = round(cap * LINE_GAP / CAP_HEIGHT)
    banner_h = PAD_TOP + len(lines) * cap + gap * (len(lines) - 1) + PAD_BOTTOM
    banner_w = max(text_width(draw, t, font) for t, _ in lines) + 2 * PAD_X

    bx0 = (CANVAS[0] - banner_w) / 2
    by0 = (CANVAS[1] - banner_h) / 2
    draw.rounded_rectangle([bx0, by0, bx0 + banner_w, by0 + banner_h],
                           radius=RADIUS, fill=BANNER)

    y = by0 + PAD_TOP
    for text, color in lines:
        box = draw.textbbox((0, 0), text, font=font)
        x = (CANVAS[0] - (box[2] - box[0])) / 2 - box[0]
        draw.text((x, y - box[1]), text, font=font, fill=color)
        y += cap + gap

    img.save(dest, "PNG", optimize=True)
    return [t for t, _ in lines], cap


def slugify(text, maxlen=60):
    t = clean_title(text).lower()
    t = (t.replace("é", "e").replace("è", "e").replace("ê", "e").replace("à", "a")
          .replace("ç", "c").replace("ô", "o").replace("û", "u").replace("î", "i")
          .replace("ù", "u").replace("â", "a"))
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:maxlen].strip("-") or "article"


# ── Programme principal ──────────────────────────────────────────────────────


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--titre", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    print(make_image(a.titre, a.out))
