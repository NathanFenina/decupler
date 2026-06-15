# Suivi de migration — WordPress → Next.js (VPS OVH)

> Fichier d'état durable. À relire au début de chaque nouvelle conversation
> pour éviter de tout reconstruire (et éviter le « prompt too long »).

## Objectif
Transformer le **site WordPress actuel** de Décupler (hacké) en site **Next.js
statique** déployé sur un **VPS OVH**. On reprend le contenu réel, pas un thème
neuf. On garde uniquement le **design** (couleurs `#07080f` / violet `#7B5CFA` /
vert `#00E5A0`, polices Syne + DM Sans).

## ⚠️ Règles critiques
- **NE JAMAIS charger l'export XML dans la conversation** : il fait **23 Mo /
  165 000 lignes** → c'est ce qui a causé « prompt too long ». On le parse
  toujours via `scripts/parse_wxr.py`, on ne lit que les résumés et les fichiers
  découpés.
- **VPS : ne PAS toucher au dossier/instance n8n.** Le site ira dans un dossier
  séparé (ex. `/var/www/decupler`). Demander confirmation avant toute commande
  sur le VPS.
- Export statique Next.js (sécurité max, pas de serveur Node exposé).

## État au 2026-06-13
- [x] Node installé (via nvm, sans sudo)
- [x] Scaffold Next.js 16 dans `site/` (TypeScript, App Router, CSS pur, export statique)
- [x] Page d'accueil placeholder de marque (à REMPLACER par le vrai contenu)
- [x] Export XML reçu : `~/Downloads/decupler.WordPress.2026-06-13.xml`
- [x] Parser écrit : `scripts/parse_wxr.py`
- [x] Contenu extrait → `content/cleaned/` :
      - 41 pages → `content/cleaned/pages/<slug>.html`
      - 19 articles → `content/cleaned/blog/<slug>.html`
      - inventaire → `content/cleaned/inventory.md`
- [x] Nettoyage HTML Elementor → contenu propre (`scripts/clean_content.py`)
      - 36 pages → `content/cleaned/pages_clean/<slug>.html` (HTML propre, e-commerce exclu)
      - 19 articles → `content/cleaned/blog_mdx/<slug>.mdx` (MDX + frontmatter)
      - Format retenu : pages = HTML, blog = MDX (validé OK SEO)
- [x] Méta SEO Yoast récupérées → `content/cleaned/seo-meta.json`
      (seo_title, description, canonical, focus_keyword, OG, noindex)
      60 entrées dont 51 avec meta description. Injectées aussi dans le
      frontmatter des MDX. À consommer via `generateMetadata` côté Next.js.
- [x] Structure de routage Next.js (build OK, 59 pages, export statique `out/`)
      - `site/src/lib/content.ts` lit `../content/cleaned/` au build
      - `site/src/app/[slug]/page.tsx` : route racine pages + articles, URLs préservées
      - `site/src/app/blog/page.tsx` : page liste du blog
      - `generateMetadata` → titres/descriptions Yoast exacts depuis seo-meta.json
      - Header/footer/home + CSS (prose, cartes blog) dans globals.css
      - Libs ajoutées : gray-matter, marked (npm via nvm)
      - ⚠️ npm/node = via nvm : `export NVM_DIR="$HOME/.nvm"; . "$NVM_DIR/nvm.sh"`
## 🔴 BLOCAGE IMAGES (2026-06-13)
Les images de contenu (`wp-content/uploads/`) sont **mortes sur le live (404) ET
absentes de Wayback** (archived_snapshots vides). → Non récupérables par scraping.
Sur agence-seo : 18/18 images de contenu introuvables en ligne.
→ Source nécessaire : **dossier `wp-content/uploads/` de l'hébergeur (FTP/SFTP)**
  (les fichiers sont probablement encore sur le disque) OU une **sauvegarde**.
  Une fois récupérées, les déposer dans `site/public/wp-content/uploads/` (même
  arborescence) → toutes les `<img src="/wp-content/uploads/...">` se résoudront.
C'est la tâche « récup uploads » de la phase 1 du plan, jamais faite.

