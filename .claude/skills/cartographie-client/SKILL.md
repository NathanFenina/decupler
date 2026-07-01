---
name: cartographie-client
description: >-
  Produit la « Cartographie des Opportunités » d'un client (livrable du Front-End
  Décupler) : une base Notion vivante, priorisée par impact business, à partir de
  son domaine + des données Ubersuggest (volume/KD/intention/SERP) et, si connectée,
  Google Search Console. Sort une base Notion complète (même schéma que « Cartographie
  SEO — Décupler ») + une vue client « Plan d'investissement », des clusters, un
  maillage et une roadmap. À utiliser quand on dit : « fais la cartographie pour
  [client/domaine] », « lance la mission Front-End pour X », « génère le Notion
  d'opportunités de tel site ». Marché par défaut : France / français.
---

# Skill : cartographie-client — la mission Front-End productisée

Ce skill **opère l'offre Front-End** décrite dans `docs/offre/blueprint-front-end-v1.md`.
Objectif : livrer une **cartographie vivante des opportunités organiques** (pas un
audit figé), sous forme de **base Notion** priorisée par **impact business**.

> Lis d'abord `docs/offre/blueprint-front-end-v1.md` (§6 mission, §7 mécanisme,
> §3 ICP). Respecte les principes (§14) : on prioralise par **business**, pas par
> métrique SEO ; on construit un **actif**, pas un livrable ; on n'expose **jamais**
> les coulisses au client (vue filtrée).

## Quand l'utiliser
- Nouveau client → produire son livrable Front-End.
- Notre propre site (dogfooding) → enrichir « Cartographie SEO — Décupler ».
- Toute demande « cartographie / plan d'opportunités » sur un domaine donné.

## Entrées à cadrer (demander si non fourni)
- **Client + domaine** (ex. `client.com`).
- **Marché / langue** (défaut France / `fr`).
- **Périmètre sémantique** : thématiques / seeds de départ (sinon, les déduire du
  domaine via `domain_keywords` + `competitors`).
