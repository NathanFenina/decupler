---
name: gsc-page-a-creer
description: >-
  Quels sujets méritent une page dédiée que je n'ai pas encore ? Analyse les
  données Google Search Console de Décupler ou de ses clients. Déclencher sur :
  quelles pages créer, sujets sans page, opportunités de contenu, trous dans mon
  site.
---

# GSC — Page a creer

**Groupe :** Produire · **Source :** Google Search Console

## La question à laquelle ce skill répond

Quels sujets méritent une page dédiée que je n'ai pas encore ?

## Données à récupérer

Toutes les requêtes du site, 6 mois, avec leur page servie.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Regrouper les requêtes en clusters sémantiques.
2. Repérer les clusters où **aucune page n'est vraiment dédiée** : les impressions sont dispersées sur des pages approximatives, avec des positions faibles.
3. Estimer le potentiel du cluster : impressions cumulées et position moyenne actuelle.
4. Vérifier l'absence de doublon avec l'inventaire interne avant de proposer une création.

## Sortie attendue

Les clusters orphelins classés par potentiel, avec pour chacun le mot-clé principal, les requêtes couvertes et la page à créer.

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
