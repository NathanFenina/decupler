---
name: gsc-reecriture-title
description: >-
  Comment réécrire mes titles et metas pour récupérer les clics que je laisse
  sur la table ? Analyse les données Google Search Console de Décupler ou de ses
  clients. Déclencher sur : réécrire les titles, améliorer le CTR, optimiser
  meta description, mes titres ne cliquent pas.
---

# GSC — Reecriture title

**Groupe :** Produire · **Source :** Google Search Console

## La question à laquelle ce skill répond

Comment réécrire mes titles et metas pour récupérer les clics que je laisse sur la table ?

## Données à récupérer

Sortie de `gsc-ctr-anormal` + title/meta actuels des pages ciblées.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Reprendre les pages identifiées en déficit de CTR.
2. Réécrire en intégrant **la formulation exacte** de la requête la plus porteuse de la page.
3. Respecter les limites d'affichage (environ 60 caractères pour le title, 155 pour la meta).
4. Proposer deux variantes par page pour permettre un test.
5. Estimer le gain de clics si le CTR rejoint la médiane de sa position.

## Sortie attendue

Un tableau : URL, title actuel → 2 propositions, meta actuelle → 2 propositions, gain de clics estimé.

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
