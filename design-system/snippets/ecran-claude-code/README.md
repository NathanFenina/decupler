# Écrans « Claude Code » pour les pages

Mise en forme d'un **échange réel** dans un terminal Claude Code, rendue en
image nette par Chromium. On ne passe pas par un générateur d'images (Gemini) :
il déforme le texte.

Règles :
- les chiffres viennent de la vraie source (Search Console, audit, API), relevés
  le jour même ; la période figure dans l'écran et dans la légende ;
- la légende reprend les chiffres en texte (Google et les IA ne lisent pas
  l'image) et la page dit que les écrans sont « mis en forme à partir des
  échanges réels » ;
- jamais d'échange inventé présenté comme réel.

Rendu (1,5x, pleine page) :

    cd design-system/snippets/ecran-claude-code
    node capture.mjs quick-wins-search-console audit-pages   # → .png

Puis conversion en JPEG (qualité 88) et `scripts/wp_upload_media.py`.
Exemples en ligne : /claude-skills-seo/, section « En vrai ».
