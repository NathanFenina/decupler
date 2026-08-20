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
Contexte : site {domaine}, panier de requêtes stratégiques.
Objectif : suivre les requêtes sur lesquelles j'ai décidé de me battre.

1. Prends le panier de requêtes défini (si je ne te l'ai pas donné,
   demande-le-moi avant de commencer — ne le devine pas).
2. Pour chaque requête : position, impressions, clics, et la PAGE qui
   se positionne.
3. Montre la trajectoire sur 6 mois, pas l'instantané. Une position 7
   qui vient de 15 et une position 7 qui vient de 3 n'appellent pas la
   même réaction.
4. Signale les franchissements de palier : entrée en page 1 (top 10),
   entrée dans le top 3, sortie de page 1.
5. Alerte si Google CHANGE la page qu'il positionne sur une requête —
   c'est souvent le signe d'une cannibalisation qui démarre.
6. Sépare les requêtes qui progressent, stagnent, et reculent.

Rends le tableau de suivi : requête | position M-5 à M | tendance |
page servie | changement de page | palier franchi. Termine par les 3
requêtes qui demandent une action ce mois-ci, et laquelle.

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
