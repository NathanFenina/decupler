#!/usr/bin/env python3
"""
build_content_map.py — Cartographie de l'existant (topical map) Décupler.

Construit la carte du contenu actuel = UNION de l'inventaire (content/cleaned/
inventory.md) et des URLs réelles de Google Search Console (qui font foi).
Pour chaque page : silo, type (pilier/cluster/offre/lead magnet/système/hack),
perfs GSC (impressions, clics, position, CTR), score d'opportunité, et action
recommandée. Volume / difficulté DataForSEO = laissés vides (2ᵉ passe ciblée).

Sorties : content/opportunities/content-map.csv, content-map.md, content-map.json
(le .json sert à alimenter la base Notion).

La classification se fait par règles (regex sur slug/titre) + un dict d'overrides
pour les piliers et cas particuliers (voir OVERRIDES).
"""
import csv
import json
import math
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GSC = ROOT / "content/opportunities/.cache/gsc.json"
INVENTORY = ROOT / "content/cleaned/inventory.md"
OUT_DIR = ROOT / "content/opportunities"

# Seuil d'impressions pour intégrer une page GSC absente de l'inventaire.
GSC_MIN_IMPR = 25

# --------------------------------------------------------------------------- #
# Silos (ordre = priorité d'affichage)
# --------------------------------------------------------------------------- #
SILOS = [
    "GEO / Référencement IA",
    "Claude Code & Skills SEO",
    "Fondamentaux SEO",
    "Outils & Data SEO",
    "SEO Local & GMB",
    "SEO Vertical",
    "Offre / Conversion",
    "Système / Légal",
    "Hack — à supprimer",
    "À classer",
]

# Règles de silo : (regex sur slug+titre) -> silo. Premier match gagne.
SILO_RULES = [
    (r"forex|casino|mahjong|peppermill|obzor|slot|togel|brokera|judi|gacor|roulette|jouer-roulette|poker|betting|bet365|kasino", "Hack — à supprimer"),
    (r"panier|commander|mon-compte|confirmation|politique|boutique|checkout|\?p=|/tag/|/category/|/page/|mentions-legales|cgv", "Système / Légal"),
    (r"claude|skill|mcp|dataforseo|openclaw|seo-os|seo-ai-systems|repo-github|model-context", "Claude Code & Skills SEO"),
    (r"local|gmb|citations|fiche|google-my-business|google-business", "SEO Local & GMB"),
    (r"ecommerce|e-commerce|saas|international|video-en-texte|transcri", "SEO Vertical"),
    (r"\bgeo\b|moteurs?-ia|moteur-ia|chatgpt|perplexity|gemini|llm|reddit-pour-les-llms|gap-geo|generative|aio|moteurs-de-recherche-ia|referencement-ia|referencement-sur-les-moteurs|dominer-les-moteurs|agent-ia-seo|prompt-geo|bootcamp-geo", "GEO / Référencement IA"),
    (r"volume-de-recherche|balise|meta-title|ahrefs|semrush|outil|nombre-de-recherche|crawler|crawl-seo", "Outils & Data SEO"),
    (r"agence|accompagnement|seo-geo-team|application-decupler|\bapp\b|bootcamp|webinaire|decupler-2|home|prix|tarif|cas-client|etude-de-cas|a-propos|newsletter|search-everywhere", "Offre / Conversion"),
    (r"audit-seo|faire-un-audit|backlink|migration|architecture|structure|ux-et-seo|redaction|analyse-des-logs|maillage|sea-vs-seo|visibilite|augmenter-visibilite", "Fondamentaux SEO"),
]

# Lead magnets (type), indépendamment du silo.
LEADMAGNET = r"webinaire|bootcamp|newsletter|matrice-gap|guide-site-ia|guide-complet|guide-pratique|checklist|template|repo-github"

# Piliers explicites (sinon = cluster). Ces pages sont les têtes de silo.
PILIERS = {
    "agence-geo", "claude-skills-seo", "seo-ai-systems", "seo-local",
    "accompagnement-seo", "agence-seo", "dominer-les-moteurs-de-recherche-ia",
    "guide-complet-connaitre-le-volume-de-recherche-dun-mot-cle",
    "referencement-ia-comment-lintelligence-artificielle-revolutionne-le-seo",
    "seo-geo-team", "decupler-2",
}