- **Concurrents** connus (sinon les trouver via `competitors`).
- **Notion** : page parente où créer la base (demander l'URL/ID ; sinon proposer).

## Outils
- **Ubersuggest (MCP)** — source mots-clés/SERP/concurrents/domaine. Vérifier
  `auth_status` avant. Marché FR : `language:"fr"` (+ `locId` via `location_suggest`
  si dispo ; sinon volumes ~globaux, le **signaler** — cf. limite ci-dessous).
- **GSC (Windsor.ai MCP)** — données réelles **si** le domaine du client y est
  connecté (`get_connectors`). Sinon, sauter et le dire.
- **Scripts** (stdlib, repo Décupler) :
  - `scripts/ubersuggest_normalize.py` — brut Ubersuggest → format scoring.
  - `scripts/gsc_normalize.py` — brut GSC → format scoring.
  - `scripts/score_opportunities.py` — fusion + score + clusters + maillage.
- **Notion** — deux voies :
  - **MCP** (`notion-create-database`, `notion-create-pages`, `notion-create-view`,
    `notion-update-data-source`, `notion-search`) : création de base, vues, recherche
    par titre, écritures ponctuelles. ⚠️ `notion-query-data-sources` (lecture SQL en
    masse) est **throttlé de façon imprévisible** — ne PAS en dépendre pour énumérer
    toutes les lignes.
  - **API REST officielle** via `scripts/notion_sync.py` (token `NOTION_TOKEN` dans
    `.env`) : **voie FIABLE** pour lire toutes les lignes (`pull`, paginé) et remplir
    des colonnes en masse (`push`, gestion native du rate limit). À utiliser dès qu'il
    faut lire/écrire >quelques lignes.

## Schéma Notion STANDARD (identique pour chaque client = produit reproductible)
La base s'appelle **« Cartographie SEO — <Client> »**. Propriétés :

| Propriété | Type | Rôle |
|---|---|---|
| **Mot clé** | title | le mot-clé / sujet |
| **Statut** | select : Existant · À créer · En cours · Publié | cycle de vie |
| **Type** | select : pilier · cluster · offre · lead magnet · système | rôle éditorial |
| **Format** | select : Page · Article | |
| **Silo** | select | grand thème (adapté au client) |
| **Cluster** | text | pilier de rattachement (Cluster X) |
| **Priorité** | select : P1 · P2 · P3 | **priorisation business** |
| **Potentiel business** | number (€) | CA/pipeline estimé |
| **Canal** | multi-select : SEO · GEO · Reddit · LinkedIn · YouTube · PR | visibilité multi-canal |
| **Intention** | select : Informationnel · Commercial · Transactionnel · Navigationnel | |
| **Volume** | number | volume de recherche |
| **KD** | number | difficulté SEO |
| **AI Overview** | checkbox | signal GEO (citation IA) |
| **Effort** | select : S · M · L | pour matrice impact × effort |
| **Action** | select : Optimiser → top 3 · Mettre à jour (quick win) · Mettre à jour · Garder / Maintenir · Vérifier indexation / Relancer · Ignorer | |
| **Position / CTR / Impressions / Clics** | number | données GSC (si dispo) |
| **Évolution position** | number | delta vs snapshot précédent (carto « vivante ») |
| **Dernière MAJ** | date | fraîcheur |
| **Slug** | text | |
| **Dans inventaire** | checkbox | déjà sur le site |

DDL de référence (via `notion-create-database` ou `update-data-source ADD COLUMN`) :
```
SELECT('P1':red,'P2':orange,'P3':blue)                         -- Priorité
NUMBER FORMAT 'euro'                                            -- Potentiel business
MULTI_SELECT('SEO':blue,'GEO':purple,'Reddit':orange,'LinkedIn':blue,'YouTube':red,'PR':green) -- Canal
SELECT('Informationnel':blue,'Commercial':orange,'Transactionnel':green,'Navigationnel':gray)  -- Intention
SELECT('S':green,'M':yellow,'L':red)                           -- Effort
CHECKBOX  -- AI Overview        DATE -- Dernière MAJ           NUMBER -- Évolution position
```

## Procédure

### Étape 0 — Cadrage & positionnement
Confirmer client/domaine/marché/concurrents/page Notion parente. Rappeler que le
livrable est un **actif vivant**, priorisé business (cf. Blueprint).

### Étape 1 — Audit domaine & concurrents (Ubersuggest)
- `domain_overview`, `domain_top_pages`, `domain_keywords` sur le domaine client.
- `competitors` (+ `domain_keywords` sur 1-3 concurrents) → repérer les mots-clés
  qu'ils captent et **pas** le client = opportunités à récupérer.
- `seo_opportunities` / `content_ideas` pour les sujets qui performent déjà.
Sauver les bruts dans `content/opportunities/.cache/`.

### Étape 2 — Expansion mots-clés (Ubersuggest) → normalisation
`keyword_suggestions` + `keyword_overview` sur les seeds/sujets (volume, KD,
intention, `monthly_searches` → tendance). Brut → cache, puis :
```bash
python3 scripts/ubersuggest_normalize.py \
    --in content/opportunities/.cache/<client>-overview.json \
    --in content/opportunities/.cache/<client>-domain.json \
    --out content/opportunities/.cache/keywords.json
```

### Étape 3 — GSC réel (si connecté à Windsor pour CE domaine)
`get_connectors` → si le `searchconsole` du client est là : `get_data` (90 j ;
query, clicks, impressions, ctr, position, page) → brut → `gsc_normalize.py`.
Sinon sauter et le **signaler** (la carto fonctionne sans, sans les quick wins).

### Étape 4 — SERP & signal GEO (optionnel)
`serp_analysis` sur le top ~30 mots-clés → `ubersuggest_normalize.py --serp-out`.
⚠️ Ubersuggest n'expose PAS l'AI Overview : laisser `AI Overview` à False et le
remplir à la main / via `brand_visibility_overview` quand c'est un vrai signal IA.

### Étape 5 — Scoring, clusters, maillage
```bash
python3 scripts/score_opportunities.py \
    --keywords content/opportunities/.cache/keywords.json \
    [--gsc content/opportunities/.cache/gsc.json] \
    [--serp content/opportunities/.cache/serp.json] \
    --inventory <inventaire client ou content/cleaned/inventory.md> \
    --date <AAAA-MM-JJ> \
    --out-md content/opportunities/<client>-<date>.md \
    --out-csv content/opportunities/<client>-<date>.csv
```

### Étape 6 — Couche business (jugement expert, PAS automatique)
Pour chaque cluster / mot-clé, renseigner :
- **Priorité** P1/P2/P3 = (impact business × intention × faisabilité), pas le score brut.
- **Potentiel business (€)** = modèle TRANSPARENT et défendable (jamais un palier au doigt mouillé) :
  `Trafic/mois = Volume × CTR(position cible)` — CTR : pos1≈0.28, top3≈0.15, top5≈0.08, top10≈0.03.
  `Potentiel €/an = Trafic/mois × conv(intention) × valeur_lead × 12`.
  Conv. visiteur→lead : transac 3 % · commercial 2 % · info/GEO 0,5 % (valeur d'assistance) · nav 0.
  `valeur_lead = valeur_client_signé × taux_closing` (à DEMANDER au client ; défaut Décupler 15 000 € × 12 % = 1 800 €).
  Toujours libeller « potentiel annuel à maturité (page classée à la position cible) » et exposer les hypothèses.
  Pré-requis : un Volume par ligne → faire une passe `keyword_overview` Ubersuggest sur les cibles « À créer ».
- **Canal** : SEO et/ou GEO/Reddit/LinkedIn/YouTube/PR selon où l'audience décide.
- **Effort** : S/M/L. P1 = fort potentiel **et** effort raisonnable.

### Étape 7 — Construction de la base Notion (le livrable)
1. `notion-create-database` (page parente fournie) avec le **schéma standard** ci-dessus.
   Titre : « Cartographie SEO — <Client> ».
2. `notion-create-pages` : 1 ligne par mot-clé/sujet (existant + à créer), champs
   remplis (Priorité, Potentiel, Canal, Cluster, Volume, KD, Intention, Statut…).
   Mettre `Dernière MAJ` = date du run.
   **Pour remplir/mettre à jour en masse une base existante**, préférer l'API REST :
   ```bash
   python3 scripts/notion_sync.py pull --db <database_id> --out .cache/notion-rows.json
   # (enrichir les lignes : priorité/potentiel/canal/intention/effort/cluster)
   python3 scripts/notion_sync.py push --db <database_id> --data <enriched.json> \
       --match-prop Slug --set "Priorité,Potentiel business,Canal,Intention,Effort,Cluster" \
       --date <AAAA-MM-JJ> [--dry-run]
   ```
3. `notion-create-view` — **vue client** board « Plan d'investissement » :
   `GROUP BY "Priorité"; SORT BY "Potentiel business" DESC;
    SHOW "Mot clé","Priorité","Potentiel business","Canal","Cluster","Statut","Volume"`.
   (Ne montrer au client QUE cette vue : pas de Score brut, pas de prompts internes.)
4. Ajouter 2 vues d'hygiène internes si pertinent (pages à désindexer, 0 impression).

### Étape 7 bis — Dashboard client « waouh » (livrable visuel)
Générer un dashboard HTML à la charte Décupler (potentiel total, top opportunités,
potentiel par thématique, roadmap par mois, « qui capte vos opportunités ») :
```bash
python3 scripts/notion_sync.py pull --db <database_id> --out .cache/<client>-final.json
python3 scripts/build_dashboard.py --in .cache/<client>-final.json \
    --title "<Client>" --date "<date>" --out content/opportunities/dashboard-<client>.html
```
C'est l'artefact qui transforme la perception « audit » → « actif/plan d'investissement ».
Envoyer le fichier au client (ou export PDF). Concurrent en tête = via `serp_analysis`.

### Étape 8 — Restitution
Présenter, dans l'esprit Blueprint :
1. **Quick wins** (striking distance GSC) — priorité immédiate.
2. **Clusters P1** (potentiel business) — chacun = 1 pilier + angle + maillage.
3. **Opportunités GEO / IA** — sujets de citation IA.
4. **Roadmap** (Mois 1→3) + lien Notion (vue client).
Puis proposer la suite : rédaction (`redaction-expert`) et/ou l'upsell Back-End
(« qui exécute ? » → infrastructure opérée — cf. Blueprint §9).

## Garde-fous
- Vérifier `auth_status` (Ubersuggest) et `get_connectors` (GSC) AVANT de promettre des données.
- **Volumes Ubersuggest = ~globaux** si pas de `locId` national → le dire au client.
- Ne jamais committer `.env` ni `.cache/`. Ne pas charger l'export XML (cf. CLAUDE.md).
- Le scoring est une aide ; la **priorisation business reste un jugement** (Blueprint §14).
- Vue client ≠ coulisses : on n'expose pas l'outillage, juste la valeur.
- Si une brique manque (GSC, SERP), continuer en dégradé et le signaler.
