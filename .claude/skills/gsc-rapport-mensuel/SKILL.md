---
name: gsc-rapport-mensuel
description: >-
  À quoi ressemble le mois écoulé, et qu'est-ce que ça veut dire ? Analyse les
  données Google Search Console de Décupler ou de ses clients. Déclencher sur :
  rapport mensuel, reporting client, bilan du mois, rapport SEO.
---

# GSC — Rapport mensuel

**Groupe :** Piloter · **Source :** Google Search Console

## La question à laquelle ce skill répond

À quoi ressemble le mois écoulé, et qu'est-ce que ça veut dire ?

## Données à récupérer

Mois courant vs M-1 vs même mois N-1. GA4 et PostHog si branchés.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Donner d'abord les chiffres clés : clics, impressions, position moyenne, avec les deux comparaisons.
2. Nommer les 3 mouvements qui expliquent l'essentiel de la variation — pas une liste de 40 lignes.
3. Croiser avec les conversions si GA4 est disponible : « le trafic monte sur les pages qui ne convertissent pas » est une information, « le trafic monte » n'en est pas une.
4. Terminer par les actions du mois suivant, priorisées.
5. Ne jamais inventer un chiffre absent des données.

## Sortie attendue

Un rapport structuré : chiffres clés, ce qui a bougé et pourquoi, actions du mois suivant.

## Le prompt

```
Lance gsc-rapport-mensuel.
Trois mouvements maximum pour expliquer la variation,
et croise avec les conversions GA4 si c'est branché.
```

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
