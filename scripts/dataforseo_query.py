#!/usr/bin/env python3
"""
dataforseo_query.py — Expansion de mots-clés + analyse SERP via l'API DataForSEO.

Brique 2 de la "machine à opportunités GEO". Lit les graines (seeds), interroge
DataForSEO Labs (Google) pour récupérer des idées de mots-clés avec volume,
difficulté (KD), CPC, concurrence et intention, puis (optionnel) analyse la SERP
pour détecter les signaux GEO purs (AI Overview, People Also Ask, featured snippet).

Sortie : un JSON normalisé prêt à être fusionné par score_opportunities.py.

Auth : variables d'environnement DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD (.env).
Aucune dépendance externe (urllib stdlib uniquement).

Exemples
--------
# Expansion de mots-clés à partir des graines GEO (marché FR)
python3 scripts/dataforseo_query.py keywords \
    --seeds content/opportunities/seeds-geo.txt \
    --out content/opportunities/.cache/dfs-keywords.json

# Analyse SERP (AI Overview / PAA) sur une liste de mots-clés
python3 scripts/dataforseo_query.py serp \
    --keywords-file content/opportunities/.cache/top-keywords.txt \
    --out content/opportunities/.cache/dfs-serp.json
"""
import argparse
import base64
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

API_BASE = "https://api.dataforseo.com"
ROOT = Path(__file__).resolve().parent.parent

# Marché FR par défaut (modifiable en CLI)
DEFAULT_LOCATION = "France"
DEFAULT_LANGUAGE = "French"


# --------------------------------------------------------------------------- #
# .env minimal loader (pas de dépendance python-dotenv)
# --------------------------------------------------------------------------- #
def load_env():
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        os.environ.setdefault(key, val)


def get_auth_header():
    login = os.environ.get("DATAFORSEO_LOGIN", "").strip()
    password = os.environ.get("DATAFORSEO_PASSWORD", "").strip()
    if not login or not password:
        sys.exit(
            "ERREUR : DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD absents du .env.\n"
            "Renseigne-les puis relance. (Compte : https://app.dataforseo.com)"
        )
    token = base64.b64encode(f"{login}:{password}".encode()).decode()
    return f"Basic {token}"


def post(endpoint, payload, retries=3):
    """POST JSON vers DataForSEO, avec retry simple."""
    url = f"{API_BASE}{endpoint}"
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": get_auth_header(),
        "Content-Type": "application/json",
    }
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=120) as resp:
                body = json.loads(resp.read().decode("utf-8"))
            if body.get("status_code") != 20000:
                raise RuntimeError(
                    f"DataForSEO status {body.get('status_code')}: "
                    f"{body.get('status_message')}"
                )
            return body
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "ignore")[:300]
            last_err = f"HTTP {e.code} {e.reason} — {detail}"
        except Exception as e:  # noqa: BLE001
            last_err = str(e)
        if attempt < retries:
            time.sleep(2 * attempt)
    sys.exit(f"ERREUR API DataForSEO ({endpoint}) après {retries} essais : {last_err}")


def read_seeds(path):
    seeds = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            seeds.append(line)
    return seeds


# --------------------------------------------------------------------------- #
# Mode "keywords" : expansion via DataForSEO Labs
# --------------------------------------------------------------------------- #
def normalize_kw_item(item, seed, source):
    info = item.get("keyword_info") or {}
    props = item.get("keyword_properties") or {}
    intent = (item.get("search_intent_info") or {}).get("main_intent")
    return {
        "keyword": item.get("keyword"),
        "search_volume": info.get("search_volume"),
        "cpc": info.get("cpc"),
        "competition": info.get("competition"),
        "competition_level": info.get("competition_level"),
        "keyword_difficulty": props.get("keyword_difficulty"),
        "search_intent": intent,
        "seed": seed,
        "source": source,
    }


