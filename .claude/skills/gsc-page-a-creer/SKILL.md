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

## Le prompt

```
Contexte : site {domaine}.
Objectif : trouver les sujets qui méritent une page et n'en ont pas.

1. Récupère toutes les requêtes du site sur 6 mois, avec la page qui
   les sert et la position obtenue.
2. Regroupe en clusters sémantiques.
3. Repère les clusters ORPHELINS : les impressions sont dispersées sur
   plusieurs pages approximatives, les positions sont faibles, et
   aucune page n'est vraiment dédiée au sujet.
4. Estime le potentiel de chaque cluster : impressions cumulées,
   position moyenne actuelle, et gain si une vraie page atteignait la
   position 5.
5. Avant de proposer une création, VÉRIFIE qu'il n'existe pas déjà une
   page sur le sujet dans l'inventaire du site. Une page en double fait
   plus de mal que pas de page.

Rends les clusters orphelins triés par potentiel, avec pour chacun : le
mot-clé principal, les requêtes couvertes, les impressions cumulées, les
pages qui les captent mal aujourd'hui, et le titre de la page à créer.
Signale explicitement les clusters où tu as un doute sur un doublon.

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
