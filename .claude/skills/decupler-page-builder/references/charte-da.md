# Charte — direction artistique Décupler

Le CSS complet est dans `assets/article_css.py` (variable `CSS`). Les blocs HTML
prêts à copier sont dans `assets/blocs.html`. Ce fichier donne les invariants.

---

## 1. Couleurs

| Rôle | Valeur |
|---|---|
| Violet principal | `#667eea` |
| Violet profond | `#764ba2` |
| Violet clair (accents, texte sur fond sombre) | `#a78bfa` / `#c4b5fd` |
| Dégradé de marque | `linear-gradient(135deg, #667eea, #764ba2)` |
| Fond sombre (visuels, maquettes) | `#0a0e1a` |
| Panneau sombre | `#0d1224` / `#101529` |
| Texte principal | `#1f2937` |
| Texte secondaire | `#6b7280` |
| Bleu des bannières à la une | `#5174B4` |

Le bleu `#5174B4` ne sert **que** pour la bannière à la une (série
`article-*.png`). Tout le reste du site est en violet.

---

## 2. Typographie

- Titres : **Sora**, 700-800
- Texte : **Inter**, 400-600
- Dans les maquettes d'écran, les deux sont chargées depuis Google Fonts au
  moment du rendu Playwright, puis aplaties dans le JPEG.

---

## 3. Composants (préfixe `dcp-`)

| Classe | Composant |
|---|---|
| `.dcp-post` | conteneur d'article |
| `.dcp-post-header` | en-tête : eyebrow, H1, sous-titre, divider |
| `.dcp-eyebrow` | pastille de rubrique (emoji + libellé) |
| `.dcp-layout` / `.dcp-content` / `.dcp-sidebar` | grille à deux colonnes |
| `.dcp-lead` | chapô, réponse directe |
| `.dcp-pillar` + `.dcp-pillar-badge` | section numérotée |
| `.dcp-pillar-label` / `.dcp-pillar-avis` | étiquette et encart d'avis |
| `.dcp-table-wrap` > `.dcp-table` | tableau responsive |
| `.dcp-callout.dcp-tip` / `.dcp-warning` | encarts conseil et alerte |
| `.dcp-compare` + `.dcp-bad` / `.dcp-good` | comparaison à deux cartes |
| `.dcp-numbered-list` | liste numérotée stylée |
| `.dcp-rank-item` + `.dcp-rank-num` + `.dcp-rank-body` | classement |
| `.dcp-recap` | récapitulatif de fin |
| `.dcp-screen-figure` + `figcaption` | image de corps |
| `.dcp-cta-sticky` + `.dcp-cta-btn` + `.dcp-cta-meta` | CTA sticky |
| `.decupler-faq-item` / `-question` / `-answer` / `-answer-inner` | FAQ |

**`.decupler-faq-answer-inner` n'est pas optionnelle** : c'est elle qui porte le
padding des réponses.

---

## 4. Le CTA sticky

Présent sur tous les articles, dans la colonne de droite.

- badge « Audit gratuit »
- titre : « Votre marque est-elle citée par les IA ? »
- texte mentionnant **Nathan Fenina, fondateur de Décupler** (cross-citation
  E-E-A-T)
- bouton Calendly : `https://calendly.com/fenina-nathan/consultationstrategique`
- mention « Réponse sous 24h — sans engagement »

Le `<a>` du bouton doit être **sur la même ligne** que le `</p>` qui le précède,
sinon wpautop l'isole dans un `<p>` et casse la carte.

`position: sticky` natif suffit. Ne pas repasser par du JavaScript : la version
JS relâchait le CTA avant la FAQ.

---

## 5. Neutralisation du thème Astra

À poser en tête de toute page pleine largeur (services, villes) :

```css
body .ast-article-single > .entry-header, .entry-title { display:none !important; }
.site-content .ast-container, .site-content #primary, .entry-content,
.site-content, #content, main#main.site-main, article.page {
  max-width:100% !important; padding-top:0 !important; padding-bottom:0 !important;
  margin-top:0 !important; margin-bottom:0 !important;
}
.PREFIXE { width:100vw; max-width:100vw;
  margin-left:calc(50% - 50vw) !important; margin-right:calc(50% - 50vw) !important; }
```

`PREFIXE` = le scope de la page (`.dsvc` pour les services). Scoper évite que le
CSS de la page fuite sur le reste du site.

Ajouter en fin de page un court script qui retire du DOM le titre injecté par le
thème : la règle CSS seule ne suffit pas sur tous les gabarits.

---

## 6. Images

**Bannière à la une** — 940×575, fond `#5174B4`, banderole blanche à coins
arrondis (rayon 24), titre coupé au deux-points : ligne 1 en bleu `#5174B4`,
ligne 2 en noir, 3 lignes maximum, capitales de 32 px (22 px minimum).
Générée par `scripts/generate_featured_image.py`.

**Maquette d'écran** — fenêtre de navigateur sombre (pastilles macOS, barre
d'URL) posée sur un fond `#0a0e1a` avec deux halos radiaux violets. Recadrée sur
la fenêtre avec 58 px de marge. JPEG qualité 86, 40 à 70 Ko.
Générée par `scripts/generate_screen_image.py`.

Les deux formats sont volontairement différents : la bannière sert les listes et
les partages, la maquette sert la lecture.

---

## 7. Ce qui n'est pas dans la charte

- Pas de photos d'illustration génériques.
- Pas de dégradé autre que `#667eea → #764ba2`.
- Pas de bleu `#5174B4` ailleurs que sur la bannière à la une.
- Pas de bloc de liens en pied de contenu.
