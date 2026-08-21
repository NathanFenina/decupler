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


## ⚠ La coquille locale ne suffit pas

`captures.mjs` injecte le fragment avec `setContent` : le navigateur n'a aucun
accès réseau, donc **les polices Google ne se chargent pas**. Le rendu utilise
les polices système, plus étroites — le texte tient là où il déborderait en
production. C'est ce qui a laissé passer un téléphone tronqué de 29 px sur la
page en ligne alors que la coquille disait « ok ».

Pour juger un rendu, passer par le miroir :

```
python3 scripts/rendu/miroir.py https://decupler.com/site-internet-offert/ /tmp/m
cd /tmp/m && python3 -m http.server 8790 --bind 127.0.0.1 &
# puis charger http://127.0.0.1:8790/page.html dans Chromium
```

`miroir.py` rapatrie la page ET ses ressources (thème Astra, polices, images),
réécrit les URL en chemins relatifs et sert le tout depuis 127.0.0.1 — que le
navigateur atteint sans proxy. Ce qu'on regarde alors est la vraie page.
