# scripts/ — Outils du projet

Scripts prévus (créés au fil des phases) :

| Script              | Rôle                                                                 | Phase |
|---------------------|----------------------------------------------------------------------|-------|
| `gsc_audit.py`      | Export Search Console : pages × clics × impressions × position 12 mois (CSV). | 3 |
| `parse_xml.py`      | Parse l'export XML, nettoie le HTML Elementor → `content/cleaned/`.   | 4 |
| `generate_images.py`| Génération d'images en batch (univers dark + violet) + alt texts.    | 4 |
| `import_wp.py`      | Réimport du contenu nettoyé via l'API REST WordPress / WP-CLI.        | 4 |

## Secrets
Les clés API (Search Console service account, DataForSEO, mot de passe d'application WP)
vont dans un fichier `.env` à la racine — JAMAIS commité (voir `.gitignore`).
Un modèle est fourni dans `.env.example`.

## DataForSEO
Branché en **MCP** directement dans Claude Code (pas un script ici) :

    claude mcp add dataforseo -- <commande du serveur MCP officiel>

## Search Console
Via un **service account** Google Cloud (API Search Console activée), clé JSON
référencée dans `.env`. Détails dans `docs/setup-gsc.md` (créé en phase 3).

## Contrôle design (skill `impeccable`)

Installé via `npx skills add github.com/pbakaus/impeccable --skill impeccable`
(le skill lui-même n'est pas commité — `skills-lock.json` permet de le
réinstaller à l'identique ; `npm install` pour les dépendances du détecteur).

Le détecteur d'anti-patterns lit un fichier HTML **avec ses `<style>` inline**,
c'est-à-dire exactement ce que `wp_publish.py` envoie dans `entry_content` :

```
npm run design:check -- content/articles/offre-site-offert.html
```

Il complète `scripts/lib/wpcss.py` (qui vérifie que WordPress ne casse pas le
balisage) : `wpcss` regarde la plomberie, `impeccable` regarde le rendu
(contraste WCAG, tailles de texte, tics visuels d'UI générée).
