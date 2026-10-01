---
name: pages-pourries
description: >-
  Repère les pages « pourries » de decupler.com (ou d'un site client WordPress
  connecté) : vides, mortes, périmées, minces, ou juste sous le seuil de trafic.
  Croise Search Console sur 180 jours, le contenu WordPress et des signaux
  d'obsolescence (anciens modèles d'IA, dates passées), puis propose une action
  par page : supprimer (410), rediriger, fusionner, mettre à jour, enrichir,
  pousser. À utiliser quand on dit : « check les pages pourries », « quelles
  pages supprimer », « nettoyage du site », « pages obsolètes », « quelles pages
  mettre à jour en priorité », « audit de contenu ».
---

# Skill : pages-pourries — l'audit de contenu qui décide quoi faire de chaque page

Objectif : un tableau court, trié par urgence, où chaque page a **un verdict et
une action**. On ne touche à rien pendant l'audit ; les actions se font ensuite,
page par page, avec sauvegarde.

## 1. Lancer l'audit

```bash
python3 .claude/skills/pages-pourries/scripts/audit.py --sortie /tmp/audit-pages
# → audit.md (lisible) et audit.json (pour les scripts)
```

Le script lit `.env` (WordPress + Search Console). Il prend toutes les pages et
articles publiés, et pour chacun : impressions, clics, position (180 jours),
nombre de mots, date de modification, constructeur (contenu ou Elementor),
mentions obsolètes, présence d'une pop-up email.

## 2. Les verdicts

| Verdict | Règle | Action par défaut |
|---|---|---|
| **vide** | < 80 mots et 0 impression | 410 si c'est un reste technique, sinon redirection |
| **morte** | 0 impression depuis 180 jours, page de plus de 6 mois | Rediriger vers le pilier du sujet, ou fusionner |
| **périmée** | Mentionne Claude 3/3.5, GPT-4/4o, Gemini 1.5/2.0, « en 2024 »… | Mettre à jour si elle a du trafic, sinon fusionner |
| **mince** | < 400 mots mais montrée par Google | Enrichir : sections manquantes (skill `gsc-sections-manquantes`) |
| **à pousser** | Position 8 à 20, ≥ 100 impressions | Quick win : title, sections, maillage (`gsc-quick-wins`) |
| **saine** | Le reste | Garder |

Les règles sont volontairement simples : **le verdict est une proposition, la
décision est humaine**. Un faux positif typique : une citation datée
(« étude Princeton 2024 ») est signalée « périmée » alors qu'elle est juste.

## 3. Avant d'agir sur une page

1. **Vérifier qu'elle n'est pas un reste technique déjà neutralisé** : les pages
   WooCommerce (boutique, panier, commander, mon-compte) sont vides mais hors
   index et hors sitemap grâce au plugin « Budget de crawl ». Ne rien faire.
2. **Vérifier la cannibalisation** avant de rediriger (skill `gsc-cannibalisation`) :
   la cible doit couvrir la même intention.
3. **Sauvegarder** le contenu et `_elementor_data` (voir `docs/memoire/lecons.md`).
4. Les redirections et les 410 passent par le plugin « Budget de crawl »
   (`dcp_crawl_redirections()`, `urls-piratage.php`), jamais par un plugin tiers.
   Ajouter le cas aux tests (`wordpress/tests/test-crawl-fix.sh`).

## 4. Mettre à jour une page périmée

- Remplacer les modèles et versions datés par les actuels, **vérifiés** (pas de
  mémoire) ; si une capture montre une ancienne interface, la refaire.
- Si la page est un lead magnet, suivre le skill `lead-magnet` (version 2 :
  logos, échanges avec Claude, preuves, pop-up campagne).
- Mettre à jour la ligne Notion « Cartographie SEO » (Action, Dernière MAJ).

## 5. Rendu

Livrer le tableau `audit.md` résumé : combien de pages par verdict, les 5
actions les plus rentables (celles qui ont déjà des impressions), et ce qui a
été laissé volontairement tel quel, avec la raison.
