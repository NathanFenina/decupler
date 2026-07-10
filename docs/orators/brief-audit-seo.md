# Brief freelance — Audit SEO + GEO complet pour **Orators**

> **À qui** : la freelance qui va construire le projet.
> **De** : Décupler (projects@decupler.com)
> **Objectif** : monter un **projet Claude Code** qui, en branchant les bons MCP,
> produit un **audit SEO complet sur une seule page HTML** (charte Décupler), sur le
> modèle de ce qu'on a déjà fait pour Décupler (la « Cartographie des Opportunités »).
> **Marché** : France / français. **Date de cadrage** : 2026-07.

---

## 1. Le principe (à retenir avant tout)

On ne fait **pas** un audit « à la main » dans un tableur. On reproduit la mécanique
Décupler :

1. Un **projet Claude Code** dédié au client (dossier séparé, son propre `.env`).
2. On **branche des MCP** (connecteurs) qui donnent les données réelles.
3. Claude **collecte, croise, score et priorise** les données.
4. Sortie = **une page HTML d'audit** à la charte, + une base **Notion vivante**
   (l'actif qu'on livre et qu'on met à jour dans le temps).

Ce qui change vs un audit classique : **on priorise par impact business, pas par
métrique SEO brute**, et le livrable est un **actif vivant**, pas un PDF figé.

> ⚠️ Le client demande 5 volets : **Technique · Backlinks · Stratégie de contenu ·
> Roadmap · Audit AI Search**. On ajoute un fil rouge transverse : **l'acquisition
> de leads** (traquer / estimer les leads par page et par mot-clé).

---

## 2. Ce qu'on a comme accès sur Orators

- ✅ **Google Search Console** (impressions, clics, positions, CTR, requêtes, pages).
- ✅ **Google Analytics 4** (sessions, conversions, événements → **leads par page**).
- ❓ CRM (HubSpot / Salesforce / GoHighLevel) : **à vérifier** — c'est ce qui permet
  de rattacher MQL/SQL. Si absent → on **estime** (voir §8).

À demander au client pour cadrer :
- Le **domaine** exact (`orators.fr` ? sous-domaines ?) et les **langues/marchés**.
- Ses **2–3 concurrents** principaux (sinon on les trouve via Ubersuggest).
- La **valeur d'un client signé** et le **taux de closing** (indispensables pour
  chiffrer le potentiel business en €, cf. §8).
- Ont-ils un **suivi de conversions** dans GA4 (formulaire, démo, devis) ? Un CRM ?

---

## 3. Les MCP à connecter (le cœur du dispositif)

| MCP | Ce qu'il apporte | Volets couverts |
|---|---|---|
| **Ubersuggest (Neil Patel)** | Mots-clés (volume, KD, intention), SERP, concurrents, **backlinks**, **audit technique** (`site_audit`, `pagespeed_audit`), **visibilité IA** (`brand_visibility_overview`, `brand_prompts`) | Contenu · Backlinks · Technique · AI Search |
| **Windsor.ai** | **GSC réel** (impressions/clics/position réelles) + **GA4** (conversions, événements = **leads par page**) | Contenu (quick wins) · Acquisition leads |
| **Notion** | Construire la **base d'opportunités vivante** + la vue « Plan d'investissement » client | Stratégie · Roadmap |
| **Screaming Frog** *(optionnel, phase 2)* | Crawl technique profond : redirections, hreflang, pages orphelines, profondeur de clic, duplications | Technique (granularité) |

**Point clé à comprendre** : **Ubersuggest couvre déjà 4 des 5 volets** (contenu,
backlinks, technique de base, IA). **Screaming Frog n'est pas indispensable au
départ** — on le branche seulement si on a besoin de granularité technique
(gros site, migration, cocons complexes). On démarre léger.

**Vérifs obligatoires AVANT de promettre des données** :
- Ubersuggest : `auth_status`.
- Windsor.ai : `get_connectors` → confirmer que **le GSC ET le GA4 d'Orators** y sont
  connectés. Si non → demander au client de connecter, sinon on tourne en dégradé.
- Ubersuggest volumes : sans `locId` national (via `location_suggest`), les volumes
  sont **~globaux** → toujours le **signaler** au client.

