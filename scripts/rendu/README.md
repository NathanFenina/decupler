# Vérification de rendu

`captures.mjs` rend un fragment HTML dans une **coquille qui reproduit la
géométrie mesurée sur decupler.com** (`.ast-container` 1280 px → `.entry-content`
à x=20, w=1240), puis capture la page par écrans successifs.

```
node scripts/rendu/captures.mjs content/articles/offre-site-offert.html /tmp/sortie 1440
```

Deux pièges appris à la dure :

1. `screenshot()` de Puppeteer ré-émule les métriques de l'écran. Ça déclenche
   un `resize`, donc un recalcul de la gouttière sur une largeur factice : les
   bandes pleine largeur perdent leur débord **sur la capture seulement**. Le
   script fige donc les marges avant de capturer.
2. Un `getBoundingClientRect()` correct ne prouve pas que l'élément est peint :
   un ancêtre en `overflow:hidden` le rogne sans changer sa géométrie. Vérifier
   au pixel (`elementFromPoint`, couleur du point) et pas seulement à la mesure.
