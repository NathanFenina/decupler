---
name: gsc-content-decay
description: >-
  Quelles pages déclinent lentement depuis plusieurs mois, avant qu'elles ne
  disparaissent ? Analyse les données Google Search Console de Décupler ou de
  ses clients. Déclencher sur : content decay, pages qui déclinent, contenu qui
  s'essouffle, pages à rafraîchir, perte progressive.
---

# GSC — Content decay

**Groupe :** Diagnostiquer · **Source :** Google Search Console

## La question à laquelle ce skill répond

Quelles pages déclinent lentement depuis plusieurs mois, avant qu'elles ne disparaissent ?

## Données à récupérer

12 derniers mois par `page` et par mois : clics, impressions, position.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Repérer les pages en baisse sur **3 mois consécutifs au minimum** — un mauvais mois isolé est du bruit, pas du déclin.
2. Calculer la pente sur 6 mois et le pourcentage perdu depuis le pic.
3. Croiser avec la date de dernière mise à jour de la page si elle est disponible.
4. Classer par volume perdu en valeur absolue, pas en pourcentage : −20 % sur une grosse page vaut plus que −80 % sur une page morte.

## Sortie attendue

Liste des pages en déclin avec pente, clics perdus, mois de bascule, et une recommandation par page (rafraîchir / fusionner / laisser mourir).

## Le prompt

```
Contexte : site {domaine}.
Objectif : repérer les pages qui s'éteignent lentement, avant qu'elles
ne disparaissent complètement.

1. Récupère 12 mois d'historique par page et par mois : clics,
   impressions, position moyenne.
2. Ne retiens une page que si elle baisse sur au moins 3 mois
   CONSÉCUTIFS. Un mauvais mois isolé est du bruit, pas du déclin.
3. Pour chaque page retenue, calcule la pente sur 6 mois, le pourcentage
   perdu depuis son pic, et le mois où la bascule commence.
4. Classe par clics perdus en VALEUR ABSOLUE, pas en pourcentage :
   −20 % sur une grosse page vaut plus que −80 % sur une page morte.
5. Si tu as la date de dernière mise à jour de chaque page, mets-la en
   face — une corrélation avec l'ancienneté oriente le diagnostic.

Rends un tableau : URL | pente 6 mois | clics perdus | mois de bascule |
recommandation. La recommandation doit trancher entre trois options
seulement : rafraîchir, fusionner, ou laisser mourir. Justifie en une
phrase pour chaque page.

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