# Overrides ponctuels {slug: {silo?, type?, action?, parent?}}
OVERRIDES = {
    "audit-geo": {"type": "cluster", "silo": "GEO / Référencement IA"},
    "audit-geo-claude-code": {"silo": "Claude Code & Skills SEO"},
    "seo-chatgpt": {"silo": "GEO / Référencement IA"},
    "reddit-pour-les-llms": {"silo": "GEO / Référencement IA"},
    "consultant-geo-optimisation-moteurs-ia": {"silo": "GEO / Référencement IA"},
    "linkedin-seo": {"silo": "GEO / Référencement IA"},
    "ia-et-seo": {"silo": "GEO / Référencement IA"},
    "fiche-gmb": {"silo": "SEO Local & GMB"},
    "citations-locales": {"silo": "SEO Local & GMB"},
    "creer-app-ecommerce": {"silo": "SEO Vertical"},
    "app": {"silo": "Offre / Conversion", "type": "offre"},
    "blog": {"silo": "Système / Légal", "type": "système"},
    "guide-site-ia-creer-un-site-premium-en-24h": {"silo": "Offre / Conversion", "type": "lead magnet"},
    "home-old-2": {"silo": "Système / Légal", "type": "système", "action": "Désindexer"},
}


def slug_of(url):
    return re.sub(r"https?://[^/]+/", "", url or "").rstrip("/") or "(home)"


def load_inventory():
    inv = {}
    if not INVENTORY.exists():
        return inv
    for line in INVENTORY.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 3 and c[0] in ("page", "post"):
            inv[c[2]] = {"type_src": c[0], "title": c[1]}
    return inv


def aggregate_gsc():
    gsc = json.loads(GSC.read_text(encoding="utf-8"))
    agg = defaultdict(lambda: {"impr": 0, "clics": 0, "wpos": 0.0})
    for r in gsc.get("queries", []):
        s = slug_of(r["page"])
        d = agg[s]
        d["impr"] += r["impressions"]
        d["clics"] += r["clicks"]
        d["wpos"] += r["position"] * r["impressions"]
    out = {}
    for s, d in agg.items():
        impr = d["impr"]
        out[s] = {
            "impressions": impr,
            "clics": d["clics"],
            "position": round(d["wpos"] / impr, 1) if impr else None,
            "ctr": round(d["clics"] / impr, 4) if impr else None,
        }
    return out


def classify_silo(slug, title):
    hay = f"{slug} {title}".lower()
    for pattern, silo in SILO_RULES:
        if re.search(pattern, hay):
            return silo
    return "À classer"


def classify_type(slug, silo):
    if silo == "Hack — à supprimer":
        return "hack"
    if silo == "Système / Légal":
        return "système"
    if silo == "Offre / Conversion":
        return "lead magnet" if re.search(LEADMAGNET, slug) else "offre"
    if re.search(LEADMAGNET, slug):
        return "lead magnet"
    if slug in PILIERS:
        return "pilier"
    return "cluster"


def opportunity_score(perf):
    """0..100 : potentiel d'optimisation = volume d'impressions × récupérabilité
    selon la position (sweet spot 6-20)."""
    impr = perf["impressions"]
    pos = perf["position"]
    if not impr:
        return 0.0
    vol = min(1.0, math.log10(impr + 1) / 4.0)  # 10k impr ≈ 1.0
    if pos is None:
        pw = 0.4
    elif pos < 4:
        pw = 0.5          # déjà bien placé : moins de marge
    elif pos <= 10:
        pw = 1.0          # page 1 basse → pousser en top 3 = quick win
    elif pos <= 20:
        pw = 0.9          # page 2 → page 1
    elif pos <= 40:
        pw = 0.6
    else:
        pw = 0.35
    return round(100 * (0.7 * vol + 0.3 * vol * pw + 0.0), 1) if False else round(
        100 * (0.6 * vol + 0.4 * (vol * pw)), 1)


