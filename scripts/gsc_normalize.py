#!/usr/bin/env python3
"""
gsc_normalize.py — Normalise les données Google Search Console.

Brique 3 de la "machine à opportunités GEO". Les données GSC sont récupérées au
runtime par Claude via le MCP Windsor.ai (connecteur `searchconsole`, champs :
query, clicks, impressions, ctr, position, page). Claude écrit le résultat brut
dans un fichier ; ce script le normalise au format attendu par
score_opportunities.py et calcule les opportunités "striking distance".

Le parseur est tolérant : il accepte une liste de lignes, ou un objet {data:[...]}
ou {result:[...]}, et reconnaît les variantes de noms de champs.

Exemple
-------
# 1) Claude appelle Windsor get_data(searchconsole) et écrit la réponse brute :
#    content/opportunities/.cache/gsc-raw.json
# 2) Normalisation :
python3 scripts/gsc_normalize.py \
    --in content/opportunities/.cache/gsc-raw.json \
    --out content/opportunities/.cache/gsc.json
"""
import argparse
import json
import sys
from pathlib import Path


def to_float(v, default=0.0):
    try:
        if isinstance(v, str):
            v = v.replace("%", "").replace(",", ".").strip()
        return float(v)
    except (TypeError, ValueError):
        return default


def to_int(v, default=0):
    return int(round(to_float(v, default)))


def extract_rows(raw):
    """Trouve la liste de lignes quel que soit l'emballage Windsor."""
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        for key in ("data", "result", "rows", "results"):
            if isinstance(raw.get(key), list):
                return raw[key]
        # parfois {result:{data:[...]}}
        for key in ("result", "data"):
            inner = raw.get(key)
            if isinstance(inner, dict):
                got = extract_rows(inner)
                if got:
                    return got
    return []


def pick(row, *names):
    for n in names:
        if n in row and row[n] not in (None, ""):
            return row[n]
    return None


def normalize(rows):
    out = []
    for r in rows:
        if not isinstance(r, dict):
            continue
        query = pick(r, "query", "Search Query", "search_query")
        if not query:
            continue
        ctr = to_float(pick(r, "ctr", "CTR"))
        # CTR peut arriver en 0-1 ou 0-100 → on normalise en 0-1
        if ctr > 1.5:
            ctr = ctr / 100.0
        out.append({
            "query": str(query).strip(),
            "clicks": to_int(pick(r, "clicks", "Clicks")),
            "impressions": to_int(pick(r, "impressions", "Impressions")),
            "ctr": round(ctr, 4),
            "position": round(to_float(pick(r, "position", "Position")), 2),
            "page": pick(r, "page", "Page", "pagepath", "Page Path") or "",
        })
    return out


def main():
    ap = argparse.ArgumentParser(description="Normalise les données GSC (Windsor) ")
    ap.add_argument("--in", dest="inp", required=True, help="JSON brut Windsor")
    ap.add_argument("--out", required=True, help="JSON normalisé")
    ap.add_argument("--striking-min", type=float, default=5.0,
                    help="Position min de la zone striking distance (défaut 5)")
    ap.add_argument("--striking-max", type=float, default=20.0,
                    help="Position max de la zone striking distance (défaut 20)")
    args = ap.parse_args()

    raw = json.loads(Path(args.inp).read_text(encoding="utf-8"))
    rows = normalize(extract_rows(raw))
    if not rows:
        sys.exit("ERREUR : aucune ligne GSC exploitable. Vérifie le dump Windsor "
                 "(champs attendus : query, clicks, impressions, ctr, position, page).")

    striking = [
        r for r in rows
        if args.striking_min <= r["position"] <= args.striking_max
        and r["impressions"] > 0
    ]
    striking.sort(key=lambda r: r["impressions"], reverse=True)

    out = {
        "meta": {
            "rows": len(rows),
            "striking_distance_count": len(striking),
            "striking_range": [args.striking_min, args.striking_max],
        },
        "queries": rows,
        "striking_distance": striking,
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[gsc] {len(rows)} requêtes · {len(striking)} en striking distance "
          f"({args.striking_min}-{args.striking_max}) → {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
