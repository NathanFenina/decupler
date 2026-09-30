---
name: lead-magnet
description: >-
  Crée ou refond une page « lead magnet » Décupler (aimant à emails vers
  Substack), version 2 : ciblée sur un mot-clé principal ET un prompt IA
  principal, authentique (logos et visuels réels des outils, échanges avec
  Claude, captures, preuves sourcées), et avec une pop-up obligatoire
  seulement pour la campagne LinkedIn (?acces=linkedin) — Google lit
  librement. Produit le HTML .lm-mcp, vérifie le rendu dans Chromium, publie
  et met à jour Notion. À utiliser pour : « crée une page lead magnet »,
  « le guide gratuit contre email », « refais ce lead magnet comme la page
  Claude Code design », « mets à jour les lead magnets », « commente X sur
  LinkedIn → reçois le guide ».
---

# Skill : lead-magnet v2 — une page qui donne tout, ranke, et capture l'email

Deux références : **/claude-code-design/** (28/09/2026) et
**/claude-skills-seo/** (29/09/2026, gabarit + générateur :
`content/articles/claude-skills-seo.body.tpl.html`,
`scripts/lead_magnet_claude_skills_seo.py`). La première est la page que
Nathan a jugée « nettement meilleure ». Ce qui a fait la différence, dans
l'ordre : les logos et visuels réels des outils, les échanges avec Claude
(« tu parles, Claude exécute »), les exemples réels (captures de sites), un
bloc « parti pris » signé, un bloc « ce que ça ne fait pas », et des commandes
repliées plutôt qu'étalées.

## 0. Avant d'écrire : cibler

1. **Mot-clé principal** : les requêtes réelles de la page (Search Console,
   180 jours, dimension page × requête) valent mieux que les volumes
   Ubersuggest, souvent vides sur ces niches. Choisir la requête qui a déjà
   des impressions en position 5-25, et une difficulté faible.
2. **Prompt principal** : la question qu'un utilisateur poserait à ChatGPT ou
   Perplexity et à laquelle la page doit être la réponse citée
   (« Quels skills installer dans Claude pour faire du SEO ? »).
3. Le ciblage de chaque lead magnet existant est dans
   `content/lead-magnets/ciblage.json` et dans la base Notion « Cartographie
   SEO » (colonnes Mot clé, Prompt principal, Fan query, Tracking de lead).
4. Vérifier la cannibalisation avec les pages voisines (`gsc-cannibalisation`).

Le mot-clé va dans le title, le H1, la meta, le premier paragraphe et un ou
deux H2. Le prompt principal devient une question de FAQ et la phrase-réponse
du premier écran.

## 1. Les blocs qui rendent la page authentique

| Bloc | Pourquoi | Comment |
|---|---|---|
| **Bande de logos** des outils cités | On voit tout de suite de quoi on parle | Logos officiels (favicon ou apple-touch-icon du site de l'outil, carrés 180 px), téléversés dans la médiathèque |
| **Visuel officiel par outil** | Preuve que l'outil existe, ancre visuelle | Image `og:image` du site de l'outil, légendée « Visuel officiel, <domaine> » |
| **Échanges avec Claude** (`.chat`) | Montre qu'on n'a rien à coder : on parle, Claude exécute | Bulle « Toi » + réponse de Claude + liste `.acts` des actions réelles qu'il lance. Toujours titrer « Exemple d'échange » : ce sont des illustrations, pas des transcriptions |
| **Commandes repliées** (`details.cmd`) | La valeur technique sans effrayer | Commandes vérifiées sur la doc officielle de chaque outil, jamais de mémoire |
| **Exemples réels** | La preuve par le résultat | Captures fournies par Nathan, légendées honnêtement (maquettes, clients, secteur) |
| **Anatomie / méthode** | Donne la méthode, pas seulement l'outil | Liste numérotée tirée des exemples réels |
| **Parti pris signé** (bande sombre `.dk`) | Une voix, une position | 2-3 paragraphes à la première personne, signés Nathan. Aucune anecdote inventée |
| **Ce que ça ne fait pas** (`.no`) | Le bloc le moins imitable | 4 limites concrètes |
| **Échanges réels** (`.chat-h.reel` ou écran `design-system/snippets/ecran-claude-code/`) | La preuve que la méthode tourne chez nous | Tâches vraiment faites sur decupler.com (quick wins GSC, audit pages pourries, trio sémantique), résumées, avec les chiffres du jour et la période. Titrer « Échange réel » |
| **Preuves Search Console** | Crédibilité | Captures fournies par Nathan, **noms de sites masqués** (accord du 29/09 : « pas besoin de citer les noms »). Légende factuelle : chiffres visibles, période, « site accompagné, nom masqué ». Avant avril 2024 (création de Décupler) : « accompagné par Nathan Fenina ». Préciser que la courbe vient d'un travail SEO complet, pas de l'outil seul. Médias déjà en ligne : 21001-21003. Ce sont des sites de Nathan (confirmé le 29/09) : légende « site piloté par Nathan Fenina, nom masqué » |
| **Livrable téléchargeable** | La valeur promise, tout de suite | Si la page promet des fichiers (skills, prompts, modèles) : un ZIP en téléchargement libre, sources versionnées dans `content/lead-magnets/<pack>/`. Exemple : `skills-seo-claude/` |
| **CTA** | Conversion | RDV Calendly en bas, encart d'inscription `.lmg-inline` sous la vidéo ou le premier bloc de valeur |

Règles de fond : jamais de chiffre client, d'avis ou de note inventés ; un
chiffre d'outil vient de sa documentation, avec la version relevée.

À retirer lors d'une refonte : affirmations invérifiables (« Top 20 SEO
France »), gains de temps chiffrés non mesurés, sections datées sur un modèle
d'IA précis. Remplacer une page existante **à la même URL** : sauvegarde du
contenu et de `_elementor_data`, `_elementor_edit_mode` vide, gabarit par
défaut (plus de `elementor_canvas`), ancienne version dans
`archives/pages-avant-refonte/`.

### Leçons de /jev-seo/ (30/09/2026, v1 jugée « pas convaincante » par Nathan)

- **Un lead magnet sans rien à emporter ne tient pas sa promesse.** Si le post
  promet un playbook, la page donne un **kit téléchargeable** (prompts,
  modèles, formules), en bande sombre dédiée, et le bouton du hero y mène.
- **Rythme** : appliquer `decupler-direction-artistique` (jamais plus de deux
  bandes claires d'affilée : ruban chiffré, bande kit sombre, parti pris avec
  la vraie photo de Nathan). La v1 enchaînait dix sections blanches.
- **Animations au défilement** (IntersectionObserver, classe `.io` → `.on`),
  jamais au chargement : sinon elles sont finies avant que le lecteur arrive.
- **Captures de rapport recadrées** sur la zone utile : une page A4 réduite à
  860 px est illisible.
- **Un parcours cliquable** des étapes (`.road` + ancres `#etape-N`) et un
  exemple avant / après concret (fictif assumé, crochets à la place des
  chiffres) valent plus qu'un paragraphe d'explication.
- Gabarit de référence : `content/articles/jev-seo.body.tpl.html`, assemblage
  `scripts/lead_magnet_jev_seo.sh`.

## 2. Assembler

```bash
python3 scripts/build_article.py \
    --body content/articles/<slug>.body.html \
    --title "<title avec le mot-clé>" --description "<meta>" \
    --faq content/articles/<slug>.faq.json \
    --extra-css design-system/landing/lm-mcp-light.css design-system/landing/lm-mcp-decupler.css design-system/landing/lm-mcp-leadmagnet.css \
    --gate "https://decupler.substack.com" \
    --gate-title "Accède au guide" --gate-desc "…" \
    --gate-delay 6000 --gate-param acces=linkedin --gate-soft-delay 25000 \
    --out content/articles/<slug>.html
```

`--gate-param acces=linkedin` : pop-up obligatoire (flou, défilement bloqué)
**seulement** pour les visiteurs du lien de campagne ; tous les autres ont une
pop-up fermable à 25 s, sans flou, une fois par session, plus l'encart
`.lmg-inline`. Le lien à mettre sur LinkedIn : `https://decupler.com/<slug>/?acces=linkedin`.

Les anciennes pages (Elementor, script maison) sont couvertes par le
**contrôleur** posé dans l'en-tête du site
(`design-system/snippets/controleur-lead-magnet.js`) ; les pages en gabarit
« canvas » n'ont pas d'en-tête : le contrôleur est alors injecté dans le widget
HTML qui contient `#ai-content-gate`.

## 3. Vérifier avant de publier (non négociable)

1. **Rendu Chromium** à 1440 et 390 px, images servies en local (le navigateur
   n'atteint pas decupler.com) : aucun débordement, grilles alignées
   (sonde : même `top` par rangée, en-têtes logo/titre centrés).
2. **Parcours pop-up** : LinkedIn obligatoire, Google fermable à 25 s, abonné
   plus rien. Avec des minuteries réelles si la page a son propre script (les
   horloges simulées ratent les `setTimeout` posés dans un MutationObserver).
3. **HTML rendu par WordPress** (`GET pages/{id}?context=edit` → `rendered`) :
   zéro `<br />`, `<p><a>`, `<p><img>`, `<p></p>` hors scripts de fin. Les
   éléments en ligne (`<span>`, `<a>`) d'un conteneur flex vont sur une seule
   ligne, sinon wpautop glisse des `<br>`.
3 bis. **Paragraphes vides visibles** : `node scripts/rendu/paragraphes_vides.mjs
   http://127.0.0.1:8230/<slug>/page.html` sur le miroir. Cible 0. Le contrôle
   par regex du point 3 ne les voit pas : wpautop écrit un `</p>` orphelin que
   le navigateur transforme en `<p>` vide, qui prend une case de grille (la
   frise « Claude écrit » passée à la ligne) ou la moitié d'un flex (les
   bannières jaunes à moitié vides, signalées par Nathan le 30/09). À la
   source : jamais `<span>`, `<i>`, `<b>` suivi d'un bloc dans le même
   conteneur ; utiliser `<div>`.
4. **Un seul H1** : mettre les métas Astra `site-post-title` et
   `ast-banner-title-visibility` à `disabled`, sinon le thème ajoute le sien.
5. Pages lead magnet ajoutées aux **exclusions de la pop-up Workshop**
   (réglage `dcp_popup` → `exclusions`), sinon deux pop-ups s'empilent.

## 4. Publier et tracer

- Brouillon, relecture, publication (`wp_publish.py` ou API REST).
- Menu : entrée dans Expertises → Nos Pépites (template Elementor 2762,
  bureau ET mobile), sauvegarde de l'en-tête avant.
- Notion « Cartographie SEO » : Mot clé, Prompt principal, Fan query,
  Tracking de lead, Statut, Dernière MAJ.
- Sitemap resoumis (`scripts/gsc.py sitemap --resoumettre`), puis demande
  d'indexation par Nathan dans Search Console.

## 5. Le code de capture seul

Pour un autre site : `design-system/snippets/capture-substack.html`
(autonome, testé). L'adresse `/api/v1/free` de Substack n'est pas une API
officielle : vérifier qu'un email de test arrive bien après chaque installation.