---

## 4. Les 5 volets de l'audit — détail par volet

Pour chaque volet : **les questions auxquelles on répond**, **les outils MCP**, **ce
qu'on sort**, **les actions**.

### 4.1 — Audit TECHNIQUE
**Questions** : le site est-il crawlable, rapide, indexable, sain ?

- **Outils** :
  - Ubersuggest `site_audit` → `site_audit_status` → `site_audit_results` /
    `site_audit_pages` (erreurs on-site : 4xx/5xx, titres/meta manquants ou dupliqués,
    H1, contenu léger, images sans alt, liens cassés, canonical, score de santé).
  - Ubersuggest `pagespeed_audit` (Core Web Vitals, mobile/desktop) sur les pages clés.
  - *(Optionnel)* Screaming Frog pour le crawl profond (hreflang, chaînes de redirection,
    pages orphelines, profondeur, duplications à l'échelle).
- **On sort** : un **tableau d'erreurs classées par gravité** (bloquant / important /
  cosmétique), avec URL, type d'erreur, impact, et **action corrective + effort (S/M/L)**.
- **Actions** : liste priorisée « à corriger » (ex. corriger les 12 pages en 404,
  compresser 40 images, réécrire 8 title dupliqués…).

### 4.2 — Audit BACKLINKS
**Questions** : quel est le profil de liens ? Est-il sain ? Où sont les opportunités ?

- **Outils** (Ubersuggest) :
  - `backlinks_overview` (nombre de domaines référents, autorité, évolution).
  - `backlinks` + `linking_domains` + `anchor_texts` (qualité, ancres, spam éventuel).
  - `backlink_opportunity` (domaines qui lient les concurrents mais **pas** Orators
    = cibles de netlinking).
  - `competitors` + `backlinks_overview` sur 2–3 concurrents → **gap de liens**.
- **On sort** : profil de liens (santé, ancres, top domaines), **liste d'opportunités
  de netlinking** classée, alerte sur d'éventuels liens toxiques.
- **Actions étape par étape** : plan de netlinking (cibles prioritaires, type d'action —
  guest post / digital PR / annuaire de niche / récupération de mentions non liées),
  avec un ordre d'exécution.

### 4.3 — Stratégie de CONTENU (sémantique)
**Questions** : sur quoi se positionner ? Quels silos, piliers, clusters, maillage ?
Où sont les **quick wins** business ?

