#!/usr/bin/env python3
"""
score_opportunities.py — Moteur de scoring & clustering des opportunités GEO.

Brique 4 (cœur) de la "machine à opportunités GEO". Fusionne :
  - les mots-clés DataForSEO (volume, KD, CPC, intention)        [obligatoire]
  - les données Google Search Console normalisées (striking dist.) [optionnel]
  - l'analyse SERP (AI Overview / PAA)                            [optionnel]
  - l'inventaire interne (pages/articles déjà publiés)           [optionnel]

Puis calcule un score d'opportunité composite, détecte les quick wins
(striking distance), regroupe les mots-clés en clusters thématiques
(1 cluster = 1 article potentiel), repère les sujets déjà couverts et propose
le maillage interne. Sortie : un rapport Markdown + un CSV priorisés.

Exemple
-------
python3 scripts/score_opportunities.py \
    --keywords content/opportunities/.cache/dfs-keywords.json \
    --gsc content/opportunities/.cache/gsc.json \
    --serp content/opportunities/.cache/dfs-serp.json \
    --inventory content/cleaned/inventory.md \
    --out-md content/opportunities/2026-06-16-geo.md \
    --out-csv content/opportunities/2026-06-16-geo.csv
"""
import argparse
import csv
import json
import math
import re
from pathlib import Path

# --------------------------------------------------------------------------- #
# Lexique GEO : pondère la pertinence "Generative Engine Optimization"
# --------------------------------------------------------------------------- #
# STRONG : termes sans ambiguïté → suffisent à eux seuls.
GEO_STRONG = [
    "generative engine", "moteur génératif", "moteur generatif",
    "ai overview", "ai overviews", " sge ", "search generative",
    "answer engine", " aeo ", "moteur de réponse", "moteur de reponse",
    "moteur de recherche ia", "moteurs de recherche ia", "recherche générative",
    "recherche generative", "référencement ia", "referencement ia",
    "seo ia", "ia seo", "geo seo", "seo geo", "visibilité ia", "visibilite ia",
    "réponses ia", "reponses ia", "seo chatgpt", "chatgpt seo",
    "seo perplexity", "seo claude", "claude seo", "seo gemini",
    "cité par chatgpt", "cite par chatgpt", "cité par les ia", "cite par les ia",
    "agence geo", "consultant geo", "audit geo", "formation geo",
    "stratégie geo", "strategie geo", "accompagnement geo", "optimisation geo",
    "dataforseo", "llms.txt", "llm seo", "seo llm", "aio", "agence aio",
    "skill claude", "claude skill", "claude code seo", "search everywhere",
]
# WEAK : marques / sigles ambigus → ne comptent qu'avec un mot de contexte SEO.
# Chaque entrée = UN concept (matché en frontière de mot pour éviter les doublons
# du type " ia"/"ia " et les faux positifs à l'intérieur d'un mot).
GEO_WEAK = [
    "geo", "ia", "chatgpt", "perplexity", "gemini", "claude", "copilot",
    "mistral", "llm", "sge", "aeo", "intelligence artificielle",
]
# CONTEXT : signale qu'on parle bien de SEO/référencement/visibilité.
GEO_CONTEXT = [
    "seo", "référencement", "referencement", "agence", "audit", "consultant",
    "visibilité", "visibilite", "ranking", "rank", "optimis", "citation",
    "cité", "cite", "moteur", "stratégie", "strategie", "formation", "skill",
    "mcp", "dataforseo", "serp", "trafic", "organique", "content gap",
]
# NEGATIVE : faux positifs fréquents (géographie, jeux, spam du hack…).
GEO_NEGATIVE = [
    "histoire", "page de garde", "mahjong", "slot", "casino", "solitaire",
    "sudoku", "poker", "terpercaya", "indonesia", "togel", "recette",
    "anniversaire", "traduction", "traducteur", "météo", "meteo", "carte",
    "géographie", "geographie", "coordonnées", "coordonnees", "localisation gps",
]

# Stopwords FR/EN minimaux pour le clustering
STOPWORDS = {
    "le", "la", "les", "un", "une", "des", "de", "du", "d", "l", "a", "à",
    "et", "ou", "en", "sur", "pour", "par", "avec", "sans", "dans", "au", "aux",
    "ce", "ces", "se", "sa", "son", "ses", "que", "qui", "quoi", "comment",
    "the", "a", "an", "of", "for", "to", "in", "on", "and", "or", "is",
    "est", "sont", "être", "etre", "plus", "votre", "vos", "mon", "ma",
}

