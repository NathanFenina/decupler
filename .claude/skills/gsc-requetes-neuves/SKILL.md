---
name: gsc-requetes-neuves
description: >-
  Sur quelles requêtes Google a-t-il commencé à me montrer, sans que j'aie de
  page dédiée ? Analyse les données Google Search Console de Décupler ou de ses
  clients. Déclencher sur : nouvelles requêtes, requêtes émergentes, sur quoi je
  commence à sortir, nouveaux mots-clés.
---

# GSC — Requetes neuves

**Groupe :** Diagnostiquer · **Source :** Google Search Console

## La question à laquelle ce skill répond

Sur quelles requêtes Google a-t-il commencé à me montrer, sans que j'aie de page dédiée ?

## Données à récupérer

Deux périodes de 28 jours consécutives, dimension `query`.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Isoler les requêtes présentes sur la période récente et **absentes** de la précédente.
2. Écarter le bruit : exiger un seuil d'impressions.
3. Pour chaque requête neuve, identifier la page qui la reçoit et juger si elle est la bonne.
4. Regrouper les requêtes neuves par thème : un cluster émergent vaut une page, pas une ligne.

## Sortie attendue

Les requêtes émergentes groupées par thème, avec la page actuellement servie et un verdict : page adaptée / à enrichir / à créer.

## Le prompt

```
Lance gsc-requetes-neuves : compare les 28 derniers jours
aux 28 précédents, groupe les requêtes émergentes par thème,
et dis-moi lesquelles n'ont pas de page adaptée.
```

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
