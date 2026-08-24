# En-tête du site

`header.html` est le contenu du **widget HTML Elementor** de l'en-tête.
Il se colle en entier — il porte son CSS, son balisage et son script.

## Ce que fait `menu_offre.py`

L'onglet « Site offert » vit dans le méga-menu **Expertises**, en sixième
colonne. Ses liens sont générés plutôt qu'écrits à la main : le menu et la
page pilier décrivent la même offre, et deux sources tenues à la main
finissent toujours par diverger.

```bash
python3 content/header/menu_offre.py
```

Trois fichiers sortent dans `/tmp` :

| Fichier | Où le coller dans `header.html` |
|---|---|
| `menu_colonne.html` | après la colonne « Les secteurs », dans `.d-side-nav` |
| `menu_onglet.html` | après `<div class="d-tab-content" id="tab-secteur">…</div>` |
| `menu_mobile.html` | après « Les Secteurs », dans le `.d-mobile-sub` d'Expertises |

## Vérifier avant de coller

```bash
node scripts/rendu/apercu_menu.mjs          # desktop : /tmp/menu-{ferme,offre,agents}.png
node scripts/rendu/apercu_menu_mobile.mjs   # mobile  : /tmp/menu-mobile.png
```