## ✅ CLONE FIDÈLE AUTONOME — approche finale qui marche (2026-06-13)
`scripts/render_pages.py` réécrit : pour chaque page, télécharge le HTML rendu
(Wayback `id_`), puis **rapatrie tous les assets en local** (live d'abord, Wayback
en secours), réécrit les URLs decupler.com → chemins locaux `/wp-content/...`,
retire trackers/scripts suspects, et écrit `site/public/<slug>/index.html` 100%
autonome. CSS/JS/polices = OK depuis le live. Images = manquantes (cf. blocage).
- Faux positifs scan malware : jquery.min.js, parallax.min.js (fromCharCode légitime).
- agence-seo : structure + CSS + JS + menu OK en local ; images en attente FTP.

## 🎯 DÉCISION FINALE design (2026-06-13)
Le clone statique Wayback (render_pages.py) a été ABANDONNÉ : sans le JS
d'Elementor, le menu et les widgets cassaient. Choix utilisateur définitif :
**pur Next.js, ultra-léger, SANS reconstruire chaque page à la main.**
→ Approche retenue : **auto-style**. On garde le contenu récupéré (titres, texte,
images, `<section>`) et un CSS générique le met en forme proprement pour les 36
pages d'un coup (sections rythmées, hero, listes vertes, images arrondies).
- Pas identique à l'Elementor d'origine (layouts multi-colonnes simplifiés) mais
  propre, à la charte, rapide, sécurisé, zéro travail manuel utilisateur.
- `clean_content.py` préserve désormais les `<section>`.
- CSS d'auto-style dans `site/src/app/globals.css` (bloc `.page-content`).
- Route `/[slug]` rend de nouveau pages + articles (clone abandonné).
- Étape suivante possible (hybride) : je redessine les 3-4 pages prioritaires
  avec de vrais composants (Hero, Grille, CTA) pour un rendu premium.
- `scripts/render_pages.py` conservé mais inutilisé (au cas où).

## 🎨 Historique : tentative clone Wayback (abandonnée)
Le HTML du XML a perdu les attributs `class` → design non reconstituable depuis
le XML. Choix utilisateur : **récupérer le rendu fidèle** (même style) plutôt que
reconstruire. Source : **Wayback Machine** (snapshots propres, hack vérifié absent).
- `scripts/render_pages.py` : télécharge le HTML rendu archivé (version brute
  `id_`), retire TOUS les `<script>` (sécu + apparence OK), ajoute `<base href>`,
  écrit un clone statique autonome dans `site/public/<slug>/index.html`.
- Articles de blog = restent en MDX/Next.js (déjà propres). Pages = clones statiques.
- Route Next `/[slug]` = ARTICLES uniquement (`generateStaticParams` = posts).
  Les pages sont servies par les fichiers `public/<slug>/index.html`.
- ⚠️ Preview : `next dev` ne sert pas l'index.html des dossiers public sur URL à
  slash final → on prévisualise via l'export statique : `npm run build` puis
  `python3 -m http.server 3000 --directory out` (= comportement nginx).

- [x] Preuve de concept : `agence-seo` clonée fidèlement, sert en 200.
- [ ] Lancer `render_pages.py` sur les 36 pages (après validation visuelle).
- [ ] Cloner aussi la home d'origine (racine `/`) si on garde le même style.
- [ ] Images/CSS : pour l'instant chargés depuis le live decupler.com via <base>.
      Rapatrier les assets (wp-content) pour que le VPS soit autonome.
- [ ] À terme (hybride) : reconstruire proprement les pages prioritaires au design system.

## ⚠️ URLs à préserver (important SEO)
- Les slugs extraits == URLs WordPress d'origine (ex. `decupler.com/seo-chatgpt/`).
- **Les ARTICLES de blog étaient à la RACINE** (`decupler.com/<slug>/`), PAS sous
  `/blog/`. Donc routage Next.js : servir pages ET articles via un catch-all
  racine `/[slug]`. Garder `/blog` uniquement comme page liste.
  → Préserve les URLs, évite des centaines de redirections 301.
- [ ] Images : récupération (FTP / Wayback) + génération
- [ ] Redirections 301 (préserver les URLs) → `docs/redirections.md`
- [ ] Déploiement VPS OVH

## Contenu (résumé)
- 60 pages/articles publiés au total. Voir `content/cleaned/inventory.md`.
- Pages techniques à ignorer : `boutique`, `panier`, `mon-compte`, `commander`
  (WooCommerce), `home-old-2` (ancienne version).
- Le site a une partie e-commerce (WooCommerce) — à décider : on la recrée ou pas.

## Prochaine étape
Choisir le format cible (MDX vs HTML) puis nettoyer le HTML Elementor d'une
première page test pour valider le rendu, avant de tout convertir.
