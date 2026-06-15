# content/ — Contenu récupéré du site hacké

## raw/ — Dépose ici l'export brut
Place ton fichier d'export WordPress ici, par exemple :

    content/raw/decupler.WordPress.xml

⚠️ Le XML est **sûr** (c'est du contenu : pages, articles, catégories, métadonnées).
En revanche, ne réimporte JAMAIS de fichiers PHP/thème/plugins de l'ancien site : c'est
là que vivent les backdoors.

Si tu as pu récupérer des fichiers via FTP, mets-les aussi ici :
- `content/raw/uploads/` — images encore présentes dans wp-content/uploads
- `content/raw/db-dump.sql` — dump SQL de secours (phpMyAdmin > Exporter)

## cleaned/ — Généré par les scripts
Le contenu parsé et nettoyé (HTML Elementor purgé : shortcodes, divs imbriquées)
sera écrit ici par `scripts/parse_xml.py`, prêt pour le réimport.

## Note confidentialité
Si tu utilises git et que le XML contient des données privées, ajoute
`content/raw/` au `.gitignore` (déjà fait par défaut).
