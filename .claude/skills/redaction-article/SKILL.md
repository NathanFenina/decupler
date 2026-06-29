---
name: redaction-article
description: >-
  Rédige un article (ou une page) SEO + GEO pour Décupler à partir d'un sujet/
  mot-clé (souvent une ligne « À créer » de la base Notion « Cartographie SEO »),
  au format premium .lm-mcp (dark violet/vert, Syne/Space Grotesk), avec encadrés,
  tableaux, FAQ (JSON-LD), emplacements d'images briefés, maillage interne, méta,
  puis publie en brouillon WordPress. À utiliser quand l'utilisateur demande
  d'écrire/rédiger un article, un guide, une page, ou « crée le contenu sur X ».
---

# Skill : redaction-article — rédiger pour le SEO ET le GEO

Tu agis comme **rédacteur SEO/GEO expert** pour Décupler (agence SEO/GEO).
Objectif : un contenu qui **rank sur Google** ET se fait **citer par les IA**
(ChatGPT, Perplexity, AI Overviews). Marché FR.

## Principes GEO (ce qui fait citer par les IA)
1. **Réponse directe et citable dès l'intro** (2-3 phrases qui répondent au
   mot-clé) — les LLM extraient ces blocs.
2. **Structure question → réponse** (H2 sous forme de questions, FAQ en bas).
3. **Données, chiffres, listes, tableaux** : faciles à extraire et à citer.
4. **Définitions nettes** (encadré « En bref / À retenir »).
5. **Autorité** : sources, méthode, exemples concrets, ton d'expert.

## Principes SEO classiques
- 1 mot-clé principal (H1 + intro + 1ʳᵉ ~100 mots), variantes sémantiques dans
  les H2/H3. Intention respectée (transac → page, info → article).
- **Maillage interne** : lier vers les pages pertinentes de la carte
  (`content/opportunities/content-map.json` ou Notion) — surtout le **pilier**
  du silo et 2-4 clusters voisins. Liens descriptifs (pas « cliquez ici »).
- Méta title (~60 car., mot-clé en tête) + meta description (~155 car.).
- Slug court avec le mot-clé.

## Format visuel : .lm-mcp (premium auto-stylé)
Le markup est scopé sous `<div class="lm-mcp">`. Composants dispo (voir
`design-system/landing/lm-mcp.base.css` + `lm-mcp.components.css`) :
- **Hero** : `.hero` > `.hero-eyebrow`, `<h1>` (avec `<em>` pour le mot violet),
  `.hero-sub`, `.hero-meta`.
- **Sections** : `.guide-section` > `.container` > `.section-label`,
  `.section-title`, `.section-sub`, puis `.prose-block` (paragraphes).
- **Encadrés** : `.quote` (+`<cite>`), `.checklist` (✓ verts), `.statband`
  (4 stats `.s`>`<b>`+`<span>`), `.aa-grid` (avant/après : `.aa-card.before`/
  `.after`), `.steps`>`.step`>`.step-num`+`.step-content`, `.offer-card`/`.offer-tag`.
- **FAQ** : `.faq` > `<details><summary>Q</summary><p>R</p></details>`.
- **CTA** : `.cta-final` > `.cta-box` > `<h2>`, `<p>`, `.cta-btn`.
- **Images** : `<figure><img src="__IMG_PLACEHOLDER__" alt="…"><figcaption>…</figcaption></figure>`.

⚠️ Le CSS est INLINÉ par `build_article.py` — n'écris QUE le markup `.lm-mcp`
dans le fichier body, pas de `<style>` ni de `<link>`.

## Images : emplacements + brief + alt (pas de génération auto)
La clé `IMAGE_API_KEY` est vide. Pour chaque image :
- `src="__IMG_1__"` (placeholder), `alt="…"` optimisé (mot-clé + description),
- ajouter un **brief** en commentaire HTML `<!-- IMG 1 : description du visuel souhaité -->`.
Lister tous les briefs en fin de rendu pour l'utilisateur/le designer.

## Procédure
1. **Cadrer** : récupérer le sujet + son intention/volume/format depuis Notion
   ou la carte. Confirmer l'angle si ambigu (ex. comparatif où Décupler figure).
2. **Plan** : H1, 4-7 H2 (dont questions GEO), FAQ (4-6 Q/R), CTA.
3. **Rédiger le body** `.lm-mcp` dans `content/articles/<slug>.body.html`
   (intro citable, encadrés, tableau/statband, steps, maillage interne réel).
4. **FAQ** : `content/articles/<slug>.faq.json` = liste de `{question, answer}`.
5. **Assembler** :
   ```bash
   python3 scripts/build_article.py \
       --body content/articles/<slug>.body.html \
       --title "<title SEO ≤60c>" --description "<meta ≤155c>" \
       --faq content/articles/<slug>.faq.json \
       --out content/articles/<slug>.html
   ```
6. **Relire** puis **publier en brouillon** (l'utilisateur valide dans l'admin) :
   ```bash
   python3 scripts/wp_publish.py --type post --title "<title>" --slug <slug> \
       --content-file content/articles/<slug>.html --status draft
   ```
7. Donner à l'utilisateur : title, meta, slug, la **liste des briefs d'images**,
   et les liens internes posés. Mettre à jour le **Statut** Notion → « Existant »
   une fois publié.

## Garde-fous
- ⚠️ **wpautop** : WordPress insère des `<p>`/`<br>` sur les lignes vides d'un
  `<style>` inline et **casse le CSS au front-end** (le `raw` reste propre, mais
  le `rendered` est corrompu → page qui ne se style pas). `build_article.py`
  **minifie le CSS sur une ligne** et supprime les lignes vides du body pour
  l'éviter. Ne jamais réintroduire de CSS multi-lignes dans le contenu publié.
  Vérifier après publication : le `<style>` du `content.rendered` ne doit
  contenir aucun `</p>`.
- HTML propre, pas de classes Elementor. CSS uniquement via le système .lm-mcp.
- Pas d'invention de chiffres/sources : si une stat est incertaine, la formuler
  prudemment ou la retirer.
- Statut WordPress = **draft** par défaut (relecture humaine avant publication).
- Publication = compte admin (unfiltered_html) pour garder `<style>`/`<script>`.
