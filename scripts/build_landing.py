#!/usr/bin/env python3
"""
build_landing.py — Prépare une landing HTML autoportante (avec son propre <style>)
pour publication dans une page WordPress SANS casser le thème.

Ce que ça fait :
  1. Extrait le <style> et le contenu <body> d'un fichier HTML complet.
  2. SCOPE tout le CSS sous un conteneur unique (ex .oom) pour qu'il ne fuie pas
     dans le thème (body/*/section deviennent .oom, .oom *, .oom section…).
     Les @keyframes et @font-face sont laissés tels quels ; les @media sont
     transformés récursivement.
  3. Enveloppe le body dans <div class="{scope}"> et le fait sortir en pleine
     largeur (breakout 100vw), masque le titre de page du thème.
  4. Minifie le CSS sur une ligne (wpautop casserait un <style> multi-lignes)
     et supprime les lignes vides du body (évite les <p>/<br> parasites).

Usage :
  python3 scripts/build_landing.py --src content/pages/x.src.html \
      --out content/pages/x.html --scope oom

Publier ensuite (nouvelle page brouillon) :
  python3 scripts/wp_publish.py --type page --title "…" --slug x \
      --content-file content/pages/x.html --status draft
"""
import argparse
import re
from pathlib import Path


def minify_css(css: str) -> str:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{}:;,>])\s*", r"\1", css)
    return css.strip()


def scope_selectors(selector_list: str, scope: str) -> str:
    dot = f".{scope}"
    out = []
    for s in (x.strip() for x in selector_list.split(",")):
        if not s:
            continue
        if s == ":root" or s == "body":
            out.append(dot)                       # vars + styles de base sur le conteneur
        elif s == "html":
            out.append("html")                    # global inoffensif (scroll-behavior)
        elif s == "*":
            out.append(f"{dot} *")
        elif s == dot or s.startswith(dot + " ") or s.startswith(dot + ":") or s.startswith(dot + "."):
            out.append(s)                         # déjà scopé
        else:
            out.append(f"{dot} {s}")
    return ",".join(out)


def scope_css(css: str, scope: str) -> str:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    result = ""
    pos, n = 0, len(css)
    while pos < n:
        brace = css.find("{", pos)
        if brace == -1:
            result += css[pos:]
            break
        prelude = css[pos:brace].strip()
        depth, j = 1, brace + 1
        while j < n and depth:
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
            j += 1
        body = css[brace + 1:j - 1]
        low = prelude.lower()
        if low.startswith(("@keyframes", "@-webkit-keyframes", "@font-face")):
            result += f"{prelude}{{{body}}}\n"
        elif low.startswith(("@media", "@supports")):
            result += f"{prelude}{{\n{scope_css(body, scope)}\n}}\n"
        elif prelude.startswith("@"):
            result += f"{prelude}{{{body}}}\n"
        else:
            result += f"{scope_selectors(prelude, scope)}{{{body}}}\n"
        pos = j
    return result


# CSS qui neutralise le thème (Astra) pour cette page : titre masqué, pleine largeur.
def theme_override(scope: str) -> str:
    return f"""
body .ast-article-single>.entry-header,body .ast-article-single .entry-title,.entry-title,
.ast-single-entry-banner,header.entry-header,.page-header,.ast-archive-description{{display:none!important;height:0!important;overflow:hidden!important;visibility:hidden!important}}
.site-content .ast-container,.site-content #primary,.entry-content,.site-content,#content{{max-width:100%!important;padding-top:0!important;padding-bottom:0!important}}
.ast-separate-container .ast-article-single{{padding:0!important;background:transparent!important}}
.{scope}{{width:100vw;max-width:100vw;margin-left:calc(50% - 50vw)!important;margin-right:calc(50% - 50vw)!important}}
html,body,#page,.site,.ast-page-wrapper,#content,.site-content{{background:#fafafa!important}}
.post-navigation,.nav-links,.ast-single-related-posts,.ast-author-box,.ast-navigation-post{{display:none!important}}
"""


# ⚠️ Aucun "&" dans le JS inline : WordPress échappe "&&" en "&#038;&#038;" au rendu,
# ce qui casse le script (Uncaught SyntaxError). Écrire les conditions sans "&&".
HIDE_TITLE_SCRIPT = (
    "<script>document.addEventListener('DOMContentLoaded',function(){"
    "document.querySelectorAll('.entry-header,.entry-title,.ast-single-entry-banner,"
    ".page-header').forEach(function(e){if(e){if(e.remove){e.remove();}}});});</script>"
)


def assert_no_amp_in_scripts(html: str) -> None:
    """WordPress transforme tout "&" du JS inline en "&#038;" → SyntaxError au front.
    On refuse de générer un fichier qui casserait en prod."""
    for script in re.findall(r"<script[^>]*>(.*?)</script>", html, flags=re.S | re.I):
        if "&" in script:
            ctx = [m.group(0) for m in re.finditer(r".{0,40}&.{0,40}", script, flags=re.S)]
            raise SystemExit(
                "❌ Le JS inline contient un « & » (ex : &&). WordPress l'échappera en "
                "&#038; et cassera le script.\n   Réécris sans « & » (if imbriqués).\n   "
                + "\n   ".join(repr(c) for c in ctx[:5])
            )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--scope", default="oom", help="Nom de la classe conteneur")
    args = ap.parse_args()

    raw = Path(args.src).read_text(encoding="utf-8")
    m_style = re.search(r"<style[^>]*>(.*?)</style>", raw, flags=re.S | re.I)
    m_body = re.search(r"<body[^>]*>(.*?)</body>", raw, flags=re.S | re.I)
    if not m_style or not m_body:
        raise SystemExit("❌ <style> ou <body> introuvable dans le source")

    scoped = scope_css(m_style.group(1), args.scope) + theme_override(args.scope)
    css = minify_css(scoped)
    body = m_body.group(1).strip()
    body = re.sub(r"\n\s*\n+", "\n", body)  # pas de lignes vides (wpautop)

    content = (
        f"<style>{css}</style>\n"
        f'<div class="{args.scope}">\n{body}\n</div>\n'
        f"{HIDE_TITLE_SCRIPT}"
    )
    assert_no_amp_in_scripts(content)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(content, encoding="utf-8")
    print(f"[landing] {args.out} · {len(content)} caractères · scope=.{args.scope}")


if __name__ == "__main__":
    main()
