#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rend une page Decupler dans Chromium et mesure le resultat.

Pourquoi ce script existe : lire le HTML ne suffit pas. Les trois derniers
defauts trouves sur les pages villes etaient tous invisibles au source —
une photo rendue a 2 000 px et decoupee en silence par overflow:hidden, une
colonne vide sur la moitie de sa hauteur, des pastilles illisibles sur un
ciel clair.

Et la capture ne suffit pas non plus : Chromium headless met en page a une
largeur et photographie a une autre, donc une capture peut montrer un
defaut qui n'existe pas. C'est deja arrive : un diagnostic « catastrophe
mobile » rendu sur un artefact de capture. D'ou la sonde DOM, qui compte
dans la page reelle les elements dont le bord droit depasse clientWidth.
C'est elle qui fait foi.

    python3 rendre.py page.html 1440
    python3 rendre.py page.html 505 21000 --cache ./loc

Le dossier de cache (--cache) permet de rapatrier images et polices en
local : sans lui, le rendu headless part sans les visuels ni Sora/Inter, et
on juge une page qui n'est pas celle du site.
"""
import argparse
import os
import re
import subprocess
import sys
import urllib.parse

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

# La sonde est injectee dans la page : elle mesure apres mise en page et
# apres chargement des images, ce qu'aucune analyse statique ne peut faire.
SONDE = """<script>window.addEventListener('load',function(){
var r=document.documentElement,n=0,pires=[];
document.querySelectorAll('body *').forEach(function(e){
  var b=e.getBoundingClientRect();
  if(b.right>r.clientWidth+1){n++;
    if(pires.length<5)pires.push(e.tagName+'.'+(e.className||'(sans classe)')
      +' right='+Math.round(b.right)+' w='+Math.round(b.width));}});
var d=document.createElement('div');d.id='SONDE';
d.setAttribute('data-v',r.clientWidth);d.setAttribute('data-s',r.scrollWidth);
d.setAttribute('data-n',n);d.setAttribute('data-h',document.body.scrollHeight);
d.setAttribute('data-q',pires.join(' || '));
d.style.display='none';document.body.appendChild(d);});</script>"""


def localise(html, cache):
    """Remplace les URL decupler.com par les fichiers du cache local."""
    if not cache or not os.path.isdir(cache):
        return html, []
    manque = []
    for u in set(re.findall(r'src="(https?://[^"]+)"', html)):
        nom = os.path.basename(urllib.parse.unquote(u.split("?")[0]))
        if os.path.exists(os.path.join(cache, nom)):
            html = html.replace(f'src="{u}"', f'src="{cache}/{nom}"')
        else:
            manque.append(nom)
    css = os.path.join(cache, "fonts.css")
    if os.path.exists(css):
        # Les polices Google ne se chargent pas en headless hors ligne : sans
        # substitution, tout le design retombe en system-ui et on juge faux.
        html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis[^>]+>',
                      "<style>" + open(css, encoding="utf-8").read() + "</style>",
                      html)
    return html, manque


def rends(fichier, largeur, hauteur, cache, sortie):
    html = open(fichier, encoding="utf-8").read()
    html, manque = localise(html, cache)
    if manque:
        print(f"   images absentes du cache (rendues vides) : {manque[:6]}")
    tmp = os.path.join(os.path.dirname(os.path.abspath(sortie)) or ".",
                       "_rendu.html")
    open(tmp, "w", encoding="utf-8").write(
        '<!doctype html><html lang="fr"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        + SONDE + '</head><body style="margin:0;background:#fff">'
        + html + "</body></html>")

    base = [CHROME, "--headless", "--disable-gpu", "--no-sandbox"]
    dom = subprocess.run(
        base + [f"--window-size={largeur},900", "--virtual-time-budget=9000",
                "--dump-dom", f"file://{tmp}"],
        capture_output=True, text=True).stdout
    m = re.search(r'<div id="SONDE" data-v="(\d+)" data-s="(\d+)" '
                  r'data-n="(\d+)" data-h="(\d+)" data-q="([^"]*)"', dom)
    ok = False
    if m:
        v, s, n, h, q = m.groups()
        ok = (v == s and n == "0")
        print(f"   sonde {largeur}px : viewport={v} scrollWidth={s} "
              f"debordements={n} hauteur={h}  {'✓' if ok else '✗'}")
        if q:
            print(f"      coupables : {q}")
    else:
        print("   ⚠️ sonde muette — la page n'a pas fini de charger ?")

    subprocess.run(
        base + ["--hide-scrollbars", f"--window-size={largeur},{hauteur}",
                f"--screenshot={sortie}", "--virtual-time-budget=11000",
                f"file://{tmp}"], capture_output=True)
    print(f"   capture : {sortie}")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fichier")
    ap.add_argument("largeur", nargs="?", type=int, default=1440)
    ap.add_argument("hauteur", nargs="?", type=int, default=16000)
    ap.add_argument("--cache", default=None,
                    help="dossier d'images et de polices rapatriees en local")
    ap.add_argument("--sortie", default=None)
    a = ap.parse_args()
    base = os.path.splitext(os.path.basename(a.fichier))[0]
    sortie = a.sortie or f"{base}-{a.largeur}.png"
    sys.exit(0 if rends(a.fichier, a.largeur, a.hauteur, a.cache, sortie) else 1)


if __name__ == "__main__":
    main()
