# Archives

Ce qui n'est plus utilisé au quotidien mais qu'on garde pour mémoire. Rien ici
n'est lu par les scripts actifs.

| Dossier | Contenu |
|---|---|
| `pages-avant-refonte/` | Versions de pages telles qu'elles étaient en ligne avant une refonte (`*.avant.html`, `_sauvegarde-*`). Utiles pour comparer ou restaurer un passage. |
| `scripts-migration/` | Extraction de l'ancien export WordPress (`parse_wxr.py`) et nettoyage du HTML Elementor (`clean_content.py`), écrits pour la migration abandonnée. Ils écrivent dans `content/cleaned/`, ignoré par git. |
| `docs/` | Journal de la migration VPS / Next.js, abandonnée. |

Les sauvegardes faites avant chaque écriture sur le site en ligne (JSON des
pages, de l'en-tête, des réglages) restent hors dépôt, dans le dossier de
travail de la session : elles peuvent contenir des données du site.