def fetch_keyword_ideas(seeds, location, language, limit):
    """
    keyword_ideas : à partir d'un lot de graines, renvoie des idées proches
    avec volume/CPC/concurrence + KD + intention. On batch par paquets de 20
    graines (limite de l'endpoint sur le champ keywords).
    """
    results = []
    batch_size = 20
    for i in range(0, len(seeds), batch_size):
        chunk = seeds[i : i + batch_size]
        payload = [{
            "keywords": chunk,
            "location_name": location,
            "language_name": language,
            "include_serp_info": False,
            "include_clickstream_data": False,
            "limit": limit,
            "order_by": ["keyword_info.search_volume,desc"],
        }]
        body = post("/v3/dataforseo_labs/google/keyword_ideas/live", payload)
        for task in body.get("tasks", []):
            for res in task.get("result") or []:
                for item in res.get("items") or []:
                    results.append(normalize_kw_item(item, ",".join(chunk[:2]) + "…", "keyword_ideas"))
        print(f"  keyword_ideas: lot {i//batch_size+1} → {len(results)} mots-clés cumulés", file=sys.stderr)
    return results


def fetch_keyword_suggestions(seeds, location, language, limit_per_seed):
    """
    keyword_suggestions : longue traîne (le mot-clé graine est contenu dans
    chaque suggestion). Un appel par graine.
    """
    results = []
    for seed in seeds:
        payload = [{
            "keyword": seed,
            "location_name": location,
            "language_name": language,
            "include_serp_info": False,
            "limit": limit_per_seed,
            "order_by": ["keyword_info.search_volume,desc"],
        }]
        body = post("/v3/dataforseo_labs/google/keyword_suggestions/live", payload)
        for task in body.get("tasks", []):
            for res in task.get("result") or []:
                for item in res.get("items") or []:
                    results.append(normalize_kw_item(item, seed, "keyword_suggestions"))
    print(f"  keyword_suggestions: {len(results)} suggestions longue traîne", file=sys.stderr)
    return results


def dedupe_keywords(rows):
    best = {}
    for r in rows:
        kw = (r.get("keyword") or "").strip().lower()
        if not kw:
            continue
        # garde la ligne la plus informative (volume connu prioritaire)
        cur = best.get(kw)
        if cur is None:
            best[kw] = r
        else:
            if (r.get("search_volume") or 0) > (cur.get("search_volume") or 0):
                best[kw] = r
    return list(best.values())


def cmd_keywords(args):
    seeds = read_seeds(args.seeds)
    print(f"[keywords] {len(seeds)} graines · {args.location} / {args.language}", file=sys.stderr)
    rows = []
    rows += fetch_keyword_ideas(seeds, args.location, args.language, args.limit)
    if args.suggestions:
        rows += fetch_keyword_suggestions(seeds, args.location, args.language, args.limit_suggestions)
    rows = dedupe_keywords(rows)
    rows.sort(key=lambda r: (r.get("search_volume") or 0), reverse=True)
    out = {
        "meta": {
            "location": args.location,
            "language": args.language,
            "seeds_count": len(seeds),
            "keywords_count": len(rows),
        },
        "keywords": rows,
    }
    write_json(args.out, out)
    print(f"[keywords] {len(rows)} mots-clés uniques → {args.out}", file=sys.stderr)


# --------------------------------------------------------------------------- #
# Mode "serp" : détection des signaux GEO (AI Overview / PAA / snippet)
# --------------------------------------------------------------------------- #
GEO_SERP_ITEMS = {
    "ai_overview",
    "people_also_ask",
    "featured_snippet",
    "knowledge_graph",
    "answer_box",
    "discussions_and_forums",
}


def cmd_overview(args):
    """
    keyword_overview : volume + difficulté (KD) + intention pour une liste de
    mots-clés, en un seul appel (jusqu'à 700). Sert à enrichir des pages/sujets
    déjà identifiés (audit de l'existant), pas à découvrir.
    """
    keywords = read_seeds(args.keywords_file)
    print(f"[overview] {len(keywords)} mots-clés · {args.location}", file=sys.stderr)
    out = {}
    batch = 700
    for i in range(0, len(keywords), batch):
        chunk = keywords[i : i + batch]
        payload = [{
            "keywords": chunk,
            "location_name": args.location,
            "language_name": args.language,
        }]
        body = post("/v3/dataforseo_labs/google/keyword_overview/live", payload)
        for task in body.get("tasks", []):
            for res in task.get("result") or []:
                for item in res.get("items") or []:
                    kw = (item.get("keyword") or "").lower().strip()
                    info = item.get("keyword_info") or {}
                    props = item.get("keyword_properties") or {}
                    intent = (item.get("search_intent_info") or {}).get("main_intent")
                    out[kw] = {
                        "search_volume": info.get("search_volume"),
                        "cpc": info.get("cpc"),
                        "competition": info.get("competition"),
                        "keyword_difficulty": props.get("keyword_difficulty"),
                        "search_intent": intent,
                    }
    write_json(args.out, {"overview": out})
    print(f"[overview] {len(out)} mots-clés enrichis → {args.out}", file=sys.stderr)


