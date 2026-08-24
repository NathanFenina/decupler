#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenere et republie une ou plusieurs pages du cluster.

Le titre, le slug et la meta viennent de content/data/pages_cluster.py :
la page WordPress n'est jamais la source de verite, le depot l'est.

    python3 scripts/wp_cluster.py supprimer-un-avis-google
    python3 scripts/wp_cluster.py --tout --statut draft
"""
import os
import re
import sys
import json
import time
import base64
import argparse
import subprocess
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "content", "data"))
from wp_publish import load_env          # noqa: E402
import pages_cluster as PC               # noqa: E402


def ids_wordpress(env, auth, slugs):
    """WordPress ne repond pas a une requete multi-slug sur les brouillons :
    on liste par statut, puis on associe."""
    site = env["WP_SITE_URL"].rstrip("/")
    trouve = {}
    for statut in ("draft", "publish"):
        for page in (1, 2, 3):
            url = (f"{site}/wp-json/wp/v2/pages?context=edit&status={statut}"
                   f"&per_page=50&page={page}&_fields=id,slug")
            req = urllib.request.Request(url, headers={"Authorization": "Basic " + auth})
            for essai in range(6):
                try:
                    lot = json.load(urllib.request.urlopen(req, timeout=90))
                    break
                except Exception:
                    if essai == 5:
                        raise
                    time.sleep(2 ** essai)
            for p in lot:
                if p["slug"] in slugs:
                    trouve[p["slug"]] = p["id"]
            if len(lot) < 50:
                break
    return trouve


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--tout", action="store_true")
    ap.add_argument("--statut", default="draft", choices=["draft", "publish"])
    ap.add_argument("--sans-publier", action="store_true", help="regenere sans toucher a WordPress")
    args = ap.parse_args()

    slugs = list(PC.PAGES) if args.tout else args.slugs
    inconnus = [s for s in slugs if s not in PC.PAGES]
    if not slugs or inconnus:
        sys.exit(f"❌ slug(s) inconnu(s) : {inconnus or 'aucun slug donne'}")

    for slug in slugs:
        r = subprocess.run([sys.executable, os.path.join(ROOT, "content/pages-src/build_page.py"), slug],
                           capture_output=True, text=True)
        if r.returncode:
            sys.exit(f"❌ {slug} : {r.stdout}{r.stderr}")
        print(f"   {r.stdout.strip()}")

    if args.sans_publier:
        return

    env = load_env()
    site = env["WP_SITE_URL"].rstrip("/")
    auth = base64.b64encode(
        f"{env['WP_USER']}:{env['WP_APP_PASSWORD']}".encode()).decode()
    ids = ids_wordpress(env, auth, set(slugs))

    for slug in slugs:
        page = PC.PAGES[slug]
        cible = ids.get(slug)
        cmd = [sys.executable, os.path.join(ROOT, "scripts/wp_publish.py"),
               "--type", "page", "--title", page["titre_seo"], "--slug", slug,
               "--excerpt", page["meta"], "--status", args.statut,
               "--content-file", os.path.join(ROOT, f"content/articles/{slug}.html")]
        if cible:
            cmd += ["--id", str(cible)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        etat = "✔" if r.returncode == 0 else "✖"
        print(f"{etat} {slug} → id {cible or 'nouveau'} ({args.statut})")
        if r.returncode:
            print((r.stdout + r.stderr)[-300:])


if __name__ == "__main__":
    main()
