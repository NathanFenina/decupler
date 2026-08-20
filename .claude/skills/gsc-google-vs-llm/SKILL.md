---
name: gsc-google-vs-llm
description: >-
  Je suis bien placé sur Google — est-ce que les IA me citent pour autant ?
  Analyse les données Google Search Console de Décupler ou de ses clients.
  Déclencher sur : visibilité IA vs Google, écart GEO, suis-je cité par ChatGPT,
  comparer position et citations.
---

# GSC — Google vs llm

**Groupe :** Piloter · **Source :** Google Search Console

## La question à laquelle ce skill répond

Je suis bien placé sur Google — est-ce que les IA me citent pour autant ?

## Données à récupérer

Requêtes cibles GSC + interrogation des moteurs génératifs (Perplexity, ChatGPT).

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Prendre les requêtes où le site est déjà bien positionné sur Google.
2. Poser ces mêmes questions aux moteurs génératifs et relever qui est cité, et à quel rang.
3. Mettre les deux colonnes face à face : l'écart est la feuille de route GEO.
4. Identifier les sources que les moteurs citent à la place — c'est là qu'il faut aller se faire mentionner.
5. Journaliser chaque relevé pour mesurer l'évolution d'un mois sur l'autre.

## Sortie attendue

Le tableau position Google / citation LLM par requête, l'écart chiffré, et les sources concurrentes à travailler.

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
