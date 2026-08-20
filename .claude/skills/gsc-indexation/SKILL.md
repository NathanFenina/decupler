---
name: gsc-indexation
description: >-
  Qu'est-ce qui n'est pas indexé, et pourquoi ? Analyse les données Google
  Search Console de Décupler ou de ses clients. Déclencher sur : indexation,
  pages non indexées, couverture, google n'indexe pas mes pages.
---

# GSC — Indexation

**Groupe :** Piloter · **Source :** Google Search Console

## La question à laquelle ce skill répond

Qu'est-ce qui n'est pas indexé, et pourquoi ?

## Données à récupérer

Rapport de couverture + inspection d'URL + sitemap.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Confronter les URLs du sitemap aux URLs réellement indexées.
2. Classer les exclusions par motif : découverte sans indexation, explorée non indexée, canonique différente, 404, redirection.
3. Traiter en priorité les pages qui comptent — une page de pagination non indexée n'est pas un problème.
4. Pour chaque motif, donner la correction concrète, pas juste le constat.

## Sortie attendue

Les pages non indexées qui comptent, groupées par motif, avec l'action de correction.

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
