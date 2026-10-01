# Routine hebdo — le vendredi, 7 h 07 (Paris)

La seule routine de decupler.com depuis le 01/10/2026. Elle remplace la
veille quotidienne, l'optimisation, le contenu et le rapport mensuel, dont
les fichiers restent dans `routines/` comme détail des étapes.

Personne ne lit pendant la routine : elle ne pose aucune question et
n'attend aucune réponse.

## 0. Partir propre
`git fetch origin main && git checkout -B claude/hebdo-<AAAA-MM-JJ> origin/main`.
Tu es le SEO manager de decupler.com : lis `CLAUDE.md`, `memoire/decisions.md`,
`memoire/passation.md` et `docs/seo/a-traiter.md`. Journal de run
`rapports/runs/<AAAA-MM-JJ>-hebdo.md` écrit dès maintenant, complété à la fin.

## 1. Contrôle du site (lecture seule)
Skill `seo-cycle`, mode veille : `seo_live.py --json`, pages prioritaires,
robots.txt, sitemap. **Retour du spam** (requêtes casino, slot, mahjong… dans
Search Console, URL inconnues) : alerte prioritaire, en tête du bilan et en
action `bloquee` (étape 5).

## 2. Les chiffres
`python3 .claude/decupler-seo/scripts/gsc.py instantane`, puis
`journal.py mesurer-tout --auto` : on mesure avant de modifier.

## 3. La page de suivi et les actions validées
1. Lis https://claude.ai/artifact/Rb2sP3EQFzedk6G2Xau6KA (outil Artifact,
   action read) et enregistre le HTML reçu dans `donnees/tableau-de-bord.html`.
2. `python3 .claude/decupler-seo/scripts/pilotage.py etat --html donnees/tableau-de-bord.html --projet-id decupler --statut validee`
3. Exécute-les, tous chantiers confondus, en respectant leur remarque :
   `marquer --statut en-cours` puis republie ; livrée : `--statut faite --lien <URL>` ;
   impossible sans quelqu'un : `--statut bloquee --attend "<qui ou quoi>"`.
   Les `decision` attendent Nathan.
4. WordPress uniquement par `.claude/decupler-seo/scripts/wp.py` (brouillon ou
   révision, sauvegarde automatique). Jamais le thème ni le CSS global (freelance).
   Chaque modification au journal (`seo-journal-mesure`).
5. Rien de validé : le travail automatique du mode optimisation (titles,
   metas, FAQ, schema, liens internes), dans ses plafonds, hors pages en
   cannibalisation. Aucune page neuve sans action validée.

## 4. Le premier vendredi du mois, en plus
Le rapport du mois écoulé et les propositions du mois : étapes de
`routines/rapport.md` (rapport, cartographie, `pilotage.py donnees`,
`proposer`, `injecter`).

## 5. Le bilan de la semaine dans la page
Écris `donnees/semaine.json` puis
`python3 .claude/decupler-seo/scripts/pilotage.py mois --html donnees/tableau-de-bord.html --projet-id decupler --fichier donnees/semaine.json` :
```json
{"mois": "AAAA-MM",
 "semaine": {"date": "<lundi de la semaine>", "resume": "3 lignes : fait, appris, bloqué",
             "chiffres": {"clics": 0, "impressions": 0}},
 "wins": [{"texte": "un gain mesuré et chiffré", "detail": "source", "lien": "preuve"}],
 "contenus": [{"titre": "", "url": "", "statut": "brouillon|publié|mis à jour", "date": "AAAA-MM-JJ", "notion": ""}],
 "reporting": {"clics": 0, "impressions": 0}}
```
- Un win est un fait mesuré (position, clics, citation IA, page indexée),
  jamais une intention ni un chiffre absent des données.
- Chaque point bloquant devient une action `bloquee` qui dit qui on attend.
- Republie (outil Artifact, publish, `url` ci-dessus, `file_path`
  `donnees/tableau-de-bord.html`, sans capabilities ; conflit : relire,
  refaire, republier une fois), puis
  `pilotage.py sauvegarder --html donnees/tableau-de-bord.html --projet-id decupler`.

## 6. Livrer
Commite (dont `journal/pilotage.json`), pousse, ouvre une PR vers main et
fusionne-la (fichiers du dépôt seulement). **Étape refusée** par les
permissions : PR laissée ouverte avec « à fusionner par un humain » dans sa
description et le journal de run, action `bloquee` sur la page
(`--attend "Nathan : fusionner la PR <n°>"`), republication, fin.
`donnees/tableau-de-bord.html`, `donnees/pilotage.json`, `donnees/actions-*.json`
et `donnees/semaine.json` sont ignorés par git : ne les supprime pas.
