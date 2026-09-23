---
name: decupler-page-ville-seo
description: >
  Produit et refond les pages villes SEO de decupler.com — « agence SEO {ville} »,
  « consultant SEO {ville} », « agence référencement {ville} » — calibrées sur la
  SERP réelle et non sur les consignes a priori : 1 100-1 400 mots, mot-clé exact
  6-8 fois, FAQ 4-6 questions, preuve chiffrée obligatoire, areaServed plutôt
  qu'une adresse inventée, et contrôle anti-duplication entre villes du même lot.
  Gère aussi les pages comparatif « meilleures agences SEO {ville} ». À utiliser
  dès qu'il faut créer, refondre ou auditer une page locale de decupler.com, ou
  qu'on parle de page ville, SEO local, « agence seo + ville », lot de villes,
  Nice, Cannes, Marseille, Toulon, Antibes, Monaco.
---

# Page ville SEO — Décupler

Ce skill existe parce que le gabarit d'origine (`decupler-page-builder`,
`gabarit-page-ville.md`) est calibré pour `agence GEO {ville}` avec les consignes
maison — 1 715 mots, mot-clé ×20, 9 questions de FAQ — et que **le relevé SERP
du 19/09/2026 les contredit**.

---

## 1. Ce que dit la SERP — la base de tout

`agence seo marseille`, 2 400 de volume, relevé Firecrawl :

| | Jones and Co **#1** | Digimood **#3** | Digimood **Nice** | Consigne maison |
|---|---|---|---|---|
| Mots | ~850 | 1 345 | **610** | ≥ 1 715 |
| Mot-clé exact | ~5× | 5× | — | ≥ 20× |
| FAQ | non | non | **non** | 9 questions |
| H2 | 1 | 5 | 6 | 12 blocs |
| Adresse locale | non | **oui** | **non** | — |
| Logos / témoignages | non | **oui** | **non** | non prévu |

Junto, modèle du gabarit d'origine, est **10ᵉ**.

Trois lectures :

1. **La longueur ne décide pas.** La page #1 fait 850 mots. Produire 1 900 mots
   nous rend deux fois plus longs que le gagnant sans gagner quoi que ce soit.
2. **L'adresse locale n'est pas requise** sur une ville satellite. La page Nice
   de Digimood ranke avec 610 mots, aucune adresse, aucune FAQ, pas retouchée
   depuis janvier 2021. Elle est portée par l'autorité du domaine et un cadrage
   honnête : « à proximité de Nice », « présent en PACA ».
3. **L'intention est mixte sur les gros volumes.** 2 des 8 premiers résultats
   sur Marseille sont des comparatifs. La page d'agence seule ne couvre pas la
   SERP.

Avant chaque nouveau lot de villes, **refaire le relevé** avec le skill
`serp-analyse` : ces chiffres datent, et une règle non sourcée finit par coûter
cher.

## 2. Cibles

| | Valeur | Contrôlé par le validateur |
|---|---|---|
| Mots | 1 100 à 1 400 | oui, plancher 1 100 |
| Mot-clé exact | 6 à 8, densité ~1 % | oui, minimum 6 |
| Densité max | 3,5 % | oui |
| H2 | 8 | oui |
| FAQ | 4 à 6 questions | oui, minimum 4 |
| JSON-LD | FAQPage + LocalBusiness **ou** areaServed | oui |
| Code postal cité | au moins un | oui |
| Lien vers une étude de cas chiffrée | obligatoire | oui |
| Liens internes | ≥ 8 | oui |

```bash
python3 .claude/skills/decupler-page-builder/scripts/validate_page.py \
  --fichier build/agence-seo-cannes.html --kw "agence SEO Cannes" \
  --slug agence-seo-cannes --type page-ville --title "..." --meta "..."
```

## 3. Ancrage local — la règle absolue

**On n'invente jamais d'adresse.** Une adresse fictive en `LocalBusiness` est un
faux signal local, sanctionné par Google, et un mensonge envers le prospect.

Décupler a **une** adresse réelle : 10 avenue Lympia privée, 06300 Nice. Elle
vit dans le schéma `ProfessionalService` du site (voir la home, page 20732), pas
dupliquée par ville.

Sur chaque page ville :

- `areaServed` avec la ville et son département
- le cadrage honnête : « depuis Nice, nous intervenons à Cannes », jamais
  « notre agence de Cannes »
- codes postaux de la ville, cités dans le texte
- 8 à 12 communes limitrophes, en `<div>` (jamais `<span>` : wpautop)
- gentilé au moins une fois (Cannois, Toulonnais, Niçois, Antibois…)

