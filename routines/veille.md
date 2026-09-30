# Routine de veille — tous les jours, 7 h 17

0. `git fetch origin main && git checkout -B claude/veille-<AAAA-MM-JJ> origin/main`. Tu es le SEO manager de decupler.com : lis CLAUDE.md, memoire/decisions.md et docs/seo/a-traiter.md.
1. Skill seo-cycle en mode veille. N'écris rien sur le site WordPress.
2. Surveille en particulier tout retour de spam (requêtes casino, slot, mahjong… dans Search Console, URL inconnues) : alerte prioritaire dans `rapports/a-valider.md`.
3. Tout va bien : seul le journal de run `rapports/runs/<AAAA-MM-JJ>-veille.md`. Sinon décris l'anomalie dans `rapports/a-valider.md` (quoi, depuis quand, combien ça coûte, quoi faire).
4. Commite et pousse la branche.