def cmd_serp(args):
    keywords = read_seeds(args.keywords_file)
    if args.max:
        keywords = keywords[: args.max]
    print(f"[serp] {len(keywords)} mots-clés analysés · {args.location}", file=sys.stderr)
    rows = []
    for kw in keywords:
        payload = [{
            "keyword": kw,
            "location_name": args.location,
            "language_name": args.language,
            "depth": 20,
        }]
        body = post("/v3/serp/google/organic/live/advanced", payload)
        present = set()
        top_domains = []
        for task in body.get("tasks", []):
            for res in task.get("result") or []:
                for item in res.get("items") or []:
                    t = item.get("type")
                    if t in GEO_SERP_ITEMS:
                        present.add(t)
                    if t == "organic" and len(top_domains) < 5:
                        top_domains.append(item.get("domain"))
        rows.append({
            "keyword": kw,
            "ai_overview": "ai_overview" in present,
            "people_also_ask": "people_also_ask" in present,
            "featured_snippet": "featured_snippet" in present,
            "serp_features": sorted(present),
            "top_domains": top_domains,
        })
        print(f"  {kw}: {sorted(present) or 'aucun signal GEO'}", file=sys.stderr)
    write_json(args.out, {"serp": rows})
    print(f"[serp] {len(rows)} analyses → {args.out}", file=sys.stderr)


# --------------------------------------------------------------------------- #
def write_json(path, obj):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def build_parser():
    p = argparse.ArgumentParser(description="DataForSEO — expansion mots-clés & SERP")
    sub = p.add_subparsers(dest="cmd", required=True)

    pk = sub.add_parser("keywords", help="Expansion de mots-clés depuis des graines")
    pk.add_argument("--seeds", required=True, help="Fichier de graines (une par ligne)")
    pk.add_argument("--out", required=True, help="Fichier JSON de sortie")
    pk.add_argument("--location", default=DEFAULT_LOCATION)
    pk.add_argument("--language", default=DEFAULT_LANGUAGE)
    pk.add_argument("--limit", type=int, default=200, help="Max d'idées par lot de graines")
    pk.add_argument("--suggestions", action="store_true", help="Ajouter la longue traîne (1 appel/graine)")
    pk.add_argument("--limit-suggestions", type=int, default=100)
    pk.set_defaults(func=cmd_keywords)

    po = sub.add_parser("overview", help="Volume + KD + intention pour une liste de mots-clés (audit)")
    po.add_argument("--keywords-file", required=True, help="Fichier de mots-clés (un par ligne)")
    po.add_argument("--out", required=True, help="Fichier JSON de sortie")
    po.add_argument("--location", default=DEFAULT_LOCATION)
    po.add_argument("--language", default=DEFAULT_LANGUAGE)
    po.set_defaults(func=cmd_overview)

    ps = sub.add_parser("serp", help="Analyse SERP : détecte AI Overview / PAA / snippet")
    ps.add_argument("--keywords-file", required=True, help="Fichier de mots-clés (un par ligne)")
    ps.add_argument("--out", required=True, help="Fichier JSON de sortie")
    ps.add_argument("--location", default=DEFAULT_LOCATION)
    ps.add_argument("--language", default=DEFAULT_LANGUAGE)
    ps.add_argument("--max", type=int, default=30, help="Limite de mots-clés analysés (coût API)")
    ps.set_defaults(func=cmd_serp)
    return p


def main():
    load_env()
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
