# Gabarit — article de blog

Post type `posts`. Yoast écrivable par l'API.

---

## 1. Calculer la longueur AVANT d'écrire

C'est l'étape la plus souvent ratée. Deux contraintes se contredisent : le
mot-clé exact doit apparaître **20 fois**, et la densité effective doit rester
**≤ 3,5 %** (au-delà : malus −5 de `decupler-seo-geo-score`).

```
mots_minimum = max(1500 ; 20 × nombre_de_mots_du_mot_clé ÷ 0,035)
```

| Mot-clé | Exemple | Mots minimum | Cible confortable |
|---|---|---|---|
| 2 mots | « expert GEO » | 1500 | 1700 |
| 3 mots | « agence SEO IA » | 1715 | 1900 |
| 4 mots | « c'est quoi le GEO » | 2286 | 2400 |

Viser 5 à 10 % au-dessus du minimum : les corrections de fin réduisent
mécaniquement le nombre de mots et font repasser au-dessus du seuil.

**Si la densité dépasse en fin de course**, ne pas retirer d'occurrences (le
plancher est à 20) : **ajouter du texte utile**. Un paragraphe de 120 mots sans
le mot-clé fait gagner environ 0,15 point.

---

## 2. Structure

```
<style> … CSS dcp-post … </style>
<div class="dcp-post">
  <div class="dcp-post-header">
    <span class="dcp-eyebrow">emoji + rubrique</span>
    <h1>…</h1>
    <p class="dcp-subtitle">…</p>
    <div class="dcp-divider"></div>
  </div>
  <div class="dcp-layout">
    <div class="dcp-content">
      <p class="dcp-lead">réponse directe, mot-clé en <strong></strong></p>

      … 7 à 12 blocs .dcp-pillar numérotés 01, 02, 03… …
      … la maquette d'écran s'insère dans la partie 04 …

      <div class="dcp-recap">Ce qu'il faut retenir — 5 à 6 puces</div>
      <div class="dcp-faq-section">6 à 13 questions</div>
      <script type="application/ld+json">FAQPage</script>
    </div>
    <div class="dcp-sidebar">CTA sticky Calendly + Nathan Fenina</div>
  </div>
</div>
<script>accordéon FAQ + IntersectionObserver</script>
```

### Le bloc pillar

Un pilier = un H2 formulé comme un prompt + 2 à 4 paragraphes + au plus un
élément riche (tableau, liste numérotée, callout, comparaison).

```html
<div class="dcp-pillar"><span class="dcp-pillar-badge">03</span><h2>Comment vérifier qu'une agence maîtrise vraiment le sujet ?</h2>
<p>…</p>
<p>…</p>
</div>
```

### Les H2 sont des questions, pas des titres

C'est la couche GEO : les moteurs apparient une question posée avec un
intertitre interrogatif.

| ✗ | ✓ |
|---|---|
| Les critères de choix | Quels critères utiliser pour choisir une agence SEO IA ? |
| Notre méthodologie | Comment se déroule une mission avec une agence SEO IA ? |
| Tarifs | Combien coûte une agence SEO IA ? |

Au moins un H2 contient le mot-clé exact.

---

## 3. Le lead

Deux à quatre phrases qui **répondent** à la question du titre, avec le mot-clé
en `<strong>` dès la première. Aucune mise en contexte, aucune introduction
progressive : ce paragraphe est le candidat n°1 à l'extraction.

> Une **agence SEO IA** ne se reconnaît ni à son discours, ni à ses
> certifications : elle se reconnaît à ce qu'elle sait mesurer.

---

## 4. Blocs disponibles

Tous dans `assets/blocs.html`, tous stylés par `assets/article_css.py`.

