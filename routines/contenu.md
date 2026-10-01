# Routine de contenu — le mardi, 7 h 22

> Ancienne routine, remplacée le 01/10/2026 par `routines/hebdo.md` (le vendredi). Gardée comme détail des étapes.

0. `git fetch origin main && git checkout -B claude/contenu-<AAAA-MM-JJ> origin/main`. Tu es le SEO manager de decupler.com : lis CLAUDE.md, memoire/decisions.md et docs/seo/a-traiter.md.

## Roadmap d'abord (skill seo-pilotage)

1. Lis le tableau de bord https://claude.ai/artifact/Rb2sP3EQFzedk6G2Xau6KA avec l'outil Artifact (action read) et enregistre le HTML reçu dans `donnees/tableau-de-bord.html` (jamais commité).
2. `python3 .claude/decupler-seo/scripts/pilotage.py etat --html donnees/tableau-de-bord.html --projet-id decupler --statut validee`
3. Exécute en priorité les actions validées de type « contenu », en respectant leur note. Pour chacune : `python3 .claude/decupler-seo/scripts/pilotage.py marquer --html donnees/tableau-de-bord.html --projet-id decupler --id <id> --statut en-cours`, republie ; une fois livrée, `--statut faite --lien <PR ou URL>`, republie. Bloquée : remets `validee` avec `--note` qui dit pourquoi.
4. Republier = outil Artifact, publish, `url` https://claude.ai/artifact/Rb2sP3EQFzedk6G2Xau6KA, `file_path` donnees/tableau-de-bord.html, sans capabilities. En cas de conflit : relis la page, refais le marquage, republie une fois.

## Puis l'article de la semaine

1. Un article : action validée de type contenu, sinon le calendrier (`rapports/calendrier-*.md`) ou le classement des opportunités ; jamais un sujet en cannibalisation.
2. Enchaîne serp_concurrents.py, brief avec triplets, rédaction dans le style de `memoire/style.md` (skills redaction-article / redaction-expert du projet), design (seo-design-pages + decupler-page-builder), images (`images_generer.py` si aucune image réelle), contrôles bloquants.
3. Publie en **brouillon** WordPress avec `python3 .claude/decupler-seo/scripts/wp.py publier` (jamais en ligne), ajoute l'article à `rapports/a-valider.md` avec son lien d'aperçu, journalise-le (page-neuve, avec les requêtes visées) et ajoute-le à `memoire/cartographie.csv`.
4. Pousse, ouvre une pull request vers main et fusionne-la (fichiers du dépôt seulement). Journal de run `rapports/runs/<AAAA-MM-JJ>-contenu.md`.

**Si une étape est refusée** par les permissions de la session (fusion, suppression, push) : n'insiste pas et n'attends aucune réponse, personne ne lit pendant la routine. Laisse la PR ouverte avec « à fusionner par un humain » dans sa description et dans le journal de run, ajoute-la sur le tableau de bord (`pilotage.py ajouter --titre "Fusionner la PR <n°>" --statut validee --lien <PR>`, puis republie), et termine. Les fichiers `donnees/tableau-de-bord.html`, `donnees/pilotage.json` et `donnees/actions-*.json` sont ignorés par git : ne les supprime pas.
