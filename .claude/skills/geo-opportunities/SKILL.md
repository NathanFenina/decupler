---
name: geo-opportunities
description: >-
  Découvre et priorise les meilleures opportunités d'articles de blog autour du
  GEO (Generative Engine Optimization) pour Décupler. Combine l'expansion de
  mots-clés via le MCP Ubersuggest (volume, difficulté, intention, SERP), les données
  réelles Google Search Console (striking distance / quick wins via le MCP
  Windsor.ai) et l'inventaire interne, puis produit un plan éditorial priorisé
  (clusters + maillage). À utiliser quand l'utilisateur demande des idées
  d'articles, des mots-clés, un plan de contenu, un audit d'opportunités SEO/GEO,
  ou « sur quoi écrire ». Marché par défaut : France / français.
---

# Skill : geo-opportunities — la machine à trouver les sujets & mots-clés GEO

Tu agis comme **expert SEO/GEO**. Objectif : sortir une liste d'opportunités
d'articles **priorisées et actionnables**, pas une liste brute de mots-clés.

GEO = *Generative Engine Optimization* : être visible/cité dans les réponses des
moteurs IA (ChatGPT, Perplexity, Gemini, Google AI Overviews…). Décupler est une
agence SEO/GEO : on cherche des sujets à fort potentiel de trafic ET de citation IA.

## Architecture (4 briques)

1. **Seeds** — `content/opportunities/seeds-geo.txt` (champ sémantique GEO, FR).
2. **Ubersuggest (MCP)** — expansion + volume/KD/intention + SERP. Appelé par Claude
   au runtime ; réponses brutes → `scripts/ubersuggest_normalize.py`.
3. **GSC (Windsor.ai MCP)** — données réelles du site → `scripts/gsc_normalize.py`.
4. **Scoring** — `scripts/score_opportunities.py` : fusion + score + clusters + maillage.

> **Source mots-clés = MCP Ubersuggest** (décision du 2026-06-30, remplace l'API
> DataForSEO). L'ancien `scripts/dataforseo_query.py` reste comme fallback si le MCP
> est indisponible, mais ne pas l'utiliser par défaut.

Cache de travail : `content/opportunities/.cache/` · Livrables : `content/opportunities/`.

## Pré-requis (vérifier AVANT de lancer)

- **Ubersuggest (MCP)** : vérifier la connexion avec `auth_status` (doit renvoyer
  un compte + tier). Si 401/déconnecté → le signaler, ne pas inventer de données.
  Marché FR : passer `language: "fr"` et le `locId` France (via `location_suggest`
  si besoin) à chaque appel.
- **GSC via Windsor.ai** : le connecteur `searchconsole` doit avoir la propriété
  **decupler.com** connectée. Vérifier avec `get_connectors`. Si seul un autre
  site est connecté, le signaler et continuer **sans GSC** (le scoring fonctionne,
  sans les quick wins).
- Python 3 (stdlib only, aucune install requise).

## Procédure

