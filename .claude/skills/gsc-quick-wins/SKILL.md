---
name: gsc-quick-wins
description: >-
  Quelles pages sont juste sous le seuil de trafic, et lesquelles rapportent le
  plus vite si on les pousse ? Analyse les données Google Search Console de
  Décupler ou de ses clients. Déclencher sur : quick wins, striking distance,
  pages en position 8-20, sur quoi travailler en priorité, gains rapides SEO.
---

# GSC — Quick wins

**Groupe :** Diagnostiquer · **Source :** Google Search Console

## La question à laquelle ce skill répond

Quelles pages sont juste sous le seuil de trafic, et lesquelles rapportent le plus vite si on les pousse ?

## Données à récupérer

`query` + `page`, 28 derniers jours : impressions, clics, CTR, position moyenne.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Filtrer les couples (requête, page) en **position 8 à 20** avec au moins 50 impressions sur la période.
2. Estimer le gain : `impressions × (CTR attendu en position 3 − CTR actuel)`. Utiliser une courbe CTR/position de référence, pas une moyenne du site.
3. Agréger par URL et trier par gain estimé décroissant.
4. Écarter les requêtes de marque : elles gonflent le classement sans rien apprendre.

## Sortie attendue

Un tableau URL · requête principale · position · impressions · gain de clics estimé, trié par gain. Top 10 commenté.

## Le prompt

```
Lance gsc-quick-wins sur les 28 derniers jours.
Écarte les requêtes de marque et donne-moi le top 10
par gain de clics estimé.
```

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
