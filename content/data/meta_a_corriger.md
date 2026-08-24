# Méta descriptions — état au 24 août 2026

## Ce qui a été fait

68 extraits écrits via l'API REST (`scripts/wp_meta_desc.py`, source :
`content/data/meta_descriptions.py`), 110–160 caractères, rédigés à partir du
contenu réel de chaque page.

7 pages laissées sans description, parce qu'elles n'ont pas vocation à être
indexées : `panier`, `mon-compte`, `commander`, `confirmation-de-rdv`,
`decupler-2` (ancienne HP), `homepage` (doublon), `boutique` (archive
WooCommerce sans contenu propre).

## Ce que ça change vraiment

Le modèle Yoast `%%excerpt%%` n'est qu'un **repli** : une méta description
saisie page par page dans Yoast l'emporte toujours sur l'extrait.

- **20 pages** n'avaient rien dans Yoast → elles servent désormais l'extrait.
  Avant, Yoast fabriquait une description automatique à partir du haut de page,
  qui commençait par le chrome du hero (« Étude de cas · SEA Étude de Cas SEA
  Serrurerie : … », « Adresse : 132 Avenue Lanterne… »).
- **48 pages** ont déjà une méta description saisie dans Yoast. L'extrait y est
  écrit mais reste inerte tant que le champ Yoast n'est pas vidé.

## Les 6 champs Yoast à vider (Yoast SEO → Outils → Éditeur en masse)

Vider le champ suffit : l'extrait déjà en place prend le relais.

| Page | Méta actuellement servie | Problème |
|---|---|---|
| `/wordpress-mcp-plugin/` | « Identifie où tes concurrents te battent sur ChatGPT… 8 sections, 13 étapes, Google Sheet inclus. » | Copie mot pour mot de `/matrice-gap-geo/`. Ne parle pas du plugin. |
| `/claude-code-seo-os/` | « Identifie où tes concurrents te battent sur ChatGPT… Framework GEO en 8 sections… » | Même texte, autre fin. Ne parle pas du SEO OS. |
| `/audit-geo-claude-code/` | « Notre équipe SEO & GEO optimise votre visibilité… » | Copie mot pour mot de `/seo-geo-team/`. Description d'agence sur un tutoriel. |
| `/newsletter/` | « Découvrez notre newsletter. » | 27 caractères. |
| `/bootcamp-geo/` | « 2 jours intensifs + SEO AI Systems offert 1 an » | Contredit la page : 1 mois en cohorte, 16 h de live, 12 places. |
| `/reddit-pour-les-llms/` | « Découvrez les discussions Reddit dédiées aux LLMs… » | Décrit Reddit, pas la méthode vendue sur la page. |

## À arbitrer

`/agence-seo/` sert « Agence SEO à Nice et Côte d'Azur » alors que la page est
nationale et qu'une page `/agence-seo-nice/` existe. Les deux se positionnent
sur la même intention locale.
