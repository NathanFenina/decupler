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
import re
from pathlib import Path


def minify_css(css):
    """Minifie le CSS sur UNE seule ligne. Indispensable : WordPress applique
    wpautop au rendu et insère des <p>/<br> sur les lignes vides d'un <style>
    inline, ce qui casse le parsing CSS au front-end."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)      # commentaires
    css = re.sub(r"\s+", " ", css)                         # tout blanc -> 1 espace
    css = re.sub(r"\s*([{}:;,>])\s*", r"\1", css)          # espaces autour de la ponctuation
    return css.strip()

ROOT = Path(__file__).resolve().parent.parent
CSS_DIR = ROOT / "design-system/landing"

FONTS = ('<link href="https://fonts.googleapis.com/css2?'
         'family=Space+Grotesk:wght@300;400;500;600;700'
         '&family=JetBrains+Mono:wght@400;500;700'
         '&family=Syne:wght@700;800&display=swap" rel="stylesheet">')

# Script de sécurité : masque le titre du thème (cf. mémoire — le CSS seul ne
# suffit pas toujours sous Astra).
# --- Lead magnet : popup email gate → Substack (form POST dans un iframe caché) ---
GATE_HTML = (
    '<div id="ai-content-gate" class="ai-popup-overlay"><div class="ai-popup-card">'
    '<span class="ai-popup-icon">{icon}</span>'
    '<h3 class="ai-popup-title">{title}</h3>'
    '<p class="ai-popup-desc">{desc}</p>'
    '<iframe name="hidden_iframe" id="hidden_iframe" style="display:none"></iframe>'
    '<form id="ai-popup-form" action="{substack}/api/v1/free" method="post" target="hidden_iframe">'
    '<input type="email" name="email" placeholder="votre@email.com" class="ai-popup-input" required>'
    '<input type="hidden" name="first_url" value="{substack}">'
    '<input type="hidden" name="first_referrer" value="https://decupler.com">'
    '<button type="submit" class="ai-popup-submit">Recevoir le guide (gratuit) →</button>'
    '<p class="ai-popup-footer">🔒 Pas de spam. Désabonnement en 1 clic.</p></form>'
    '<div id="ai-success-msg" class="ai-success-message">✅ C\'est bon ! Bonne lecture.</div>'
    '</div></div>'
)
GATE_SCRIPT = (
    "<script>document.addEventListener('DOMContentLoaded',function(){"
    "var p=document.getElementById('ai-content-gate'),f=document.getElementById('ai-popup-form'),"
    "s=document.getElementById('ai-success-msg'), i=document.getElementById('hidden_iframe'),sub=false;"
    "function op(){if(localStorage.getItem('lmg_sub')==='true')return;"
    "if(document.cookie.indexOf('lmg_sub=true')!==-1)return;p.classList.add('active');"
    "document.body.classList.add('lmg-gated');document.body.style.overflow='hidden'}"
    "setTimeout(op,%(delay)s);"
    "function cl(){p.classList.remove('active');document.body.classList.remove('lmg-gated');document.body.style.overflow='auto'}"
    "if(f)f.addEventListener('submit',function(){sub=true;var b=f.querySelector('button[type=submit]');"
    "b.textContent='Validation…';b.style.opacity='0.7'});"
    "if(i)i.onload=function(){if(sub){f.style.display='none';s.style.display='block';"
    "localStorage.setItem('lmg_sub','true');document.cookie='lmg_sub=true; max-age=31536000; path=/';"
    "setTimeout(cl,1500);sub=false}};"
    "if(location.search.indexOf('reset=true')!==-1){localStorage.removeItem('lmg_sub');"
    "document.cookie='lmg_sub=; max-age=0; path=/'}});</script>"
)

HIDE_TITLE_SCRIPT = (
    "<script>document.addEventListener('DOMContentLoaded',function(){"
    "document.querySelectorAll('.entry-header,.entry-title,.ast-single-entry-banner,"
    ".page-header').forEach(function(e){e&&e.remove&&e.remove()});});</script>"
)


def read_css(extra=None):
    base = (CSS_DIR / "lm-mcp.base.css").read_text(encoding="utf-8")
    comp = (CSS_DIR / "lm-mcp.components.css").read_text(encoding="utf-8")
    css = f"{base}\n{comp}"
    for path in (extra or []):
        css += "\n" + Path(path).read_text(encoding="utf-8")
    return css


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
    ap.add_argument("--extra-css", nargs="*", default=[],
                    help="Fichiers CSS additionnels (skins/overlays) chargés après base+components")
    ap.add_argument("--img", nargs="*", default=[],
                    help="Remplacements de placeholders d'image, ex : __IMG_1__=https://…/img.png")
    ap.add_argument("--gate", default=None,
                    help="Active la popup email→Substack. Valeur = base Substack, ex https://decupler.substack.com")
    ap.add_argument("--gate-title", default="Débloquez le guide complet")
    ap.add_argument("--gate-desc", default="Laissez votre email pour recevoir le guide et nos meilleures méthodes SEO/GEO.")
    ap.add_argument("--gate-icon", default="🛠️")
    ap.add_argument("--gate-delay", default="5000", help="Délai (ms) avant l'apparition de la popup")
    args = ap.parse_args()

    body = Path(args.body).read_text(encoding="utf-8").strip()
    for mapping in args.img:
        key, _, url = mapping.partition("=")
        body = body.replace(key, url)
    body = re.sub(r"\n\s*\n+", "\n", body)  # supprime les lignes vides (évite wpautop)
    faq = json.loads(Path(args.faq).read_text(encoding="utf-8")) if args.faq else None

    gate_html = gate_script = ""
    if args.gate:
        sub = args.gate.rstrip("/")
        gate_html = GATE_HTML.format(icon=args.gate_icon, title=args.gate_title,
                                     desc=args.gate_desc, substack=sub)
        gate_script = GATE_SCRIPT % {"delay": args.gate_delay}

    parts = [
        FONTS,
        f"<style>{minify_css(read_css(args.extra_css))}</style>",
        body,
        gate_html,
        "" if args.no_hide_title else HIDE_TITLE_SCRIPT,
        gate_script,
        article_jsonld(args.title, args.description, args.author),
        faq_jsonld(faq),
    ]
    # tout sur des lignes simples : wpautop ne transforme que les lignes vides
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
