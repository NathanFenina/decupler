# Gabarit — page service

Post type `pages`. **Yoast non écrivable par l'API** : fournir les valeurs à
Nathan pour saisie manuelle.

Pages existantes : `/audit-geo/`, `/cartographie-ia/`, `/eeat-google/`.

---

## 1. Ce qui distingue une page service

Une page service vend une prestation. Elle n'explique pas un concept (article)
et ne cible pas un territoire (page ville). Sa colonne vertébrale est
**problème → preuve → offre → réservation**.

Contraintes :

- mot-clé validé par un volume réel (Semrush) avant d'écrire — pas d'intuition
- **mot-clé exact ≥ 20 fois**, densité ≤ 3,5 %
- **un seul H1** : le thème en injecte un second, à masquer
- **CTA Calendly sur chaque section pleine largeur**
- **bandeau E-E-A-T** avec photo de Nathan Fenina, LinkedIn, Calendly
- **mention YMYL bien visible** dès qu'on parle de résultats ou de budget
- captures de l'application Décupler pour matérialiser la promesse

---

## 2. Structure

| # | Bloc | Rôle | CTA |
|---|---|---|---|
| 1 | **Hero pleine largeur** | H1 + promesse en une phrase + preuve chiffrée | oui |
| 2 | **Le problème** | H2 en prompt : ce que le prospect vit aujourd'hui | — |
| 3 | **Section violette** | ce que la prestation change, en 3 points | oui |
| 4 | **Bandeau capture d'app** | l'écran de l'application Décupler, légendé | oui |
| 5 | **La méthode** | 5 à 6 étapes numérotées, avec livrable par étape | — |
| 6 | **Ce qui est inclus / exclu** | tableau à deux colonnes, honnête sur les limites | — |
| 7 | **Bandeau E-E-A-T** | Nathan Fenina : photo, parcours, LinkedIn, Calendly | oui |
| 8 | **Bandeau YMYL** | limites, absence de garantie, cadre déontologique | — |
| 9 | **FAQ** | 6 à 8 questions d'objection commerciale | — |
| 10 | **Bande CTA finale** | réservation | oui |

---

## 3. CSS de neutralisation du thème

Obligatoire en tête de chaque page service, sinon le thème ajoute un titre en
double et 60 px de blanc :

```css
body .ast-article-single > .entry-header, .entry-title { display:none !important; }
.site-content .ast-container, .site-content #primary, .entry-content,
.site-content, #content, main#main.site-main, article.page {
  max-width:100% !important; padding-top:0 !important; padding-bottom:0 !important;
  margin-top:0 !important; margin-bottom:0 !important;
}
.dsvc { width:100vw; max-width:100vw;
  margin-left:calc(50% - 50vw) !important; margin-right:calc(50% - 50vw) !important; }
```

Plus, en fin de page, un court script qui retire du DOM le titre injecté par le
thème — la règle CSS seule ne suffit pas sur certains gabarits.

Le CSS de la page est **scopé** sous un préfixe (`.dsvc`) pour ne pas fuiter sur
le reste du site.

---

## 4. Le bandeau E-E-A-T

Composant réutilisable, identique sur les trois pages service :

- photo de Nathan Fenina
- une phrase de parcours, pas un titre ronflant
- lien LinkedIn
- lien Calendly
- mention explicite du rattachement à Décupler

C'est le levier d'autorité maison. Sur une page service, il est plus efficace
que trois paragraphes d'arguments.

---

## 5. Le bandeau YMYL

Dès que la page évoque un résultat, un délai ou un budget, ajouter une mention
visible qui rappelle qu'aucun résultat n'est garanti et que la sélection finale
appartient aux moteurs.

Ce n'est pas seulement de la prudence : les moteurs génératifs reprennent
volontiers les pages qui bornent leurs promesses, et écartent celles qui
promettent trop.

---

## 6. Recherche de mot-clé

Avant d'écrire, produire une liste de candidats et la faire valider dans
Semrush. Retenir un mot-clé qui a du volume et une intention commerciale, pas le
plus flatteur.

Cas réel : `eeat google` a été retenu contre une formulation plus longue et sans
volume, et l'URL a été changée en conséquence. Ne pas s'attacher à un slug avant
validation.

---

## 7. Avant de pousser

- vérifier qu'il n'y a **qu'un seul `<h1>`** rendu
- vérifier qu'aucun bandeau n'est sans CTA
- vérifier l'absence de ligne vide hors CSS (wpautop)
- vérifier le rendu réel dans un navigateur : un `<span>` isolé passe la
  validation HTML et casse quand même la grille après wpautop
- fournir les trois valeurs Yoast à saisir manuellement
