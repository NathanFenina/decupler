# Couverture Yoast + Rank Math → grille seo-geo-score

Ce fichier prouve que le skill **reproduit les vérifications pertinentes** de Yoast
et de Rank Math (rien d'important n'est oublié), puis dit ce qu'on **ajoute** en plus
(GEO/AEO) et ce qu'on **laisse volontairement de côté** (hors périmètre d'un audit
on-page de contenu). L'objectif est le réalisme : un utilisateur habitué à Yoast/Rank
Math doit retrouver ses repères.

## Analyse SEO (Yoast) / SEO de base + Supplémentaires (Rank Math)

| Vérification Yoast / Rank Math | Couvert dans | 
|---|---|
| Mot-clé dans le title / au début du title | Cat 1 (title) |
| Mot-clé dans la meta description | Cat 1 (meta) |
| Mot-clé dans l'URL / slug | Cat 1 (URL) |
| Mot-clé dans les 10 % / l'intro | Cat 1 (intro) |
| Mot-clé dans le contenu | Cat 1 |
| Mot-clé dans les sous-titres | Cat 1 (sous-titre) |
| Mot-clé dans les attributs alt | Cat 2 (alt) + Cat 1 |
| Densité du mot-clé (+ alerte sur-optimisation) | Cat 1 (densité) **+ malus global** |
| Mot-clé déjà utilisé ailleurs (cannibalisation) | Cat 5 (intention) — à signaler si connu |
| Distribution du mot-clé | Cat 1 (intro + corps + sous-titres) |
| Longueur du title (largeur) | Cat 2 (title) |
| Longueur de la meta description | Cat 2 (meta) |
| Longueur du contenu (nb de mots) | Cat 3 (longueur) |
| Liens internes | Cat 5 (liens internes) |
| Liens sortants (présents, dofollow) | Cat 5 (liens externes) |
| Title contient un *power word* | Cat 2 (title) — bonus, cf. note |
| Title contient un nombre | Cat 2 (title) — bonus, cf. note |

## Analyse de lisibilité (Yoast) / Lisibilité du contenu (Rank Math)

| Vérification | Couvert dans |
|---|---|
| Longueur des phrases | Cat 4 (phrases) |
| Longueur des paragraphes | Cat 4 (paragraphes) |
| Répartition des sous-titres | Cat 3 (fréquence sous-titres) |
| Mots de transition | Cat 4 (transitions) |
| Voix passive | Cat 4 (voix passive) |
| Phrases consécutives (même début) | Cat 4 (clarté) — jugement |
| Flesch / facilité de lecture | Cat 4 (clarté) — indice, pas vérité (FR) |
| Table des matières (TOC) | Cat 3 (éléments scannables) — bonus |
| Présence d'images / vidéos | Cat 2 (images) + Cat 3 (scannable) |

## Ce que le skill AJOUTE (au-delà de Yoast/Rank Math)

Toute la **catégorie 6 — GEO / AEO** : réponse citable en intro, structure Q→R,
faits extractibles, données structurées FAQ/Q&A, clarté des entités, fraîcheur.
Yoast et Rank Math ne mesurent pas l'optimisation pour les moteurs IA — c'est la
valeur ajoutée de Décupler. C'est pourquoi un contenu à bonne FAQ + JSON-LD peut
scorer un peu plus haut ici que dans Rank Math (écart normal et voulu).

## Notes sur les *bonus* (power word, nombre, TOC)

Ces trois signaux viennent de Rank Math (Yoast ne les a pas tous). Ils sont **utiles
mais secondaires** : on les traite comme des **micro-bonus/malus à l'intérieur** du
critère concerné (un title sans power word ni nombre passe 🟡 plutôt que 🟢 sur ce
point), pas comme des catégories à part. Ça évite d'alourdir la grille tout en
gardant le réalisme « façon Rank Math ».

## Hors périmètre (volontairement)

Le skill audite **un contenu** (on-page). Il ne fait pas : crawl technique du site,
vitesse/Core Web Vitals, indexabilité, maillage à l'échelle du site, backlinks,
duplicate content inter-pages. Ces sujets relèvent d'un audit technique séparé —
à préciser à l'utilisateur si sa demande glisse vers là.
