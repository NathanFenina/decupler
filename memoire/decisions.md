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
| 2026-10-01 | **Une seule routine, le vendredi 7 h 07** (`routines/hebdo.md`) ; les quatre anciennes sont désactivées | Trop de routines pour un site à 15-20 clics/semaine | Nathan |
| 2026-10-01 | **Page de suivi en onglets par mois** : à décider (bloqué, à valider), fait, à faire par chantier, wins, contenus, reporting ; copie de la roadmap dans `journal/pilotage.json` | Une page complète qui recense tout | Nathan |
| 2026-10-01 | **Notion = bibliothèque des contenus**, alimentée depuis le dépôt ; `memoire/cartographie.csv` fait foi | Naviguer facilement sans risque de perdre l'information | Nathan / Claude |
| 2026-10-01 | **Pages villes** : une page par intention ; « expert seo + ville » et « agence référencement + ville » sont absorbés par les pages consultant/agence existantes, pas de page dédiée | Volumes faibles (30 à 210/mois), cannibalisation | Claude (22/09), rappelé le 01/10 |

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
  `netlinking-outreach` ; les analyses Search Console passent par
  `seo-gsc-analyses` de la méthode (les `gsc-*` en doublon ont été retirés le 01/10).
- **Points ouverts** : `docs/seo/a-traiter.md` (piratage, cannibalisation,
  pages d'offre loin, design). À traiter avant de lancer du contenu neuf sur
  les mêmes sujets.
- Le thème WordPress est fait par un freelance externe : les routines ne
  touchent jamais au thème ni au CSS global.

## Avant le 30/09 — reprises de l'ancienne mémoire (docs/memoire, fusionnée le 01/10)

### Règles permanentes (Nathan)

- Ne jamais inventer : adresse (seule : 10 avenue Lympia, 06300 Nice), chiffre
  client, note, avis, anecdote. Une image générée ne représente jamais un lieu
  réel ni une personne de l'équipe.
- Secrets dans `.env`, jamais dans le dépôt ni dans la conversation.
- Ne jamais charger l'export XML WordPress (23 Mo) dans la conversation.
- Accès Notion permanent : ne plus demander (22/09). Depuis le 30/09, Notion
  n'est plus la source : `memoire/cartographie.csv` fait foi, Notion sert de
  bibliothèque des contenus (01/10). Agir sans demander
  d'autorisation à chaque étape (29/09) ; les actions irréversibles restent
  réversibles quand c'est possible (rétrograder plutôt que supprimer, sauvegarder
  avant d'écrire).
- Pas d'identifiant de modèle d'IA dans les commits ni les contenus publiés.

### SEO et contenu

- Pages locales : « agence » pour le 06 et le Var, « consultant » pour les
  grandes villes ; une page seulement là où il y a des recherches (22/09).
- Doublons d'intention : redirection 301 seulement si la cible couvre déjà
  l'intention ; sinon on garde les deux et on relie (23/09).
- Spam du piratage : 410 + sitemap des URL supprimées, pas de demandes de
  suppression une par une ; les préfixes restants ne valent pas le temps
  (0 impression depuis juillet) (29/09).
- Lead magnets : pop-up obligatoire seulement pour `?acces=linkedin` ; Google
  lit librement (pénalité des interstitiels intrusifs sur mobile) (28/09).
- Chaque lead magnet a un mot-clé principal ET un prompt IA principal (29/09).
- /claude-code-design/ remplace le guide « site premium en 24h » (28/09),
  mot-clé « claude code design » (170/mois, difficulté 20).

### Technique

- Tout correctif serveur passe par un plugin versionné et testé dans un vrai
  WordPress (banc SQLite + Yoast), jamais par un réglage fait à la main dans
  l'admin sans trace.
- Trio sémantique : une seule Organisation (`#organization`) et une seule
  Personne (`#nathan-fenina`) ; les blocs JSON-LD référencent ces @id (29/09).
- Le thème final sera fait par un freelance : le contenu reste en HTML
  sémantique, sans dépendance à Elementor pour les nouvelles pages.