INTENT_WEIGHT = {
    "informational": 1.0,   # idéal pour le blog GEO
    "commercial": 0.9,      # comparatifs, "meilleur X"
    "transactional": 0.6,   # plutôt pour pages service
    "navigational": 0.3,    # marque/produit existant
    None: 0.7,
}


def tokens(text):
    words = re.findall(r"[a-zA-Zàâäéèêëïîôöùûüç0-9]+", (text or "").lower())
    return [w for w in words if w not in STOPWORDS and len(w) > 2]


def geo_relevance(keyword):
    """
    0..1 : pertinence GEO.
      - termes STRONG → pertinence élevée (suffisent seuls)
      - termes WEAK (marques/sigles ambigus) → ne comptent qu'avec un mot de
        CONTEXTE SEO, ou si ≥2 indices faibles se cumulent
      - un terme NEGATIVE sans STRONG → écarté (géographie, jeux, spam du hack)
    """
    k = f" {(keyword or '').lower()} "
    strong = sum(1 for t in GEO_STRONG if t in k)
    if strong:
        return min(1.0, 0.7 + 0.1 * strong)

    if any(n in k for n in GEO_NEGATIVE):
        return 0.0

    # frontière de mot : "copilot" matche "copilote", mais "ia" ne matche pas
    # "francaise"/"indonesia" et n'est pas compté deux fois.
    weak = sum(1 for t in GEO_WEAK if re.search(r"\b" + re.escape(t), k))
    has_context = any(c in k for c in GEO_CONTEXT)
    if weak and has_context:
        return 0.65
    if weak >= 2:
        return 0.55
    return 0.0


# --------------------------------------------------------------------------- #
# Sous-scores (chacun 0..1)
# --------------------------------------------------------------------------- #
def volume_score(v):
    v = v or 0
    if v <= 0:
        return 0.0
    return min(1.0, math.log10(v + 1) / 4.0)  # 10k recherches ≈ 1.0


def difficulty_score(kd):
    if kd is None:
        return 0.6  # neutre si inconnu
    return max(0.0, 1.0 - (kd / 100.0))  # KD 0 → 1.0, KD 100 → 0.0


def intent_score(intent):
    return INTENT_WEIGHT.get(intent, 0.7)


# --------------------------------------------------------------------------- #
# Chargement des données
# --------------------------------------------------------------------------- #
def load_json(path):
    if not path:
        return None
    p = Path(path)
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def parse_inventory(path):
    """Parse inventory.md (table markdown) → liste {type,title,slug,tokens}."""
    if not path or not Path(path).exists():
        return []
    pages = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0].lower() in ("type", "----", ":---"):
            continue
        if set(cells[0]) <= set("-: "):
            continue
        typ, title, slug = cells[0], cells[1], cells[2]
        if typ.lower() not in ("page", "post"):
            continue
        pages.append({
            "type": typ, "title": title, "slug": slug,
            "tokens": set(tokens(title)) | set(tokens(slug.replace("-", " "))),
        })
    return pages


def build_gsc_index(gsc):
    """map: requête normalisée → ligne GSC ; + set striking distance."""
    idx = {}
    striking = set()
    if not gsc:
        return idx, striking
    for r in gsc.get("queries", []):
        idx[r["query"].lower().strip()] = r
    for r in gsc.get("striking_distance", []):
        striking.add(r["query"].lower().strip())
    return idx, striking


def build_serp_index(serp):
    idx = {}
    if not serp:
        return idx
    for r in serp.get("serp", []):
        idx[(r.get("keyword") or "").lower().strip()] = r
    return idx


# --------------------------------------------------------------------------- #
# Coverage interne + maillage
# --------------------------------------------------------------------------- #
def coverage(keyword, pages):
    """Retourne (déjà_couvert: bool, liens_internes: [titles])."""
    kt = set(tokens(keyword))
    if not kt:
        return False, []
    scored = []
    for pg in pages:
        if not pg["tokens"]:
            continue
        overlap = len(kt & pg["tokens"])
        if overlap == 0:
            continue
        ratio = overlap / len(kt)
        scored.append((ratio, overlap, pg))
    scored.sort(reverse=True, key=lambda x: (x[0], x[1]))
    covered = bool(scored and scored[0][0] >= 0.8)
    links = [f"{pg['title']} (/{pg['slug']})" for _, _, pg in scored[:3]]
    return covered, links


