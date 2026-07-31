# Grille de scoring — seo-geo-score

Référence de notation du skill. Le **score global est sur 100 points**, réparti
sur **6 catégories**. Chaque **critère** reçoit un feu :

- 🟢 **Vert** = critère respecté → **100 % des points** du critère.
- 🟡 **Orange** = partiellement respecté / améliorable → **50 % des points** (arrondi au supérieur).
- 🔴 **Rouge** = problème → **0 point**.
- ⚪ **N/A** = non applicable au type de contenu → le critère est **retiré du total**,
  et les points sont **redistribués au prorata** dans sa catégorie (voir plus bas).

Le total de la catégorie = somme des points de ses critères. Le score global = somme
des 6 catégories, arrondi à l'entier.

## Table des matières
- [Comment noter un critère](#comment-noter-un-critère)
- [Bandes de score global](#bandes-de-score-global)
- [Catégorie 1 — Mot-clé & sémantique (20 pts)](#catégorie-1--mot-clé--sémantique-20-pts)
- [Catégorie 2 — Balises techniques & méta (18 pts)](#catégorie-2--balises-techniques--méta-18-pts)
- [Catégorie 3 — Structure & titres Hn (16 pts)](#catégorie-3--structure--titres-hn-16-pts)
- [Catégorie 4 — Lisibilité (16 pts)](#catégorie-4--lisibilité-16-pts)
- [Catégorie 5 — Maillage & E-E-A-T (15 pts)](#catégorie-5--maillage--e-e-a-t-15-pts)
- [Catégorie 6 — GEO / AEO (15 pts)](#catégorie-6--geo--aeo-15-pts)
- [Gérer le N/A et les infos manquantes](#gérer-le-na-et-les-infos-manquantes)

---

## Comment noter un critère

Pour chaque critère, applique le seuil décrit dans les colonnes 🟢 / 🟡 / 🔴.
Quand tu hésites entre deux feux, choisis le **plus sévère** — un audit qui
flatte ne sert à personne. Chaque critère porte aussi une **recommandation
concrète** dès qu'il n'est pas vert : quoi changer, pas juste « c'est moyen ».

Le raisonnement derrière la grille : elle reproduit la logique du plugin **Yoast**
(présence du mot-clé, balises, lisibilité) et y ajoute une couche **GEO/AEO** —
parce que se faire citer par ChatGPT, Perplexity ou les AI Overviews demande des
signaux que Yoast n'évalue pas (réponse directe extractible, structure Q→R,
faits chiffrés, clarté des entités).

---

## Bandes de score global

| Score /100 | Feu | Interprétation |
|---|---|---|
| **80–100** | 🟢 | Bien optimisé. Prêt à publier ou ajustements mineurs. |
| **55–79** | 🟡 | Correct mais des optimisations importantes restent à faire. |
| **0–54** | 🔴 | Sous-optimisé. Retravail nécessaire avant de viser un bon ranking. |

Ces bandes sont un point de départ ; elles font partie de ce qu'on **calibre**
contre le jugement humain.

### Malus « sur-optimisation » (appliqué au score global)

La densité du mot-clé est déjà un critère (catégorie 1), mais un critère à 3 points
ne reflète pas la réalité : quand un mot-clé exact revient 20 fois, un SEO humain
voit un contenu **globalement dégradé**, pas juste « un point en moins ». Le bourrage
nuit à la lisibilité, au naturel et à la confiance — donc il doit peser sur **tout**
le score, comme le font Yoast et Rank Math qui affichent un avertissement rouge franc.

Après avoir calculé le score global, applique ce **malus** selon la densité du
mot-clé exact (occurrences × longueur du mot-clé / nombre total de mots) :

| Densité du mot-clé exact | Malus global |
|---|---|
| ≤ 3,5 % | 0 (rien à retirer) |
| 3,5 % – 5 % | **−5** |
| 5 % – 6,5 % | **−8** |
| > 6,5 % | **−12** |

Exemple réel : une page à **83/100** avec « content marketing » à **6,23 %** →
malus −8 → **75/100**. C'est bien plus proche du ressenti d'un SEO qui voit le
mot-clé répété à chaque phrase. Signale toujours le malus dans le rapport
(« score 83, −8 sur-optimisation → **75/100** ») pour que la correction soit lisible.

---

## Catégorie 1 — Mot-clé & sémantique (20 pts)

Le cœur de l'analyse Yoast : le mot-clé principal doit être présent aux endroits
qui comptent, sans sur-optimisation.

| Critère | Pts | 🟢 Vert | 🟡 Orange | 🔴 Rouge |
|---|---|---|---|---|
| Mot-clé dans le **title** (balise SEO) | 3 | Présent, idéalement en début | Présent mais noyé en fin | Absent |
| Mot-clé dans le **H1** | 3 | Présent (exact ou proche) | Variante seulement | Absent |
| Mot-clé dans l'**intro** (100 premiers mots) | 3 | Présent naturellement | Présent au-delà de 100 mots | Absent de tout le début |
| Mot-clé dans la **meta description** | 2 | Présent | Variante | Absent |
| Mot-clé dans **≥ 1 sous-titre** (H2/H3) | 2 | Oui, naturel | Variante lointaine | Aucun sous-titre ne le porte |
| Mot-clé dans l'**URL / slug** | 2 | Présent, slug propre | Partiel | Absent |
| **Densité** du mot-clé | 3 | 0,5 – 2,5 % (idéal ~1–1,5 %) | 2,5 – 3,5 % ou 0,3 – 0,5 % | > 3,5 % (bourrage) ou ~0 % |
| **Champ sémantique** / variantes | 2 | Nombreux termes liés & synonymes | Quelques-uns | Répétition du seul mot-clé exact |

**Notes de calcul :**
- Densité = (occurrences du mot-clé exact + variantes proches) / nombre total de mots.
- « Bourrage » (> 3,5 %) est pénalisé aussi durement que l'absence : Google et les
  IA lisent la sur-optimisation comme un signal de spam.

---

## Catégorie 2 — Balises techniques & méta (18 pts)

Ici on juge la **qualité technique** des balises, indépendamment du mot-clé
(qui est déjà couvert en catégorie 1).

| Critère | Pts | 🟢 Vert | 🟡 Orange | 🔴 Rouge |
|---|---|---|---|---|
| Longueur du **title** | 4 | 50–60 caractères | 40–49 ou 61–65 | < 40, > 65, ou absent |
| **Meta description** | 4 | 120–156 car., incitative (verbe d'action) | 100–119 / 157–170, ou plate | < 100, > 170, ou absente |
| **Slug / URL** | 3 | Court, minuscules, tirets, sans stop-words | Correct mais long ou avec petits mots | Illisible, majuscules, underscores, paramètres |
| **Balises `alt`** des images | 4 | Toutes les images ont un alt descriptif | Alt partiels ou génériques | Alt absents (ou aucune image sur un contenu qui en aurait besoin) |
| **Données structurées** (schema.org) | 3 | Article/FAQ/Breadcrumb ou équivalent présent | Balisage minimal | Aucun balisage |

**Note :** si le contenu fourni ne montre pas le title/meta/slug (ex. on ne t'a
collé que le corps), ne devine pas : marque le critère **N/A** et signale à
l'utilisateur qu'il faut fournir ces éléments pour une note fiable (voir section
N/A). Ne mets pas 🔴 pour une info simplement absente de ce qui t'a été fourni.

---

## Catégorie 3 — Structure & titres Hn (16 pts)

| Critère | Pts | 🟢 Vert | 🟡 Orange | 🔴 Rouge |
|---|---|---|---|---|
| **H1 unique** et présent | 3 | Exactement un H1, clair | H1 présent mais dupliqué/flou | Aucun H1 ou plusieurs H1 |
| **Hiérarchie Hn** logique | 3 | Pas de saut de niveau (H2→H3→…) | 1 saut mineur | Structure incohérente (H2→H4, titres décoratifs) |
| **Fréquence des sous-titres** | 3 | Un H2/H3 tous les ~300 mots | Quelques blocs longs sans titre | Longs pavés (> 500 mots) sans sous-titre |
| **Longueur du contenu** vs intention | 4 | Adaptée (info/transactionnel) et couvre le sujet | Un peu court/long | Beaucoup trop court pour le sujet ou délayé |
| **Éléments scannables** (listes, tableaux, gras) | 3 | Présents et utiles | Rares | Bloc de texte massif sans respiration visuelle |

**Repères de longueur (indicatifs, à ajuster selon l'intention) :** article de
blog informationnel 800–2000 mots ; page service/produit 400–1000 mots ; landing
courte possible si l'intention est transactionnelle. Ne pas fétichiser le nombre
de mots : un contenu court qui répond parfaitement à l'intention vaut mieux qu'un
long délayé.

---

## Catégorie 4 — Lisibilité (16 pts)

Reproduit l'analyse de lisibilité de Yoast, adaptée au français.

| Critère | Pts | 🟢 Vert | 🟡 Orange | 🔴 Rouge |
|---|---|---|---|---|
| **Longueur des phrases** | 4 | Majorité ≤ 20 mots | 25 % à 35 % de phrases > 20 mots | > 35 % de phrases longues |
| **Longueur des paragraphes** | 4 | ≤ 4 lignes / ~150 mots | Quelques paragraphes longs | Pavés > 200 mots récurrents |
| **Mots de transition** | 3 | Présents (≥ ~30 % des phrases) | Quelques-uns | Quasi absents (texte haché) |
| **Voix passive** | 2 | < 10 % des phrases | 10–20 % | > 20 % |
| **Clarté / jargon** | 3 | Langage clair, jargon expliqué | Un peu technique sans explication | Jargon dense, phrases alambiquées |

**Note français :** les indices type Flesch sont calés sur l'anglais ; utilise-les
comme indice, pas comme vérité. Le vrai juge, c'est : « un lecteur pressé
comprend-il en diagonale ? »

---

## Catégorie 5 — Maillage & E-E-A-T (15 pts)

Liens + signaux d'expertise/autorité/fiabilité (Experience, Expertise,
Authoritativeness, Trust).

| Critère | Pts | 🟢 Vert | 🟡 Orange | 🔴 Rouge |
|---|---|---|---|---|
| **Liens internes** pertinents | 4 | ≥ 3 liens internes utiles | 1–2 | Aucun |
| **Liens externes** d'autorité | 2 | ≥ 1 source externe crédible | Lien externe faible/non pertinent | Aucun |
| **Textes d'ancrage** descriptifs | 2 | Ancres explicites | Mélange | « cliquez ici », URLs nues |
| **Données chiffrées / sources** | 3 | Chiffres sourcés, faits vérifiables | Quelques affirmations sans source | Zéro donnée, tout est vague |
| **Signaux d'expertise** (auteur, date, expérience concrète) | 2 | Auteur/date/exemples vécus | Partiel | Anonyme, daté, générique |
| **Cohérence avec l'intention** de recherche | 2 | Répond exactement à l'intention du mot-clé | Répond partiellement | Hors-sujet vs intention |

---

## Catégorie 6 — GEO / AEO (15 pts)

La couche qui va au-delà de Yoast : optimiser pour être **cité par les moteurs
IA** (ChatGPT, Perplexity, Gemini, Google AI Overviews). Principe : les LLM
extraient des **blocs de réponse autonomes, factuels et bien identifiés**.

| Critère | Pts | 🟢 Vert | 🟡 Orange | 🔴 Rouge |
|---|---|---|---|---|
| **Réponse directe & citable dès l'intro** | 3 | 2–3 phrases répondent au mot-clé d'emblée | Réponse noyée plus bas | Aucune réponse claire extractible |
| **Structure question → réponse** | 3 | H2 en questions et/ou FAQ dédiée | Quelques formulations Q/R | Aucun format Q/R |
| **Faits extractibles** (chiffres, définitions nettes, listes) | 3 | Nombreux blocs autonomes citables | Quelques-uns | Prose continue sans point d'ancrage |
| **Données structurées FAQ / Q&A** | 2 | JSON-LD FAQ/QAPage présent | Balisage partiel | Aucun |
| **Clarté des entités** | 2 | Sujet, marque, lieux, personnes nommés explicitement | Entités floues par endroits | Références vagues (« notre solution », « la ville ») |
| **Fraîcheur / mise à jour** | 2 | Date récente ou signaux d'actualité | Daté mais encore valable | Périmé, non daté |

---

## Gérer le N/A et les infos manquantes

Le skill s'applique à **tous types de contenus** (article, page service, landing,
fiche produit) et il arrive qu'on te fournisse un contenu **partiel** (ex. juste
le corps, sans le title ni la meta). Deux règles :

1. **Info non fournie ≠ critère raté.** Si tu ne peux pas juger un critère parce
   que l'élément n'a pas été fourni (title, meta, slug, images, balisage), marque-le
   **⚪ N/A** et **liste-le explicitement** dans le rapport (« non évaluable : title
   non fourni »). N'invente pas, et ne mets pas 🔴.

2. **Redistribution.** Quand un critère est N/A, retire ses points du total de sa
   catégorie et **re-normalise** la catégorie sur les critères restants, puis
   ramène le tout sur 100. Exemple : si la catégorie 2 (18 pts) a un critère de
   4 pts en N/A, note les 14 pts restants puis multiplie par 18/14. Signale toujours
   quand un score est calculé sur une base partielle — un score « sous réserve »
   doit être annoncé comme tel.

Un critère **réellement absent** (ex. le title existe mais ne contient pas le
mot-clé, ou il n'y a aucun lien interne alors que le contenu s'y prête) reste 🔴 :
là ce n'est pas une info manquante, c'est une optimisation ratée.
