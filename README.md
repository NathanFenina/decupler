# Décupler — Atelier contenu & SEO (Claude Code → WordPress)

Ce dépôt est l'**atelier de contenu** du site WordPress de Décupler. On l'utilise
avec **Claude Code** pour **générer des pages/articles et les publier directement
dans WordPress** via l'API REST, + outillage SEO.

> ⚠️ Ce projet **ne contient pas le thème** WordPress (géré ailleurs) et n'a plus
> rien à voir avec Next.js. Voir `CLAUDE.md` pour le contexte complet.

## Prérequis
- **Claude Code** (CLI ou extension VS Code)
- **Python 3** + dépendances : `pip install beautifulsoup4 markdownify`
- Un compte **administrateur** sur le WordPress Décupler

## Installation (pour un nouveau collaborateur)
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/NathanFenina/decupler.git
   cd decupler
   ```
2. Créer son fichier de secrets **`.env`** (jamais commité) :
   ```bash
   cp .env.example .env
   ```
3. Dans WordPress → **Utilisateurs → ton profil → Mots de passe d'application**,
   créer un mot de passe (nom : `Claude Code`) et le coller dans `.env` :
   ```
   WP_SITE_URL=https://decupler.com
   WP_USER=ton-identifiant
   WP_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx xxxx
   ```
   👉 Chaque personne a **son propre** mot de passe d'application (révocable).

## Workflow : créer et publier du contenu
1. Demander à Claude : « écris-moi une page/un article sur X ».
2. Claude rédige le HTML (design system `.lm-mcp`, voir `design-system/landing/`).
3. Publication (par défaut en **brouillon**, on relit dans l'admin avant mise en ligne) :
   ```bash
   python3 scripts/wp_publish.py --type page \
     --title "Mon titre" --slug mon-titre \
     --content-file /tmp/page.html --status draft
   ```
   Options : `--type post|page`, `--id <id>` (mettre à jour), `--status draft|publish`.

## Structure du dépôt
    scripts/wp_publish.py        → publication WordPress (API REST)  ← cœur
    scripts/parse_wxr.py         → extraction de l'ancien export XML (référence)
    scripts/clean_content.py     → nettoyage HTML → MDX (référence)
    design-system/tokens.css     → charte (couleurs, polices)
    design-system/landing/       → CSS réutilisable des landing pages (.lm-mcp)
    content/pages-publiees/      → pages publiées (HTML de référence)
    docs/                        → historique migration, notes
    CLAUDE.md                    → contexte & règles du projet (À LIRE)

## Design system des pages
Fond `#07070e` · Violet `#6366f1` · Vert `#10b981` · Titres **Syne** · Corps
**Space Grotesk**. Système de composants `.lm-mcp` dans `design-system/landing/`.
Exemple complet de page : `content/pages-publiees/ahrefs-contenu-ia-assez-bon.html`.

## Sécurité
- `.env` (mots de passe) est **gitignored** — ne jamais le committer.
- Mots de passe d'application **révocables** depuis WordPress à tout moment.
