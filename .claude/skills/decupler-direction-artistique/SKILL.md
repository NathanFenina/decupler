---
name: decupler-direction-artistique
description: >
  Direction artistique des pages decupler.com : ce qui fait qu'une page se
  lit comme un travail d'agence et non comme un texte produit en serie.
  Contient le diagnostic « page detectable », la taxonomie des bandes (six
  types, avec la regle d'alternance), la loi du rythme vertical, la
  bibliotheque de matiere qui differencie, et la boucle de verification au
  rendu reel (Chromium + sonde DOM) — celle qui a trouve trois defauts que
  la lecture du HTML n'avait pas vus. A utiliser avant de pousser toute page
  ou landing, et des qu'on dit : le design fait amateur, c'est trop generique,
  ca ressemble a de l'IA, le bas de page est vide, il manque des photos, il
  manque des bannieres differentes, la page est plate, les encadres sont mal
  alignes.
---

# Direction artistique Décupler

Ce skill ne remplace pas `decupler-design-blocs` (les blocs et les correctifs
Astra/wpautop) ni `decupler-page-ville-seo` (le contenu et le SEO). Il répond
à une autre question, celle que Nathan a posée trois fois avant qu'elle soit
traitée : **pourquoi la page a l'air d'avoir été produite à la chaîne, et
comment on arrête ça.**

---

## 1. Le diagnostic « page détectable »

Une page se fait repérer comme générée sur six signes. Ils sont visuels avant
d'être textuels — un lecteur les voit en trois secondes de défilement, avant
d'avoir lu une phrase.

| # | Signe | Ce qu'on voit | Le correctif |
|---|---|---|---|
| 1 | **Monotonie des bandes** | Blanc, lavande, blanc, lavande sur 13 000 px | Six types de bande, §2, avec la règle d'alternance |
| 2 | **Aucune photo sous le hero** | Une image en haut, puis 10 000 px de texte | Au moins **deux** photos, dont une en seconde moitié |
| 3 | **Grilles orphelines** | Une ligne de 3, puis une ligne de 2 | Un nombre de cellules **multiple du nombre de colonnes** |
| 4 | **Uniformité typographique** | Tous les corps de texte à la même taille | La bande éditoriale monte à 1,19 rem, le ruban descend à 0,845 |
| 5 | **Rien qui engage** | Que des affirmations positives et interchangeables | Un bloc « ce qu'on ne fait pas », §4 |
| 6 | **Pied de page en sifflet** | FAQ, liens, CTA — et 180 px de blanc entre chaque | Le pied porte la bande auteur, §2 |

**Le test des trois secondes.** Réduire la capture pleine page à 200 px de
large et la regarder. On doit distinguer au moins quatre zones de valeur
différentes. Si la vignette est une colonne uniforme, la page est plate, quel
que soit le contenu.

```bash
python3 -c "
from PIL import Image
im = Image.open('capture-1440.png'); im.thumbnail((200, 4000))
im.save('vignette.png')"
```

## 2. Les six types de bande

Chaque type a un rôle. Les empiler au hasard ne produit pas du rythme, juste
du bruit.

| Classe | Fond | Rôle | Fréquence par page |
|---|---|---|---|
| `.bl` | blanc | Section de fond, texte long | 4 à 6 |
| `.bl bl-lav` | `#f7f5fd` | Section de fond, alternance | 3 à 5 |
| `.bphoto` | photo pleine largeur | **Ancrage** — une vraie photo du lieu | 1, jamais 2 |
| `.ruban` | `#14122b`, ~50 px | **Respiration** — coupe deux grandes sections | 1 à 2 |
| `.bl bl-dk` | dégradé radial sombre | **Prise de parole** — parti pris signé | 1, jamais 2 |
| `.bl bl-lav` + `.aut` | lavande + carte | **Signature** — l'auteur, en pied | 1 |

**La règle d'alternance.** Jamais plus de **deux** bandes claires
consécutives sans une bande photo, un ruban ou une bande sombre entre elles.
C'est la règle qui manquait : les pages villes du 22/09 en enchaînaient cinq.

**Ordre qui marche sur une page ville**, éprouvé sur cinq pages :

```
hero → pourquoi → ranker(lav) → méthode → preuves(lav)
     → BPHOTO → zone → RUBAN → budget(lav) → livrables
     → bandeau photo → duo(lav) → BL-DK → variantes
     → FAQ(lav) → voisines → AUT(lav) → CTA dégradé
```

Les trois bandes en capitales sont celles qui cassent la série. Les retirer
rend la page plate même si le texte ne change pas d'un mot.

## 3. Les photos

**Jamais d'image générée pour représenter un lieu réel.** Une page « agence
SEO Toulon » qui affiche une ville inventée par un modèle est un faux, et
c'est le genre de faux qu'un prospect local repère immédiatement.

Où trouver de vraies photos, dans l'ordre :

1. **La médiathèque WordPress.** Chercher par slug avant tout upload —
   WordPress ne dédoublonne pas, un second upload décale le slug d'origine
   en `-1`. Le site a déjà des photos réelles de Nice, Marseille, Paris,
   Lyon, Lille, Bordeaux, Nantes, Toulouse.
2. **Wikimedia Commons**, licences CC. Le script est dans
   `references/commons.py`. Deux pièges :
   - Demander une **taille de vignette standard** (`/thumb/.../1920px-...`),
     sinon Wikimedia renvoie 429 sur l'original.
   - Filtrer le domaine public : c'est le marqueur le plus fiable d'une
     gravure ancienne. Les photos modernes sont en CC BY-SA.
   - **Afficher le crédit et la licence dans la bande.** C'est la condition
     de la licence, pas une politesse.
3. **Gemini / gpt-image-1**, et seulement pour de l'abstrait : schéma,
   maquette d'interface, texture. Jamais un lieu, jamais un visage, jamais
   un logo.

**Recadrage.** Une bande fait 21:9 (2000 × 858). Le point d'ancrage vertical
dépend de la photo et se choisit à l'œil, pas par défaut — sur une vue
plongeante la ville est au milieu, sur un panorama de port elle est en haut.

**Le piège `aspect-ratio`.** Les attributs HTML `width` et `height` sont des
*indications de présentation*. Quand les deux sont posés, ils gagnent contre
`aspect-ratio` en CSS. Il faut déclarer `height:auto` explicitement.

**Le piège du sélecteur enfant.** Un `<img>` frère direct d'un `<div>` se
fait avaler par wpautop, donc on l'encapsule — et à partir de là `.bloc > img`
ne matche plus. Utiliser le sélecteur descendant `.bloc img`. Ce bug a fait
rendre une photo à 2 000 px dans un cadre de 490, découpée en silence par
`overflow:hidden`.

## 4. La matière qui différencie

« Pas assez de matière » ne se règle pas avec un paragraphe de plus sur
l'importance du SEO. Trois blocs portent tout le poids :

**Les livrables, avec leur cadence.** Ce qui arrive dans la boîte mail, six
items, chacun avec sa fréquence. Vérifiable, donc crédible.

**Ce qu'on ne fait pas.** Le bloc le moins imitable de la page : dire non est
concret. Il doit contenir au moins un refus qui coûte de l'argent (« pas
d'engagement de 12 mois », « un seul client par métier et par zone »). Un
bloc de refus sans coût réel se lit comme de la posture.

**Le parti pris, à la première personne, signé.** Trois paragraphes, une
anecdote vraie, une position qui fait perdre des contrats. C'est le seul
endroit de la page où quelqu'un parle. Sans lui, la page n'a pas d'auteur.

Chacun de ces trois blocs est **écrit ville par ville**. Recopié, il se fait
prendre par le contrôle de duplication — et il a raison de le prendre.

## 5. Le rythme vertical

- Une bande de fond : `padding` de `clamp(56px, 6.5vw, 92px)`.
- **Deux bandes de même fond qui se suivent produisent 180 px de blanc.**
  C'est le « bas de page vide ». Soit on fusionne, soit on change le fond.
- Un ruban : 17 px de padding. Il doit *trancher*, pas respirer.
- La mesure du texte long : 70 caractères (`.nr`). L'éditorial sombre : 64.
- Titre de bande photo : 22 caractères max, sinon il passe sur trois lignes
  et mange la photo.

## 6. Les animations

Reprise de `decupler-design-blocs`, parce que c'est la règle la plus violée :
**jamais d'opacité**. Un `from { opacity: 0 }` rend le texte invisible partout
où le JS ne tourne pas — crawler IA compris. Pour une agence qui vend du GEO,
c'est auto-destructeur. On anime la translation seulement.

Et il faut un `IntersectionObserver`, pas une animation au chargement : jouée
au chargement, l'animation d'un bloc situé à 9 000 px est terminée avant que
l'utilisateur n'y arrive. Nathan a signalé deux fois « il manque des
animations » alors qu'elles étaient là — elles avaient fini de jouer.

## 7. La boucle de vérification

**Lire le HTML ne suffit pas.** Les trois derniers défauts trouvés étaient
tous invisibles à la lecture du source : une photo à 2 000 px découpée, une
colonne vide, des pastilles illisibles sur un ciel clair.

```bash
# 1. Validateur : mots, densite, Hn, liens, duplication du lot
python3 .claude/skills/decupler-page-builder/scripts/validate_page.py \
    --manifeste lot.json          # tableau JSON, pas un objet

# 2. Rendu reel + sonde DOM, aux deux largeurs qui comptent
python3 rendre.py <slug> 1440 16000
python3 rendre.py <slug> 505 21000
```

La sonde compte les éléments dont le bord droit dépasse `clientWidth`. **Elle
est la vérité, pas la capture** : Chromium headless met en page à une largeur
et photographie à une autre, donc une capture peut montrer un défaut qui
n'existe pas — et cacher celui qui existe. Un diagnostic « catastrophe
mobile » a déjà été rendu sur un artefact de capture.

Cibles : `scrollWidth == clientWidth` et **débordements = 0**.

```bash
# 3. Le HTML rendu par WordPress, apres wpautop — pas le fichier pousse
GET /wp-json/wp/v2/pages/{id}?_fields=content
```

Compter `<p><a>`, `<p><img>`, `<p><div>`, `<p></p>`. **Les quatre à zéro.**
C'est ce contrôle qui a rattrapé les cartes vides du bloc « villes voisines ».

## 8. Ce qui reste interdit

- Inventer une adresse, un chiffre client, une note ou un avis. Le siège réel
  est **10 avenue Lympia privée, 06300 Nice** — et c'est le seul. Ailleurs :
  `areaServed`, jamais un `postalAddress`.
- `width: 100vw`. `100vw` inclut la barre de défilement : 15 px de
  débordement, découpés en silence. Le pleine largeur vient du conteneur
  (`ast-site-content-layout = full-width-container`).
- Une ligne vide hors du `<style>`, ou une ligne qui commence par une balise
  inline (`a`, `img`, `span`, `svg`, `b`, `i`, `em`, `strong`).
- Framer Motion. C'est du React ; le site est WordPress + Astra.
