---
name: gsc-brief-depuis-requetes
description: >-
  Comment écrire un brief à partir de ce que les gens tapent vraiment, pas de ce
  qu'un outil suggère ? Analyse les données Google Search Console de Décupler ou
  de ses clients. Déclencher sur : brief à partir de GSC, brief basé sur mes
  données, plan d'article depuis Search Console.
---

# GSC — Brief depuis requetes

**Groupe :** Produire · **Source :** Google Search Console

## La question à laquelle ce skill répond

Comment écrire un brief à partir de ce que les gens tapent vraiment, pas de ce qu'un outil suggère ?

## Données à récupérer

Requêtes d'une page ou d'un cluster, 6 mois.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Partir des requêtes réelles : elles portent le vocabulaire exact des acheteurs.
2. Grouper par intention, puis ordonner les groupes par volume d'impressions — cet ordre devient le plan Hn.
3. Extraire les formulations interrogatives : elles deviennent des H3 ou des entrées de FAQ.
4. Compléter avec la SERP (via DataForSEO ou Firecrawl) uniquement pour ce que GSC ne peut pas dire : ce que couvrent les concurrents.

## Sortie attendue

Un brief : angle, plan Hn ordonné, vocabulaire imposé, questions à traiter, et le volume d'impressions qui justifie chaque section.

## Le prompt

```
Lance gsc-brief-depuis-requetes pour le cluster « audit seo ».
Ordonne le plan Hn par volume d'impressions et impose
le vocabulaire exact des requêtes.
```

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
