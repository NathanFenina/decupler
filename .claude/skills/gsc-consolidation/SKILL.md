---
name: gsc-consolidation
description: >-
  Comment fusionner mes pages qui se cannibalisent, sans perdre de trafic ?
  Analyse les données Google Search Console de Décupler ou de ses clients.
  Déclencher sur : fusionner des pages, consolidation, plan de redirection,
  regrouper mes contenus.
---

# GSC — Consolidation

**Groupe :** Produire · **Source :** Google Search Console

## La question à laquelle ce skill répond

Comment fusionner mes pages qui se cannibalisent, sans perdre de trafic ?

## Données à récupérer

Sortie de `gsc-cannibalisation` + contenu des pages concernées.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Désigner la page canonique : meilleure position, meilleure profondeur, meilleurs signaux business.
2. Lister ce que les pages absorbées apportent d'unique et qui doit être **transféré** avant redirection.
3. Produire le plan de redirection 301, une ligne par URL.
4. Lister les liens internes à mettre à jour pour ne pas laisser de chaînes de redirection.

## Sortie attendue

Le plan de fusion : page cible, contenu à transférer, redirections 301, liens internes à corriger.

## Le prompt

```
Contexte : site {domaine}.
Objectif : fusionner mes pages cannibales sans perdre de trafic.

1. Pars des conflits identifiés par gsc-cannibalisation.
2. Pour chaque groupe, désigne la page canonique selon trois critères,
   dans cet ordre : meilleure position moyenne, meilleure profondeur de
   contenu, meilleure intention business.
3. Lis les pages absorbées et liste ce qu'elles apportent d'UNIQUE et
   qui doit être transféré avant redirection — sections, exemples,
   données, visuels. C'est l'étape qu'on saute et qui coûte le trafic.
4. Produis le plan de redirections 301, une ligne par URL source.
5. Liste les liens internes pointant vers les URLs absorbées et qui
   doivent être repointés, pour ne pas laisser de chaînes de
   redirection.
6. Indique les requêtes à surveiller après la fusion et le délai
   raisonnable avant de juger (compte 4 à 6 semaines).

Rends : page cible, contenu à transférer section par section, tableau
de redirections, liens internes à corriger, requêtes à surveiller.

Ne jamais inventer un chiffre : si la donnée manque ou si le volume
est trop faible pour conclure, dis-le explicitement.
Indique toujours la période et le volume qui portent tes conclusions.
```

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
