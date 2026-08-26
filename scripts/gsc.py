#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Google Search Console en direct, sans intermediaire.

Lit GSC_CLIENT_ID, GSC_CLIENT_SECRET et GSC_REFRESH_TOKEN dans .env ou dans
l'environnement (secrets Claude Code). Voir scripts/gsc_auth.py pour les
obtenir. Aucune dependance : urllib suffit.

    python3 scripts/gsc.py sites
    python3 scripts/gsc.py perf --site https://decupler.com/ --jours 28
    python3 scripts/gsc.py perf --site https://decupler.com/ --par page --lignes 40
    python3 scripts/gsc.py perf --site https://decupler.com/ --par query --compare
    python3 scripts/gsc.py inspect --site https://decupler.com/ --url https://decupler.com/agent-vocal-ia/
"""
import os
import sys
import json
import time
import argparse
import datetime
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://www.googleapis.com/webmasters/v3"
INSPECT = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"


def env():
    cle = {}
    chemin = os.path.join(ROOT, ".env")
    if os.path.exists(chemin):
        for ligne in open(chemin, encoding="utf-8"):
            ligne = ligne.strip()
            if ligne and not ligne.startswith("#") and "=" in ligne:
                k, v = ligne.split("=", 1)
                cle[k.strip()] = v.strip()
    for k in ("GSC_CLIENT_ID", "GSC_CLIENT_SECRET", "GSC_REFRESH_TOKEN"):
        cle[k] = cle.get(k) or os.environ.get(k, "")
    manque = [k for k, v in cle.items() if not v and k.startswith("GSC_")]
    if manque:
        sys.exit(f"❌ Manque {', '.join(manque)}. Lance scripts/gsc_auth.py sur ta "
                 f"machine, puis mets les valeurs dans les secrets d'environnement.")
    return cle


_jeton = {"valeur": None, "expire": 0}


def jeton():
    """Un access token vit une heure ; on le remint quand il approche."""
    if _jeton["valeur"] and time.time() < _jeton["expire"] - 120:
        return _jeton["valeur"]
    c = env()
    data = urllib.parse.urlencode({
        "client_id": c["GSC_CLIENT_ID"], "client_secret": c["GSC_CLIENT_SECRET"],
        "refresh_token": c["GSC_REFRESH_TOKEN"], "grant_type": "refresh_token"}).encode()
    r = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
    with urllib.request.urlopen(r, timeout=60) as rep:
        d = json.load(rep)
    _jeton.update(valeur=d["access_token"], expire=time.time() + d.get("expires_in", 3600))
    return _jeton["valeur"]


def appel(url, corps=None):
    r = urllib.request.Request(
        url,
        data=json.dumps(corps).encode() if corps is not None else None,
        method="POST" if corps is not None else "GET",
        headers={"Authorization": "Bearer " + jeton(),
                 "Content-Type": "application/json"})
    for essai in range(5):
        try:
            with urllib.request.urlopen(r, timeout=120) as rep:
                return json.load(rep)
        except urllib.error.HTTPError as e:
            corps_err = e.read().decode("utf-8", "replace")
            # 429 et 5xx se retentent, le reste non : une erreur de requete
            # ne se repare pas en la rejouant.
            if e.code in (429, 500, 502, 503) and essai < 4:
                time.sleep(2 ** essai)
                continue
            sys.exit(f"❌ HTTP {e.code} : {corps_err[:400]}")
        except Exception as e:
            if essai == 4:
                sys.exit(f"❌ {e}")
            time.sleep(2 ** essai)


def fenetre(jours, decalage=0):
    """GSC accuse 2 a 3 jours de retard : on ne demande jamais hier."""
    fin = datetime.date.today() - datetime.timedelta(days=3 + decalage)
    return (fin - datetime.timedelta(days=jours - 1)).isoformat(), fin.isoformat()


def cmd_sites(a):
    d = appel(f"{API}/sites")
    lignes = [(s["siteUrl"], s.get("permissionLevel", "")) for s in d.get("siteEntry", [])]
    print(f"{len(lignes)} propriete(s) :\n")
    for u, p in sorted(lignes):
        print(f"  {u:<48} {p}")


def requete(site, dims, debut, fin, lignes, filtres=None):
    corps = {"startDate": debut, "endDate": fin, "dimensions": dims,
             "rowLimit": lignes, "dataState": "final"}
    if filtres:
        corps["dimensionFilterGroups"] = [{"filters": filtres}]
    d = appel(f"{API}/sites/{urllib.parse.quote(site, safe='')}/searchAnalytics/query", corps)
    return d.get("rows", [])


def cmd_perf(a):
    debut, fin = fenetre(a.jours)
    dims = [] if a.par == "total" else [a.par]
    lignes = requete(a.site, dims, debut, fin, a.lignes)
    if a.json:
        print(json.dumps({"debut": debut, "fin": fin, "rows": lignes}, ensure_ascii=False))
        return
    print(f"\n{a.site} · {debut} → {fin} ({a.jours} jours)")
    if a.compare:
        d2, f2 = fenetre(a.jours, a.jours)
        avant = {tuple(r.get("keys", [])): r for r in requete(a.site, dims, d2, f2, a.lignes)}
        print(f"comparé à {d2} → {f2}")
    else:
        avant = {}
    print()
    if not lignes:
        print("  aucune donnée sur la période")
        return
    if a.par == "total":
        r = lignes[0]
        print(f"  clics        {r['clicks']:>10,.0f}")
        print(f"  impressions  {r['impressions']:>10,.0f}")
        print(f"  CTR          {r['ctr']*100:>9.2f} %")
        print(f"  position     {r['position']:>10.1f}")
        if avant:
            b = list(avant.values())[0]
            print(f"\n  évolution    clics {r['clicks']-b['clicks']:+,.0f} · "
                  f"impressions {r['impressions']-b['impressions']:+,.0f} · "
                  f"position {b['position']-r['position']:+.1f}")
        return
    lg = max((len(r["keys"][0]) for r in lignes), default=10)
    lg = min(lg, 62)
    print(f"  {'':<{lg}} {'clics':>7} {'impr.':>9} {'CTR':>7} {'pos.':>6}"
          + ("  évol. clics" if avant else ""))
    for r in lignes:
        k = r["keys"][0]
        k = k[:lg - 1] + "…" if len(k) > lg else k
        ligne = (f"  {k:<{lg}} {r['clicks']:>7,.0f} {r['impressions']:>9,.0f} "
                 f"{r['ctr']*100:>6.1f}% {r['position']:>6.1f}")
        if avant:
            b = avant.get(tuple(r["keys"]))
            ligne += f"  {r['clicks']-b['clicks']:+8,.0f}" if b else "      nouveau"
        print(ligne)


def cmd_inspect(a):
    urls = a.url or [u.strip() for u in open(a.fichier, encoding="utf-8") if u.strip()]
    print(f"\n{len(urls)} URL à inspecter · quota 2 000/jour\n")
    compte = {}
    for u in urls:
        d = appel(INSPECT, {"inspectionUrl": u, "siteUrl": a.site, "languageCode": "fr"})
        r = d.get("inspectionResult", {}).get("indexStatusResult", {})
        verdict = r.get("verdict", "?")
        couv = r.get("coverageState", "")
        compte[couv or verdict] = compte.get(couv or verdict, 0) + 1
        marque = {"PASS": "✔", "NEUTRAL": "•", "FAIL": "✖"}.get(verdict, "?")
        court = u.replace("https://decupler.com", "")
        print(f"  {marque} {court:<48} {couv}")
        if r.get("lastCrawlTime"):
            print(f"      dernier passage : {r['lastCrawlTime'][:10]}"
                  f" · robots : {r.get('robotsTxtState','')}"
                  f" · canonique Google : {(r.get('googleCanonical') or '—').replace('https://decupler.com','')}")
    print("\n  Récapitulatif :")
    for k, v in sorted(compte.items(), key=lambda x: -x[1]):
        print(f"    {v:>3} · {k}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("sites", help="liste les proprietes accessibles")
    p.set_defaults(f=cmd_sites)

    p = sub.add_parser("perf", help="clics, impressions, CTR, position")
    p.add_argument("--site", required=True)
    p.add_argument("--jours", type=int, default=28)
    p.add_argument("--par", default="total",
                   choices=["total", "page", "query", "date", "country", "device"])
    p.add_argument("--lignes", type=int, default=25)
    p.add_argument("--compare", action="store_true", help="vs la periode precedente")
    p.add_argument("--json", action="store_true")
    p.set_defaults(f=cmd_perf)

    p = sub.add_parser("inspect", help="etat d'indexation (API URL Inspection)")
    p.add_argument("--site", required=True)
    p.add_argument("--url", nargs="*")
    p.add_argument("--fichier", help="un fichier avec une URL par ligne")
    p.set_defaults(f=cmd_inspect)

    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
