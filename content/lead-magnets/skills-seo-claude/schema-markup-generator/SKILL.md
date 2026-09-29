---
name: schema-markup-generator
description: >-
  Génère des données structurées JSON-LD valides (Article, FAQPage, HowTo,
  Product, LocalBusiness, Organization, Person, BreadcrumbList, VideoObject)
  à partir d'une page ou d'une description. À utiliser quand on demande
  « ajoute du schema », « JSON-LD », « données structurées », « rich results ».
---

# Données structurées JSON-LD

## Règles

1. Uniquement le vocabulaire schema.org, dans un seul bloc
   `<script type="application/ld+json">` avec un `@graph`.
2. Toutes les propriétés requises par Google pour le type, plus les
   recommandées quand l'information existe.
3. **Jamais de donnée inventée** : pas de note, d'avis, de prix ou d'adresse
   qui ne figure pas dans la page. Ce qui manque est listé à part.
4. Une seule Organisation et une seule Personne par site, chacune avec un
   `@id` stable (`https://exemple.com/#organization`), et tous les autres nœuds
   y font référence par `@id` au lieu de les redéclarer.
5. `sameAs` seulement vers des profils officiels vérifiés.

## Sortie

1. Le bloc JSON-LD prêt à coller.
2. La liste des informations manquantes qui débloqueraient un résultat enrichi.
3. Le lien pour tester : https://search.google.com/test/rich-results