**On n'invente pas non plus de clientèle.** « Nos clients cannois », « mes
dossiers monégasques », « dans les entreprises que je vois » affirment une
présence locale qu'on ne peut pas prouver. Écrire ce qui est vrai du marché
(« une entreprise cannoise part rarement d'un site vierge »), pas une
expérience supposée. Relecture faite sur tout le lot le 23/09 : sept phrases
reprises.

## 4. Priorité de production

L'ancrage n'est crédible qu'en **06 et 83**. Ailleurs — Marseille en tête — on
attaque sans le levier de Digimood, donc on passe par le comparatif.

1. **Nice** — refonte. 1 600 de volume, déjà publiée (ID 20098, 2 155 mots),
   mais **0 lien interne** et le mot-clé exact une seule fois. Gain le plus
   rapide du lot, et elle devient la page de référence.
2. **Cannes** (1 000), **Toulon** (1 000) — création
3. **Antibes** (210), **Monaco** (390), **agence seo 06** (390) — création
4. **Marseille** (2 400) — comparatif, pas page d'agence
5. Le reste des 36 lignes de la base Notion, par volume

## 5. Structure

8 H2, dans cet ordre. Les H2 sont des questions.

1. **Hero** — H1 avec le mot-clé, sous-titre, 3 chiffres réels attribués à leur
   mission, CTA
2. **Pourquoi une agence SEO à {ville} ?** — 2 paragraphes propres à la ville,
   tissu économique réel
3. **Qu'est-ce qui fait ranker à {ville} ?** — 4 à 6 points, formulés localement
4. **Comment on travaille ?** — méthode en 4 étapes, courte
5. **Quels résultats ?** — 1 à 2 missions chiffrées, avec lien vers l'étude de
   cas complète. **Le bloc qui remplace l'adresse locale absente.**
6. **Où intervenons-nous ?** — codes postaux, communes, cadrage honnête
7. **Combien ça coûte ?** — fourchette et ce qui la fait varier
8. **FAQ** — 4 à 6 questions, dont 2 propres à la ville
9. Bandeau E-E-A-T Nathan + CTA de clôture

Blocs et CSS : skill `decupler-design-blocs`, scope `.dcp-v`.

## 6. Anti-duplication — le point qui fait échouer les lots

Un premier jet naïf produit 40 % de phrases identiques entre deux villes.

**À rédiger ville par ville, jamais dupliqué :**
l'accroche, les 2 paragraphes de contexte, les 4-6 points « ce qui fait ranker »,
l'introduction de la méthode, le piège local, l'introduction et la note de la
zone d'intervention, le 2ᵉ paragraphe de budget, le CTA final, et au moins 2 des
questions de FAQ.

Structurer en deux fichiers : **données** (slug, gentilé, département, codes
postaux, communes, secteurs dominants, photo) et **blocs rédigés** par ville.
Voir `references/villes.json`.

**Contrôle obligatoire** avant de pousser le lot :

```bash
python3 .claude/skills/decupler-page-builder/scripts/validate_page.py \
  --lot build/ --manifeste lot.json
```

Seuil d'alerte : plus de 6 phrases communes de ≥ 6 mots entre deux pages. Une
rédaction correcte descend à 1.

## 7. Maillage — 5 liens par page, pas plus

- **1 montant** vers le pilier `seo-local`, ancre exacte, dans les 150 premiers
  mots
- **2 à 3 latéraux** vers les villes voisines du même département. Au-delà, la
  grille de communes devient une ferme de liens
- **1 croisé** vers la page GEO de la même ville quand elle existe (Nice,
  Marseille, Lyon, Paris, Toulouse, Bordeaux, Lille, Nantes)
- **1 preuve** vers une étude de cas du même secteur —
  `etude-de-cas-seo-reux-travaux` pour l'artisanat,
  `etude-de-cas-seo-atoo-energie` pour l'énergie
- **1 descendant** vers une ressource GMB : `fiche-gmb`, `citations-locales`,
  `obtenir-des-avis-google`

URLs mortes qui répondent **410 et non 404** — ne jamais les utiliser :
`/search-everywhere/`, `/tarifs/`, `/llms.txt`.

## 8. Pages comparatif (Marseille, Nice)

Intention distincte, page distincte. Décidé : **on cite les concurrents
nommément et Décupler figure honnêtement dedans.**

- Digimood, Jones and Co, Ad's up, Junto, Skynet France, Noiise — avec leurs
  vrais points forts
- Décupler à sa juste place, pas en premier par défaut
- Un critère de différenciation explicite par agence
- Aucune note inventée, aucun faux avis, aucun classement chiffré non sourcé
- Slug : `meilleures-agences-seo-{ville}`

C'est l'angle où l'absence d'adresse locale ne pénalise pas.

## 9. Publication

Avant tout push, le lot entier passe ces contrôles, dans cet ordre :

1. `validate_page.py --manifeste` sur **toutes** les pages du lot — c'est ce
   qui mesure la duplication entre pages (seuil : 4 phrases communes).
2. Rendu réel à 1440 et 505 px avec sonde DOM : zéro débordement.
3. Impeccable en mode navigateur (voir `decupler-direction-artistique` §8).
4. Après le push, relire le rendu WordPress par l'API (`context=edit`) :
   `raw` identique au build, zéro `<p>` parasite, zéro `<br />`, JSON-LD
   valide, toutes les images en 200. C'est ce contrôle qui a trouvé le
   `<br />` que wpautop glissait entre les deux blocs JSON-LD.

- Post type `pages`, statut `draft`. **Ne jamais publier sans relecture.**
- Chercher le slug avant de créer : sinon WordPress crée un doublon `-2`
- Relire et conserver le statut existant au push
- Yoast : écrivable par l'API **si** le plugin `decupler-yoast-rest` est activé
  (ZIP installable depuis l'admin, ou fichier dans `wp-content/mu-plugins/`).
  Sinon, fournir title et meta à Nathan pour saisie manuelle
- Audits séquentiels : au-delà d'une dizaine d'appels concurrents, le serveur
  renvoie des comptages incohérents
