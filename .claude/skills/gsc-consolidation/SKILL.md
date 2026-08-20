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

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
