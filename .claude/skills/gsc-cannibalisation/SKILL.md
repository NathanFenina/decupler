---
name: gsc-cannibalisation
description: >-
  Quelles pages de mon site se battent entre elles sur la même requête ? Analyse
  les données Google Search Console de Décupler ou de ses clients. Déclencher
  sur : cannibalisation, deux pages même mot-clé, mes pages se concurrencent,
  quelle page garder.
---

# GSC — Cannibalisation

**Groupe :** Diagnostiquer · **Source :** Google Search Console

## La question à laquelle ce skill répond

Quelles pages de mon site se battent entre elles sur la même requête ?

## Données à récupérer

`query` + `page` sur 3 mois : impressions, clics, position par couple.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Isoler les requêtes servies par **2 URLs ou plus** avec des impressions significatives sur chacune.
2. Signaler les cas où Google **alterne** entre les URLs d'un mois sur l'autre : c'est le vrai symptôme, pas la simple co-présence.
3. Désigner l'URL à garder : celle qui a la meilleure position moyenne ET les meilleurs signaux de conversion.
4. Distinguer la vraie cannibalisation d'une couverture légitime (une page catégorie et une page produit peuvent coexister).

## Sortie attendue

Par requête : les URLs en conflit, laquelle garder, et l'action (fusion + redirection, désoptimisation, ou différenciation d'intention).

## Le prompt

```
Contexte : site {domaine}.
Objectif : trouver les pages qui se font concurrence entre elles.

1. Récupère les couples (requête, page) sur les 3 derniers mois.
2. Isole les requêtes servies par 2 URLs ou plus, avec des impressions
   significatives sur chacune (au moins 30).
3. Distingue deux situations, c'est essentiel :
   - VRAIE cannibalisation : Google ALTERNE entre mes URLs d'un mois
     sur l'autre. C'est le symptôme qui compte.
   - Couverture légitime : une page catégorie et une page produit
     peuvent coexister sur la même requête sans problème.
4. Pour chaque conflit réel, désigne l'URL à garder : celle qui a la
   meilleure position moyenne ET la meilleure intention business.
5. Mesure ce que le conflit coûte : compare la position moyenne quand
   les deux pages se battent à la meilleure position observée.

Rends, par requête : les URLs en conflit, leurs positions mois par mois,
laquelle garder, et l'action — fusion et redirection, désoptimisation de
la perdante, ou différenciation d'intention. Ne propose une fusion que
si les deux pages traitent réellement le même sujet.

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
