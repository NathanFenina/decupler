#!/usr/bin/env python3
"""
Nettoyage du contenu extrait (content/cleaned/) pour Next.js.

- Pages  : HTML nettoyé (on retire styles/scripts/svg + tous les attributs
           parasites class/style/id/data-*). -> content/cleaned/pages_clean/<slug>.html
- Blog   : conversion en MDX avec frontmatter. -> content/cleaned/blog_mdx/<slug>.mdx

Usage:
    python3 scripts/clean_content.py
"""
import os
import re
import glob
import json

from bs4 import BeautifulSoup, Comment
from markdownify import markdownify as md

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLEAN = os.path.join(ROOT, "content", "cleaned")

# Méta SEO Yoast produites par parse_wxr.py
SEO_META = {}
_meta_path = os.path.join(CLEAN, "seo-meta.json")
if os.path.exists(_meta_path):
    SEO_META = json.load(open(_meta_path, encoding="utf-8"))


def yaml_escape(s):
    return (s or "").replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()

# Pages techniques / e-commerce à ignorer (décision utilisateur : pas d'e-commerce)
SKIP = {"boutique", "panier", "mon-compte", "commander", "home-old-2"}

# Attributs qu'on garde (le reste est supprimé)
KEEP_ATTRS = {
    "a": {"href"},
    "img": {"src", "alt"},
}


def read_meta(raw):
    """Récupère titre/url/date depuis les commentaires en tête de fichier."""
    meta = {"titre": "", "url": "", "date": ""}
    for key in meta:
        m = re.search(rf"<!--\s*{key}:\s*(.*?)\s*-->", raw)
        if m:
            meta[key] = m.group(1)
    return meta


def clean_soup(raw):
    soup = BeautifulSoup(raw, "html.parser")

    # Retirer commentaires (dont nos métadonnées)
    for c in soup.find_all(string=lambda t: isinstance(t, Comment)):
        c.extract()
    # Retirer styles, scripts, svg (icônes décoratives)
    for tag in soup(["style", "script", "svg", "noscript", "iframe"]):
        tag.decompose()

    # Nettoyer les attributs parasites
    for tag in soup.find_all(True):
        allowed = KEEP_ATTRS.get(tag.name, set())
        for attr in list(tag.attrs):
            if attr not in allowed:
                del tag.attrs[attr]

    # Déballer les div/span/figure (mise en page Elementor) MAIS garder les
    # <section> : elles donnent le rythme vertical de la page (auto-stylées en CSS).
    for tag in soup.find_all(["div", "span", "figure"]):
        tag.unwrap()
    # Supprimer les <section> devenues vides
    for tag in soup.find_all("section"):
        if not tag.get_text(strip=True) and not tag.find("img"):
            tag.decompose()

    # Supprimer les balises devenues vides
    for tag in soup.find_all(["p", "li", "h1", "h2", "h3", "h4"]):
        if not tag.get_text(strip=True) and not tag.find("img"):
            tag.decompose()

    return soup


def process_pages():
    out_dir = os.path.join(CLEAN, "pages_clean")
    os.makedirs(out_dir, exist_ok=True)
    n = 0
    for path in sorted(glob.glob(os.path.join(CLEAN, "pages", "*.html"))):
        slug = os.path.splitext(os.path.basename(path))[0]
        if slug in SKIP:
            continue
        raw = open(path, encoding="utf-8").read()
        meta = read_meta(raw)
        soup = clean_soup(raw)
        html = str(soup).strip()
        if len(html) < 200:
            continue
        with open(os.path.join(out_dir, slug + ".html"), "w", encoding="utf-8") as f:
            f.write(html)
        n += 1
    return n


def process_blog():
    out_dir = os.path.join(CLEAN, "blog_mdx")
    os.makedirs(out_dir, exist_ok=True)
    n = 0
    for path in sorted(glob.glob(os.path.join(CLEAN, "blog", "*.html"))):
        slug = os.path.splitext(os.path.basename(path))[0]
        raw = open(path, encoding="utf-8").read()
        meta = read_meta(raw)
        soup = clean_soup(raw)
        markdown = md(str(soup), heading_style="ATX", strip=["style", "script"])
        # compacter les lignes vides multiples
        markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()

        seo = SEO_META.get(slug, {})
        title = yaml_escape(meta["titre"] or slug)
        seo_title = yaml_escape(seo.get("seo_title") or title)
        description = yaml_escape(seo.get("description"))
        with open(os.path.join(out_dir, slug + ".mdx"), "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f'title: "{title}"\n')
            f.write(f'seoTitle: "{seo_title}"\n')
            f.write(f'description: "{description}"\n')
            f.write(f'date: "{meta["date"][:10]}"\n')
            f.write(f'slug: "{slug}"\n')
            if seo.get("focus_keyword"):
                f.write(f'focusKeyword: "{yaml_escape(seo["focus_keyword"])}"\n')
            f.write(f'sourceUrl: "{meta["url"]}"\n')
            f.write("---\n\n")
            f.write(markdown + "\n")
        n += 1
    return n


if __name__ == "__main__":
    p = process_pages()
    b = process_blog()
    print(f"Pages nettoyées (HTML) : {p}  -> content/cleaned/pages_clean/")
    print(f"Articles convertis (MDX): {b}  -> content/cleaned/blog_mdx/")
