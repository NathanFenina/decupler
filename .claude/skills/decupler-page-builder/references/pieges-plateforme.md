# Pièges plateforme — decupler.com

Tous constatés en production, tous coûteux, tous invisibles au premier abord.
À lire avant le premier push.

---

## 1. wpautop : WordPress réécrit votre HTML

WordPress insère des retours à la ligne autour des balises de bloc, puis
enveloppe dans `<p>` tout ce qui traîne. Deux conséquences.

**Les lignes vides sont dangereuses.** Une ligne vide au milieu du HTML crée un
`<p></p>` parasite, parfois au milieu d'une grille flex, qui casse la mise en
page. **Aucune ligne vide dans le contenu**, sauf à l'intérieur du bloc
`<style>` où elles sont sans effet.

**Les éléments inline orphelins sont pires.** Un `<span>`, `<svg>`, `<a>`,
`<b>` ou `<i>` qui est frère direct d'un élément de bloc se fait envelopper
dans un `<p>` — et l'ouverture du `<p>` avale la fermeture du bloc suivant.

```html
<!-- casse : le </div> est avalé -->
<div class="carte"><span>Recherche</span></div>

<!-- sûr : que des blocs entre blocs -->
<div class="carte"><div class="etiquette">Recherche</div></div>
```

Règle pratique : dans un conteneur qui contient des `<div>`, n'utilisez que des
`<div>`. Un `<svg>` isolé se enveloppe dans un `<div>`.

Le validateur détecte les deux cas.

---

## 2. Yoast : asymétrie articles / pages

| Post type | `_yoast_wpseo_title` | `_metadesc` | `_focuskw` |
|---|---|---|---|
| `posts` (articles) | écrivable API | écrivable API | écrivable API |
| `pages` | **ignoré** | **ignoré** | **ignoré** |

L'API accepte la requête, renvoie 200, et **jette silencieusement** les champs
Yoast sur une page. Vérifiable via `OPTIONS /wp/v2/pages` : les clés n'y
figurent pas dans le schéma `meta` accessible en écriture.

Conséquence : pour toute page ville ou service, **fournir les valeurs à Nathan
pour saisie manuelle**, et ne pas prétendre que c'est fait.

---

## 3. Elementor

**Le cache bloque les mises à jour.** Une écriture API dans `_elementor_data`
n'apparaît pas sur le site tant que « Effacer les fichiers et les données »
(Elementor → Outils) n'a pas été cliqué. Le contenu en base est pourtant bien
modifié — vérifiable en relisant le champ. Toujours prévenir quand une
modification passe par ce champ.

**`_elementor_data` n'est pas lisible partout :**

| Post type | Lecture | Écriture |
|---|---|---|
| `posts`, `pages` | oui | oui |
| `elementor_library` (header, footer) | **non** | oui |

Pour modifier le header ou le footer, on ne peut donc pas partir de l'existant :
il faut livrer le HTML complet à coller à la main dans le widget.

**`_elementor_edit_mode`** vaut `'builder'` (rendu depuis `_elementor_data`) ou
`''` (rendu depuis `content`). La bascule est réversible et utile quand on veut
reprendre la main sur une page construite dans Elementor.

---

## 4. Thème Astra

Deux corrections systématiques sur toute page pleine largeur.

```css
/* le thème réserve 4em de marge : 60px de blanc au-dessus du hero */
.site-content #primary { margin: 0 !important; }
/* le thème affiche son propre titre : H1 en double */
body .ast-article-single > .entry-header, .entry-title { display: none !important; }
```

Le bloc complet de neutralisation est dans `references/charte-da.md`.

**Pleine largeur** dans un thème contraint :

```css
.bloc { width: 100vw; margin-left: calc(50% - 50vw); margin-right: calc(50% - 50vw); }
```

**`position: sticky` fonctionne** malgré le `overflow-x: hidden` du body —
vérifié empiriquement sur les 23 articles. Ne pas repasser par du JavaScript,
qui relâchait le CTA avant la FAQ.

---

## 5. URL supprimées : 410, pas 404

Le site renvoie **410 Gone** sur les URL supprimées. Un test qui ne cherche que
404 les considère vivantes. `scripts/check_urls.py` traite 404 et 410 comme
mortes.

URL connues mortes, à ne jamais utiliser en maillage : `/search-everywhere/`,
`/tarifs/`, `/llms.txt`.

---

## 6. Médias : collisions de slug

WordPress ne dédoublonne pas les fichiers : un second upload de
`article-mon-slug.jpg` devient `article-mon-slug-1.jpg`, et le **slug du média
d'origine peut se décaler** en `-2`. Après quelques allers-retours on se
retrouve avec quatre fichiers pour une image.

Règle : chercher le média par slug avant tout upload, et le réutiliser.
`push_wp.py` le fait. En cas de désordre déjà installé, supprimer tous les
médias correspondants puis repousser une fois.

---

## 7. Publication : ne rien déprogrammer

Un `POST /wp/v2/posts/{id}` avec `"status": "draft"` **déprogramme** un article
planifié, sans avertissement.

`push_wp.py` relit le statut existant et le conserve. Ne jamais forcer un statut
en dur dans un script de mise à jour.

Même logique pour le slug : chercher l'article par slug **avant** de créer,
sinon WordPress crée un doublon suffixé `-2`.

---

## 8. Rate limiting

Au-delà d'une dizaine de requêtes concurrentes, le serveur renvoie des réponses
incohérentes (comptages qui varient d'un appel à l'autre). Les audits doivent
être **séquentiels**, quitte à être lents.
