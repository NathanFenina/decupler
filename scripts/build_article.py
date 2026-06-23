#!/usr/bin/env python3
"""
build_article.py — Assemble un article HTML publiable au format .lm-mcp.

Prend un fragment de body (le markup <div class="lm-mcp">…</div> rédigé par le
skill) et l'enrobe avec : les polices Google, le CSS .lm-mcp (base + composants,
lu depuis design-system/landing/), le script de masquage du titre du thème, et
le JSON-LD (FAQPage + Article) pour le SEO/GEO. Produit un HTML prêt à publier
via scripts/wp_publish.py.

Le CSS est INLINÉ (WordPress n'a pas accès aux fichiers du repo). Compte admin
avec unfiltered_html requis pour que <style>/<script> survivent (cf. mémoire).

Exemple
-------
python3 scripts/build_article.py \
    --body content/articles/meilleure-agence-geo.body.html \
    --title "Meilleure agence GEO : comment la choisir (critères 2026)" \
    --description "Comment choisir la meilleure agence GEO ? Les 7 critères..." \
    --faq content/articles/meilleure-agence-geo.faq.json \
    --out content/articles/meilleure-agence-geo.html
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS_DIR = ROOT / "design-system/landing"

FONTS = ('<link href="https://fonts.googleapis.com/css2?'
         'family=Space+Grotesk:wght@300;400;500;600;700'
         '&family=JetBrains+Mono:wght@400;500;700'
         '&family=Syne:wght@700;800&display=swap" rel="stylesheet">')

# Script de sécurité : masque le titre du thème (cf. mémoire — le CSS seul ne
# suffit pas toujours sous Astra).
HIDE_TITLE_SCRIPT = (
    "<script>document.addEventListener('DOMContentLoaded',function(){"
    "document.querySelectorAll('.entry-header,.entry-title,.ast-single-entry-banner,"
    ".page-header').forEach(function(e){e&&e.remove&&e.remove()});});</script>"
)


def read_css():
    base = (CSS_DIR / "lm-mcp.base.css").read_text(encoding="utf-8")
    comp = (CSS_DIR / "lm-mcp.components.css").read_text(encoding="utf-8")
    return f"{base}\n{comp}"


def faq_jsonld(faq):
    if not faq:
        return ""
    entities = [{
        "@type": "Question",
        "name": q["question"],
        "acceptedAnswer": {"@type": "Answer", "text": q["answer"]},
    } for q in faq]
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def article_jsonld(title, description, author):
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "author": {"@type": "Organization", "name": author},
        "publisher": {"@type": "Organization", "name": "Décupler"},
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def main():
    ap = argparse.ArgumentParser(description="Assemble un article .lm-mcp publiable")
    ap.add_argument("--body", required=True, help="Fragment HTML (markup .lm-mcp)")
    ap.add_argument("--title", required=True)
    ap.add_argument("--description", required=True)
    ap.add_argument("--faq", help="JSON : liste de {question, answer}")
    ap.add_argument("--author", default="Décupler")
    ap.add_argument("--out", required=True)
    ap.add_argument("--no-hide-title", action="store_true",
                    help="Ne pas injecter le script de masquage du titre")
    args = ap.parse_args()

    body = Path(args.body).read_text(encoding="utf-8").strip()
    faq = json.loads(Path(args.faq).read_text(encoding="utf-8")) if args.faq else None

    parts = [
        FONTS,
        f"<style>\n{read_css()}\n</style>",
        body,
        "" if args.no_hide_title else HIDE_TITLE_SCRIPT,
        article_jsonld(args.title, args.description, args.author),
        faq_jsonld(faq),
    ]
    html = "\n".join(p for p in parts if p)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(html, encoding="utf-8")

    chars = len(html)
    print(f"[article] {args.out} · {chars} caractères")
    print(f"          title: {args.title}")
    print(f"          meta : {args.description[:80]}…")
    if faq:
        print(f"          FAQ  : {len(faq)} questions (JSON-LD FAQPage)")
    print(f"\nPublier en brouillon :")
    print(f'  python3 scripts/wp_publish.py --type post --title "{args.title}" \\')
    print(f'      --content-file {args.out} --status draft')


if __name__ == "__main__":
    main()
