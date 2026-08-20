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

## Le prompt

```
Contexte : site {domaine}, surveillance hebdomadaire.
Objectif : ne remonter que ce qui mérite vraiment mon attention.

1. FIXE LES SEUILS AVANT de regarder les données. Sinon on justifie
   après coup ce qu'on a trouvé.
   Seuils proposés, à ajuster : −25 % de clics sur une URL qui pesait
   plus de 100 clics/mois ; −3 positions sur une requête stratégique ;
   −30 % de CTR à position stable ; disparition totale d'une page.
2. Compare les 7 derniers jours aux 4 semaines précédentes, sur des
   jours ÉQUIVALENTS. Un lundi contre un dimanche ne veut rien dire.
3. Écarte les variations explicables par la saisonnalité connue.
4. Ne remonte que ce qui dépasse un seuil. Une alerte qui se déclenche
   toutes les semaines n'est plus lue par personne.
5. Pour chaque alerte, donne la cause probable et l'action immédiate.

Rends soit la liste des alertes classées par gravité, soit — et c'est
une réponse parfaitement valable — la confirmation explicite qu'il n'y
a rien à signaler cette semaine, avec les seuils qui ont été testés.

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
