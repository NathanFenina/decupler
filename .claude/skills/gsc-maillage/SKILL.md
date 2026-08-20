---
name: gsc-maillage
description: >-
  Quels liens internes ajouter, et depuis quelles pages exactement ? Analyse les
  données Google Search Console de Décupler ou de ses clients. Déclencher sur :
  maillage interne, liens internes, quelles pages lier, netlinking interne.
---

# GSC — Maillage

**Groupe :** Produire · **Source :** Google Search Console

## La question à laquelle ce skill répond

Quels liens internes ajouter, et depuis quelles pages exactement ?

## Données à récupérer

Requêtes par page sur tout le site.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Calculer la proximité sémantique entre pages à partir du recouvrement de leurs requêtes.
2. Proposer un lien quand une page A reçoit des requêtes proches du sujet d'une page B mieux positionnée.
3. Proposer l'ancre à partir de la requête réelle partagée, jamais une ancre générique.
4. Prioriser les liens venant des pages qui reçoivent déjà du trafic — un lien depuis une page morte ne vaut rien.

## Sortie attendue

Un tableau : page source, page cible, ancre proposée, requête qui la justifie, trafic de la page source.

## Le prompt

```
Lance gsc-maillage sur tout le site.
Propose les ancres à partir des requêtes réelles partagées,
et ne pars que de pages qui reçoivent déjà du trafic.
```

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
