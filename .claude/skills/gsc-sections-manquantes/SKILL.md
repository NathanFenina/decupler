---
name: gsc-sections-manquantes
description: >-
  Quelles questions cette page reçoit-elle sans y répondre ? Analyse les données
  Google Search Console de Décupler ou de ses clients. Déclencher sur : sections
  manquantes, ma page ne répond pas à tout, enrichir une page, que rajouter dans
  cet article.
---

# GSC — Sections manquantes

**Groupe :** Produire · **Source :** Google Search Console

## La question à laquelle ce skill répond

Quelles questions cette page reçoit-elle sans y répondre ?

## Données à récupérer

Toutes les requêtes servies par UNE URL, 3 mois.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Récupérer l'intégralité des requêtes que la page reçoit, y compris celles à faibles impressions.
2. Les regrouper en intentions distinctes.
3. Confronter chaque intention au contenu réel de la page : la traite-t-elle explicitement, ou Google l'a-t-il servie par défaut ?
4. Ne proposer que les sections **absentes** — ne jamais réécrire ce qui existe déjà.

## Sortie attendue

La liste des sections à ajouter, avec pour chacune les requêtes qui la justifient et le volume d'impressions en jeu.

## Le prompt

```
Lance gsc-sections-manquantes sur /ma-page/.
Sors les requêtes qu'elle reçoit et ne traite pas,
et propose uniquement les sections absentes.
```

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
