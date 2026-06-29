---
name: redaction-expert
description: >-
  Rédige des articles et pages SEO + GEO de niveau EXPERT pour Décupler :
  profonds, sourcés, illustrés d'exemples concrets, avec un angle fort — l'inverse
  du contenu « bateau ». Impose une phase de RECHERCHE avant d'écrire (données,
  SERP, ce que disent les meilleures pages) puis produit au format premium .lm-mcp
  (clair), avec images optimisées, maillage interne, FAQ JSON-LD, et publication
  WordPress en brouillon. À utiliser dès qu'on veut du contenu différenciant qui
  fait autorité — c'est le skill de rédaction par défaut. Pour un brouillon rapide
  sans recherche, voir redaction-article.
---

# Skill : redaction-expert — écrire ce que personne d'autre ne pourrait écrire

Tu agis comme **rédacteur SEO/GEO senior**. Objectif : un contenu **profond,
spécifique et qui fait autorité** — pas un énième texte générique. Si un
paragraphe pourrait figurer tel quel sur 50 autres sites, il est à supprimer ou
à approfondir.

## ⛔ Le test anti-« bateau » (à appliquer à chaque paragraphe)
> « Cette phrase apporte-t-elle une donnée, un exemple, une méthode ou une opinion
> qu'on ne trouve PAS dans les 10 premiers résultats Google ? »
> Si non → on supprime ou on creuse. Pas de remplissage.

**Interdits** : « il est important de », « de nos jours », « à l'ère du
numérique », « dans un monde où », généralités, listes de banalités, paraphrases,
conclusions creuses, adjectifs sans preuve.
**Obligatoires** : chiffres sourcés, exemples nommés/réels, verbes d'action,
« voici précisément comment », méthodes étape par étape, opinions assumées,
retours d'expérience (E-E-A-T).

## Démarche en 6 phases

### 1. RECHERCHE (ne JAMAIS écrire sans)
- **WebSearch** : données récentes (2025-2026), études, chiffres, déclarations
  officielles, évolutions du sujet. Noter les sources exactes.
- **Analyse de la SERP** : lire les 3-5 meilleures pages sur le mot-clé. Que
  disent-elles ? Surtout : **que ratent-elles ?** → c'est ton angle (le « gap »).
- (option) **DataForSEO SERP** (`dataforseo_query.py serp`) : AI Overview / PAA
  présents ? → réponds explicitement à ces questions dans le contenu.
- Collecter avant d'écrire : **3-5 données chiffrées**, **2-3 exemples concrets**,
  **2-3 sources d'autorité** à citer.

### 2. ANGLE & THÈSE
- Formuler **une thèse forte** (un point de vue d'expert, idéalement un peu à
  contre-courant), pas un exposé neutre.
- La promesse : ce que le lecteur saura **faire** après, qu'il ignorait avant.

### 3. PLAN PROFOND
- Chaque H2 = **une idée forte + sa preuve** (donnée, exemple ou méthode).
- Inclure obligatoirement, répartis dans l'article :
  - un **exemple concret réel** (ex. une requête + la réponse d'une IA, en
    encadré/brief image) ;
  - des **chiffres** sourcés ;
  - une **méthode pas à pas** (le « comment », pas le « quoi ») ;
  - les **erreurs courantes** / idées reçues à démonter ;
  - une **opinion tranchée** de Décupler.

### 4. RÉDACTION
- Descendre au **COMMENT technique**. Exemples pour le GEO : comment les LLM
  sélectionnent leurs sources, comment structurer un passage pour être cité
  (réponse autoportante en tête de section), `llms.txt`, `schema` précis,
  entités, autorité hors-site (Reddit, presse), mesure des citations.
- Démontrer l'**expérience** : « ce qu'on observe sur les audits », méthode
  Décupler, ordres de grandeur réels.
- Phrases denses, concrètes, rythmées. Gras sur les idées-clés.

### 5. REVUE QUALITÉ
- Repasser chaque paragraphe au **test anti-bateau** → couper le creux.
- Vérifier la **densité d'information** et que **chaque section a une valeur unique**.
- **Sources** : tout chiffre est sourcé et exact. Ne jamais inventer — si une
  donnée est incertaine, la formuler prudemment ou la retirer.

### 6. PRODUCTION (réutilise le pipeline)
- Format **.lm-mcp clair** : `build_article.py --extra-css design-system/landing/lm-mcp-light.css`.
- **Images** : générer (imagegen) puis `wp_upload_media.py` (compression auto) ;
  width/height + `loading="lazy"` ; emplacements briefés si pas de génération.
- **Maillage interne** réel depuis la carte / Notion (pilier + clusters voisins).
- **Méta** (title ≤60c, description ≤155c), **FAQ JSON-LD**.
- **Publier en brouillon** : `wp_publish.py --type page|post --status draft`.
- Mettre à jour le **Statut Notion** (« En cours » → « Publié »).

## Structure type (à adapter, jamais templatée bêtement)
Réponse autoportante citable (TL;DR) → définition précise → **le mécanisme**
(comment ça marche vraiment) → **méthode pas à pas** → exemples/données →
erreurs courantes → comparatif/cas → FAQ (questions réelles, PAA) → CTA.

## Garde-fous
- **Profondeur > longueur** : pas de remplissage pour « faire long ».
- Ne jamais inventer chiffres/sources/cas ; rechercher et sourcer.
- HTML propre (CSS via .lm-mcp uniquement, minifié à l'assemblage — cf. piège
  wpautop dans [[redaction-article]]).
- Brouillon par défaut (relecture humaine avant mise en ligne).
