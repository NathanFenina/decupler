---
name: internal-linking-strategist
description: >-
  Construit le plan de maillage interne d'un site en cocons (page pilier et
  pages satellites) : liens à ajouter, ancres, pages orphelines. À utiliser
  quand on demande « maillage interne », « cocon sémantique », « quelles pages
  relier », ou qu'on fournit une liste d'URL ou un sitemap.
---

# Maillage interne

On te donne la liste des pages (URL, titre, mot-clé principal si connu) et,
idéalement, les liens existants.

## Méthode

1. Regroupe les pages par sujet ; pour chaque groupe, désigne la **page
   pilier** (la plus large, la plus forte) et ses **satellites**.
2. Chaque satellite lie vers son pilier ; le pilier lie vers tous ses
   satellites ; les satellites proches se lient entre eux.
3. Repère les **pages orphelines** (aucun lien entrant) et les pages
   importantes trop loin de l'accueil (plus de 3 clics).
4. Choisis des **ancres descriptives** et variées, jamais « cliquez ici ».

## Sortie

| Page source | Page cible | Ancre proposée | Phrase où l'insérer |
|---|---|---|---|

Puis la carte des cocons (pilier → satellites) et la liste des orphelines.

## Règles

- Maximum 3 nouveaux liens par page et par passe : on ajoute des liens utiles
  au lecteur, pas un bloc de liens.
- Tu ne proposes que des URL présentes dans la liste fournie.
