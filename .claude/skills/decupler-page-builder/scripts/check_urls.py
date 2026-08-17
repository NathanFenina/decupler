#!/usr/bin/env python3
"""Regenere l'inventaire des URLs vivantes de decupler.com.

Le site renvoie 410 Gone (pas 404) sur les URLs supprimees : les deux comptent
comme mortes. Les requetes sont SEQUENTIELLES — au-dela d'une dizaine d'appels
concurrents le serveur renvoie des reponses incoherentes.

    python check_urls.py                      # inventaire complet depuis le site
    python check_urls.py --urls a.json        # revalide une liste existante
"""
import os
import sys
import json
import time
import argparse
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wp_client import WP, load_env  # noqa: E402

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(os.path.dirname(ICI), "references", "urls.json")

# mortes connues, conservees pour memoire meme si elles disparaissent de l'index
MORTES_CONNUES = ["/search-everywhere/", "/tarifs/", "/llms.txt"]


def statut(url, ua="DecuplerSkill/1.0"):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": ua})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    except urllib.error.HTTPError as ex:
        return ex.code
    except Exception:
        return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--urls", help="JSON d'URLs a revalider au lieu de l'index")
    ap.add_argument("--sortie", default=SORTIE)
    a = ap.parse_args()

    wp = WP(load_env())
    site = wp.site

    if a.urls:
        cibles = json.load(open(a.urls, encoding="utf-8"))
    else:
        cibles = []
        for pt in ("posts", "pages"):
            page = 1
            while True:
                d, h = wp.get(pt, {"per_page": 100, "page": page,
                                   "status": "publish", "_fields": "link"})
                cibles += [urllib.parse.urlparse(x["link"]).path for x in d]
                if page >= int(h.get("X-WP-TotalPages", 1)):
                    break
                page += 1
        cibles += MORTES_CONNUES

    cibles = sorted({c if c.startswith("/") else "/" + c for c in cibles})
    vivantes, mortes = [], {}
    print(f"{len(cibles)} URLs a verifier (sequentiel)\n")
    for i, u in enumerate(cibles, 1):
        c = statut(site + u)
        if c == 200:
            vivantes.append(u)
        else:
            mortes[u] = c
            print(f"  {c}  {u}")
        if i % 25 == 0:
            print(f"  … {i}/{len(cibles)}")
        time.sleep(0.15)

    json.dump({"site": site, "vivantes": sorted(vivantes),
               "mortes": mortes}, open(a.sortie, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"\n✓ {len(vivantes)} vivantes · {len(mortes)} mortes → {a.sortie}")
    if mortes:
        print("  ⚠ ne jamais mailler vers ces URLs")


if __name__ == "__main__":
    main()
