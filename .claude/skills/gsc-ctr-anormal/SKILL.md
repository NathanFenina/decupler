---
name: gsc-ctr-anormal
description: >-
  Quelles pages sous-performent en clics compte tenu de la position qu'elles
  occupent déjà ? Analyse les données Google Search Console de Décupler ou de
  ses clients. Déclencher sur : CTR faible, beaucoup d'impressions peu de clics,
  mes titles ne donnent pas envie, taux de clic anormal.
---

# GSC — Ctr anormal

**Groupe :** Diagnostiquer · **Source :** Google Search Console

## La question à laquelle ce skill répond

Quelles pages sous-performent en clics compte tenu de la position qu'elles occupent déjà ?

## Données à récupérer

`query` + `page`, 28 jours : impressions, clics, CTR, position.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Établir la **courbe CTR/position du site** (CTR médian observé pour chaque position) — c'est la référence, pas un standard générique.
2. Repérer les pages dont le CTR est nettement sous la médiane de leur propre position.
3. Filtrer sur un minimum d'impressions pour éviter les faux positifs statistiques.
4. Vérifier la SERP : un AI Overview ou un featured snippet concurrent explique parfois tout le déficit.

## Sortie attendue

Les pages à fort potentiel de CTR, avec l'écart chiffré à la courbe. Passer la main à `gsc-reecriture-title`.

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
