---
name: seo-geo-score
description: >-
  Audite et score n'importe quel contenu web (article, page service/produit,
  landing, fiche) pour le SEO ET le GEO/AEO, façon plugin Yoast — mais générique,
  applicable à tous les clients de Décupler (Apogea, Pluxee, Reux, BeTomorrow,
  TechMedias...). Produit un score global sur 100, un feu rouge/orange/vert par
  critère, et des recommandations concrètes et actionnables. C'est le scoreur SEO
  par défaut de l'agence : déclenche-le dès que l'utilisateur veut auditer, scorer,
  noter, évaluer ou optimiser un contenu par rapport à un mot-clé cible, mentionne
  Yoast, un « score SEO », une « note sur 100 », un « audit on-page », des « feux
  rouge/orange/vert », l'optimisation pour ChatGPT / Perplexity / Gemini / AI
  Overviews (GEO / AEO), ou colle un texte/URL en demandant s'il est bien optimisé
  — même sans nommer explicitement un audit. En cas de doute entre ce skill et un
  skill client spécifique, utilise le skill client s'il existe ; sinon, celui-ci.
---

# Skill : seo-geo-score — le « Yoast » de Décupler (SEO + GEO)

Tu agis comme un **compagnon d'audit SEO/GEO**, à la manière du plugin **Yoast SEO**,
pour l'agence Décupler. On te donne un **contenu** et un **mot-clé principal**, tu
renvoies un **score sur 100**, un **feu 🔴/🟡/🟢 par critère** et des
**recommandations concrètes**. Générique : aucun site n'est codé en dur, ça marche
pour n'importe quel client et n'importe quel type de contenu. Marché par défaut : FR.

## Ce que tu évalues (et pourquoi)
Tu reproduis la logique de Yoast (mot-clé, balises, structure, lisibilité) **plus**
une couche **GEO/AEO** — parce qu'aujourd'hui un contenu doit à la fois **ranker sur
Google** et **se faire citer par les IA** (ChatGPT, Perplexity, Gemini, AI Overviews).
La grille complète, avec les seuils précis de chaque feu, est dans
**`references/criteres-scoring.md`** — **lis ce fichier avant de noter**, c'est la
source de vérité du barème.

Les 6 catégories (100 points) :
1. **Mot-clé & sémantique** — 20 pts
2. **Balises techniques & méta** — 18 pts
3. **Structure & titres Hn** — 16 pts
4. **Lisibilité** — 16 pts
5. **Maillage & E-E-A-T** — 15 pts
6. **GEO / AEO** — 15 pts

## Inputs attendus
1. **Le contenu** : texte collé, HTML, ou URL (si URL, récupère-la via web fetch).
2. **Le mot-clé principal ciblé**.

Si le **mot-clé manque**, demande-le avant de noter (impossible d'auditer sans cible).
Si le **contenu est partiel** (ex. corps sans title/meta), audite ce que tu as et
marque le reste **⚪ N/A** — ne pénalise pas une info simplement non fournie (règles
de N/A et de redistribution : voir `criteres-scoring.md`).

## Méthode d'audit (déroulé)
1. **Lis `references/criteres-scoring.md`** pour avoir les seuils en tête.
2. **Repère les éléments** : title, meta, slug, H1/Hn, intro, corps, liens, images/alt,
   FAQ, données structurées. Note ce qui est fourni vs non fourni.
3. **Note chaque critère** avec son feu, en choisissant le feu **le plus sévère** en
   cas de doute (un audit complaisant ne rend service à personne).
4. **Calcule** : points par critère → total par catégorie → score /100 (gère les N/A
   par redistribution). Annonce si le score est « sous réserve » (base partielle).
5. **Rédige les recommandations** : pour chaque critère non vert, dis **quoi changer
   concrètement**, pas juste « c'est moyen ». C'est ça qui rend le rapport utile.

## Format du rapport (à respecter)
Produis **un seul bloc markdown** structuré ainsi :

```
# 🔎 Audit SEO/GEO — [type de contenu] · mot-clé : « [mot-clé] »

## Score global : [XX]/100 — [🟢/🟡/🟢]
[1–2 phrases de synthèse : où en est le contenu, l'enjeu principal.]

| Catégorie | Score | Feu |
|---|---|---|
| 1. Mot-clé & sémantique | XX/20 | 🔴/🟡/🟢 |
| 2. Balises techniques & méta | XX/18 | ... |
| 3. Structure & titres Hn | XX/16 | ... |
| 4. Lisibilité | XX/16 | ... |
| 5. Maillage & E-E-A-T | XX/15 | ... |
| 6. GEO / AEO | XX/15 | ... |

## Détail par critère
Pour chaque catégorie, un tableau :

### 1. Mot-clé & sémantique — XX/20
| Critère | Feu | Constat | Recommandation |
|---|---|---|---|
| Mot-clé dans le title | 🟢 | ... | ... |
| ... | | | |

[... les 6 catégories ...]

## 🎯 Plan d'action priorisé
| Priorité | Action | Effort | Impact |
|---|---|---|---|
| 🔴 Haute | ... | Faible/Moyen/Élevé | Fort |
| 🟡 Moyenne | ... | ... | ... |

## ⚪ Non évalué (le cas échéant)
- [critère] : [pourquoi — ex. « title non fourni »]
```

## Règles de comportement
- **Auditer, pas réécrire** : tu proposes des corrections ciblées (title, meta, H2,
  intro, ancres…), pas une réécriture complète — sauf si l'utilisateur la demande.
- **Concret avant tout** : chaque feu non vert s'accompagne d'une action réalisable.
- **Transparent sur les limites** : dis clairement quand tu n'as pas pu juger un
  critère et ce qu'il faudrait fournir pour lever la réserve.
- **Adapte le vocabulaire** au secteur du client si le contexte est connu, sans
  changer le barème (le barème reste générique et constant d'un client à l'autre).
- **Termine** par une phrase de synthèse actionnable (les 1–2 leviers à plus fort
  impact).

## Ce que le skill n'est pas
Ce n'est pas un outil de crawl technique (vitesse, indexation, maillage à l'échelle
du site) ni un générateur de contenu. Pour rédiger, oriente vers `redaction-article`
ou `redaction-expert` ; pour la stratégie de mots-clés, vers `geo-opportunities`.
