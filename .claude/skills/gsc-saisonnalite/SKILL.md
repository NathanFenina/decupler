---
name: gsc-saisonnalite
description: >-
  Cette baisse est-elle un problème, ou mon creux annuel habituel ? Analyse les
  données Google Search Console de Décupler ou de ses clients. Déclencher sur :
  saisonnalité, est-ce normal cette baisse, creux annuel, comparer à l'an
  dernier.
---

# GSC — Saisonnalite

**Groupe :** Diagnostiquer · **Source :** Google Search Console

## La question à laquelle ce skill répond

Cette baisse est-elle un problème, ou mon creux annuel habituel ?

## Données à récupérer

16 mois d'historique minimum, par mois.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Comparer le mois courant au **même mois de l'année précédente**, pas au mois précédent.
2. Calculer l'indice saisonnier de chaque mois sur l'historique disponible.
3. Décider si l'écart observé sort de la fourchette saisonnière normale.
4. Le dire franchement quand il n'y a pas assez d'historique pour conclure.

## Sortie attendue

Un verdict : saisonnier attendu / anomalie réelle / historique insuffisant, avec le graphique année sur année.

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
