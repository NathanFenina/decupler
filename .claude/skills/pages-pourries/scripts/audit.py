#!/usr/bin/env python3
"""Audit des pages « pourries » de decupler.com.

Croise, pour chaque page et article publiés :
  - Search Console sur 180 jours (impressions, clics, position) ;
  - le contenu WordPress (nombre de mots, date de modification, constructeur) ;
  - des signaux d'obsolescence (anciens modèles d'IA, années passées) ;
  - la présence d'une pop-up email (information : le contrôleur de l'en-tête
    la rend fermable pour tout visiteur hors campagne ?acces=linkedin).

Chaque page reçoit un verdict et une action proposée. Rien n'est modifié.

    python3 .claude/skills/pages-pourries/scripts/audit.py --sortie /tmp/audit
    → /tmp/audit/audit.json et /tmp/audit/audit.md

Secrets : .env (WP_SITE_URL, WP_USER, WP_APP_PASSWORD, GSC_*), jamais affichés.
"""
import argparse
import base64
import datetime
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
sys.path.insert(0, os.path.join(RACINE, "scripts"))
from wp_publish import load_env  # noqa: E402
import gsc  # noqa: E402

# Mentions qui datent un contenu IA. Une seule suffit à le signaler.
OBSOLETE = [
    (r"claude\s*3(\.5)?\b", "Claude 3 / 3.5"),
    (r"gpt-?4o?\b(?!\.\d)", "GPT-4 / 4o"),
    (r"gemini\s*1\.5", "Gemini 1.5"),
    (r"gemini\s*2\.0", "Gemini 2.0"),
    (r"\ben\s+2024\b", "« en 2024 »"),
    (r"\b2024\s*:", "titre daté 2024"),
]
SEUILS = {"mince": 400, "vieux_jours": 365}


def wp(env, chemin):
    auth = base64.b64encode(f"{env['WP_USER']}:{env['WP_APP_PASSWORD']}".encode()).decode()
    url = env["WP_SITE_URL"].rstrip("/") + "/wp-json/wp/v2/" + chemin
    r = urllib.request.Request(url, headers={"Authorization": "Basic " + auth, "User-Agent": "decupler-audit/1.0"})
    with urllib.request.urlopen(r, timeout=90) as f:
        return json.load(f)


def texte(brut):
    brut = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", brut, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", brut))).strip()


def contenus(env):
    for t in ("pages", "posts"):
        page = 1
        while True:
            lot = wp(env, f"{t}?per_page=50&page={page}&status=publish&context=edit"
                          "&_fields=id,slug,link,title,content,modified,meta,template")
            for x in lot:
                x["_type"] = t
                yield x
            if len(lot) < 50:
                break
            page += 1


def verdict(p):
    """Règles simples et lisibles : la décision finale reste humaine."""
    imp, pos, mots, age = p["impressions"], p["position"], p["mots"], p["age_jours"]
    if p["mots"] < 80 and imp == 0:
        return "vide", "Supprimer (410) ou rediriger vers la page la plus proche"
    if imp == 0 and age > 180:
        return "morte", "Rediriger vers le pilier du sujet, ou fusionner"
    if p["obsolete"] and imp > 0:
        return "périmée", "Mettre à jour (modèles, dates, captures) : elle reçoit encore du trafic"
    if p["obsolete"]:
        return "périmée", "Mettre à jour ou fusionner"
    if 8 <= (pos or 99) <= 20 and imp >= 100:
        return "à pousser", "Quick win : title, sections manquantes, maillage"
    if mots < SEUILS["mince"] and imp > 0:
        return "mince", "Enrichir : elle est montrée mais n'a pas la matière"
    return "saine", "Garder"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", default="/tmp/audit-pages")
    ap.add_argument("--jours", type=int, default=180)
    a = ap.parse_args()
    os.makedirs(a.sortie, exist_ok=True)
    env = load_env()

    deb, fin = gsc.fenetre(a.jours)
    lignes = gsc.requete("https://decupler.com/", ["page"], deb, fin, 25000)
    perf = {urllib.parse.urlparse(r["keys"][0]).path.strip("/"): r for r in lignes}

    aujourdhui = datetime.date.today()
    res = []
    for x in contenus(env):
        brut = x["content"]["raw"]
        ed = (x.get("meta") or {}).get("_elementor_data") or ""
        source = brut if len(texte(brut)) > 200 or not ed or ed == "[]" else ed
        t = texte(source.replace("\\n", " ").replace("\\/", "/"))
        chemin = urllib.parse.urlparse(x["link"]).path.strip("/")
        g = perf.get(chemin, {})
        modif = datetime.date.fromisoformat(x["modified"][:10])
        p = {
            "type": x["_type"][:-1], "id": x["id"], "slug": x["slug"], "url": x["link"],
            "titre": html.unescape(x["title"]["raw"]),
            "impressions": g.get("impressions", 0), "clics": g.get("clicks", 0),
            "position": round(g["position"], 1) if g else None,
            "mots": len(t.split()), "modifie": x["modified"][:10], "age_jours": (aujourdhui - modif).days,
            "constructeur": "elementor" if ed and ed != "[]" else "contenu",
            "obsolete": sorted({lib for motif, lib in OBSOLETE if re.search(motif, t, re.I)}),
            "popup": "ai-content-gate" in (brut + ed),
        }
        p["verdict"], p["action"] = verdict(p)
        res.append(p)

    res.sort(key=lambda p: (["vide", "morte", "périmée", "mince", "à pousser", "saine"].index(p["verdict"]), -p["impressions"]))
    with open(os.path.join(a.sortie, "audit.json"), "w", encoding="utf-8") as f:
        json.dump({"periode": [deb, fin], "pages": res}, f, ensure_ascii=False, indent=1)

    compte = {}
    for p in res:
        compte[p["verdict"]] = compte.get(p["verdict"], 0) + 1
    md = [f"# Audit des pages — {aujourdhui.isoformat()}", "",
          f"Search Console du {deb} au {fin}. {len(res)} contenus publiés.", "",
          " · ".join(f"**{k}** : {v}" for k, v in compte.items()), ""]
    for v in ["vide", "morte", "périmée", "mince", "à pousser"]:
        lot = [p for p in res if p["verdict"] == v]
        if not lot:
            continue
        md += [f"## {v.capitalize()} ({len(lot)})", "", "| Page | Impr. | Clics | Pos. | Mots | Modifiée | Détail | Action |",
               "|---|---:|---:|---:|---:|---|---|---|"]
        for p in lot:
            md.append(f"| /{p['slug']}/ | {p['impressions']} | {p['clics']} | {p['position'] or '—'} | {p['mots']} | "
                      f"{p['modifie']} | {', '.join(p['obsolete']) or ''}{' · pop-up email' if p['popup'] else ''} | {p['action']} |")
        md.append("")
    with open(os.path.join(a.sortie, "audit.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print("\n".join(md[:6]))
    print(f"\n→ {a.sortie}/audit.md")


if __name__ == "__main__":
    main()