# --------------------------------------------------------------------------- #
# Scoring principal
# --------------------------------------------------------------------------- #
def score_row(kw, gsc_idx, striking, serp_idx, pages, min_geo):
    keyword = kw.get("keyword") or ""
    rel = geo_relevance(keyword)
    if rel < min_geo:
        return None  # hors périmètre GEO

    key = keyword.lower().strip()
    gsc_row = gsc_idx.get(key)
    in_striking = key in striking

    # Volume : DataForSEO si dispo, sinon proxy via les impressions GSC (90j).
    sv = kw.get("search_volume")
    volume_estimated = False
    if sv is None and gsc_row:
        sv = gsc_row.get("impressions")  # borne basse de la demande réelle
        volume_estimated = True
    vs = volume_score(sv)
    ds = difficulty_score(kw.get("keyword_difficulty"))
    is_ = intent_score(kw.get("search_intent"))
    serp_row = serp_idx.get(key, {})
    has_aio = bool(serp_row.get("ai_overview"))
    has_paa = bool(serp_row.get("people_also_ask"))

    # Score composite 0..100
    base = (
        0.30 * vs +
        0.22 * ds +
        0.18 * rel +
        0.15 * is_ +
        0.15 * (1.0 if (has_aio or has_paa) else 0.0)
    )
    score = base * 100

    # Bonus quick win GSC (le site a déjà des impressions en position 5-20)
    if in_striking:
        score += 18
    elif gsc_row:
        score += 6

    covered, links = coverage(keyword, pages)
    if covered:
        score -= 12  # déjà traité → priorité moindre pour un NOUVEL article

    score = round(max(0.0, min(100.0, score)), 1)

    # Type de contenu suggéré
    kl = keyword.lower()
    if any(w in kl for w in ("comment", "pourquoi", "qu'est", "guide", "tuto")):
        ctype = "Guide / How-to"
    elif any(w in kl for w in ("meilleur", "comparatif", "vs", "alternative", "prix", "tarif")):
        ctype = "Comparatif / Commercial"
    elif any(w in kl for w in ("agence", "consultant", "service", "audit")):
        ctype = "Page service / Landing"
    else:
        ctype = "Définition / Pilier"

    return {
        "keyword": keyword,
        "score": score,
        "search_volume": sv,
        "volume_estimated": volume_estimated,
        "keyword_difficulty": kw.get("keyword_difficulty"),
        "cpc": kw.get("cpc"),
        "search_intent": kw.get("search_intent"),
        "geo_relevance": round(rel, 2),
        "origin": kw.get("source", "dataforseo"),
        "quick_win": in_striking,
        "gsc_position": gsc_row.get("position") if gsc_row else None,
        "gsc_impressions": gsc_row.get("impressions") if gsc_row else None,
        "gsc_clicks": gsc_row.get("clicks") if gsc_row else None,
        "ai_overview": has_aio,
        "people_also_ask": has_paa,
        "already_covered": covered,
        "content_type": ctype,
        "internal_links": links,
    }


# --------------------------------------------------------------------------- #
# Clustering greedy par token-tête
# --------------------------------------------------------------------------- #
# Préfixes de requêtes conversationnelles / IA à éviter comme nom de pilier.
NOISE_PREFIXES = (
    "is it", "evaluate", "i want", "i need", "je veux", "je cherche",
    "je souhaite", "j'aimerais", "peux-tu", "peux tu", "comment puis",
    "what is", "how to", "can you", "please",
)


def clean_pillar(members):
    """Choisit un nom de pilier propre : le membre le mieux scoré qui ne soit
    ni trop long ni préfixé par une formulation conversationnelle."""
    best = sorted(members, key=lambda m: m["score"], reverse=True)
    for m in best:
        kw = m["keyword"].strip()
        kl = kw.lower()
        if len(kw) <= 55 and not any(kl.startswith(p) for p in NOISE_PREFIXES):
            return m
    return best[0]  # fallback : le mieux scoré


