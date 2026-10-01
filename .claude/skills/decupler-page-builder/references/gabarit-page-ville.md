# Gabarit — page ville

Post type `pages`. Yoast est désormais **écrivable par l'API** via le mu-plugin
`wordpress/mu-plugins/decupler-yoast-rest.php` (à déposer dans
`wp-content/mu-plugins/`). Sans ce fichier, l'API renvoie 200 et jette
silencieusement les champs : il faut alors repasser par la saisie manuelle.

Requête type : `agence GEO {ville}`. Structure inspirée de junto.fr, adaptée à
la charte Décupler.

---

## 0. Ce que dit la SERP réelle — relevé du 19/09/2026

Mesuré sur `agence seo marseille` (2 400 de volume), via Firecrawl.

| | Jones and Co **#1** | Digimood **#3** | Ce gabarit (avant) |
|---|---|---|---|
| Mots | ~850 | 1 345 | ≥ 1 715 |
| Mot-clé exact | ~5× | 5× | ≥ 20× |
| FAQ | aucune | aucune | 9 questions |
| H2 / H3 | 1 / 3 | 5 / 6 | 12 blocs |
| Codes postaux / communes | non | **oui** | oui |
| Logos + témoignages | non | **oui** | non prévu |
| Chiffres de résultats | non | **oui** | non prévu |
| Adresse physique locale | — | **oui** | non prévu |

**Junto, dont ce gabarit s'inspirait, est 10ᵉ.**

Trois conséquences, appliquées dans `scripts/validate_page.py` :

1. **Ni la longueur ni la densité ne décident** sur ces requêtes. Les seuils
   `page-ville` passent à 6 occurrences et 1 100 mots (contre 20 et 1 715 pour
   les articles, inchangés). Produire 1 900 mots nous rendrait deux fois plus
   longs que la page #1 sans gagner le facteur discriminant.
2. **Le facteur discriminant est la preuve.** Le validateur exige désormais,
   pour `page-ville` : un code postal cité, un JSON-LD `LocalBusiness` **ou**
   `areaServed`, et un lien vers une étude de cas chiffrée. Voir la correction
   du 21/09 ci-dessous : l'adresse locale n'est pas requise.
3. **2 des 8 premiers résultats sont des comparatifs** (« les 15 meilleures
   agences SEO à Marseille »). L'intention est mixte : sur les gros volumes,
   la page d'agence seule ne couvre pas toute la SERP.

**Correction du 21/09/2026 — l'adresse locale n'est pas requise.** Le premier
relevé, fait sur la page Marseille de Digimood (où ils ont un bureau), avait
conclu qu'une adresse locale était le facteur décisif. Vérification sur leur
page Nice (`digimood.com/agence-seo/nice/`) : **610 mots, 6 H2, aucune adresse,
aucun LocalBusiness, aucune FAQ, aucun logo, aucun témoignage**, dernière
modification janvier 2021 — et elle ranke. Leur H1 dit « à proximité de Nice »,
avec une section « Digimood présent en PACA ».

Donc, sur une ville satellite : `areaServed` et un cadrage honnête suffisent.

**Règle absolue : on n'invente jamais d'adresse.** Une adresse fictive en
LocalBusiness est un faux signal local, sanctionné par Google et mensonger
envers le prospect. Une seule adresse réelle (Nice) portée par le schéma
`Organization` du site, et `areaServed` sur chaque page ville.

---

## 1. Contraintes propres au local

- **Mot-clé exact ≥ 6 fois**, densité ~1 %, 1 100 à 1 400 mots (voir §0).
  L'ancienne règle des 20 occurrences reste valable pour les **articles**.
- **Codes postaux** de la ville, cités explicitement dans le texte.
- **Communes limitrophes** : 8 à 12, en grille, dans la section « zone
  d'intervention ». Ce sont elles qui font la profondeur locale.
- **Gentilé** utilisé au moins une fois (Toulousains, Bordelais…).
- **Photo de la ville**, hébergée dans la médiathèque, alt avec le mot-clé.
- **Un CTA sur chaque bandeau**, sans exception.
- **Zéro duplication entre villes** : c'est le point qui fait échouer les pages
  locales. Voir §4.

---

## 2. Structure

Structure d'origine, calibrée `agence GEO {ville}` en 12 blocs. Sur une page
**SEO** ville, viser 1 100-1 400 mots : garder les blocs 1, 2, 3, 7, 10, 11, 12
et traiter 5, 6, 8, 9 en une seule section courte. Chaque bloc en pleine
largeur (`width:100vw`) :

