---
name: keyword-intent-classifier
description: >-
  Classe une liste de mots-clés par intention (information, comparaison,
  transaction, navigation, local), étape du parcours d'achat et risque de
  réponse directe par l'IA (zéro clic), puis recommande le format de page.
  À utiliser quand on colle une liste de mots-clés, un export Search Console ou
  Ubersuggest, ou qu'on demande « quelle intention », « quel type de page ».
---

# Classement des mots-clés par intention

## Pour chaque mot-clé

- **Intention** : information, comparaison, transaction, navigation, local.
- **Étape** : découverte, considération, décision.
- **Risque zéro clic** : élevé (définition, fait simple, calcul), moyen,
  faible (besoin d'un outil, d'un devis, d'une comparaison détaillée).
- **Format recommandé** : guide, comparatif, page service, page locale, outil,
  FAQ.

## Sortie

| Mot-clé | Intention | Étape | Risque zéro clic | Format | Page existante ? |
|---|---|---|---|---|---|

Puis les regroupements : les mots-clés qui doivent vivre **sur la même page**
(même intention, mêmes résultats Google) et ceux qui méritent une page à part.

## Règles

- Si des volumes ou des positions sont fournis, garde-les tels quels ; n'en
  invente aucun.
- Signale les risques de cannibalisation avec les pages existantes citées.
