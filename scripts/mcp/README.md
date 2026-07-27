# MCP Gemini — génération d'images

Serveur MCP autonome (`gemini_images.py`) pour générer des images avec **Google
Gemini** (« Nano Banana », `gemini-2.5-flash-image`) directement depuis Claude,
et illustrer nos articles/pages et ceux des sites clients.

- **Zéro dépendance** : uniquement la bibliothèque standard Python 3.9+.
  Aucun `pip`, aucun `venv`, aucune installation réseau.
- Enregistre l'image sur le disque et renvoie son chemin, prêt à téléverser dans
  WordPress via `scripts/wp_upload_media.py`.

## 1. Clé API

1. Récupère une clé sur https://aistudio.google.com/apikey
2. Renseigne-la dans le `.env` du dépôt (jamais commité) :

   ```
   GEMINI_API_KEY=xxxxxxxx
   ```

   Le serveur lit aussi `GOOGLE_API_KEY` / `IMAGE_API_KEY`, et charge
   automatiquement le `.env` à la racine du dépôt.

## 2. Installation

### Dans ce dépôt (automatique)
Le fichier `.mcp.json` à la racine déclare déjà le serveur : ouvre le projet
avec Claude Code et approuve le serveur au premier lancement. Rien d'autre à faire.

### Partout (tous tes projets) — scope utilisateur
```bash
claude mcp add gemini-images -s user -- \
  python3 /chemin/absolu/vers/decupler/scripts/mcp/gemini_images.py
```
Vérifier : `claude mcp list` (doit afficher `gemini-images: … ✓ Connected`).
Retirer : `claude mcp remove gemini-images -s user`.

> Sur une autre machine, adapte le chemin absolu vers `gemini_images.py`.
> La clé est lue depuis l'environnement ou depuis un `.env` — voir plus haut.

### Autres clients MCP (Cursor, Claude Desktop, etc.)
Même principe : commande `python3`, argument = chemin du script, et
`GEMINI_API_KEY` dans l'environnement.

## 3. Utilisation

Deux outils sont exposés :

- **`generate_image`** — génère une image depuis un prompt.
  - `prompt` (obligatoire) : description détaillée.
  - `output_path` (optionnel) : chemin du fichier (défaut : `./generated-images/gemini-<horodatage>.png`).
  - `input_images` (optionnel) : images de référence à éditer / dont s'inspirer.
  - `aspect_ratio` (optionnel) : ex. `16:9`, `1:1`, `3:2`.
  - `model` (optionnel) : défaut `gemini-2.5-flash-image`.
- **`list_models`** — rappelle les modèles disponibles et vérifie la clé.

Exemple de demande à Claude :

> « Génère un visuel de couverture 16:9 pour l'article “Agence GEO”, style dark
> violet/vert Décupler, et enregistre-le dans `content/articles/images/hero.png`. »

Puis, pour publier :
```bash
python3 scripts/wp_upload_media.py --file content/articles/images/hero.png \
  --title "Couverture Agence GEO" --alt "Illustration d'une agence GEO"
```

## Variables d'environnement

| Variable            | Rôle                                   | Défaut                    |
|---------------------|----------------------------------------|---------------------------|
| `GEMINI_API_KEY`    | Clé API (obligatoire)                  | —                         |
| `GEMINI_IMAGE_MODEL`| Modèle par défaut                      | `gemini-2.5-flash-image`  |
| `GEMINI_IMAGE_DIR`  | Dossier de sortie par défaut           | `./generated-images`      |

---

# MCP Yoast SEO — métadonnées WordPress

Serveur MCP autonome (`yoast_seo.py`) pour **lire et écrire les métadonnées Yoast
SEO** des articles et pages WordPress (titre SEO, méta description, requête cible,
canonical, indexation, Open Graph) — sans passer par l'admin WP.

- **Zéro dépendance** (bibliothèque standard Python).
- Réutilise les identifiants WordPress du `.env` (les mêmes que `wp_publish.py`) :
  `WP_SITE_URL`, `WP_USER`, `WP_APP_PASSWORD`.

## Installation
Déjà déclaré dans le `.mcp.json` du dépôt — rien à faire côté Claude Code (juste
approuver au 1er lancement). Aucune clé supplémentaire : il utilise le `.env`.

## Écriture SEO : le mu-plugin (une fois)
WordPress **protège** les métadonnées Yoast (préfixe `_`) : la **lecture**
(`get_seo`) marche telle quelle, mais l'**écriture** (`set_seo`) est ignorée tant
que le site n'autorise pas ces champs via REST.

→ Une seule action côté site, à confier au freelance : déposer le fichier
`wordpress/decupler-yoast-rest.php` dans **`wp-content/mu-plugins/`** (créer le
dossier si besoin). C'est un « must-use plugin » : actif automatiquement, sûr
(écriture réservée aux utilisateurs pouvant éditer les contenus), rien à activer.

Sans ce plugin, `set_seo` te préviendra clairement que les champs ont été ignorés.

## Outils
- **`find_content`** — cherche un article/page (mot-clé, slug), brouillons inclus → renvoie les IDs.
- **`get_seo`** — lit les métadonnées Yoast d'un contenu (`id` ou `slug`).
- **`set_seo`** — écrit : `seo_title`, `meta_description`, `focus_keyphrase`,
  `canonical`, `noindex`, `nofollow`, `og_title`, `og_description`, `og_image`,
  `twitter_title`, `twitter_description`.

Exemple de demande à Claude :

> « Trouve la page “agence GEO”, mets le titre SEO “Agence GEO : … | Décupler”,
> la méta description à ~155 caractères et la requête cible “agence GEO”. »
