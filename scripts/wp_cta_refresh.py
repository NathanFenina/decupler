#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remplace le CSS du CTA « 10 prompts » dans les pages deja publiees.

Le CSS du CTA est inline dans chaque page : corriger le composant ne change
rien aux pages deja en ligne tant qu'on ne les repousse pas. Deux defauts a
corriger, tous deux releves par le detecteur d'anti-patterns d'impeccable :

  · blanc sur #8b5cf6 plafonnait a 4,23:1, sous le seuil WCAG AA de 4,5 ;
  · le titre en degrade transparent (background-clip:text) est une signature
    « genere par IA », et sa couleur reelle est transparent.

Ce script ne touche QUE le bloc <style> du CTA. Le contenu de la page, son
titre, son slug et son statut restent tels quels.

    python3 scripts/wp_cta_refresh.py --dry-run
    python3 scripts/wp_cta_refresh.py
"""
import os
import re
import sys
import json
import time
import base64
import argparse
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "content", "components"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "lib"))
from wp_publish import load_env     # noqa: E402
import cta_prompts as CTA           # noqa: E402
import wpcss                        # noqa: E402

# Le CSS neuf, passe par le meme durcissement que lors d'une publication :
# wpautop coupe sur les lignes vides, y compris dans un <style>.
CSS_NEUF = wpcss.harden(CTA.CSS)

# Un bloc <style> est celui du CTA s'il declare la variable --pv du composant.
BLOC = re.compile(r'<style>(?:(?!</style>).)*?\.pcta\{--pv:(?:(?!</style>).)*?</style>', re.S)

# Pages volontairement ignorees : ni indexees, ni servies aux visiteurs.
IGNORE = {"homepage", "decupler-2"}


def appel(url, auth, data=None):
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8") if data is not None else None,
        headers={"Authorization": "Basic " + auth, "Content-Type": "application/json"},
        method="POST" if data is not None else "GET")
    for essai in range(6):
        try:
            return json.load(urllib.request.urlopen(req, timeout=120))
        except urllib.error.HTTPError:
            raise
        except Exception:
            if essai == 5:
                raise
            time.sleep(2 ** essai)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--statut", default="publish", choices=["publish", "draft"])
    args = ap.parse_args()

    env = load_env()
    site = env["WP_SITE_URL"].rstrip("/")
    auth = base64.b64encode(
        f"{env['WP_USER']}:{env['WP_APP_PASSWORD']}".encode()).decode()

    pages = []
    for num in (1, 2, 3):
        lot = appel(f"{site}/wp-json/wp/v2/pages?context=edit&status={args.statut}"
                    f"&per_page=50&page={num}&_fields=id,slug,content", auth)
        pages += lot
        if len(lot) < 50:
            break

    fait = saute = 0
    for p in pages:
        html = p["content"].get("raw") or ""
        if p["slug"] in IGNORE or ".pcta{--pv:" not in html:
            continue
        neuf, n = BLOC.subn(lambda _: CSS_NEUF, html)
        if n != 1:
            print(f"   ? {p['slug']} : {n} bloc(s) CTA trouve(s), page ignoree")
            continue
        if neuf == html:
            saute += 1
            continue
        if args.dry_run:
            print(f"   ~ {p['id']:>6} /{p['slug']}/")
            continue
        appel(f"{site}/wp-json/wp/v2/pages/{p['id']}", auth, {"content": neuf})
        fait += 1
        print(f"   ✔ {p['id']:>6} /{p['slug']}/")

    print(f"\n{fait} page(s) mise(s) a jour, {saute} deja a jour.")


if __name__ == "__main__":
    main()
