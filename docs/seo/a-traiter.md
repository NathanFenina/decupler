# À traiter — SEO de decupler.com

Relevé le 29/09/2026 depuis Search Console (propriété `https://decupler.com/`),
avec la méthode decupler-seo 3.4. À reprendre dans la conversation dédiée à
Décupler. Cocher au fur et à mesure.

## 1. Le piratage : nettoyé, mais le trafic réel a baissé de moitié

- Le pic de juin (1 918 clics la semaine du 15/06) était du spam : requête
  « mahjongjp88 » sur la page d'accueil, pages casino et `/detail/…`.
  Les URL de spam répondent aujourd'hui 410 (casino) ou 404 (`/detail/`) :
  plus aucune requête de spam dans Search Console. **Nettoyage OK.**
- Trafic réel : 35 à 48 clics par semaine en mai, 15 à 20 aujourd'hui.
  Pages qui reçoivent des impressions : 170 (avril-mai) → 95 (septembre).
- [ ] Vérifier dans Search Console > Sécurité et actions manuelles qu'aucune
      action n'est en cours.
- [ ] Lister les pages légitimes qui ont perdu toutes leurs impressions
      depuis mai (désindexées pendant le piratage ?) et les faire réindexer.

## 2. Cannibalisation : un mot-clé, plusieurs pages

- [ ] « agence geo » : /agence-geo/, /agences-geo-france/, /meilleure-agence-geo/
- [ ] « agence geo nice » : /agence-seo/ et /agence-geo-nice/ — /agence-seo/
      est positionnée sur « agence geo nice » au lieu de « agence seo », et
      c'est la plus forte baisse du mois (24e → 45e).
- [ ] « eeat » : /eeat-google/ et /e-e-a-t/ (fusionner, redirection 301)

## 3. Pages commerciales loin dans les résultats (90 jours)

| Page | Impressions | Position |
|---|---|---|
| /agence-geo/ | 1 836 | 63 |
| /accompagnement-seo/ | 790 | 59 |
| /audit-geo/ | 1 612 | 38 |
| /agence-seo/ | 606 | 34 |

- [ ] Plan de reconquête des pages d'offre (brief par `serp_concurrents.py`,
      design `seo-design-pages`, triplets, maillage depuis les articles).

## 4. Gisements rapides (beaucoup d'impressions, peu de clics)

- [ ] /claude-skills-seo/ : 3 995 impressions, position 21, CTR 0,2 %
      (et baisse 4e → 9e sur « skills seo » ce mois-ci)
- [ ] /installer-mcp-data-for-seo-sur-chatgpt/ : 1 575 impressions,
      position 25 (mais 3e sur « mcp data for seo »)

## 5. Cartographie

- `memoire/cartographie.csv` : 161 lignes proposées automatiquement
  (`cartographie.py initialiser`), à **fusionner avec le dashboard Notion
  existant** de la cartographie Décupler, qui fait foi.
- `docs/seo/cartographie-2026-09.md` : premier tableau mensuel.
- [ ] Page d'accueil : son mot-clé principal détecté est
      « cherche agence seo avec supervision humaine 24/7 » — à choisir.
- [ ] Remplacer les prompts proposés (« Que faut-il savoir sur… ») par de
      vraies questions, puis mesurer ChatGPT/Gemini
      (`cartographie.py mensuel --prompts`).
- [ ] 89 pages sans mot-clé principal (pas assez de données) : à attribuer
      ou à regrouper.

## 6. Design (relevé par l'audit des composants)

- [ ] Popup aimant à leads : pas de bouton fermer, bloque le défilement,
      s'ouvre à 5 s sur mobile (interstitiel intrusif pour Google) →
      composant email-gate accessible.
- [ ] Bannières WordPress : chiffres sans source (« +235 % », « 5.0/5 »),
      icônes emoji, Google Fonts chargées dans la bannière.
- [ ] Contraste : blanc sur violet des CTA à 4,23:1 (minimum 4,5:1).