def cluster(rows):
    rows_sorted = sorted(rows, key=lambda r: r["score"], reverse=True)
    clusters = []
    used = set()
    for r in rows_sorted:
        kid = r["keyword"].lower()
        if kid in used:
            continue
        head_tokens = set(tokens(r["keyword"]))
        members = [r]
        used.add(kid)
        for o in rows_sorted:
            oid = o["keyword"].lower()
            if oid in used:
                continue
            ot = set(tokens(o["keyword"]))
            shared = head_tokens & ot
            if len(shared) >= 2 or (head_tokens and head_tokens <= ot):
                members.append(o)
                used.add(oid)
        total_vol = sum((m["search_volume"] or 0) for m in members)
        head = clean_pillar(members)  # nom de pilier propre
        clusters.append({
            "pillar": head["keyword"],
            "score": r["score"],
            "keywords_count": len(members),
            "total_volume": total_vol,
            "content_type": head["content_type"],
            "quick_win": any(m["quick_win"] for m in members),
            "ai_overview": any(m["ai_overview"] for m in members),
            "already_covered": head["already_covered"],
            "internal_links": head["internal_links"],
            "members": members,
        })
    clusters.sort(key=lambda c: (c["score"], c["total_volume"]), reverse=True)
    return clusters


# --------------------------------------------------------------------------- #
# Rendu
# --------------------------------------------------------------------------- #
def fmt(v, suffix=""):
    return f"{v}{suffix}" if v not in (None, "") else "—"


def render_markdown(clusters, rows, meta):
    n_qw = sum(1 for r in rows if r["quick_win"])
    n_aio = sum(1 for r in rows if r["ai_overview"])
    n_cov = sum(1 for r in rows if r["already_covered"])
    lines = []
    lines.append(f"# Opportunités de contenu GEO — {meta['date']}")
    lines.append("")
    lines.append(f"> Marché : **{meta['location']} / {meta['language']}** · "
                 f"{len(rows)} mots-clés GEO retenus · {len(clusters)} clusters "
                 f"(= articles potentiels)")
    lines.append("")
    lines.append("## Synthèse")
    lines.append("")
    lines.append(f"- **{len(clusters)} clusters thématiques** (1 cluster ≈ 1 article pilier)")
    lines.append(f"- **{n_qw} quick wins** (déjà en striking distance GSC, position 5–20)")
    lines.append(f"- **{n_aio} mots-clés avec AI Overview** (GEO pur — opportunité de citation IA)")
    lines.append(f"- **{n_cov} déjà couverts** par une page/article existant (→ maillage / mise à jour)")
    lines.append("")

    # Quick wins en avant
    qw = [r for r in rows if r["quick_win"]]
    qw.sort(key=lambda r: r["score"], reverse=True)
    if qw:
        lines.append("## ⚡ Quick wins (priorité immédiate — déjà des impressions GSC)")
        lines.append("")
        lines.append("| Mot-clé | Score | Pos. GSC | Impressions | Volume | KD | Type |")
        lines.append("|---|--:|--:|--:|--:|--:|---|")
        for r in qw[:20]:
            lines.append(
                f"| {r['keyword']} | {r['score']} | {fmt(r['gsc_position'])} | "
                f"{fmt(r['gsc_impressions'])} | {fmt(r['search_volume'])} | "
                f"{fmt(r['keyword_difficulty'])} | {r['content_type']} |"
            )
        lines.append("")

    # Clusters
    lines.append("## 🗂️ Clusters prioritaires (= plan éditorial)")
    lines.append("")
    lines.append("| # | Pilier (article) | Score | Mots-clés | Volume total | Type | AIO | Couvert | Maillage interne |")
    lines.append("|--:|---|--:|--:|--:|---|:--:|:--:|---|")
    for i, c in enumerate(clusters[:40], 1):
        aio = "✅" if c["ai_overview"] else ""
        cov = "⚠️" if c["already_covered"] else ""
        links = "<br>".join(c["internal_links"][:2]) if c["internal_links"] else "—"
        lines.append(
            f"| {i} | **{c['pillar']}** | {c['score']} | {c['keywords_count']} | "
            f"{fmt(c['total_volume'])} | {c['content_type']} | {aio} | {cov} | {links} |"
        )
    lines.append("")

    # Détail des 10 premiers clusters
    lines.append("## 🔎 Détail des 10 premiers clusters")
    lines.append("")
    for i, c in enumerate(clusters[:10], 1):
        lines.append(f"### {i}. {c['pillar']}  ·  score {c['score']}")
        lines.append("")
        lines.append(f"- Type : {c['content_type']} · Volume cumulé : {fmt(c['total_volume'])}"
                     + (" · ⚡ quick win" if c["quick_win"] else "")
                     + (" · 🤖 AI Overview présent" if c["ai_overview"] else ""))
        if c["internal_links"]:
            lines.append(f"- Maillage interne suggéré : {', '.join(c['internal_links'])}")
        lines.append("- Mots-clés du cluster :")
        for m in sorted(c["members"], key=lambda x: (x["search_volume"] or 0), reverse=True)[:12]:
            tag = " ⚡" if m["quick_win"] else ""
            lines.append(f"  - {m['keyword']} — vol {fmt(m['search_volume'])}, "
                         f"KD {fmt(m['keyword_difficulty'])}, {m['search_intent'] or 'intention ?'}{tag}")
        lines.append("")
    return "\n".join(lines)


