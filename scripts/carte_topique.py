#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Carte topique : range les URL du sitemap en silos et y colle les mesures GSC.

Pourquoi ce script plutot qu'un tableur : un silo n'est pas un repertoire,
c'est une INTENTION commerciale. « agence-geo-lyon » et « agence-geo-nice »
appartiennent au meme silo geographique alors que rien dans leur URL ne les
relie, et « installer-mcp-data-for-seo-sur-chatgpt » n'a rien a voir avec
« agence-referencement-chatgpt » malgre le mot commun. Le classement est donc
une regle ecrite, relue et versionnee — pas un tri manuel a refaire.

Sortie : le tableau par silo, les grappes qui se cannibalisent, et les URL
declarees au sitemap que Google n'indexe pas.

    # 1. recuperer le sitemap
    python3 scripts/carte_topique.py --sitemap        > /tmp/sitemap.txt
    # 2. croiser avec un export d'inspection d'URL (voir scripts/gsc.py)
    python3 scripts/carte_topique.py --sitemap-fichier /tmp/sitemap.txt \
        --perf /tmp/plan-333.csv

Le fichier --perf est un CSV a point-virgule avec au moins les colonnes
url, clics_12m, impressions_12m, position_moy.
"""
import argparse
import collections
import csv
import re
import sys
import urllib.parse
import urllib.request

SITE = "https://decupler.com"

# Les silos, dans l'ordre : le PREMIER motif qui correspond gagne, donc les
# regles les plus specifiques sont en haut. Chaque entree dit ce que le silo
# vend, parce que c'est la seule question qui compte pour un maillage.
SILOS = [
    ("GEO — pages villes",
     r"agence-geo-(bordeaux|lille|lyon|marseille|nantes|nice|paris|toulouse)"),
    ("SEO local — villes 06/83",
     r"(agence|consultant|expert|freelance)-(seo|referencement)-"
     r"(nice|cannes|antibes|monaco|toulon|grasse|menton|frejus|cagnes|cannet)"),
    ("GEO — offre & marque",
     r"(agence-geo$|meilleure-agence-geo|audit-geo|playbook-geo|bootcamp-geo"
     r"|consultant-geo$|visibilite-llm|dominer-les-moteurs|devenir-la-reference"
     r"|matrice-gap-geo|seo-geo-team|seo-ai-systems)"),
    ("GEO — editorial",
     r"(cest-quoi-le-geo|expert-geo|freelance-geo|geo-saas|agences-geo-france"
     r"|top-agences-geo|reddit-pour|forum-llm|worflow-recherche-prompt-geo"
     r"|audit-geo-claude-code|agence-aeo)"),
    ("Outillage Claude / MCP",
     r"(claude-skills|claude-code|installer-mcp|mcp-agent|wordpress-mcp"
     r"|openclawseo|connecter-search-console-claude|ahrefs-contenu-ia)"),
    ("Moteurs IA nommes",
     r"(chatgpt|perplexity|gemini|visibilite-chatgpt|etre-cite-par"
     r"|comment-apparaitre)"),
    ("SEO classique — offre",
     r"(^agence-seo$|accompagnement-seo|machine-de-guerre-seo|seo-local"
     r"|seo-saas|seo-e-commerce|automatisation-seo|mesurer-sa-visibilite"
     r"|visibilite-en-ligne|organic-opportunity-map|cartographie-ia"
     r"|mini-analyse|agence-referencement-ia|agence-seo-ia"
     r"|agence-visibilite-ia)"),
    ("Google Business Profile",
     r"(fiche-gmb|agent-fiche-google|agent-posts-google|agent-messagerie-google"
     r"|citations-locales|avis-google|obtenir-des-avis|repondre-aux-avis"
     r"|supprimer-un-avis|agent-mots-cles-locaux)"),
    ("Agents IA — produit",
     r"agent-(estimation|parrainage|rappel|rapport|reactivation|relance"
     r"|satisfaction|sms|vocal)"),
    ("Sites web — produit",
     r"(creation-site-internet|site-gratuit-local|site-internet-offert"
     r"|guide-site-ia|creer-app-ecommerce|chatbot-wordpress"
     r"|standard-telephonique|transformer-une-video|app$|boutique|commander"
     r"|panier|mon-compte)"),
    ("Preuve — etudes de cas", r"(etude-de-cas|cas-clients)"),
    ("Acquisition", r"(webinaire|newsletter|confirmation-de-rdv|politique"
                    r"|decupler-2|blog$)"),
    ("SEO classique — editorial", r".+"),  # tout le reste : c'est le fourre-tout
]

# Les grappes a surveiller : une intention, plusieurs pages. Le mot commun ne
# suffit pas a definir une grappe — c'est pour ca qu'elles sont listees a la
# main, avec ce qu'on veut en garder.
GRAPPES = {
    "ChatGPT": (r"(chatgpt|comment-apparaitre|etre-cite)", 2),
    "agence + discipline": (r"^agence-(seo|geo|aeo|referencement|visibilite)"
                            r"(?!-(bordeaux|lille|lyon|marseille|nantes|paris"
                            r"|toulouse|nice|cannes|antibes|monaco|toulon))", 2),
    "avis Google": (r"avis-google", 1),
    "villes GEO hors 06": (r"agence-geo-(bordeaux|lille|lyon|marseille|nantes"
                           r"|paris|toulouse)", 7),
}


def slug(u):
    return urllib.parse.unquote(u).replace(SITE + "/", "").rstrip("/")


def silo(u):
    s = slug(u)
    for nom, rx in SILOS:
        if re.search(rx, s):
            return nom
    return "NON CLASSE"


def recupere_sitemap():
    """Lit l'index puis chaque sous-sitemap. Yoast en publie un par type."""
    def lis(url):
        r = urllib.request.Request(url, headers={"User-Agent": "decupler-carte/1.0"})
        return urllib.request.urlopen(r, timeout=90).read().decode("utf-8", "replace")

    index = lis(SITE + "/sitemap_index.xml")
    out = []
    for sm in re.findall(r"<loc>([^<]+sitemap\.xml)</loc>", index):
        nom = sm.rsplit("/", 1)[-1].replace(".xml", "")
        for u in re.findall(r"<loc>([^<]+)</loc>", lis(sm)):
            if not u.endswith(".xml"):
                out.append((nom, u))
    return out


