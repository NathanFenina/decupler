# En-tête du site

`header.html` est le contenu du **widget HTML Elementor** de l'en-tête.
Il se colle en entier — il porte son CSS, son balisage et son script.

## Ce que fait `menu_offre.py`

L'entrée « Site offert » du menu, desktop et mobile, est générée à partir de
`content/data/agents_locaux.py` : le menu et la page pilier décrivent la même
chose, les écrire deux fois à la main c'est garantir qu'ils divergeront.

```bash
python3 content/header/menu_offre.py     # écrit /tmp/menu_desktop.html et /tmp/menu_mobile.html
```

Puis réinjecter les deux blocs dans `header.html`, entre les commentaires
`<!-- SITE OFFERT -->` et `<!-- EXPERTISES -->`.

## Vérifier avant de coller

```bash
node scripts/rendu/apercu_menu.mjs          # desktop : /tmp/menu-{ferme,offre,agents}.png
node scripts/rendu/apercu_menu_mobile.mjs   # mobile  : /tmp/menu-mobile.png
```
