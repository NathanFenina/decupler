# Dossier — Skill `yoast-score` (Décupler)

> Le « Yoast + Rank Math » de Décupler, en mieux : il **note** un contenu sur 100
> (feux 🔴🟡🟢 par critère, façon Yoast), **explique pourquoi**, puis **ré-optimise
> le contenu lui-même** — ce qu'aucun plugin ne fait. Générique : **tous les
> domaines / tous les clients** (Apogea, Pluxee, Reux, BeTomorrow, TechMedias…).

Ce dossier documente le skill de A à Z : rôle, déclenchement, entrées, processus,
grille complète (critères + seuils + pourquoi), conditions/règles, couverture
Yoast/Rank Math, et les **exemples réels avant/après** qui ont servi au calibrage.

---

## 1. À quoi il sert

- **Remplacer Yoast/Rank Math** de bout en bout, dans Claude, sans passer par le
  plugin WordPress. On travaille le contenu, on le colle dans WP une fois optimisé.
- **Deux modes** :
  - **Audit** → score /100 + feux par critère + recommandations + *pourquoi*.
  - **Ré-optimisation** → réécrit le contenu pour viser le vert et livre un fichier
    prêt à coller, avec un **avant/après** de score.
- **S'applique à tout** : article de blog, page service/produit, landing, fiche ;
  n'importe quel client ; marché FR par défaut.

## 2. Quand il se déclenche

Dès qu'on veut **auditer / scorer / noter / évaluer** un contenu sur un mot-clé, ou
**optimiser / ré-optimiser / corriger / réécrire** pour le SEO, ou qu'on parle de
Yoast, Rank Math, « score SEO », « note sur 100 », feux rouge/orange/vert, ou
d'optimisation pour les IA (GEO/AEO). En cas de contenu spécifique à un client qui a
son propre skill, ce dernier prime ; sinon, c'est ce skill générique.

## 3. Entrées (inputs)

| Entrée | Obligatoire | Rôle |
|---|---|---|
| **Contenu** (texte / HTML / URL) | ✅ | Ce qu'on audite |
| **Mot-clé principal** | ✅ | Commande tout le score (comme le focus keyphrase Yoast) |
| **Mots-clés secondaires** | ⬜ | Variantes / longue traîne, à couvrir naturellement |
| **Liste des liens/pages du site** | ⬜ | Pour insérer du **maillage interne** pertinent en ré-optimisation |

**Important — le choix du mot-clé est un travail amont** (volume/KD/intention via
Search Console, Semrush, Ubersuggest, ou les skills `geo-opportunities` /
`cartographie-client`). Ce skill **audite contre le mot-clé fourni**, il ne le
choisit pas. S'il manque, il le **déduit** du title/H1/URL et l'annonce clairement.

## 4. Processus (déterministe = réaliste et reproductible)

1. **Mesure objective** via le script `scripts/analyze_content.py` : nombre de mots,
   densité du mot-clé (exacte **et distribuée**, façon Yoast), malus sur-optimisation,
   % de phrases longues, mots de transition, liens internes/externes, images+alt,
   titres Hn, présence FAQ/schema. → *On mesure, on ne devine pas.*
2. **Notation** sur la grille (`references/criteres-scoring.md`), en croisant les
   mesures et le jugement qualitatif (pertinence, ton, intention). Doute → feu le plus
   sévère.
3. **Calcul** : points → total par catégorie → score brut → **malus sur-optimisation**
   → score final. Gestion des N/A par redistribution.
4. **Rapport** : score, tableau des feux, détail par critère **avec le “pourquoi”**,
   plan d'action priorisé.
5. **Ré-optimisation** (si demandée) : réécriture visant le vert, maillage interne
   depuis les liens fournis, densité maîtrisée, FAQ/GEO, puis **fichier + avant/après**.

## 5. La grille de notation (100 points, 6 catégories)

Détail complet des seuils 🔴/🟡/🟢 et du *pourquoi* de chaque critère :
voir **`references/criteres-scoring.md`**. Résumé :

| # | Catégorie | Pts | Critères (résumé) |
|---|---|---|---|
| 1 | **Mot-clé & sémantique** | 20 | mot-clé dans title, H1, intro, meta, sous-titre, URL ; densité ; champ sémantique |
| 2 | **Balises techniques & méta** | 18 | longueur title, meta description, slug, alt images, données structurées |
| 3 | **Structure & titres Hn** | 16 | H1 unique, hiérarchie Hn, fréquence des sous-titres, longueur, éléments scannables |
| 4 | **Lisibilité** | 16 | longueur des phrases, des paragraphes, mots de transition, voix passive, clarté |
| 5 | **Maillage & E-E-A-T** | 15 | liens internes/externes, ancres, données/sources, expertise, intention |
| 6 | **GEO / AEO** | 15 | réponse citable, structure Q→R, faits extractibles, FAQ schema, entités, fraîcheur |

**Chaque critère porte une phrase “pourquoi”** dans la grille (ex. *Title* : « c'est le
signal de pertinence le plus fort et le texte cliqué dans les résultats »).

