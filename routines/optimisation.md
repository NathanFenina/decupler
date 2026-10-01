# Routine d'optimisation — le jeudi, 7 h 27

0. `git fetch origin main && git checkout -B claude/optimisation-<AAAA-MM-JJ> origin/main`. Tu es le SEO manager de decupler.com : lis CLAUDE.md, memoire/decisions.md et docs/seo/a-traiter.md.

## Roadmap d'abord (skill seo-pilotage)

1. Lis le tableau de bord https://claude.ai/artifact/Rb2sP3EQFzedk6G2Xau6KA avec l'outil Artifact (action read) et enregistre le HTML reçu dans `donnees/tableau-de-bord.html` (jamais commité).
2. `python3 .claude/decupler-seo/scripts/pilotage.py etat --html donnees/tableau-de-bord.html --projet-id decupler --statut validee`
3. Exécute en priorité les actions validées de type « optimisation », en respectant leur note. Pour chacune : `python3 .claude/decupler-seo/scripts/pilotage.py marquer --html donnees/tableau-de-bord.html --projet-id decupler --id <id> --statut en-cours`, republie ; une fois livrée, `--statut faite --lien <PR ou URL>`, republie. Bloquée : remets `validee` avec `--note` qui dit pourquoi.
4. Republier = outil Artifact, publish, `url` https://claude.ai/artifact/Rb2sP3EQFzedk6G2Xau6KA, `file_path` donnees/tableau-de-bord.html, sans capabilities. En cas de conflit : relis la page, refais le marquage, republie une fois.

## Puis le travail de la semaine

1. Skill seo-cycle en mode optimisation ; seo-opportunites pour choisir les pages. Ne touche pas aux pages en cannibalisation tant que la décision n'est pas validée sur le tableau de bord.
2. Sur WordPress, uniquement par `python3 .claude/decupler-seo/scripts/wp.py` : title et meta (`wp.py meta`), contenus en révision, jamais de mise en ligne directe d'une page publiée ; garde-fou respecté. Skills du projet : yoast-score, decupler-page-builder.
3. Journalise chaque modification avec seo-journal-mesure. Liste dans `rapports/a-valider.md` ce qui attend une validation dans l'admin WordPress.
4. Pousse, ouvre une pull request vers main et fusionne-la (fichiers du dépôt seulement). Journal de run `rapports/runs/<AAAA-MM-JJ>-optimisation.md`.

**Si une étape est refusée** par les permissions de la session (fusion, suppression, push) : n'insiste pas et n'attends aucune réponse, personne ne lit pendant la routine. Laisse la PR ouverte avec « à fusionner par un humain » dans sa description et dans le journal de run, ajoute-la sur le tableau de bord (`pilotage.py ajouter --titre "Fusionner la PR <n°>" --statut validee --lien <PR>`, puis republie), et termine. Les fichiers `donnees/tableau-de-bord.html`, `donnees/pilotage.json` et `donnees/actions-*.json` sont ignorés par git : ne les supprime pas.
