# Projet Décupler — Atelier contenu & SEO (WordPress)

## Rôle de ce projet
Ce dossier Claude Code est **l'atelier de contenu et de SEO** du site WordPress
de Décupler. Son but unique :

> **Générer des articles et des pages avec Claude, puis les publier directement
> dans WordPress** (via l'API REST), + outillage SEO.

Ce projet **NE construit PAS** le thème WordPress (c'est un **freelance externe**
qui s'en charge, ailleurs) et n'a **plus rien à voir avec Next.js** (migration
abandonnée — voir historique dans `docs/`).

## Contexte
- Le site WordPress de Décupler a été **hacké**, puis **réparé par une freelance**.
- On abandonne **Elementor + Astra** → un **thème custom léger** est réalisé par
  le freelance (un seul CSS, charte ci-dessous). En attendant, le site tourne
  encore sous Elementor + Astra : l'en-tête est le template Elementor 2762.
- Décupler est une **agence SEO/GEO** : l'objectif est de **produire du contenu
  en volume**, optimisé pour le référencement (Google + moteurs IA).

## Workflow principal : publier dans WordPress
1. L'utilisateur demande : « écris-moi un article/une page sur X ».
2. Claude rédige le contenu (HTML).
3. Claude publie via `scripts/wp_publish.py` (API REST WordPress).
   - Authentification : **mot de passe d'application** WordPress, dans `.env`
     (`WP_SITE_URL`, `WP_USER`, `WP_APP_PASSWORD`). `.env` n'est JAMAIS commité.
   - Par défaut **statut = brouillon** : l'utilisateur relit dans l'admin WP
     avant de publier.
   - Gère articles (`post`) et pages (`page`), avec titre, slug, extrait.

Exemple :
```
python3 scripts/wp_publish.py --type post --title "Titre" --slug titre \
    --content-file /tmp/article.html --status draft
```

## Design system Décupler (charte — à transmettre au freelance)
- Fond : `#07080f` (dark) · Violet : `#7B5CFA` · Vert : `#00E5A0`
- Titres : **Syne** · Corps : **DM Sans** · Univers : dark + violet, épuré.
- Source de vérité : `design-system/tokens.css`.
Le contenu généré doit rester **propre** (HTML sémantique : `h2/h3/p/ul/table…`),
sans CSS inline ni classes Elementor, pour bien s'intégrer au thème du freelance.

## Mémoire du projet — À LIRE au début de chaque session
- `docs/memoire/etat-du-site.md` — ce qui est en ligne (plugins et versions,
  scripts posés dans l'en-tête, sécurité, Search Console). À mettre à jour en fin
  de session.
- `docs/memoire/decisions.md` — ce qui a été tranché, et pourquoi.
- `docs/memoire/lecons.md` — les pièges techniques déjà payés (wpautop,
  Elementor, Chromium, Search Console…).
- `docs/memoire/plan.md` — la suite, dans l'ordre.
- Base Notion « Cartographie SEO » (97c5e3eaa05b4d0aa2277004a93971f6) : une
  ligne par page (mot-clé, prompt principal, action, priorité). Accès permanent.

## Structure du repo
Voir `README.md` pour la carte complète. L'essentiel :
- `scripts/` — publication WordPress (`wp_publish.py`), inventaire des pages
  publiées (`inventaire.py`, régénère `content/cleaned/inventory.md`), assemblage des pages
  (`build_article.py`), Search Console (`gsc.py`), rendu réel (`rendu/`).
- `.claude/skills/` — une méthode par tâche : `lead-magnet` (v2),
  `pages-pourries`, `trio-semantique`, `decupler-page-ville-seo`,
  `decupler-direction-artistique`, `gsc-*`, `redaction-*`…
- `wordpress/plugins/` — plugins maison versionnés et testés (`wordpress/tests/`).
- `content/` — contenus ; `content/lead-magnets/ciblage.json` pour le ciblage.
- `design-system/` — charte, CSS `.lm-mcp`, snippets autonomes.
- `archives/` — sauvegardes « avant refonte », scripts de l'ancienne migration.
- `.env` / `.env.example` — secrets (WP, GSC, DataForSEO).

## Génération d'images (MCP Gemini)
- Serveur MCP `gemini-images` (`scripts/mcp/gemini_images.py`) → génère des
  images avec **Google Gemini** (« Nano Banana », `gemini-2.5-flash-image`) pour
  illustrer articles/pages (Décupler + sites clients).
- Outil `generate_image` : enregistre un fichier image, puis on le téléverse dans
  WordPress via `scripts/wp_upload_media.py`.
- Clé : `GEMINI_API_KEY` dans `.env`. Détails/installation : `scripts/mcp/README.md`.

## Outillage SEO (prévu)
- Google Search Console (script Python, service account — voir `.env`).
- DataForSEO (via MCP ou script).

## Règles techniques
- **NE JAMAIS charger l'export XML WordPress dans la conversation** : il fait
  ~23 Mo (cause de « prompt too long »). Le contenu utile est déjà extrait dans
  `content/cleaned/`.
- Contenu généré = **HTML sémantique propre**, pensé SEO (structure Hn, méta
  description, maillage interne vers les pages existantes : les lister par
  l'API REST WordPress, pas par un inventaire figé).
- Toute modification du site en ligne : **sauvegarde avant**, vérification
  **après** sur le site réel (HTML rendu, miroir Chromium). Les correctifs
  serveur passent par un plugin versionné et testé, jamais par un réglage fait
  à la main sans trace.
- Trio sémantique : une seule Organisation (`https://decupler.com/#organization`)
  et une seule Personne (`https://decupler.com/#nathan-fenina`) ; tout bloc
  JSON-LD y fait référence par `@id`.
- Sécurité WordPress (côté hébergeur/freelance) : minimum de plugins, Wordfence,
  MAJ auto, sauvegardes externes.

## Google Search Console
- `scripts/gsc.py sites | perf | inspect`, sans intermédiaire.
- **Compte de service** (recommandé) : `GSC_SA_JSON` = le contenu entier du
  fichier de clé. Pas d'écran de consentement, pas de jeton qui expire. Il faut
  ajouter le `client_email` de la clé comme utilisateur dans Search Console,
  propriété par propriété.
- **OAuth utilisateur** (alternative) : `GSC_CLIENT_ID`, `GSC_CLIENT_SECRET`,
  `GSC_REFRESH_TOKEN` via `scripts/gsc_auth.py`. Ouvre les 23 propriétés d'un
  coup, mais l'écran de consentement Google est laborieux et le jeton expire
  tous les 7 jours tant que l'app reste en mode test.
- Les secrets vont dans l'environnement — jamais dans le dépôt ni le chat.
