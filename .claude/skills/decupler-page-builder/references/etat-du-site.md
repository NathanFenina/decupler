# État du site decupler.com

Ce fichier vieillit. **Le régénérer avant tout lot de contenu** :

```bash
cd /chemin/du/projet          # là où se trouve le .env
python ~/.claude/skills/decupler-page-builder/scripts/check_urls.py
```

L'inventaire machine est dans `references/urls.json` (`vivantes` / `mortes`),
consommé par `validate_page.py --urls`.

Dernier relevé : **17/08/2026 — 101 URLs vivantes, 3 mortes.**

---

## 1. URLs mortes — ne jamais mailler vers elles

| URL | Code |
|---|---|
| `/search-everywhere/` | 410 |
| `/tarifs/` | 410 |
| `/llms.txt` | 410 |

Le site renvoie **410 Gone**, pas 404. Un test qui ne cherche que 404 les
considère vivantes.

Ces trois URLs sont recommandées par le skill `decupler-seo-geo-score`, qui n'a
pas été mis à jour. Ne pas les reprendre.

Remplacements sémantiques utilisés :
`/search-everywhere/` → `/playbook-geo/` · `/tarifs/` → aucun équivalent, ne pas
lier.

---

## 2. Plateforme

| Élément | Valeur |
|---|---|
| CMS | WordPress, API REST `/wp-json/wp/v2/` |
| Auth | Basic, application password (lecture du `.env`, **jamais d'écriture**) |
| Thème | Astra |
| Constructeur | Elementor (header, footer, quelques pages) |
| SEO | Yoast |
| Calendly | `https://calendly.com/fenina-nathan/consultationstrategique` |

---

## 3. Contenus produits

**Pages villes (8)** — Nice, Paris, Toulouse, Bordeaux, Lyon, Lille, Nantes,
Marseille.

**Pages services (3)** — `/audit-geo/`, `/cartographie-ia/`, `/eeat-google/`.

**Cluster GEO 2026 (16 articles)** — calendrier de parution dans
`references/maillage.md` §5. Un article ne lie que ses prédécesseurs.

---

## 4. Cibles de maillage permanentes

Vérifiées à 200. Ancres suggérées dans `references/maillage.md` §4.

```
/agence-seo/            /agence-geo/              /agence-geo-nice/
/seo-local/             /visibilite-llm/          /mesurer-sa-visibilite/
/app/                   /cas-clients/             /claude-skills-repo-github/
/audit-geo-claude-code/ /reddit-pour-le-geo/      /maillage-interne-wordpress/
/agences-geo-france/    /playbook-geo/            /seo-ai-systems/
/audit-geo/             /cartographie-ia/         /eeat-google/
```

---

## 5. Skill voisin — la grille de notation

Le skill de notation s'appelle **`yoast-score`** dans ce dépôt
(`.claude/skills/yoast-score/`), et `decupler-seo-geo-score` sur certains
postes. `validate_page.py` cherche les deux noms, d'abord dans le dépôt puis
chez l'usager ; la variable d'environnement `DECUPLER_ANALYZE` permet de forcer
le chemin.

Il fournit `scripts/analyze_content.py`, dont `validate_page.py` dépend pour
les mesures : nombre de mots, occurrences exactes, densité, position du
mot-clé.

Seuils de densité de sa grille, repris ici :

| Densite effective | Verdict | Malus |
|---|---|---|
| 0 % | ABSENT | — |
| <= 2,5 % | OK | 0 |
| <= 3,5 % | un peu haute | 0 |
| <= 5 % | SUR-OPTIMISATION | -5 |
| <= 6,5 % | — | -8 |
| > 6,5 % | — | -12 |

C'est ce seuil de 3,5 % qui commande toute la formule de longueur.
