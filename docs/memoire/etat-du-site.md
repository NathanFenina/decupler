# État de decupler.com — mémoire de travail

Dernière mise à jour : **29/09/2026**. À relire au début de chaque session, à
mettre à jour à la fin. Ce qui est ici a été vérifié sur le site en ligne.

## Plugins maison (wordpress/plugins/)

| Plugin | Version en ligne | Version dans le dépôt | Rôle |
|---|---|---|---|
| decupler-crawl-fix « Budget de crawl » | **1.3.4** | 1.3.4 | robots.txt, llms.txt, 410 des 350 URL de spam, redirections 301, pages hors index, purge du cache Elementor |
| decupler-popup « Pop-up Workshop » | 1.0.0 | 1.0.0 | Invitation au workshop du 8/10, s'arrête seule le 8/10 à 12 h 30 |
| decupler-entite « Entité » | **1.0.1** | 1.0.1 (`url` de la Personne = /nathan-fenina/) | Organisation + Nathan Fenina dans le graphe Yoast (trio sémantique) |
| decupler-yoast-rest | 1.0 | hors dépôt | Expose les métas Yoast à l'API REST |

Nathan installe les ZIP à la main (Extensions → Téléverser → Remplacer).
Constaté le 30/09 : crawl-fix 1.3.4 et entite 1.0.1 actives.

## Réglages et scripts posés en ligne (hors plugins)

- **En-tête du site** = template Elementor **2762**, un seul widget HTML
  (`.dcp-header`). Contient : menu codé en dur (bureau + mobile), bouton
  « Workshop live · 8 oct. », et le **contrôleur des pop-ups lead magnet**
  (`design-system/snippets/controleur-lead-magnet.js`). Sauvegardes dans
  `scratchpad/conso/backup-2762-*`.
- **Pied de page** = template Elementor **2788** (widget HTML `.footer-seo-ia`).
  29/09 : ajout de `box-sizing:border-box` (il débordait de 40 px sur mobile,
  sur toutes les pages). Sauvegarde : `scratchpad/conso/backup-2788-footer-avant-boxsizing.json`.
- Page en gabarit **elementor_canvas** (pas d'en-tête) : creer-app-ecommerce
  (7668) — contrôleur injecté dans son widget. claude-skills-seo (7679) est
  repassée en gabarit par défaut le 29/09 (refonte v2).
- Réglage `dcp_popup.exclusions` : toutes les pages lead magnet (sinon la
  pop-up Workshop s'empile sur la leur).

## Pop-ups email (lead magnets)

- Lien de campagne LinkedIn : `https://decupler.com/<slug>/?acces=linkedin`
  → pop-up obligatoire. Tous les autres visiteurs : pop-up fermable à 25 s.
- Ciblage mot-clé + prompt de chaque lead magnet : `content/lead-magnets/ciblage.json`
  et base Notion « Cartographie SEO » (97c5e3eaa05b4d0aa2277004a93971f6).

## Sécurité

- 29/09 : **7 comptes administrateurs « maintable »** (IDs 6 à 12, sans email,
  inscrits « en 2020 », insérés directement en base) → rétrogradés abonnés,
  mots de passe aléatoires. Sauvegarde : `scratchpad/conso/backup-comptes-maintable.json`.
  Contrôle programmé le 30/09. Reste à faire par la freelance : scan Wordfence
  complet, inspection de `wp-content/mu-plugins/` et du `functions.php` du
  thème, puis suppression des comptes.
- Comptes légitimes : 3 (admin6091, « Nathan Fenina », utilisé par l'API) et
  5 (admin@decupler.com).

## Search Console

- 30/08 → 26/09 : 1 seule impression sur les pages de spam (contre 3 308 en
  mai). Le compteur « Dans l'index » (321) baissera quand Google repassera sur
  les 410 (sitemap des URL supprimées lu le 28/09).
- Pages locales et nouvelles pages : détectées, pas encore indexées ;
  demandes d'indexation manuelles en cours (Nathan).

## Pages récentes

- /jev-seo/ (21035) publiée le 30/09, refaite en v2 le même jour (design +
  kit ZIP `kit-jev-seo-geo-decupler.zip`, sources `content/lead-magnets/kit-jev-seo-geo/`) :
  playbook Jev (mot-clé « jev seo »), menu
  Nos Pépites, exclue de la pop-up Workshop, CTA workshop du 8/10 à remplacer
  après l'événement (rappel du 8/10). Preuve : audit jev-seo réel de
  decupler.com, 97 → 98 après corrections du 30/09 : 9 liens cassés
  (/a-propos, /search-everywhere), titles/metas en double
  (audit-geo-claude-code, seo-geo-team), lien du pied de page 2788 vers
  l'ancien guide. Sauvegardes : scratchpad/conso/liens-casses/.
- /claude-skills-seo/ (7679) refaite en v2 le 29/09 (mot-clé « claude seo ») :
  pack ZIP de 10 skills en français (média 21004,
  `uploads/2026/09/skills-seo-claude-decupler.zip`, sources dans
  `content/lead-magnets/skills-seo-claude/`), 3 captures Search Console
  anonymisées (médias 21001-21003), logos 20996-20999 (Search Console, DataForSEO,
  Screaming Frog, WordPress). Ancienne version : `archives/pages-avant-refonte/`.
- /claude-code-design/ (20928) publiée le 28/09 ; remplace l'ancien guide
  « site premium en 24h » (6263), redirection dans crawl-fix 1.3.4.
- 21 pages locales publiées (23-24/09), GEO Ready (20880).
- /nathan-fenina/ (20995) : page d'entité **publiée le 29/09** avec son parcours
  (ingénieur en informatique ; développeur et chef de projet digital chez de
  grands comptes : Société Générale, Decathlon, Pluxee). Signatures de
  /claude-skills-seo/ et /claude-code-design/ reliées à cette page.
- 48 pages : blocs JSON-LD `Person` reliés à `#nathan-fenina`, URL LinkedIn
  unifiée (`/in/nathan-fenina/`) le 29/09.
- Audit « pages pourries » du 29/09 : 4 vides (restes WooCommerce, hors index),
  1 morte, 13 périmées, 20 à pousser — voir le skill `pages-pourries`.
