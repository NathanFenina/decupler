---
name: trio-semantique
description: >-
  Aligne les trois couches qui font qu'un moteur (Google, ChatGPT, Perplexity,
  Gemini) comprend QUI parle et DE QUOI : l'entité (Décupler, Nathan Fenina, ou
  la marque d'un client), les données structurées (JSON-LD schema.org relié par
  des @id stables), et le contenu (les mêmes faits, dits de la même façon,
  partout). Audite, corrige et vérifie. À utiliser quand on parle de trio
  sémantique, d'entité, de knowledge graph, de sameAs, de JSON-LD, de schema,
  d'E-E-A-T, de « Google ne sait pas qui on est », « ChatGPT ne nous cite pas
  comme expert », ou avant de créer une page auteur / à propos.
---

# Skill : trio-semantique — entité, données structurées, contenu

Un moteur ne classe pas des pages, il relie des **entités**. Il cite quelqu'un
quand il peut répondre à trois questions : qui est-ce (entité), comment le
sait-il sans ambiguïté (données structurées), et est-ce que tout ce qu'il lit
concorde (contenu). Il suffit qu'une couche flanche pour que l'expert devienne
trois inconnus.

## 1. La source de vérité

Tout part d'une fiche d'identité **vérifiée**, jamais inventée :

| Élément | Décupler (relevé du 29/09/2026) | Source |
|---|---|---|
| Raison sociale | DECUPLER, SAS | Registre national des entreprises (outil infosociétés) |
| SIREN / TVA | 927480319 / FR43927480319 | idem |
| Création | 10/04/2024 | idem |
| Siège | 10 avenue Lympia, 06300 Nice | idem — **seule adresse autorisée** |
| Dirigeant | Nathan Fenina, président | idem |
| Profils | LinkedIn `/in/nathan-fenina/`, YouTube `@nathanfenina`, `decupler.substack.com`, fiche annuaire-entreprises | vérifiés en ligne |

Pour un client : même tableau, rempli avec `search_company` puis `get_company`
(MCP infosociétés), et les profils vérifiés un par un (code 200). Un fait qu'on
ne peut pas sourcer ne va ni dans le JSON-LD ni dans le texte.

## 2. Couche données : des @id stables, une seule fois chaque entité

- **Organisation** : `https://decupler.com/#organization`
- **Personne** : `https://decupler.com/#nathan-fenina`
- Chaque bloc JSON-LD qui parle de Nathan ou de Décupler **référence ces @id**
  (`"author": {"@id": ".../#nathan-fenina"}`) au lieu de redécrire l'entité sans
  identifiant — sinon le moteur voit une personne de plus.

Sur decupler.com, c'est le plugin **`decupler-entite`** (wordpress/plugins/) qui
complète le graphe Yoast sur toutes les pages : données officielles, sameAs,
fondateur, fusion des « personnes » Yoast dans `#nathan-fenina`. Les générateurs
(`scripts/build_article.py`, `build_ville.py`) écrivent déjà ces @id.
Tests : `DOSSIER=… wordpress/tests/test-entite.sh` (15 vérifications).

### Audit rapide d'un site

```bash
# Pour chaque page clé : blocs JSON-LD, types, @id, sameAs
python3 - <<'EOF'
import urllib.request,re,json
for p in ['', 'agence-geo/', 'consultant-seo-nice/', 'claude-code-design/']:
    h=urllib.request.urlopen('https://decupler.com/'+p).read().decode()
    ids=set(re.findall(r'"@id":\s*"([^"]+#[^"]+)"',h))
    print(p or '/', sorted(i for i in ids if 'nathan' in i or 'person' in i or 'organization' in i))
EOF
```

Signaux d'alerte : une Organisation sans `sameAs` ; plusieurs @id pour la même
personne (`#/schema/person/<empreinte>` de Yoast + un @id maison) ; des blocs
`"@type": "Person"` sans @id ; deux URL différentes pour le même profil.

## 3. Couche contenu : dire les mêmes faits partout

- Même nom, même fonction, même ville, même date de création sur toutes les
  pages, dans le texte visible **et** dans le JSON-LD.
- Une **page d'entité** par entité (« entity home ») : la page qui décrit Nathan
  Fenina (parcours vérifiable, profils, publications), vers laquelle pointent
  les sameAs et les bylines. À créer en brouillon, faits sourcés uniquement,
  validés par Nathan avant publication.
- Les pages expertes portent une **signature** (bloc auteur) reliée à l'entité.
- Les preuves (études de cas, chiffres) nomment la source ; aucun chiffre client
  inventé.

## 4. Couche entité hors du site

Ce qui se voit ailleurs confirme ce qui est dit chez soi : fiche Google
Business Profile, LinkedIn (entreprise et personne), annuaires professionnels,
Wikidata si les critères de notoriété sont remplis (ne pas créer d'élément
Wikidata pour une entité non notable : il sera supprimé). Garder les mêmes
nom, adresse, description courte partout.

## 5. Vérification

1. Tests du plugin verts (banc WordPress + Yoast).
2. Sur le site en ligne : une seule Organisation et une seule Personne par page,
   aucune référence `#/schema/person/` restante, sameAs présents.
3. Test des résultats enrichis de Google sur 2 ou 3 pages (Nathan le lance :
   l'outil demande un navigateur).
4. Consigner l'état dans `docs/memoire/etat-du-site.md`.
