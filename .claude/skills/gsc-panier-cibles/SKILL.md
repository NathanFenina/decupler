---
name: gsc-panier-cibles
description: >-
  Où en sont les requêtes sur lesquelles j'ai décidé de me battre ? Analyse les
  données Google Search Console de Décupler ou de ses clients. Déclencher sur :
  suivi de mots-clés, mes requêtes cibles, positions suivies, où j'en suis sur
  mes mots-clés.
---

# GSC — Panier cibles

**Groupe :** Piloter · **Source :** Google Search Console

## La question à laquelle ce skill répond

Où en sont les requêtes sur lesquelles j'ai décidé de me battre ?

## Données à récupérer

Un panier de requêtes défini par le client, suivi mois par mois.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Suivre position, impressions et clics pour chaque requête du panier.
2. Afficher la trajectoire sur 6 mois, pas seulement l'instantané.
3. Signaler les requêtes qui franchissent un palier (entrée en page 1, entrée dans le top 3).
4. Indiquer la page qui se positionne, et alerter si Google en change.

## Sortie attendue

Le tableau de suivi avec trajectoire, paliers franchis, et changements de page servie.

## Le prompt

```
Lance gsc-panier-cibles sur mes 20 requêtes stratégiques.
Montre la trajectoire sur 6 mois et signale les paliers
et les changements de page servie.
```

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