def recommend_action(slug, silo, typ, perf):
    if typ == "hack":
        return "Désindexer / Supprimer"
    if typ == "système":
        return "Ignorer"
    impr, pos = perf["impressions"], perf["position"]
    if impr == 0:
        return "Vérifier indexation / Relancer"
    if pos and pos > 15 and impr >= 100:
        return "Mettre à jour (quick win)"
    if pos and 5 <= pos <= 15 and impr >= 60:
        return "Optimiser → top 3"
    if pos and pos <= 5:
        return "Garder / Maintenir"
    return "Mettre à jour"


def build():
    inv = load_inventory()
    gsc = aggregate_gsc()

    # Union : tous les slugs d'inventaire + slugs GSC significatifs / hack.
    HACK_RE = r"forex|casino|mahjong|peppermill|obzor|slot|togel|brokera"
    slugs = set(inv)
    for s, perf in gsc.items():
        if perf["impressions"] >= GSC_MIN_IMPR or re.search(HACK_RE, s):
            slugs.add(s)
    # exclure le bruit technique
    slugs = {s for s in slugs if not re.search(r"\?p=|/feed|/wp-|/page/\d", s)}

    rows = []
    for slug in slugs:
        meta = inv.get(slug, {})
        title = meta.get("title") or slug.replace("-", " ").title()
        perf = gsc.get(slug, {"impressions": 0, "clics": 0, "position": None, "ctr": None})
        ov = OVERRIDES.get(slug, {})
        silo = ov.get("silo") or classify_silo(slug, title)
        typ = ov.get("type") or classify_type(slug, silo)
        score = opportunity_score(perf)
        action = ov.get("action") or recommend_action(slug, silo, typ, perf)
        rows.append({
            "page": title,
            "slug": slug,
            "silo": silo,
            "type": typ,
            "parent": ov.get("parent", ""),
            "impressions": perf["impressions"],
            "clics": perf["clics"],
            "position": perf["position"],
            "ctr": perf["ctr"],
            "score": score,
            "volume": "",          # DataForSEO — 2ᵉ passe
            "kd": "",              # DataForSEO — 2ᵉ passe
            "action": action,
            "in_inventory": slug in inv,
        })

    rows.sort(key=lambda r: (SILOS.index(r["silo"]) if r["silo"] in SILOS else 99,
                             -r["score"]))
    return rows


def write_outputs(rows):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # CSV
    cols = ["silo", "type", "page", "slug", "parent", "impressions", "clics",
            "position", "ctr", "score", "volume", "kd", "action", "in_inventory"]
    with open(OUT_DIR / "content-map.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    # JSON (pour Notion)
    (OUT_DIR / "content-map.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    # Markdown groupé par silo
    lines = ["# Cartographie du contenu — Décupler", "",
             f"> {len(rows)} pages · source : inventaire ∪ Google Search Console "
             f"(90 j) · volume/KD à enrichir via DataForSEO", ""]
    by_silo = defaultdict(list)
    for r in rows:
        by_silo[r["silo"]].append(r)
    for silo in SILOS:
        if silo not in by_silo:
            continue
        grp = by_silo[silo]
        tot = sum(r["impressions"] for r in grp)
        lines.append(f"## {silo}  ·  {len(grp)} pages · {tot} impr")
        lines.append("")
        lines.append("| Page | Type | Impr | Clics | Pos | Score | Action |")
        lines.append("|---|---|--:|--:|--:|--:|---|")
        for r in grp:
            pos = r["position"] if r["position"] is not None else "—"
            lines.append(f"| {r['page'][:45]} (`/{r['slug'][:35]}`) | {r['type']} | "
                         f"{r['impressions']} | {r['clics']} | {pos} | {r['score']} | {r['action']} |")
        lines.append("")
    (OUT_DIR / "content-map.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    rows = build()
    write_outputs(rows)
    from collections import Counter
    c = Counter(r["silo"] for r in rows)
    print(f"[map] {len(rows)} pages cartographiées")
    for silo in SILOS:
        if silo in c:
            print(f"  {c[silo]:>3}  {silo}")
    print(f"  → {OUT_DIR/'content-map.md'}")
    print(f"  → {OUT_DIR/'content-map.csv'}")
    print(f"  → {OUT_DIR/'content-map.json'}")
