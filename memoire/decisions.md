# Décisions

Une ligne par décision humaine. Les agents lisent ce fichier avant de
proposer quoi que ce soit : une proposition déjà refusée ne revient pas.

C'est aussi ici qu'un projet adapte la méthode sans la modifier : un dossier
de benchmarks ou une source des faits à un autre endroit, une routine de
contenu déjà en place, une règle propre au client.

| Date | Décision | Contexte | Par |
|---|---|---|---|
| 2026-09-30 | Création du projet | Onboarding |  |

## 2026-09-30 — Adoption de decupler-seo (Claude, pour Nathan)

- **Publication WordPress en brouillon** (`scripts/wp.py` de la méthode, mode
  `assisted`) : les routines créent et modifient en brouillon ou en révision ;
  la mise en ligne reste une validation humaine dans l'admin WordPress.
- **Cartographie** : le dashboard Notion « Cartographie SEO — Décupler » fait
  foi. `memoire/cartographie.csv` est la copie de travail des routines ; la
  réconcilier avec Notion avant toute décision (skill `seo-cartographie`).
- **Skills propres au projet prioritaires** : `decupler-page-builder`,
  `redaction-article`, `redaction-expert`, `yoast-score`, `lead-magnet`,
  `netlinking-outreach` et les analyses `gsc-*` de `.claude/skills/`.
- **Points ouverts** : `docs/seo/a-traiter.md` (piratage, cannibalisation,
  pages d'offre loin, design). À traiter avant de lancer du contenu neuf sur
  les mêmes sujets.
- Le thème WordPress est fait par un freelance externe : les routines ne
  touchent jamais au thème ni au CSS global.
