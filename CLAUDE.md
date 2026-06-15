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
  le freelance (un seul CSS, charte ci-dessous).
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

## Structure du repo
- `scripts/wp_publish.py` — publication WordPress via API REST (cœur du projet).
- `scripts/parse_wxr.py`, `clean_content.py` — ont servi à extraire l'ancien
  contenu depuis l'export XML (référence ; voir `content/cleaned/`).
- `content/cleaned/` — ancien contenu récupéré + **`seo-meta.json`** (titres/méta
  Yoast d'origine). Utile pour : maillage interne, éviter les doublons, audits.
- `design-system/tokens.css` — la charte.
- `docs/` — historique migration (archive).
- `.env` / `.env.example` — secrets (WP, GSC, DataForSEO).

## Outillage SEO (prévu)
- Google Search Console (script Python, service account — voir `.env`).
- DataForSEO (via MCP ou script).

## Règles techniques
- **NE JAMAIS charger l'export XML WordPress dans la conversation** : il fait
  ~23 Mo (cause de « prompt too long »). Le contenu utile est déjà extrait dans
  `content/cleaned/`.
- Contenu généré = **HTML sémantique propre**, pensé SEO (structure Hn, méta
  description, maillage interne vers les pages existantes listées dans
  `content/cleaned/inventory.md`).
- Sécurité WordPress (côté hébergeur/freelance) : minimum de plugins, Wordfence,
  MAJ auto, sauvegardes externes.
