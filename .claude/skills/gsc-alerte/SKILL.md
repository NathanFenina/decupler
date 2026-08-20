---
name: gsc-alerte
description: >-
  Qu'est-ce qui vient de décrocher et que je n'ai pas vu ? Analyse les données
  Google Search Console de Décupler ou de ses clients. Déclencher sur : alerte
  SEO, surveillance, prévenir si ça baisse, monitoring Search Console.
---

# GSC — Alerte

**Groupe :** Piloter · **Source :** Google Search Console

## La question à laquelle ce skill répond

Qu'est-ce qui vient de décrocher et que je n'ai pas vu ?

## Données à récupérer

7 derniers jours vs les 4 semaines précédentes.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Définir les seuils avant de regarder les données, pour éviter de justifier après coup.
2. Surveiller : chute de clics d'une URL importante, perte de position sur une requête stratégique, effondrement de CTR, disparition d'une page de l'index.
3. Comparer à des jours équivalents — un lundi contre un dimanche ne veut rien dire.
4. Ne remonter que ce qui dépasse le seuil : une alerte qui crie tout le temps n'est plus lue.

## Sortie attendue

Une liste d'alertes ou, mieux, la confirmation explicite qu'il n'y a rien à signaler.

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
