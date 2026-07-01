---
name: lead-magnet
description: >-
  Crée une landing « lead magnet » Décupler (aimant à emails) : une offre de
  contenu gratuit à forte valeur, dans le skin clair « home-aligned », avec une
  popup de capture email branchée sur Substack (le contenu se débloque contre
  un email). Idéal pour les campagnes « commente X sur LinkedIn → reçois le
  guide ». Produit le HTML .lm-mcp + la popup gate, puis publie en brouillon
  WordPress. À utiliser quand l'utilisateur dit : « crée une page lead magnet »,
  « une landing pour capturer des emails », « le guide gratuit contre email ».
---

# Skill : lead-magnet — landing aimant à emails (→ Substack)

Objectif : une page qui **donne beaucoup de valeur** ET **capture l'email** via
une popup branchée sur Substack. Même exigence de fond que `redaction-expert`
(profondeur, données, sources) — c'est un contenu premium, pas un teaser creux.

## Le mécanisme de capture (déjà intégré à `build_article.py`)
- Une **popup** apparaît après quelques secondes (scroll bloqué, contenu flouté).
- Le formulaire **POST vers Substack** (`{substack}/api/v1/free`) dans un
  **iframe caché** (contourne le cross-domaine → pas de redirection).
- Au submit → l'iframe se charge → **contenu débloqué**, abonnement **mémorisé**
  (localStorage + cookie `lmg_sub`) pour ne plus réafficher la popup.
- `?reset=true` dans l'URL réinitialise (pour tester).
- Substack Décupler : `https://decupler.substack.com`.

## Procédure
1. **Rédiger le corps** `content/articles/<slug>.body.html` au format `.lm-mcp`
   (hero + badge, réponse/offre claire, preuve chiffrée via `.statband`/
   `.metric-row`, le contenu de valeur en `.steps`/`.checklist`/`.aa-grid`,
   tableau comparatif, FAQ, CTA de conversion). Skin clair « home-aligned ».
   Appliquer les principes de [[redaction-expert]] (données, sources, « comment »).
2. **FAQ** : `content/articles/<slug>.faq.json`.
3. **Assembler AVEC la popup gate** :
   ```bash
   python3 scripts/build_article.py \
       --body content/articles/<slug>.body.html \
       --title "<title>" --description "<meta>" \
       --faq content/articles/<slug>.faq.json \
       --extra-css design-system/landing/lm-mcp-light.css design-system/landing/lm-mcp-decupler.css design-system/landing/lm-mcp-leadmagnet.css \
       --img "__IMG_1__=<url>" \
       --gate "https://decupler.substack.com" \
       --gate-title "Débloquez le guide complet" \
       --gate-desc "Laissez votre email — je vous envoie le guide + mes meilleures méthodes." \
       --gate-delay 5000 \
       --out content/articles/<slug>.html
   ```
4. **Publier en brouillon** (`wp_publish.py --type page --status draft`), relire,
   puis publier. **Tester la popup** : ouvrir avec `?reset=true`, vérifier que
   l'email atterrit bien dans Substack (liste des abonnés).

## Bonnes pratiques
- **Valeur d'abord** : donne le contenu réel (pas juste un sommaire). Un lead
  magnet généreux se partage et convertit mieux.
- **CTA de sortie** : en bas, un CTA vers l'offre payante / le RDV (Calendly).
- La popup n'a **pas de bouton fermer** par défaut (gate assumé). Pour l'adoucir,
  ajouter un `.ai-popup-close` (croix) + un handler dans le script.
- ⚠️ **wpautop** : ne jamais mettre de CSS/JS multi-lignes dans le contenu ;
  `build_article.py` minifie et injecte le script gate sur une ligne (cf. piège
  documenté dans [[redaction-article]]).
