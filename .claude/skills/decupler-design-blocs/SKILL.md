---
name: decupler-design-blocs
description: >
  Bibliothèque de blocs HTML+CSS prêts à coller dans une page decupler.com :
  hero avec canvas animé, grille de logos clients, liste de missions chiffrées,
  FAQ + JSON-LD, bandeau E-E-A-T, CTA, zone d'intervention locale. Chaque bloc
  embarque les correctifs Astra, wpautop et Elementor déjà payés en production,
  et la règle d'or des animations (jamais d'opacité, sinon les crawlers IA ne
  voient rien). À utiliser dès qu'on construit ou refond une page ou une
  landing sur decupler.com, qu'on parle de design, de hero, de bannière,
  d'animation, de bloc réutilisable, ou que le rendu casse (titres de la mauvaise
  couleur, texte invisible, blanc au-dessus du hero, mise en page éclatée).
---

# Blocs de design Décupler

Chaque bloc est validé en production. Les commentaires expliquent **pourquoi**
une ligne est là : ne pas les retirer sans avoir relu l'incident.

HTML dans `assets/blocs-v2.html`, CSS dans `assets/skin.css`.

---

## 1. Les cinq règles qui ont coûté cher

**1. Redéclarer la couleur des titres.** Astra pose un `color` explicite sur
`h1`/`h2`/`h3`. Une règle explicite bat une valeur héritée quelle que soit la
spécificité — donc `color` sur le conteneur ne suffit pas et les titres passent
en bleu nuit sur fond sombre.

```css
.SCOPE h1, .SCOPE h2, .SCOPE h3 { color: var(--tx) !important; }
```

**2. Jamais d'opacité dans une animation d'entrée.** Un `from { opacity: 0 }`
rend le texte invisible partout où l'animation ne tourne pas : crawler IA, JS
coupé, capture headless, `prefers-reduced-motion` mal géré. Pour une agence qui
vend du GEO, c'est auto-destructeur. **Animer la translation seulement.**

```css
@keyframes dcpIn { from { transform: translateY(18px) } to { transform: none } }
```

**3. Charger les polices.** Déclarer `font-family:"Syne"` sans le `<link>`
Google Fonts dans la page fait tomber tout le design en `system-ui`. Le `<link>`
va **dans le contenu de la page**, pas seulement dans un aperçu local.

**4. Aucune ligne vide hors du `<style>`.** wpautop transforme une ligne vide en
`<p></p>` parasite, parfois au milieu d'une grille flex.

**5. Que des `<div>` entre des `<div>`.** Un `<span>`, `<svg>`, `<img>`,
`<canvas>` ou `<a>` frère direct d'un bloc se fait envelopper dans un `<p>`, et
l'ouverture du `<p>` avale la fermeture du bloc suivant. Encapsuler tout
élément inline dans un `<div>`.

## 2. Neutralisation du thème

À poser en tête de toute page pleine largeur, avant les blocs :

```css
body .ast-article-single > .entry-header, .entry-title { display:none !important; }
.site-content .ast-container, .site-content #primary, .entry-content,
.site-content, #content, main#main.site-main, article.page {
  max-width:100% !important; padding-top:0 !important; padding-bottom:0 !important;
  margin-top:0 !important; margin-bottom:0 !important;
}
.SCOPE { width:100vw; max-width:100vw;
  margin-left:calc(50% - 50vw) !important; margin-right:calc(50% - 50vw) !important; }
```

`SCOPE` = une classe propre à la page (`.dcp-h` pour la home, `.dsvc` pour les
services, `.dcp-v` pour les villes). **Toujours scoper** : sinon le CSS de la
page fuit sur le reste du site.

## 3. Les blocs

> **Direction artistique :** ce tableau donne les briques. Le rythme, la
> règle d'alternance des bandes et la boucle de vérification au rendu réel
> sont dans le skill **`decupler-direction-artistique`** — à lire avant de
> pousser une page, c'est lui qui répond à « c'est trop générique » et
> « le bas de page est vide ».

| Bloc | Classe | Quand |
|---|---|---|
| Hero canvas « graphe de citations » | `.hero` + `.cv` | Page d'accueil, landing GEO |
| Hero sobre (sans canvas) | `.hero.plain` | Pages villes, services |
| Chiffres attribués | `.pf` | Preuve : un chiffre, ce qu'il mesure, **la mission d'où il vient** |
| Grille de logos | `.marks` | Logos hétérogènes ramenés à un gris uniforme |
| Missions chiffrées | `.ms` | Nom, date, 2-3 résultats mesurés |
| Outillage / services | `.tech` | Grille 3 colonnes — mettre un multiple de 3, sinon cellule vide visible |
| Zone d'intervention | `.zone` | Pages villes : codes postaux + communes en `<div>` |
| FAQ + JSON-LD | `.faq` | `.decupler-faq-answer-inner` **obligatoire**, elle porte le padding |
| Bandeau E-E-A-T | `.eeat` | Photo de Nathan, fonction, LinkedIn, Calendly |
| CTA de clôture | `.cta` | Un par page, en fin |
| **Bande photo pleine largeur** | `.bphoto` | Une vraie photo du lieu, texte en surimpression, crédit CC affiché. Une par page |
| **Ruban de faits** | `.ruban` | Bande fine et sombre, rôle purement rythmique entre deux grandes sections |
| **Bande sombre éditoriale** | `.bl-dk` | Le parti pris, première personne, signé. Une par page, jamais deux |
| **Livrables** | `.livr` | Six cellules, ce qui arrive chaque mois et à quelle cadence |
| **On fait / on ne fait pas** | `.duo` | Deux colonnes, la seconde barrée. Le bloc le moins imitable d'une page |
| **Bande auteur (E-E-A-T)** | `.aut` | Grande photo verticale + biographie, en pied. Remplace l'ancien `.eeat` à 60 px |

