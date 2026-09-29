#!/usr/bin/env python3
"""Inventaire des contenus publiés sur decupler.com, depuis l'API WordPress.

Remplace l'inventaire que produisait l'ancien export XML : les scripts
d'opportunités (score_opportunities.py, build_content_map.py) lisent
content/cleaned/inventory.md pour savoir quelles pages existent déjà.

    python3 scripts/inventaire.py            # écrit content/cleaned/inventory.md

Le fichier est ignoré par git : il se régénère à la demande.
"""
import base64
import html
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from wp_publish import load_env  # noqa: E402

SORTIE = ROOT / "content" / "cleaned" / "inventory.md"


def wp(env, chemin):
    auth = base64.b64encode(f"{env['WP_USER']}:{env['WP_APP_PASSWORD']}".encode()).decode()
    url = env["WP_SITE_URL"].rstrip("/") + "/wp-json/wp/v2/" + chemin
    req = urllib.request.Request(url, headers={"Authorization": "Basic " + auth, "User-Agent": "decupler-inventaire/1.0"})
    with urllib.request.urlopen(req, timeout=90) as f:
        return json.load(f)


def main():
    env = load_env()
    lignes = []
    for type_wp, type_court in (("pages", "page"), ("posts", "post")):
        page = 1
        while True:
            lot = wp(env, f"{type_wp}?per_page=100&page={page}&status=publish&_fields=id,slug,title,modified")
            for x in lot:
                titre = html.unescape(x["title"]["rendered"]).replace("|", "/").strip()
                lignes.append((type_court, titre, x["slug"], x["modified"][:10], x["id"]))
            if len(lot) < 100:
                break
            page += 1
    lignes.sort(key=lambda l: (l[0], l[2]))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    with open(SORTIE, "w", encoding="utf-8") as f:
        f.write(f"# Inventaire decupler.com — {len(lignes)} contenus publiés\n\n")
        f.write("| type | titre | slug | modifié | id |\n|---|---|---|---|---|\n")
        for l in lignes:
            f.write("| " + " | ".join(str(c) for c in l) + " |\n")
    print(f"{len(lignes)} contenus → {SORTIE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
