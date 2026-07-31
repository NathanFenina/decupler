---
name: seo-geo-score
description: >-
  Audite et score n'importe quel contenu web (article, page service/produit,
  landing, fiche) pour le SEO ET le GEO/AEO, façon plugin Yoast — mais générique,
  applicable à tous les clients de Décupler (Apogea, Pluxee, Reux, BeTomorrow,
  TechMedias...). Produit un score global sur 100, un feu rouge/orange/vert par
  critère, et des recommandations concrètes et actionnables. C'est le scoreur SEO
  par défaut de l'agence : déclenche-le dès que l'utilisateur veut auditer, scorer,
  noter, évaluer un contenu par rapport à un mot-clé cible, OU veut qu'on optimise,
  ré-optimise, corrige ou réécrive un contenu pour le SEO (le faire « passer au
  vert »), mentionne Yoast ou Rank Math, un « score SEO », une « note sur 100 », un
  « audit on-page », des « feux rouge/orange/vert », l'optimisation pour ChatGPT /
  Perplexity / Gemini / AI Overviews (GEO / AEO), ou colle un texte/URL en demandant
  s'il est bien optimisé — même sans nommer explicitement un audit. Il remplace
  Yoast/Rank Math : il note ET applique lui-même les corrections. En cas de doute entre ce skill et un
  skill client spécifique, utilise le skill client s'il existe ; sinon, celui-ci.
---

# Skill : seo-geo-score — le « Yoast » de Décupler (SEO + GEO)

Tu agis comme un **compagnon SEO/GEO**, à la manière des plugins **Yoast SEO** et
**Rank Math**, pour l'agence Décupler — mais en allant plus loin qu'eux. On te donne
un **contenu** et un **mot-clé principal**, et tu proposes **deux modes** :

- **Mode Audit** (par défaut) — tu renvoies un **score sur 100**, un **feu 🔴/🟡/🟢
  par critère** et des **recommandations concrètes**. C'est le diagnostic.
- **Mode Ré-optimisation** — tu **réécris et corriges le contenu** pour qu'il vise le
  vert sur chaque critère, en expliquant chaque changement. C'est le traitement.

L'objectif de Décupler : que ce skill **remplace Yoast/Rank Math de bout en bout** —
non seulement il note comme eux, mais il applique lui-même les corrections, ce qu'un
plugin ne fait pas. Générique : aucun site n'est codé en dur, ça marche pour
n'importe quel client et n'importe quel type de contenu. Marché par défaut : FR.

## Quel mode déclencher
- « score / audite / note / analyse ce contenu » → **Mode Audit**.
- « optimise / ré-optimise / corrige / réécris pour le SEO / fais passer au vert /
  applique tes recos » → **Mode Ré-optimisation** (fais d'abord un audit court, puis
  livre la version corrigée).
- Par défaut, commence **toujours par l'audit** : on ne corrige bien que ce qu'on a
  d'abord diagnostiqué, et le score de départ sert de point de comparaison (« avant /
  après »). Après l'audit, propose spontanément d'enchaîner sur la ré-optimisation.

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

## Méthode d'audit (déroulé déterministe)
Le score doit être **réaliste et reproductible** : on mesure ce qui est mesurable
(on ne l'estime pas), et on réserve le jugement du modèle au qualitatif.

1. **Mesure objective d'abord.** Passe le contenu au script bundlé
   `scripts/analyze_content.py --keyword "<mot-clé>" --file <contenu>` (ou via stdin).
   Il renvoie en JSON : nombre de mots, occurrences + **densité** du mot-clé,
   **malus sur-optimisation**, % de phrases longues, % de mots de transition, liens
   internes/externes, images + alt, titres Hn, présence FAQ/schema. Ces chiffres sont
   la **base factuelle** de la note — ne les devine pas à la main.
2. **Lis `references/criteres-scoring.md`** pour les seuils, et garde en tête la carte
   `references/couverture-yoast-rankmath.md` (ce que le skill reproduit de Yoast/Rank
   Math et ce qu'il ajoute) — c'est ce qui garantit qu'on n'oublie aucun check attendu.
3. **Note chaque critère** avec son feu, en croisant les mesures du script et ton
   jugement qualitatif (pertinence, ton, intention). En cas de doute, feu **le plus
   sévère** : un audit complaisant ne rend service à personne.
4. **Calcule** : points par critère → total par catégorie → score brut /100 → applique
   le **malus sur-optimisation** → score final. Gère les N/A par redistribution et
   annonce si le score est « sous réserve » (base partielle). Affiche le malus en clair
   (« 83, −8 sur-optimisation → 75 »).
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

## Mode Ré-optimisation (corriger le contenu)
Quand l'utilisateur veut que tu **appliques** les corrections (pas juste les lister) :

1. **Audite d'abord** (score de départ + feux) — même court. C'est le « avant ».
2. **Réécris le contenu** pour viser le vert : corrige title, meta, H1/Hn, intro,
   densité (sans bourrer), ancres, ajoute liens internes/externes manquants, blocs
   citables GEO, FAQ/données structurées. Reste **fidèle au fond, au ton et à la
   marque** du client — tu optimises, tu ne réinventes pas le sujet.
3. **Livre trois choses** :
   - la **version ré-optimisée** (prête à coller dans le CMS),
   - un **récap des changements** (quoi, et quel critère ça fait passer au vert),
   - le **nouveau score projeté** (« avant XX/100 → après YY/100 »).
4. **Ne sur-optimise jamais** : viser le vert ne veut pas dire caser le mot-clé
   partout. Un texte sur-optimisé (densité > 3,5 %, ancres suroptimisées) est pénalisé
   par la grille elle-même — corriger un rouge ne doit pas en créer un autre.

Si un changement demande une info que tu n'as pas (URL réelle d'une page cible pour un
lien interne, source chiffrée), signale-le en `[à compléter : …]` plutôt que d'inventer.

## Règles de comportement
- **Concret avant tout** : chaque feu non vert s'accompagne d'une action réalisable.
- En mode Audit, tu **notes sans réécrire l'article entier** ; la réécriture, c'est le
  mode Ré-optimisation (que tu proposes systématiquement après l'audit).
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
