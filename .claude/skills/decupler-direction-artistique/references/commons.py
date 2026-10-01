#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cherche sur Wikimedia Commons des photos libres de ville, en paysage.

Pourquoi Commons et pas une image generee : une page « agence SEO Toulon »
qui affiche une ville inventee par un modele est un faux. Commons donne de
vraies photos, sous licence libre, avec l'auteur a citer — on cite.
"""
import json, os, re, sys, time, urllib.parse, urllib.request

UA = {"User-Agent": "decupler-seo/1.0 (https://decupler.com; projects@decupler.com)"}
API = "https://commons.wikimedia.org/w/api.php?"
# Gravures, plans et cartes anciennes : on veut une photo, pas une estampe.
REJET = re.compile(r"plan|carte|map|gravure|FMIB|engraving|1[6-9]\d\d|"
                   r"blason|coat of arms|logo|drapeau|flag", re.I)


def api(params):
    u = API + urllib.parse.urlencode(params)
    for essai in range(4):
        try:
            return json.load(urllib.request.urlopen(
                urllib.request.Request(u, headers=UA), timeout=60))
        except Exception:
            if essai == 3:
                raise
            time.sleep(2 ** essai)


def candidats(requete, mini_large=1800, n=12):
    d = api({"action": "query", "format": "json", "generator": "search",
             "gsrsearch": f"filetype:bitmap {requete}", "gsrnamespace": "6",
             "gsrlimit": str(n * 3), "prop": "imageinfo",
             "iiprop": "url|extmetadata|size|mime", "iiurlwidth": "1600"})
    out = []
    for p in (d.get("query", {}).get("pages") or {}).values():
        ii = p["imageinfo"][0]
        em = ii.get("extmetadata", {})
        titre = p["title"]
        if REJET.search(titre):
            continue
        if ii["mime"] not in ("image/jpeg", "image/png"):
            continue
        # Paysage seulement : les bandeaux du site sont larges.
        if ii["width"] < mini_large or ii["width"] <= ii["height"] * 1.2:
            continue
        lic = (em.get("LicenseShortName", {}).get("value") or "")
        if not re.search(r"CC|Public domain|CC0", lic, re.I):
            continue
        auteur = re.sub(r"<[^>]+>", "", em.get("Artist", {}).get("value") or "").strip()
        out.append({"titre": titre, "url": ii["url"], "vignette": ii["thumburl"],
                    "l": ii["width"], "h": ii["height"], "licence": lic,
                    "auteur": auteur[:70],
                    "page": "https://commons.wikimedia.org/wiki/"
                            + urllib.parse.quote(titre.replace(" ", "_"))})
        if len(out) >= n:
            break
    return out


if __name__ == "__main__":
    print(json.dumps(candidats(" ".join(sys.argv[1:])), ensure_ascii=False, indent=1))