Les six derniers sont définis dans
`../decupler-page-ville-seo/assets/skin-ville.css` (ajouts du 22/09) et
assemblés par `build_ville.py`.

## 4. Le hero canvas

Un graphe de nœuds-marques qui dérivent, reliés en violet, traversés par des
impulsions vertes quand une « citation » se déclenche. Canvas 2D vanilla,
~90 lignes, aucune dépendance CDN.

- Texte **toujours dans le HTML**, jamais peint par le canvas
- `.cv { z-index:0; pointer-events:none }` et `.hero > .in { position:relative;
  z-index:1 }` — l'ordre de peinture explicite, ne pas compter sur `z-index:-1`
- `<canvas>` encapsulé dans un `<div>` (règle 5)
- Voile en dégradé radial par-dessus le canvas, sous le texte
- `prefers-reduced-motion` → une seule frame statique
- Animation coupée quand l'onglet passe en arrière-plan

**Framer Motion ne marche pas ici** : c'est une bibliothèque React, le site est
WordPress + Astra + Elementor sans React. L'équivalent vanilla est **Motion
One** (motion.dev, même auteur, ~5 ko, chargeable depuis jsDelivr) — mais le
canvas maison ne demande aucune dépendance, donc ne pas en ajouter sans raison.

## 5. Images

- Chercher le média par slug **avant** tout upload : WordPress ne dédoublonne
  pas, un second upload décale le slug d'origine en `-1`, `-2`…
- Logos clients : `filter: brightness(0) invert(1); opacity:.6`, plus
  `max-height` — ils arrivent en noir ou en couleur, sans ça la grille part
  dans tous les sens sur fond sombre
- Toujours `width`, `height` et `loading="lazy"` sur les `<img>`
- Génération : MCP `gemini-images` ou `scripts/openai_images.py` (gpt-image-1),
  puis `scripts/wp_upload_media.py`

## 6. Avant de pousser

1. `python3 .claude/skills/decupler-page-builder/scripts/validate_page.py
   --fichier ... --type page-ville|article|page-service --kw ... --slug ...`
2. Rendu réel, pas seulement le HTML :

```bash
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --disable-gpu \
  --no-sandbox --hide-scrollbars --window-size=1440,3000 \
  --screenshot=out.png --virtual-time-budget=8000 "file://$PWD/page.html"
```

   Envelopper le fragment dans un `<body style="background:#07080f">` avec le
   `<link>` Google Fonts, sinon on juge un rendu qui n'est pas celui du site.

3. Vérifier en base que le CSS est bien arrivé :
   `GET /wp-json/wp/v2/pages/{id}?context=edit&_fields=content`
4. Relire le statut existant et le conserver au push — un `status:"draft"` en
   dur **déprogramme** un contenu planifié.
5. Elementor : une écriture dans `_elementor_data` n'apparaît qu'après
   « Effacer les fichiers et les données » (Elementor → Outils). Le prévenir.

## 7. Ce qui n'est pas dans la charte

Pas de photo d'illustration générique, pas de dégradé autre que celui de la
marque, pas de bleu `#5174B4` ailleurs que sur la bannière à la une, pas de bloc
de liens en pied de contenu.

## 8. La charte réelle — tranché par relevé le 22/09/2026

**C'est `charte-da.md` qui est en production, pas `tokens.css`.** Vérifié en
extrayant les couleurs et les polices de `decupler.com/agence-geo-nice/`, la
page que Nathan désigne comme référence :

| | Site réel (mesuré) | `tokens.css` (théorique) |
|---|---|---|
| Fond | **blanc `#ffffff`**, bandes `#f7f5fd` et `#ece9f8` | `#07080f` (dark) |
| Violet | **`#667eea` (18×) → `#764ba2` (9×)** | `#7B5CFA` |
| Texte | `#1a1a2e`, secondaire `#4a4a6a`, tertiaire `#8b8ba7` | `#e8e9f2` |
| Titres | **Sora** 700 | Syne 800 |
| Corps | **Inter** | DM Sans |
| Vert | absent | `#00E5A0` |

`CLAUDE.md` déclare `tokens.css` « source unique de vérité » : **c'est faux**,
aucune page du site ne l'applique. Construire en dark violet/vert produit une
page qui ne ressemble pas au site — erreur commise deux fois cette semaine.

**Toujours partir de `assets/reference-page-ville.html`**, qui reproduit le
langage réel : pill d'eyebrow lavande, H1 avec une partie en `<em>` violet, deux
CTA (violet dégradé plein + blanc outline) suivis d'une micro-mention grise,
cartes flottantes à droite du hero, bande de confiance à 4 chiffres, grille
numérotée à badges ronds, maquette « requête posée à ChatGPT », méthode en liste
numérotée, tableau comparatif à en-tête dégradé, photo de ville en carte 3:4
avec légende en overlay, grille de communes, bande CTA finale en dégradé plein.

Les blocs de `assets/skin.css` et `assets/blocs-v2.html` sont en dark
(`tokens.css`) : ils ne servent que si Nathan valide un jour ce basculement.
Par défaut, utiliser la référence claire.
