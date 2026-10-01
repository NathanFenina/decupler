# Passation — decupler.com (au 1er octobre 2026)

Ce que la conversation de pilotage commune aux trois projets a appris et laissé
ouvert pour ce site. Dorénavant, decupler.com se pilote **uniquement depuis ce
dépôt**. Lire ce fichier à l'ouverture d'une conversation, avec la page de suivi
et `docs/seo/a-traiter.md`.

Ce dépôt est **public** : aucun secret, aucun accès, aucune donnée client ici.

## Où sont les choses

| Quoi | Où |
|---|---|
| Roadmap, avancement, validation | En haut de l'artifact existant « Chantiers decupler.com » : https://claude.ai/artifact/Rb2sP3EQFzedk6G2Xau6KA. Le compte rendu d'origine est conservé dessous (`<template id="hote">`) : pour le mettre à jour, modifier ce bloc, jamais le reste de la page |
| Points ouverts | `docs/seo/a-traiter.md` (piratage, cannibalisation, pages d'offre, design) |
| Cartographie | `memoire/cartographie.csv` fait foi ; l'ancienne base Notion n'est plus qu'une archive |
| Consignes des routines | `routines/<mode>.md` — les modifier ici suffit |
| Méthode | `.claude/` — synchronisée depuis decupler-seo, ne pas la modifier ici |

Il n'y a **qu'une** page de suivi : la page « Pilotage Décupler » créée un temps a
été supprimée.

## Les routines (session dédiée « Décupler — pilotage SEO (routines) »)

| Routine | Quand (Paris) | Ce qu'elle fait |
|---|---|---|
| Veille | tous les jours, 7 h 17 | contrôle, alerte prioritaire si le spam revient (casino, slot, mahjong…) |
| Contenu | mardi, 7 h 22 | un article en **brouillon WordPress**, jamais en ligne |
| Optimisation | jeudi, 7 h 27 | title/meta et révisions par `wp.py` ; évite les pages en cannibalisation |
| Rapport et roadmap | le 1er, 7 h 37 | rapport, cartographie, au plus 8 actions proposées |

**Rapport d'octobre non produit** : le 01/10, la session a refusé que la routine
fusionne sa propre PR et elle est restée en attente ; la relance n'a rien poussé
(aucune branche `claude/rapport-*`). À relancer depuis la conversation des
routines. Les consignes sont corrigées : désormais la PR reste ouverte et
s'affiche sur la roadmap « Fusionner la PR n° … ».

## Ce qu'on sait du site

- Le pic de juin était le piratage (requêtes de spam) ; nettoyé, URL de spam en 410.
- Le vrai recul : ~35 à 48 clics/semaine en mai, 15 à 20 fin septembre ; pages avec
  impressions passées de 170 à 95.
- Pages d'offre loin : agence-geo (pos. ~63), accompagnement-seo (~59), audit-geo (~38),
  agence-seo (~34). Gisements rapides : claude-skills-seo (pos. ~21, CTR 0,2 %),
  installer-mcp-data-for-seo (pos. ~25).
- 3 cannibalisations : « agence geo » (/agence-geo/, /agences-geo-france/,
  /meilleure-agence-geo/), « agence geo nice » (/agence-seo/, /agence-geo-nice/),
  « eeat » (/eeat-google/, /e-e-a-t/). Décisions à prendre sur la roadmap avant
  d'optimiser ces pages.
- **82 % des impressions viennent de France** ; ailleurs les pages sont vers la 50e place.

## International — décidé le 30/09 et le 01/10

**Anglais, sans plugin multilingue** (décision de Nathan) : pages
`decupler.com/en/<page>/`.
1. Retirer d'abord la redirection 301 posée sur `/en/` lors du nettoyage du 22/09.
2. Page parente `en` dans WordPress ; chaque page anglaise en page enfant, publiée
   par `wp.py` (brouillon).
3. `lang="en"` et hreflang FR ↔ EN ajoutés par le plugin maison « Budget de crawl »
   (versionné dans ce dépôt).

Cibles (volumes mensuels DataForSEO) :
- **États-Unis — GEO et IA** : « generative engine optimization » 4 400, « ai seo agency »
  1 600, « geo agency » 720, « claude seo » 480. Pages : GEO agency, AI SEO agency,
  traduction des pages Claude SEO.
- **Moyen-Orient — SEO local** : « seo agency dubai » 8 100 aux Émirats ; GEO quasi nul ;
  Arabie saoudite 140, Qatar 50. Page « SEO & GEO agency — Dubai and the Gulf ». Il
  faudra une preuve de présence dans le Golfe (client, partenaire, adresse).

**Francophonie, sans traduction** (proposé, refusable sur la roadmap) : une vraie page
par pays avec contenu local — Québec (« consultant seo » 1 900, « agence seo » 720),
Belgique (390 / 260), Suisse (210 / 170), Maroc / Tunisie (140 / 70, CTR déjà 24 à 30 %).

## Questions en attente de Nathan

- Importer une fois la base Notion « Cartographie SEO » dans `memoire/cartographie.csv` ?
- Mot-clé principal de la page d'accueil : celui de Search Console est absurde, à choisir.

## Astuces de travail

- Avant une tâche : la chercher sur la page de suivi. Après :
  `pilotage.py ajouter … --statut faite --lien <URL>`, puis republier (lire la page juste
  avant, sinon la publication est refusée).
- WordPress : toujours par `.claude/decupler-seo/scripts/wp.py`, brouillon ou révision,
  sauvegarde automatique avant écriture. Jamais le thème ni le CSS global (freelance).
- Client qui veut Notion : `cartographie.py exporter --notion-csv`, généré depuis le dépôt.
- Mise à jour de la méthode : `python3 .claude/decupler-seo/scripts/projet.py sync .`
