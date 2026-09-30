# Routine de rapport — le 1er du mois, 7 h 37

0. `git fetch origin main && git checkout -B claude/rapport-<AAAA-MM-JJ> origin/main`. Tu es le SEO manager de decupler.com : lis CLAUDE.md, memoire/decisions.md et docs/seo/a-traiter.md.

## Le rapport

1. Skill seo-cycle en mode rapport : mesure les modifications arrivées à échéance, mets à jour memoire/apprentissages.md, régénère la demande et le calendrier du mois.
2. `python3 .claude/decupler-seo/scripts/cartographie.py mensuel --prompts` (ChatGPT et Gemini).
3. `rapport.py` : rapports/<AAAA-MM>.md et .json, section « Lecture et décisions » rédigée. Mets à jour `docs/seo/a-traiter.md` (ce qui est réglé, ce qui reste). Vérifie les runs du mois (rapports/runs/ et branches claude/*) et signale toute absence en tête du rapport.

## Roadmap du mois (skill seo-pilotage)

1. Lis le tableau de bord https://claude.ai/artifact/Rb2sP3EQFzedk6G2Xau6KA avec l'outil Artifact (action read) et enregistre le HTML reçu dans `donnees/tableau-de-bord.html` (jamais commité).
2. Puis :
   ```bash
   python3 .claude/decupler-seo/scripts/pilotage.py donnees --sortie donnees/pilotage.json
   python3 .claude/decupler-seo/scripts/pilotage.py proposer --mois <AAAA-MM du mois qui commence> --projet-id decupler --sortie donnees/actions-<AAAA-MM>.json
   python3 .claude/decupler-seo/scripts/pilotage.py injecter --html donnees/tableau-de-bord.html --projet-id decupler --donnees donnees/pilotage.json --actions donnees/actions-<AAAA-MM>.json
   ```
3. Republie avec l'outil Artifact (publish, `url` https://claude.ai/artifact/Rb2sP3EQFzedk6G2Xau6KA, `file_path` donnees/tableau-de-bord.html, sans capabilities). En cas de conflit : relis, refais l'injection, republie une fois.
4. Résume dans le rapport les actions proposées ; Nathan les valide sur le tableau de bord.

## Livrer

Commite, pousse, ouvre une pull request vers main et fusionne-la (fichiers du dépôt seulement). Journal de run `rapports/runs/<AAAA-MM-JJ>-rapport.md`.