| # | Bloc | Contenu | CTA |
|---|---|---|---|
| 1 | **Hero** | H1 avec le mot-clé, sous-titre, bande de confiance (chiffres réels, attribués à la mission) | oui |
| 2 | **Contexte** | H2 en prompt : « Pourquoi une agence GEO à {ville} ? » — 2-3 paragraphes propres à la ville | — |
| 3 | **Bénéfices** | 6 bénéfices en H3, formulés localement | — |
| 4 | **Bandeau lila** | pourquoi le local compte pour les moteurs + un visuel | oui |
| 5 | **Méthode** | 6 étapes numérotées + visuel | — |
| 6 | **Comparatif** | tableau : agence locale / agence nationale / interne | — |
| 7 | **Zone d'intervention** | codes postaux + grille de communes + photo de la ville | oui |
| 8 | **Secteurs** | 4 secteurs dominants de la ville, nommés | — |
| 9 | **Budget** | fourchettes et ce qui les fait varier | oui |
| 10 | **FAQ** | 4 à 6 questions, dont 2 spécifiquement locales | — |
| 11 | **Bandeau E-E-A-T** | Nathan Fenina, photo, LinkedIn, Calendly | oui |
| 12 | **Bande CTA** | clôture | oui |

Les H2 sont des questions, comme pour les articles.

---

## 3. Visuels

Quatre visuels alternent selon la ville pour éviter la répétition entre pages :
`chat`, `score`, `bars`, `browser`. **Ne jamais utiliser le même visuel sur deux
villes voisines** — une page Toulouse et une page Bordeaux ne doivent pas se
ressembler au premier coup d'œil.

S'ajoutent la photo de la ville (§1) et l'image à la une (bannière bleue).

---

## 4. Éviter la duplication entre villes — la partie critique

Un premier jet naïf produit 40 % de phrases identiques entre deux villes. C'est
rédhibitoire.

**Ce qui doit être unique à chaque ville**, et donc rédigé ville par ville :

- l'accroche et les deux paragraphes de contexte
- les 6 bénéfices (formulés avec le tissu économique local)
- l'introduction de la section méthode
- le piège local évoqué
- l'introduction de la zone d'intervention et sa note de bas de section
- l'introduction des secteurs
- l'introduction du tableau comparatif
- le deuxième paragraphe de budget
- le texte du CTA final
- au moins 2 des questions de FAQ

Structurer les données en deux fichiers : un fichier de **données** (slug,
gentilé, département, codes postaux, communes, statistique locale, secteurs,
photo) et un fichier de **blocs rédigés** ville par ville.

**Contrôle obligatoire** : comparer les phrases de ≥ 6 mots entre toutes les
pages du lot. Seuil d'alerte : plus de 6 phrases communes. En pratique, une
rédaction correcte descend à 1.

---

## 5. Zone d'intervention

La section qui fait la différence sur le local. Elle contient :

- une phrase d'introduction propre à la ville
- les **codes postaux** en toutes lettres
- une **grille de 8 à 12 communes limitrophes**, en `<div>` (jamais en `<span>` :
  wpautop)
- la **photo de la ville**, avec largeur et hauteur explicites
- une note de bas de section, unique elle aussi
- un CTA

---

## 6. E-E-A-T

Bandeau obligatoire en fin de page : photo de Nathan Fenina, fonction, lien
LinkedIn, lien Calendly. C'est le levier d'autorité maison, et il compte double
sur une page commerciale locale.

Sur les pages qui touchent au budget ou à des promesses de résultat, ajouter la
mention YMYL de façon visible.

---

## 7. CSS à ne pas oublier

Le thème Astra doit être neutralisé sur toute page pleine largeur — bloc
complet dans `references/charte-da.md` :

- masquer `.entry-header` et `.entry-title` (H1 en double)
- `#primary { margin: 0 }` (60 px de blanc au-dessus du hero)
- `.bloc { width:100vw; margin-left:calc(50% - 50vw) }`
- un petit script en fin de page qui retire le titre du thème du DOM

---

## 8. Pages villes existantes

Nice, Paris, Toulouse, Bordeaux, Lyon, Lille, Nantes, Marseille.

Avant d'en créer une nouvelle, relire deux pages existantes pour vérifier que
les blocs communs n'ont pas dérivé, et récupérer la liste des phrases déjà
utilisées.