- **Outils** :
  - Ubersuggest : `domain_overview`, `domain_keywords`, `domain_top_pages` (ce que le
    site capte déjà), `competitors` + `domain_keywords` concurrents (ce qu'on **rate**),
    `keyword_suggestions` + `keyword_overview` + `content_ideas` + `seo_opportunities`
    (expansion mots-clés : volume, KD, intention, tendance).
  - Windsor.ai `get_data` sur **GSC** (90 j) → **striking distance / quick wins** :
    les pages en position 5–20 qui montent vite = priorité immédiate.
  - Ubersuggest `serp_analysis` sur le top mots-clés → qui domine, quel format gagne.
- **On sort** :
  - Les **silos / thématiques** (grands univers de contenu).
  - Les **pages piliers** (1 par cluster) + **clusters** rattachés.
  - Le **maillage interne** recommandé (quelle page pointe vers quelle page).
  - Les **quick wins** GSC (à optimiser maintenant), les **trous** à créer.
- **Actions** : liste « À créer » / « À optimiser » / « À maintenir », chacune avec
  priorité, potentiel business (€), canal (SEO/GEO), effort.

> C'est **exactement** le schéma de la base Notion Décupler (voir §6). On réutilise
> le skill `cartographie-client` : mêmes colonnes, même scoring, même dashboard.

### 4.4 — Audit AI SEARCH / GEO (le différenciant)
**Questions** : Orators est-il **cité** par les moteurs IA (ChatGPT, Perplexity,
Gemini, Google AI Overviews) ? Sur quels prompts ? Comment gagner ces citations ?

- **Outils** :
  - Ubersuggest `brand_config` → `brand_visibility_overview` (part de voix de la marque
    dans les réponses IA) + `brand_prompts` (sur quels prompts la marque apparaît/manque).
  - **Reverse-engineering des « fan-out queries »** : identifier les questions que les
    LLM se posent en cascade autour d'un sujet, et vérifier si Orators y répond.
  - **Monitoring manuel multi-LLM** : tester une **batterie de prompts** réels sur
    ChatGPT / Perplexity / Gemini / Claude + Google AI Overviews, et noter :
    Orators est-il cité ? avec quelle source ? à côté de quels concurrents ?
- **On sort** :
  - Un **jeu de prompts principaux** (les questions cibles du marché d'Orators).
  - Un **tableau de monitoring** : prompt × moteur IA × cité (oui/non) × source × concurrents.
  - Les **sujets de citation IA** à travailler (contenu structuré, FAQ, données, définitions).
- **Actions** : plan GEO (formats qui se font citer : réponses directes, tableaux
  comparatifs, FAQ JSON-LD, données chiffrées, pages « définition »).

> ⚠️ Ubersuggest n'expose **pas** l'AI Overview dans le SERP classique : la colonne
> « AI Overview » de la base se remplit à la main / via `brand_visibility_overview`.

### 4.5 — ROADMAP
**Questions** : dans quel ordre exécute-t-on tout ça sur 3–6 mois ?

- Synthèse des 4 volets ci-dessus, **priorisée impact × effort**.
- **On sort** une roadmap claire par mois :
  - **Mois 1** : quick wins GSC + corrections techniques bloquantes.
  - **Mois 2** : piliers P1 (contenu) + premières actions netlinking.
  - **Mois 3+** : clusters, GEO, netlinking récurrent, création de contenu en volume.
- Chaque item = responsable, effort, résultat attendu, KPI de suivi.

---

## 5. Fil rouge transverse — ACQUISITION DE LEADS

Le client veut orienter l'audit **business / leads**, pas juste trafic. On veut
répondre à : *« quelle page / quel mot-clé génère des leads (et des MQL/SQL) ? »*

- **Si tracking existant (GA4 avec conversions)** :
  - Windsor.ai `get_data` sur **GA4** → conversions/événements **par landing page**
    (formulaire, démo, devis, téléchargement).
  - Croiser **GSC (mot-clé → page)** × **GA4 (page → conversion)** = **leads estimés
    par mot-clé/page**.
- **Si CRM connecté (HubSpot/Salesforce/GoHighLevel via Windsor)** :
  - Rattacher **MQL / SQL** à la source/page d'entrée → vraie valeur pipeline.
- **Si rien n'est traqué** :
  - On **estime** avec le modèle business transparent (cf. §8) et on **recommande**
    de poser le tracking (événements GA4 + UTM + CRM) comme action Mois 1.

**Livrable de ce fil rouge** : dans la base, chaque page/mot-clé porte un
**Potentiel business (€)** et, quand la donnée existe, un **nb de leads / conversions**.

---

## 6. Le scoring & la priorisation business (ne pas sauter)

On ne classe **jamais** par volume brut. Modèle **transparent et défendable** :

```
Trafic/mois       = Volume × CTR(position cible)
                    CTR : pos1 ≈ 0,28 · top3 ≈ 0,15 · top5 ≈ 0,08 · top10 ≈ 0,03
Potentiel €/an    = Trafic/mois × conv(intention) × valeur_lead × 12
                    conv visiteur→lead : transac 3 % · commercial 2 % · info/GEO 0,5 % · nav 0
valeur_lead       = valeur_client_signé × taux_closing   (À DEMANDER au client)
```

- **Priorité P1/P2/P3** = impact business × intention × faisabilité (jugement expert,
  pas le score brut).
- **P1** = fort potentiel **et** effort raisonnable.
- Toujours libeller « potentiel annuel à maturité (page à la position cible) » et
  **exposer les hypothèses**.

---

## 7. Le livrable — la page HTML d'audit

Une **page HTML unique** à la **charte Décupler** (fond `#07080f`, violet `#7B5CFA`,
vert `#00E5A0`, titres **Syne**, corps **DM Sans**), qui présente dans l'ordre :

1. **Synthèse exécutive** : santé globale, top 3 leviers, potentiel business total (€).
2. **Technique** : score de santé + tableau erreurs priorisées.
3. **Backlinks** : profil + opportunités de netlinking.
4. **Contenu / sémantique** : silos, piliers, clusters, maillage, quick wins, potentiel €.
5. **AI Search / GEO** : tableau de monitoring multi-LLM + plan de citation.
6. **Acquisition leads** : leads/conversions par page (réels ou estimés).
7. **Roadmap** : plan Mois 1 → 3(–6), priorisé impact × effort.

En parallèle, la **base Notion vivante** (schéma standard Décupler, cf. skill
`cartographie-client`) sert d'actif qu'on met à jour dans le temps ; on ne montre au
client **que la vue « Plan d'investissement »** (jamais les coulisses/outillage).

---

## 8. Setup du projet (arborescence à monter)

Repartir de la structure Décupler (un dossier client dédié) :

```
orators/
├── .env                      # secrets — JAMAIS commité (voir .env.example)
├── CLAUDE.md                 # rôle du projet (audit Orators)
├── content/
│   └── opportunities/
│       └── .cache/           # bruts Ubersuggest / GSC / GA4 (jamais commités)
├── docs/
│   └── audit/                # brouillons, notes
└── scripts/                  # réutiliser ceux de Décupler
    ├── ubersuggest_normalize.py
    ├── gsc_normalize.py
    ├── score_opportunities.py
    └── build_dashboard.py    # génère la page HTML d'audit
```

`.env` à remplir (jamais commité) :
```
# Ubersuggest, Windsor.ai (GSC + GA4), Notion → via MCP/tokens
NOTION_TOKEN=...
WINDSOR_API_KEY=...
# valeur business (pour le scoring €)
VALEUR_CLIENT_SIGNE=...
TAUX_CLOSING=...
```

---

## 9. Checklist de démarrage (dans l'ordre)

1. [ ] Cadrer avec le client : domaine, marché, concurrents, **valeur client × closing**,
       tracking GA4/CRM existant ?
2. [ ] Créer le projet Claude Code `orators/` + `.env`.
3. [ ] Connecter les MCP : **Ubersuggest**, **Windsor.ai**, **Notion**
       (Screaming Frog seulement si besoin).
4. [ ] Vérifier `auth_status` (Ubersuggest) et `get_connectors` (GSC **+** GA4 d'Orators).
5. [ ] **Technique** : `site_audit` + `pagespeed_audit`.
6. [ ] **Backlinks** : `backlinks_overview` + `backlink_opportunity` + gap concurrents.
7. [ ] **Contenu** : domaine + concurrents + expansion mots-clés + quick wins GSC.
8. [ ] **AI Search** : `brand_visibility_overview` + `brand_prompts` + monitoring multi-LLM.
9. [ ] **Leads** : GA4 conversions par page (ou estimation via modèle §6).
10. [ ] **Scoring** : priorité + potentiel € par ligne.
11. [ ] Construire la **base Notion** (schéma standard) + vue client.
12. [ ] Générer la **page HTML d'audit** (charte Décupler).
13. [ ] **Roadmap** Mois 1→3 + restitution client.

---

## 10. Garde-fous (les règles Décupler)

- Vérifier les accès (auth) **avant** de promettre des données ; sinon tourner en
  dégradé et **le dire**.
- Volumes Ubersuggest **~globaux** sans `locId` national → le signaler.
- **Jamais** committer `.env` ni les `.cache/`.
- Le scoring est une **aide** ; la priorisation reste un **jugement business**.
- **Vue client ≠ coulisses** : on n'expose pas l'outillage, uniquement la valeur.
- HTML propre, sémantique, à la charte (pas de CSS inline sale, pas de classes parasites).

---

### En un mot
On rejoue **exactement** la mécanique Décupler (skill `cartographie-client` +
scoring business + dashboard HTML), en l'élargissant aux volets **technique**,
**backlinks** et **AI Search**, le tout **orienté acquisition de leads**. La bonne
nouvelle : **Ubersuggest + Windsor.ai + Notion suffisent pour démarrer** ;
Screaming Frog reste une option de granularité technique.