def write_csv(path, rows):
    cols = ["keyword", "score", "origin", "search_volume", "volume_estimated",
            "keyword_difficulty", "cpc", "search_intent", "geo_relevance",
            "quick_win", "gsc_position", "gsc_impressions", "gsc_clicks",
            "ai_overview", "people_also_ask", "already_covered", "content_type"]
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda x: x["score"], reverse=True):
            w.writerow(r)


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="Scoring & clustering des opportunités GEO")
    ap.add_argument("--keywords", required=True, help="JSON DataForSEO (mode keywords)")
    ap.add_argument("--gsc", help="JSON GSC normalisé (gsc_normalize.py)")
    ap.add_argument("--serp", help="JSON SERP (dataforseo_query serp)")
    ap.add_argument("--inventory", default="content/cleaned/inventory.md")
    ap.add_argument("--out-md", required=True)
    ap.add_argument("--out-csv", required=True)
    ap.add_argument("--date", default="", help="Date du rapport (AAAA-MM-JJ)")
    ap.add_argument("--min-geo", type=float, default=0.5,
                    help="Pertinence GEO minimale pour retenir un mot-clé (0..1)")
    args = ap.parse_args()

    kw_data = load_json(args.keywords)
    if not kw_data:
        raise SystemExit(f"ERREUR : fichier mots-clés introuvable : {args.keywords}")
    gsc = load_json(args.gsc)
    serp = load_json(args.serp)
    pages = parse_inventory(args.inventory)

    gsc_idx, striking = build_gsc_index(gsc)
    serp_idx = build_serp_index(serp)

    # Liste unifiée de candidats : mots-clés DataForSEO + requêtes GSC réelles.
    # Les requêtes GSC où le site a déjà des impressions sont des opportunités
    # à part entière (quick wins), pas seulement un bonus sur DataForSEO.
    candidates = {}
    for kw in kw_data.get("keywords", []):
        k = (kw.get("keyword") or "").lower().strip()
        if k:
            candidates[k] = dict(kw, source="dataforseo")
    n_dfs = len(candidates)
    if gsc:
        for q in gsc.get("queries", []):
            k = q["query"].lower().strip()
            if k in candidates:
                continue  # données DataForSEO plus riches → on garde
            candidates[k] = {
                "keyword": q["query"],
                "search_volume": None,
                "keyword_difficulty": None,
                "cpc": None,
                "competition": None,
                "search_intent": None,
                "seed": "gsc",
                "source": "gsc",
            }
    n_gsc_only = len(candidates) - n_dfs

    rows = []
    for kw in candidates.values():
        r = score_row(kw, gsc_idx, striking, serp_idx, pages, args.min_geo)
        if r:
            rows.append(r)
    rows.sort(key=lambda r: r["score"], reverse=True)

    clusters = cluster(rows)

    meta = {
        "date": args.date or "rapport",
        "location": (kw_data.get("meta") or {}).get("location", "France"),
        "language": (kw_data.get("meta") or {}).get("language", "French"),
    }
    md = render_markdown(clusters, rows, meta)
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(md, encoding="utf-8")
    write_csv(args.out_csv, rows)

    n_qw = sum(1 for r in rows if r["quick_win"])
    print(f"[score] {len(rows)} candidats GEO retenus "
          f"({n_dfs} DataForSEO + {n_gsc_only} requêtes GSC) · "
          f"{n_qw} quick wins · {len(clusters)} clusters")
    print(f"        Markdown → {args.out_md}")
    print(f"        CSV      → {args.out_csv}")


if __name__ == "__main__":
    main()
