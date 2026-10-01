# Décisions

Une ligne par décision humaine. Les agents lisent ce fichier avant de
proposer quoi que ce soit : une proposition déjà refusée ne revient pas.

C'est aussi ici qu'un projet adapte la méthode sans la modifier : un dossier
de benchmarks ou une source des faits à un autre endroit, une routine de
contenu déjà en place, une règle propre au client.

| Date | Décision | Contexte | Par |
|---|---|---|---|
| 2026-09-30 | Création du projet | Onboarding |  |
| 2026-10-01 | **Anglais sans plugin multilingue** : pages `decupler.com/en/<page>/` (page parente `en`, `lang`/hreflang par le plugin « Budget de crawl », retirer d'abord la 301 sur `/en/`) ; cibles États-Unis (GEO/IA) et Moyen-Orient (SEO local, Dubaï) | Décision de Nathan | Nathan |
| 2026-10-01 | **Une seule page de suivi** : la roadmap vit en haut de « Chantiers decupler.com » ; la page « Pilotage Décupler » est supprimée | Éviter les doublons entre conversations | Nathan |
| 2026-10-01 | **Pilotage depuis ce dépôt uniquement** ; contexte dans `memoire/passation.md` | Fin de la conversation commune aux trois projets | Nathan |

## 2026-09-30 — Adoption de decupler-seo (Claude, pour Nathan)

- **Publication WordPress en brouillon** (`scripts/wp.py` de la méthode, mode
  `assisted`) : les routines créent et modifient en brouillon ou en révision ;
  la mise en ligne reste une validation humaine dans l'admin WordPress.
- **Cartographie et suivi** (30/09, décision de Nathan) : plus de Notion.
  `memoire/cartographie.csv` fait foi, et la page de suivi
  https://claude.ai/artifact/Rb2sP3EQFzedk6G2Xau6KA trace roadmap, avancement
  et chiffres (skills `seo-cartographie` et `seo-pilotage`). L'ancienne base
  Notion reste une archive, à consulter pour reprendre ses données.
- **International** (30/09) : version anglaise pour les États-Unis (demande
  GEO et IA) et le Moyen-Orient (SEO local, Dubaï en tête), plus des pages
  francophones hors de France (Québec, Belgique, Suisse, Maghreb). Détail et
  volumes dans la page de suivi.
- **Skills propres au projet prioritaires** : `decupler-page-builder`,
  `redaction-article`, `redaction-expert`, `yoast-score`, `lead-magnet`,
  `netlinking-outreach` et les analyses `gsc-*` de `.claude/skills/`.
- **Points ouverts** : `docs/seo/a-traiter.md` (piratage, cannibalisation,
  pages d'offre loin, design). À traiter avant de lancer du contenu neuf sur
  les mêmes sujets.
- Le thème WordPress est fait par un freelance externe : les routines ne
  touchent jamais au thème ni au CSS global.
