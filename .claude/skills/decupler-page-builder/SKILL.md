---
name: decupler-page-builder
description: Produit des pages et des articles Décupler prêts à publier dans WordPress — article de blog, page ville, page service. Donne le gabarit selon le type, applique les consignes SEO/GEO maison (mot-clé ×20, maillage contextuel, images, CTA, E-E-A-T), valide automatiquement, puis pousse sans rien casser. À utiliser dès qu'il faut créer ou refondre un contenu sur decupler.com.
---

# Décupler — fabrique de pages et d'articles

Ce skill produit du contenu **publiable en l'état** sur decupler.com. Il ne
donne pas des conseils : il donne un gabarit, des contraintes chiffrées, un
validateur bloquant et un script de publication.

Il complète `decupler-seo-geo-score`, qui note un contenu existant. Ici on en
fabrique un.

## 1. Identifier le type de page

Tout part de là. Les trois types n'ont ni la même structure, ni les mêmes
contraintes, ni les mêmes pièges de publication.

| Le sujet est… | Type | Gabarit | Post type WP |
|---|---|---|---|
| une question, un concept, un « comment faire » | **article** | `references/gabarit-article.md` | `posts` |
| « agence GEO {ville} », un service + une ville | **page ville** | `references/gabarit-page-ville.md` | `pages` |
| une offre commerciale (audit, cartographie…) | **page service** | `references/gabarit-page-service.md` | `pages` |

**Conséquence immédiate, à connaître avant d'écrire :** les champs Yoast
(`_yoast_wpseo_title`, `_metadesc`, `_focuskw`) sont **écrivables par l'API sur
les articles, pas sur les pages**. Pour une page ville ou service, il faut
prévenir Nathan qu'il devra les saisir à la main, et lui fournir les valeurs.

## 2. Les consignes qui s'appliquent aux trois types

Non négociables. Le validateur les fait respecter.

- **Mot-clé exact ≥ 20 fois**, sans dépasser 3,5 % de densité effective
  (au-delà, malus −5 de la grille de scoring).
- **Longueur minimale** :
  `mots = max(1500 ; 20 × nombre_de_mots_du_mot_clé ÷ 0,035)`
  → 2 mots : 1500 · 3 mots : 1715 · 4 mots : 2286.
  C'est le calcul le plus souvent raté. Voir `references/gabarit-article.md`.
- **Mot-clé** dans le slug, le title, le H1, les 100 premiers mots, et au moins
  un H2.
- **H2 formulés comme des prompts** — des questions telles qu'un acheteur les
  pose, pas des étiquettes marketing. C'est la couche GEO.
- **Réponse directe en tête** : les deux premières phrases répondent à la
  question, avant toute mise en contexte.
- **≥ 8 liens internes contextuels**, ancrés dans le fil du texte.
  Jamais de bloc « À découvrir aussi » en pied de page. Voir
  `references/maillage.md`.
- **2 images minimum** : bannière bleue en une + maquette d'écran dans le
  corps, alt contenant le mot-clé.
- **CTA sur chaque bandeau** + sidebar sticky Calendly.
- **Cross-citation Nathan Fenina ↔ Décupler** au moins une fois : c'est le
  levier E-E-A-T maison.
- **FAQ + JSON-LD FAQPage** en bas de contenu.
- **Aucune ligne vide hors CSS**, aucun inline orphelin : wpautop casse tout.
  Voir `references/pieges-plateforme.md`.

## 3. Le déroulé

```
1. Cadrer      → type de page, mot-clé, angle, longueur cible (formule ci-dessus)
2. Écrire      → gabarit du type + assets/blocs.html + assets/article_css.py
3. Valider     → python scripts/validate_page.py --fichier page.html --kw "..." --slug "..."
4. Illustrer   → generate_featured_image.py + generate_screen_image.py
5. Pré-vol     → python scripts/push_wp.py --dry-run
6. Publier     → python scripts/push_wp.py
```

**Ne jamais sauter l'étape 5.** Le push écrase du contenu réel et peut
déprogrammer des articles planifiés.

## 4. Anti-cannibalisation

Dès qu'on produit plusieurs contenus sur des requêtes proches — 16 articles GEO,
8 pages villes — le risque n'est pas la qualité, c'est la redite.

Règle : **un contenu = un angle**, attribué à l'avance et écrit en tête du
fichier de données. Angles déjà utilisés pour la famille « agence » : comment
choisir / ce qu'elle fait / périmètre / mesure / extractibilité. Pour la famille
« ChatGPT » : mécanique de sélection / socle technique / mode opératoire /
suivi / sources tierces.

Le validateur compare les phrases de ≥ 8 mots entre tous les contenus du lot et
bloque au-delà de 3 phrases communes. La sidebar CTA est exclue du calcul,
sinon elle déclenche un faux positif sur tout le lot.

## 5. Références

| Fichier | Quand l'ouvrir |
|---|---|
| `references/gabarit-article.md` | à chaque article |
| `references/gabarit-page-ville.md` | à chaque page ville |
| `references/gabarit-page-service.md` | à chaque page service |
| `references/charte-da.md` | pour tout composant visuel |
| `references/pieges-plateforme.md` | **avant le premier push**, et à chaque bug inexpliqué |
| `references/maillage.md` | pour poser les liens |
| `references/etat-du-site.md` | pour savoir quelles URL existent encore |
| `references/journal.md` | pour comprendre pourquoi une règle existe |

## 6. Scripts

| Script | Rôle |
|---|---|
| `scripts/validate_page.py` | tous les contrôles bloquants |
| `scripts/generate_featured_image.py` | bannière bleue 940×575 |
| `scripts/generate_screen_image.py` | maquette d'écran 16 modèles |
| `scripts/check_urls.py` | régénère l'inventaire des URL vivantes |
| `scripts/push_wp.py` | publication qui préserve statut et programmation |
| `scripts/wp_client.py` | client REST partagé |

Tous lisent le `.env` du projet en **lecture seule**. Ne jamais y écrire.
