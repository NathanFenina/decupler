#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ecrit les meta descriptions des pages WordPress deja publiees.

Yoast n'expose AUCUN champ SEO dans son schema REST (verifie : 32 meta sur le
type `page`, aucune SEO ; pas de route d'ecriture sous /yoast/v1/). En revanche,
Yoast > Types de contenu > Pages > Modele de meta description est regle sur
`%%excerpt%%` : la meta description servie dans le <head> est donc l'extrait
WordPress — un champ coeur, lui parfaitement ecrivable via l'API REST.

Ce script pousse content/data/meta_descriptions.py dans le champ `excerpt`.
Il ne touche ni au contenu, ni au titre, ni au statut.

    python3 scripts/wp_meta_desc.py --dry-run        # verifie sans ecrire
    python3 scripts/wp_meta_desc.py                  # ecrit tout
    python3 scripts/wp_meta_desc.py --ids 6090,5233  # ecrit une selection
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
sys.path.insert(0, os.path.join(ROOT, "content", "data"))

from wp_publish import load_env          # noqa: E402
from meta_descriptions import METAS      # noqa: E402

MINI, MAXI = 110, 160


def appel(url, auth, data=None):
    """GET/POST avec retry : decupler.com coupe la connexion par intermittence."""
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8") if data is not None else None,
        headers={"Authorization": "Basic " + auth,
                 "Content-Type": "application/json"},
        method="POST" if data is not None else "GET",
    )
    for essai in range(6):
        try:
            return json.load(urllib.request.urlopen(req, timeout=90))
        except urllib.error.HTTPError:
            raise
        except Exception:
            if essai == 5:
                raise
            time.sleep(2 ** essai)


def extrait_brut(x):
    """Uniquement `raw` : `rendered` contient l'extrait auto-genere par WP a
    partir du contenu (plusieurs milliers de caracteres ici), qui n'est pas ce
    qu'on ecrit."""
    if isinstance(x, dict):
        x = x.get("raw") or ""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", x)).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--ids", default=None, help="liste d'IDs separes par des virgules")
    args = ap.parse_args()

    cibles = METAS
    if args.ids:
        garder = {int(x) for x in args.ids.split(",")}
        cibles = {i: t for i, t in METAS.items() if i in garder}

    hors = [(i, len(t)) for i, t in cibles.items() if not MINI <= len(t) <= MAXI]
    if hors:
        sys.exit(f"❌ Longueurs hors format {MINI}-{MAXI} : {hors}")

    env = load_env()
    site = env["WP_SITE_URL"].rstrip("/")
    auth = base64.b64encode(
        f"{env['WP_USER']}:{env['WP_APP_PASSWORD']}".encode()).decode()

    ok = saute = 0
    for pid, meta in sorted(cibles.items()):
        page = appel(f"{site}/wp-json/wp/v2/pages/{pid}"
                     "?context=edit&_fields=id,slug,excerpt", auth)
        actuel = extrait_brut(page.get("excerpt", ""))
        if actuel == meta:
            saute += 1
            print(f"   = {pid:>6} /{page['slug']}/ (deja a jour)")
            continue
        if args.dry_run:
            print(f"   ~ {pid:>6} /{page['slug']}/ ({len(actuel)} → {len(meta)})")
            continue
        appel(f"{site}/wp-json/wp/v2/pages/{pid}", auth, {"excerpt": meta})
        ok += 1
        print(f"   ✔ {pid:>6} /{page['slug']}/ ({len(meta)} c.)")

    print(f"\n{ok} page(s) mise(s) a jour, {saute} deja a jour, "
          f"{len(cibles)} traitee(s).")


if __name__ == "__main__":
    main()