def charge_perf(chemin):
    perf = {}
    with open(chemin, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f, delimiter=";"):
            u = urllib.parse.unquote(r["url"]).rstrip("/")
            perf[u] = {
                "clics": int(r.get("clics_12m") or 0),
                "imp": int(r.get("impressions_12m") or 0),
                "pos": float(r.get("position_moy") or 0),
                "pile": r.get("pile", ""),
            }
    return perf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sitemap", action="store_true",
                    help="imprime le sitemap (type<espace>url) et s'arrete")
    ap.add_argument("--sitemap-fichier",
                    help="sitemap deja recupere, au lieu d'un appel reseau")
    ap.add_argument("--perf", help="CSV des mesures GSC")
    a = ap.parse_args()

    if a.sitemap_fichier:
        urls = [tuple(l.split(None, 1)) for l in
                open(a.sitemap_fichier, encoding="utf-8") if l.strip()]
        urls = [(t, u.strip()) for t, u in urls]
    else:
        urls = recupere_sitemap()
        if a.sitemap:
            for t, u in urls:
                print(f"{t} {u}")
            return

    sitemap = {u.rstrip("/"): t for t, u in urls}
    perf = charge_perf(a.perf) if a.perf else {}

    tab = collections.defaultdict(
        lambda: {"n": 0, "idx": 0, "clics": 0, "imp": 0, "pos": []})
    for u in sitemap:
        d = tab[silo(u)]
        d["n"] += 1
        p = perf.get(u)
        if p:
            d["idx"] += 1
            d["clics"] += p["clics"]
            d["imp"] += p["imp"]
            if p["pos"]:
                d["pos"].append(p["pos"])

    print(f'{"silo":30} {"URL":>4} {"idx":>4} {"clics":>6} {"imp":>8} {"pos":>6}')
    print("-" * 64)
    for s, d in sorted(tab.items(), key=lambda x: -x[1]["imp"]):
        pos = sum(d["pos"]) / len(d["pos"]) if d["pos"] else 0
        print(f'{s:30} {d["n"]:>4} {d["idx"]:>4} {d["clics"]:>6} '
              f'{d["imp"]:>8} {pos:>6.1f}')
    print("-" * 64)
    print(f'{"TOTAL":30} {len(sitemap):>4} '
          f'{sum(d["idx"] for d in tab.values()):>4} '
          f'{sum(d["clics"] for d in tab.values()):>6} '
          f'{sum(d["imp"] for d in tab.values()):>8}')

    if perf:
        print("\n=== Grappes : plusieurs pages pour une intention ===")
        for nom, (rx, cible) in GRAPPES.items():
            membres = []
            for u in sitemap:
                if re.search(rx, slug(u)):
                    p = perf.get(u)
                    membres.append((p["clics"] if p else -1,
                                    p["imp"] if p else 0, slug(u)))
            if len(membres) <= cible:
                continue
            membres.sort(reverse=True)
            tc = sum(m[0] for m in membres if m[0] > 0)
            print(f'\n  {nom} : {len(membres)} pages, {tc} clics '
                  f'→ cible {cible}')
            for c, i, s in membres:
                etat = "non indexée" if c < 0 else f"{c:>4} clics {i:>6} imp"
                print(f'    {etat:22} {s}')

        muettes = [u for u in sitemap if u not in perf]
        print(f"\n=== Declarees au sitemap, absentes de l'index : "
              f"{len(muettes)}/{len(sitemap)} "
              f"({100 * len(muettes) // len(sitemap)} %) ===")
        par_silo = collections.Counter(silo(u) for u in muettes)
        for s, n in par_silo.most_common():
            print(f'  {n:>3}  {s}')


if __name__ == "__main__":
    sys.exit(main())
