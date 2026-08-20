---
name: gsc-gagnants-perdants
description: >-
  Qu'est-ce qui monte et qu'est-ce qui tombe depuis le mois dernier ? Analyse
  les données Google Search Console de Décupler ou de ses clients. Déclencher
  sur : évolution mensuelle, gagnants perdants, comparaison mois précédent,
  qu'est-ce qui a bougé.
---

# GSC — Gagnants perdants

**Groupe :** Diagnostiquer · **Source :** Google Search Console

## La question à laquelle ce skill répond

Qu'est-ce qui monte et qu'est-ce qui tombe depuis le mois dernier ?

## Données à récupérer

Deux périodes comparables, par `page` et par `query`.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Comparer clics, impressions et position sur des périodes de longueur identique.
2. Classer séparément les gains et les pertes, en valeur absolue.
3. Pour chaque mouvement important, donner la cause probable (renvoyer vers `gsc-chute-trafic`).
4. Ne jamais présenter un pourcentage sans le volume associé.

## Sortie attendue

Deux tableaux (top gains / top pertes) avec volume, variation, et cause probable.

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