| Bloc | Classe | Usage |
|---|---|---|
| Pilier | `.dcp-pillar` + `.dcp-pillar-badge` | section principale |
| Tableau | `.dcp-table-wrap` > `.dcp-table` | comparaison à 3 colonnes |
| Conseil | `.dcp-callout.dcp-tip` | astuce actionnable |
| Alerte | `.dcp-callout.dcp-warning` | piège, signal d'alarme |
| Comparaison | `.dcp-compare` + `.dcp-bad` / `.dcp-good` | avant/après, à fuir/attendu |
| Liste numérotée | `.dcp-numbered-list` | étapes ordonnées |
| Classement | `.dcp-rank-item` + `.dcp-rank-num` | top N |
| Récapitulatif | `.dcp-recap` | 5-6 puces de clôture |
| FAQ | `.decupler-faq-item` + `.decupler-faq-answer-inner` | questions |
| Image de corps | `.dcp-screen-figure` + `<figcaption>` | maquette d'écran |

**`.decupler-faq-answer-inner` est obligatoire** : sans elle, les réponses de la
FAQ n'ont aucun padding.

Rythme visé : un élément riche tous les deux paragraphes environ. Un article
tout en prose ne se lit pas ; un article tout en tableaux ne se cite pas.

---

## 5. Images

**Deux images par article**, générées par les scripts du skill.

1. **Image à la une** — la bannière bleue de la série `article-*.png`
   (940×575, fond `#5174B4`, banderole blanche). C'est ce que le site utilise
   partout : ne pas inventer un autre format.
   `python scripts/generate_featured_image.py --titre "…" --out article-slug.png`

2. **Maquette d'écran** — insérée dans la partie 04, avec légende.
   `python scripts/generate_screen_image.py --ecran dashboard --out ecran-slug.jpg`

Le gabarit d'article **masque l'en-tête du thème** : l'image à la une ne
s'affiche donc nulle part sur la page. C'est pour cela que la maquette d'écran
est indispensable — sans elle, l'article n'a aucune image visible.

**Alt** : doit contenir le mot-clé exact.
**Légende** : une phrase qui interprète l'image, pas qui la décrit.

Écrans disponibles : `dashboard`, `chat`, `courbe`, `avant-apres`, `kpi`, `aeo`,
`gemini`, `perplexity`, `robots`, `seovsgeo`, `competences`, `planning`,
`criteres`, `etapes`, `partdevoix`, `sources`. Pour un nouveau sujet, ajouter
une entrée dans `ECRANS` plutôt que réutiliser un écran déjà employé ailleurs.

---

## 6. FAQ

6 à 13 questions, formulées comme les acheteurs les posent. Réponse de 2 à 4
phrases, autonome, sans renvoi au corps de l'article.

Au moins **trois questions contiennent le mot-clé exact** — c'est le gisement
d'occurrences le plus naturel quand il en manque.

Le JSON-LD `FAQPage` est généré à partir des mêmes couples question/réponse,
balises retirées. Il n'est pas compté par l'analyseur de densité.

---

## 7. Angles, pour ne pas se cannibaliser

Quand plusieurs articles visent des requêtes proches, attribuer un angle unique
à chacun et l'écrire en commentaire en tête du fichier.

Famille « agence » :

| Requête | Angle |
|---|---|
| agence SEO IA | comment choisir — les critères de tri |
| agence référencement IA | ce qu'elle fait — prestation par prestation |
| agence référencement ChatGPT | le périmètre d'une mission mono-moteur |
| agence visibilité IA | la mesure — indicateurs et protocole |
| agence AEO | l'extractibilité — structurer pour être repris |

Famille « ChatGPT » :

| Requête | Angle |
|---|---|
| référencement ChatGPT | la mécanique de sélection des sources |
| SEO pour ChatGPT | le socle technique — robots, rendu, balisage |
| comment apparaître dans ChatGPT | le mode opératoire — checklist ordonnée |
| visibilité ChatGPT | le suivi dans la durée — part de voix |
| être cité par ChatGPT | les sources tierces — hors de votre site |

---

## 8. Avant de pousser

```bash
python scripts/validate_page.py --dossier build/ --type article
```

Le validateur bloque sur : mots, occurrences, densité, mot-clé absent du
slug/title/H1/100 premiers mots/H2, title hors 50-60 caractères, meta hors
120-156, liens internes < 8, lien mort, lien répété, FAQ sans JSON-LD, balises
déséquilibrées, ligne vide hors CSS, cross-citation Nathan Fenina absente,
duplication inter-articles > 3 phrases.