### Bandes de score global
- **80–100 🟢** : bien optimisé, prêt / ajustements mineurs.
- **55–79 🟡** : correct, optimisations importantes à faire.
- **0–54 🔴** : sous-optimisé, retravail nécessaire.

## 6. Conditions & règles clés

- **Malus sur-optimisation (anti-bourrage)** — appliqué au score global selon la
  densité du mot-clé : 3,5–5 % → −5 ; 5–6,5 % → −8 ; > 6,5 % → −12. Parce qu'un
  mot-clé répété partout dégrade *tout* le contenu, pas juste un critère.
- **Occurrences vs densité (le “25 fois”)** — ce qui compte est la **densité ~1,5–2,5 %**,
  pas un compte brut. Sur un article **long** (~2 500 mots), viser 1,5–2,5 % revient
  naturellement à **~25-35 occurrences** ; sur une page courte, beaucoup moins. On ne
  gonfle jamais le compte au prix de la densité.
- **Correspondance distribuée** — le mot-clé compte même avec de petits mots au milieu
  (« rénovation **à** Fontainebleau »), comme Yoast. Évite de pénaliser à tort un
  mot-clé local bien placé.
- **Mots-clés secondaires** — présents naturellement (quelques fois, idéalement dans un
  sous-titre) ; leur sur-répétition est pénalisée comme le principal.
- **Maillage interne** — depuis la liste de liens fournie, on insère des liens vers les
  pages **réellement pertinentes**, ancres naturelles ; jamais d'URL inventée.
- **N/A + redistribution** — une info non fournie (title/meta/slug absent de ce qui est
  collé) = ⚪ N/A, retirée du total et redistribuée ; score annoncé « sous réserve ».
  Une optimisation *ratée* (title présent mais sans mot-clé) reste 🔴.
- **Priorité en ré-optimisation** — d'abord l'important ET le **réellement modifiable**
  dans le contenu (title, meta, H1, intro, densité, sous-titres, maillage, FAQ).

## 7. Couverture Yoast + Rank Math

Le skill reproduit **tous les checks pertinents** de Yoast (analyse SEO + lisibilité)
et de Rank Math, **plus** la couche GEO/AEO qu'ils n'ont pas. Détail du mapping :
voir **`references/couverture-yoast-rankmath.md`**. Hors périmètre (volontaire) :
crawl technique, vitesse, backlinks, indexation — c'est un audit **de contenu**.

## 8. Exemples réels — avant / après (calibrage)

### Exemple A — TechMedias, article « Content Marketing 2026 »
Mot-clé : **content marketing**. Référence **Rank Math : 73/100**.

| Étape | Résultat |
|---|---|
| Skill **avant** correction du barème | 83/100 (trop gentil : bourrage sous-pondéré) |
| Après ajout du **malus sur-optimisation** | **75/100** — aligné sur Rank Math (73), +2 = bonus GEO (FAQ+schema) |
| Cause de l'écart initial | densité réelle **6,24 %** (mot-clé 20× en 641 mots), non pas 3,64 % |
| **Ré-optimisation** | densité **6,24 % → 2,30 %**, phrases longues 42 % → ~20 %, +2 liens externes, meta étoffée → **score projeté ~94/100** |

*Enseignement :* le compte brut trompe ; c'est la densité qui parle. Le malus a
recalé le skill sur Rank Math.

### Exemple B — Reux Travaux, page « À propos »
Mot-clé business : **entreprise de rénovation Fontainebleau**. Référence Rank Math : 65
(mais focus keyword RM inconnu → non comparable pile).

| Étape | Résultat |
|---|---|
| Skill (mot-clé quasi absent : « rénovation » 1×) | **59/100** (cat. mot-clé 5/20) |
| Point clé | le **mot-clé commande tout** : la même page sur « entreprise ReuxTravaux Fontainebleau » (présent dans le title) scorerait ~15 pts de plus |
| Bug de mesure trouvé | « rénovation **à** Fontainebleau » comptait 0 en exact → correction “distribuée” ajoutée |
| **Ré-optimisation** | mot-clé injecté (title/H1/intro/sous-titre, densité 0 → 2 %), meta ajoutée, phrases 71 % → 33 %, mini-FAQ + JSON-LD → **score projeté ~90/100** |

*Enseignement :* une page « À propos » n'est pas la bonne cible pour un mot-clé
commercial ; et surtout, **préciser le bon mot-clé est décisif**.

## 9. Contenu du skill (arborescence)

```
yoast-score/
├── SKILL.md                              ← le "prompt" : rôle, modes, processus, format
├── README.md                             ← ce dossier
├── scripts/
│   └── analyze_content.py                ← le "code" : mesures objectives
└── references/
    ├── criteres-scoring.md               ← la grille (critères, seuils, pourquoi, malus)
    └── couverture-yoast-rankmath.md      ← mapping Yoast + Rank Math → grille
```

## 10. Installation

Le skill est livré empaqueté en **`yoast-score.skill`**. Pour l'enregistrer :
ouvre le fichier `.skill` dans Claude et clique sur **« Save skill »** (installation
dans ton profil). Il devient alors disponible partout, pour tous les domaines/clients.
