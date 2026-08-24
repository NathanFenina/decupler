# Skills installés

Installés avec `npx skills add`, pas commités (4 Mo de dépendances tierces).
Pour les remettre en place sur une machine neuve :

```bash
npx skills add pbakaus/impeccable                       # design : critique, animate, bolder, polish
npx skills add anthropics/skills@frontend-design        # direction artistique, anti-template
npx skills add leonxlnx/taste-skill@design-taste-frontend  # anti-slop landing pages
npx skills add coreyhaines31/marketingskills@ai-seo     # citabilité LLM, AEO/GEO
npx skills add coreyhaines31/marketingskills@seo-audit  # audit on-page
npx skills add addyosmani/web-quality-skills@seo        # SEO technique, Lighthouse
npx skills add agricidaniel/claude-seo@seo-geo          # GEO, position officielle Google
```

## Qui sert à quoi

| Besoin | Skill |
|---|---|
| La page est fade, manque de personnalité | `frontend-design`, `design-taste-frontend` |
| Ajouter de l'animation, du mouvement | `impeccable animate` |
| La page est trop sage | `impeccable bolder` |
| Contrôle qualité avant publication | `impeccable audit` + `impeccable critique` |
| Profondeur de contenu, structure Hn | `seo-audit` |
| Être cité par ChatGPT / Perplexity | `ai-seo`, `seo-geo` |
| SEO technique, schema, sitemap | `seo` |

Deux skills existent déjà côté claude.ai (pas dans ce dépôt) :
`decupler-seo-geo-score` et `seo-geo-score` — ils notent /100 puis réécrivent.