### Étape 0 — Cadrage
Confirmer le périmètre avec l'utilisateur si non précisé : thématique (par défaut
le champ GEO complet via les seeds), marché (défaut **France / French**), et s'il
veut élargir les seeds (lui proposer d'éditer `seeds-geo.txt`).

### Étape 1 — Expansion via Ubersuggest (MCP)
Pour chaque graine de `seeds-geo.txt` (marché FR : `language:"fr"` + `locId` France),
appeler au runtime le MCP Ubersuggest :
- `keyword_suggestions` (graines → longue traîne : related, questions, comparaisons) ;
- `keyword_overview` sur les graines + meilleures suggestions (volume, CPC,
  `seo_difficulty`, `competition`, `monthly_searches` → tendance) ;
- en complément utile : `content_ideas` (sujets qui performent déjà) et
  `seo_opportunities` / `domain_keywords` si on part d'un domaine concurrent.

Écrire **toutes les réponses brutes** (concaténées ou en plusieurs fichiers) dans
`content/opportunities/.cache/`, puis normaliser :
```bash
python3 scripts/ubersuggest_normalize.py \
    --in content/opportunities/.cache/ubs-overview.json \
    --in content/opportunities/.cache/ubs-suggestions.json \
    --out content/opportunities/.cache/keywords.json
```
Le normaliseur est tolérant (accepte n'importe quelle sortie Ubersuggest, harmonise
volume/KD/intention) et produit le format attendu par le scoring.

### Étape 2 — GSC via Windsor.ai (si decupler.com connecté)
Récupérer au runtime les requêtes des **90 derniers jours** via le MCP Windsor.ai
(outil `get_data`, connecteur `searchconsole`, account `https://www.decupler.com/`),
champs : `query, clicks, impressions, ctr, position, page`. Écrire la réponse
**brute** dans `content/opportunities/.cache/gsc-raw.json`, puis :
```bash
python3 scripts/gsc_normalize.py \
    --in content/opportunities/.cache/gsc-raw.json \
    --out content/opportunities/.cache/gsc.json
```
Si decupler.com n'est pas connecté à Windsor : sauter cette étape et le signaler.

### Étape 3 — SERP & signal GEO (optionnel mais recommandé)
Prendre le top ~30 mots-clés (volume × pertinence GEO) et appeler `serp_analysis`
sur chacun (MCP Ubersuggest). Sauver les réponses brutes puis :
```bash
python3 scripts/ubersuggest_normalize.py \
    --serp-in content/opportunities/.cache/ubs-serp.json \
    --serp-out content/opportunities/.cache/serp.json
```
⚠️ **Limite Ubersuggest** : il n'expose **pas** nativement la présence d'AI Overview
(le champ `ai_overview` reste donc à False). Pour le signal GEO pur, s'appuyer plutôt
sur : les **questions** remontées par `keyword_suggestions` (proxy PAA) et, pour la
visibilité dans les moteurs IA, `brand_visibility_overview` / `brand_prompts`.

### Étape 4 — Scoring & plan éditorial
```bash
python3 scripts/score_opportunities.py \
    --keywords content/opportunities/.cache/keywords.json \
    --gsc content/opportunities/.cache/gsc.json \
    --serp content/opportunities/.cache/serp.json \
    --inventory content/cleaned/inventory.md \
    --date <AAAA-MM-JJ> \
    --out-md content/opportunities/<AAAA-MM-JJ>-geo.md \
    --out-csv content/opportunities/<AAAA-MM-JJ>-geo.csv
```
Omettre `--gsc` et/ou `--serp` s'ils n'ont pas été générés. Utiliser la date du
jour (fournie dans le contexte) pour `<AAAA-MM-JJ>`.

### Étape 5 — Restitution
Lire le `.md` produit et présenter à l'utilisateur, dans cet ordre :
1. **Quick wins** (striking distance GSC) — à traiter en priorité.
2. **Clusters prioritaires** (top 10) — chaque cluster = 1 article pilier, avec
   angle GEO, type de contenu et maillage interne suggéré.
3. **Sujets à AI Overview** — opportunités de citation IA.
Proposer ensuite de passer à la rédaction (autre étape : génération de contenu).

## Modèle de scoring (pour expliquer si on te le demande)

**Candidats** = mots-clés Ubersuggest **+ requêtes GSC réelles** (chaque requête où
le site a des impressions est une opportunité à part entière, pas juste un bonus).
Filtre de pertinence GEO : termes forts (sans ambiguïté) vs termes faibles
(marques/sigles « ia », « geo », « claude »… qui exigent un mot de contexte SEO)
+ liste négative (géographie, jeux, spam). Seuil `--min-geo` (défaut 0.5).

Score 0–100 = 30 % volume (log) · 22 % faisabilité (inverse KD) · 18 %
pertinence GEO · 15 % intention (info/commercial favorisés) · 15 % présence
AI Overview/PAA. **Bonus** : +18 si striking distance GSC (quick win), +6 si
impressions GSC. **Malus** : −12 si déjà couvert par une page existante (→ devient
une cible de maillage/mise à jour plutôt qu'un nouvel article).

⚠️ **Proxy volume** : pour une requête GSC sans donnée Ubersuggest, le « volume »
affiché = **impressions GSC sur 90 j** (borne basse, marqué `volume_estimated`),
pas le volume de recherche national. Pour obtenir les vrais volumes, enrichir ces
requêtes via `keyword_overview` (Ubersuggest) en 2ᵉ passe.

## Garde-fous
- Ne jamais committer `.env` ni le contenu de `.cache/`.
- Ne pas charger l'export XML WordPress (cf. CLAUDE.md).
- Si une brique manque (Ubersuggest ou GSC), continuer en dégradé et le dire
  clairement — ne pas bloquer tout le pipeline.
- Le scoring est une aide à la décision : garder l'œil expert (pertinence
  éditoriale, saisonnalité, alignement avec l'offre Décupler).
