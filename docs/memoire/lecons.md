# Leçons techniques — les pièges déjà payés

Chaque ligne a coûté au moins une erreur. Les relire avant de toucher au site.

## WordPress et Elementor

- **wpautop** transforme les lignes vides en `<p>` et les éléments en ligne
  isolés sur une ligne en `<br>`/`<p><a>`. Contenu sans ligne vide ; scripts et
  CSS sur une seule ligne ; `<span>`/`<a>` d'un conteneur flex sur une seule
  ligne. Vérifier le HTML **rendu** (`?context=edit` → `rendered`), pas le source.
- **`</p>` orphelin de wpautop** : `<div><span>🔑</span><p>…` produit un `<p>`
  vide qui prend une case de grille ou de flex. Invisible au contrôle par regex,
  visible au navigateur : `scripts/rendu/paragraphes_vides.mjs`. Filet global le
  30/09 : `.lm-mcp p:empty{display:none}` dans l'en-tête 2762.
- Une écriture de `_elementor_data` par l'API est stockée mais **pas affichée**
  tant que le cache d'Elementor n'est pas purgé : le plugin crawl-fix purge à
  chaque changement.
- Pages en gabarit `elementor_canvas` : pas d'en-tête du site, donc aucun
  script de l'en-tête ne s'y exécute.
- Page construite dans Elementor (`_elementor_edit_mode = builder`) : le rendu
  vient de `_elementor_data`, pas de `content` ; modifier les deux.
- Double H1 : le thème Astra ajoute le titre de la page ; métas
  `site-post-title` et `ast-banner-title-visibility` à `disabled`.
- Yoast n'accepte pas `_yoast_wpseo_canonical` par l'API REST (le plugin
  decupler-yoast-rest n'expose que title, metadesc, focuskw).
- Yoast ne publie l'Organisation que si le logo est réglé.
- Politique de mots de passe (Wordfence) : un mot de passe sans symbole est
  refusé par l'API.

## Navigateur et tests

- Chromium ne passe pas le proxy de la session (certificat) : ne jamais
  désactiver la vérification TLS ; passer par `scripts/rendu/miroir.py`
  (curl rapatrie la page, servie en local).
- Horloge simulée de Playwright (`page.clock`) : elle ne fait pas avancer les
  `setTimeout` posés depuis un MutationObserver. Pour ces cas, minuteries réelles.
- La capture pleine page laisse blanches les images `loading="lazy"` hors
  écran : forcer `loading = 'eager'` avant la capture, ou capturer par écran.
- `miroir.py` (corrigé le 29/09) : WordPress écrit ses `<link rel=stylesheet>`
  entre apostrophes, et une CSS enregistrée en `.bin` est ignorée par le
  navigateur. Symptôme : page décalée à gauche, colonne de contenu de largeur 0.
  Avant de conclure à un bug du site, vérifier que le thème (astra main.min.css)
  s'est bien chargé dans la copie.
- Débordement horizontal : chercher l'élément dont le bord droit dépasse la
  fenêtre sans parent en `overflow:hidden`. Le 29/09, c'était le pied de page
  (template Elementor 2788) : `padding` + `width:100%` sans `box-sizing`.
- `pkill -f` ne doit pas correspondre à sa propre commande : `routeur.ph[p]`.
- Firecrawl (compte connecté) peut tomber à court de crédits : lire les README
  GitHub directement (raw.githubusercontent.com) pour vérifier une commande.

## Outils d'audit

- jev-seo (github.com/AgriciDaniel/jev-seo) tourne dans la session :
  `scratchpad/jev/jev-seo`, venv, `REQUESTS_CA_BUNDLE=/root/.ccr/ca-bundle.crt`.
  Sans `TYPESAFE_API_KEY` : audit partiel (pas de jugements Jev) ; sans
  `PAGESPEED_API_KEY` : PageSpeed renvoie 429. Rendre le rapport en images :
  capturer les `<section>` de `report.html` avec Playwright (pas de pdftoppm).
- Une coupure du proxy pendant un crawl produit de faux « liens cassés » en
  masse (30/09 : /organic-opportunity-map « injoignable » sur 56 pages alors
  qu'elle répondait 200). Toujours revérifier une alerte P1 au curl avant de
  corriger.

## Search Console

- Le rapport d'indexation a plusieurs jours de retard ; la vérité page par
  page vient de l'API d'inspection (`scripts/gsc.py inspect`).
- La propriété accessible est `https://decupler.com/` (pas `sc-domain:`).
- Les demandes de suppression masquent ~6 mois ; seule la re-exploration
  (410/404) retire vraiment une URL. « Expirée » = souvent déjà sortie de l'index.
