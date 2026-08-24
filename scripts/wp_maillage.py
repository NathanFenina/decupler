#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bascule les pages du cluster de EN_ATTENTE vers LIENS, une fois publiees.

Le pilier et les pages metier ne rendent une carte d'agent cliquable que si
son slug figure dans agents_locaux.LIENS. Ce script interroge WordPress,
deplace dans LIENS toutes les entrees dont la page est effectivement publiee,
puis rappelle ce qu'il reste a regenerer.

    python3 scripts/wp_maillage.py --dry-run
    python3 scripts/wp_maillage.py
"""
import os
import re
import sys
import json
import time
import base64
import argparse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "content", "data"))
from wp_publish import load_env      # noqa: E402
import agents_locaux as A            # noqa: E402

SRC = os.path.join(ROOT, "content/data/agents_locaux.py")


def publies(env, auth):
    site = env["WP_SITE_URL"].rstrip("/")
    vus = set()
    for num in (1, 2, 3):
        url = (f"{site}/wp-json/wp/v2/pages?context=edit&status=publish"
               f"&per_page=50&page={num}&_fields=slug")
        req = urllib.request.Request(url, headers={"Authorization": "Basic " + auth})
        for essai in range(6):
            try:
                lot = json.load(urllib.request.urlopen(req, timeout=120))
                break
            except Exception:
                if essai == 5:
                    raise
                time.sleep(2 ** essai)
        vus |= {p["slug"] for p in lot}
        if len(lot) < 50:
            break
    return vus


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    env = load_env()
    auth = base64.b64encode(
        f"{env['WP_USER']}:{env['WP_APP_PASSWORD']}".encode()).decode()
    en_ligne = publies(env, auth)

    a_basculer = {a: url for a, url in A.EN_ATTENTE.items()
                  if url.rstrip("/").rsplit("/", 1)[-1] in en_ligne}
    if not a_basculer:
        print("Rien a basculer : aucune page en attente n'est publiee.")
        return
    for a, url in sorted(a_basculer.items()):
        print(f"   → {a:<20} {url}")
    if args.dry_run:
        return

    s = open(SRC, encoding="utf-8").read()
    for a, url in a_basculer.items():
        ligne = re.search(rf"\n *'{re.escape(a)}': *'{re.escape(url)}',", s).group(0)
        s = s.replace(ligne, "", 1)
        s = s.replace("LIENS = {", "LIENS = {" + f"\n    '{a}': '{url}',", 1)
    open(SRC, "w", encoding="utf-8").write(s)
    print(f"\n{len(a_basculer)} agent(s) rendu(s) cliquable(s). "
          "Regenerer le pilier et les pages metier :\n"
          "   python3 content/pages-src/build_offre.py && "
          "python3 content/pages-src/build_metier.py --tout")


if __name__ == "__main__":
    main()
