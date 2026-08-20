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
Contexte : site {domaine}, marché France.
Objectif : trouver où je gagne le plus de trafic pour le moins d'effort.

1. Récupère les couples (requête, page) sur les 28 derniers jours :
   impressions, clics, CTR, position moyenne.
2. Ne garde que la position 8 à 20, avec au moins 50 impressions.
3. Écarte les requêtes contenant ma marque : elles gonflent le
   classement sans rien m'apprendre.
4. Construis la courbe CTR/position de MON site — le CTR médian que
   j'observe à chaque position. N'utilise pas une courbe standard.
5. Estime le gain par couple :
   impressions × (CTR médian en position 3 − CTR actuel).
6. Agrège par URL, additionne, trie par gain décroissant.

Rends un tableau : URL | requête principale | position | impressions |
gain estimé en clics/mois. Puis commente le top 10 : pour chacune, une
phrase sur ce qui bloque probablement (intention mal servie, page trop
courte, title faible).

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
