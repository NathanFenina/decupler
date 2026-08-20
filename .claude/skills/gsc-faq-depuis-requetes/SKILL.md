---
name: gsc-faq-depuis-requetes
description: >-
  Quelles questions dois-je mettre en FAQ, en me basant sur ce qu'on me demande
  vraiment ? Analyse les données Google Search Console de Décupler ou de ses
  clients. Déclencher sur : FAQ depuis GSC, questions fréquentes réelles,
  quelles questions ajouter, FAQ basée sur les données.
---

# GSC — Faq depuis requetes

**Groupe :** Produire · **Source :** Google Search Console

## La question à laquelle ce skill répond

Quelles questions dois-je mettre en FAQ, en me basant sur ce qu'on me demande vraiment ?

## Données à récupérer

Requêtes interrogatives d'une page ou d'un site, 6 mois.

Deux voies possibles, au choix selon le client :

- **Connecteur Windsor.ai** — branché en un clic, aucun code. C'est la voie par défaut chez Décupler.
- **Service account Google** — `GSC_CREDENTIALS_JSON` et `GSC_SITE_URL` dans `.env`, puis les scripts locaux du repo. À privilégier quand on veut la donnée brute et pas d'intermédiaire.

## Méthode

1. Isoler les requêtes qui commencent par un interrogatif (comment, pourquoi, combien, quel, est-ce que…) ou qui en ont la forme.
2. Dédupliquer les reformulations d'une même question.
3. Trier par impressions et retenir celles qui ne sont pas déjà traitées dans le corps de la page.
4. Rédiger des réponses courtes et autonomes — c'est ce format que les moteurs génératifs citent.

## Sortie attendue

Le bloc FAQ rédigé + le JSON-LD `FAQPage` correspondant, prêt à coller.

## Le prompt

```
Lance gsc-faq-depuis-requetes sur /ma-page/.
Garde les questions non traitées dans le corps de page
et sors-moi le JSON-LD FAQPage.
```

## Règles

- **Ne jamais inventer un chiffre.** Si la donnée manque, le dire — pas l'estimer en silence.
- Toujours indiquer la **période** et le **volume** sur lesquels repose une conclusion.
- Un pourcentage sans son volume absolu n'est pas une information.
- Écarter les **requêtes de marque** des analyses de performance, sauf demande contraire.
- Les données GSC sont **échantillonnées et plafonnées** : au-delà de ~1 000 lignes, paginer ou segmenter par page/date.
