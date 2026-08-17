# Maillage interne

Règle fondatrice : **jamais de bloc « À découvrir aussi sur Décupler » en pied
de contenu**. Les liens se posent dans le fil du texte, ancrés sur des
expressions qui existent déjà.

Un bloc de liens en pied est ignoré des lecteurs et dilué pour les moteurs. Une
ancre contextuelle transmet du sens.

---

## 1. Les six règles

1. **≥ 8 liens internes** par contenu.
2. **Ancre = une expression déjà présente** dans le texte. On n'ajoute pas une
   phrase pour caser un lien ; si aucune ancre ne se présente, c'est que le lien
   n'est pas pertinent — ou qu'il manque une idée au texte.
3. **Jamais dans un Hn**, une légende, un lien existant, un bloc de code.
4. **Un lien maximum par segment de texte**, pour aérer.
5. **Jamais en contexte négatif.** Une ancre qui tombe sur « méthode
   propriétaire opaque » ou « accepter un seul moteur » associe une page
   Décupler à une mauvaise pratique. Contrôle visuel obligatoire.
6. **Jamais l'ancre du mot-clé principal** de la page courante, ni un lien vers
   elle-même.

---

## 2. Ne jamais publier de lien mort

Deux causes de liens morts, deux parades.

**URL supprimée** — le site renvoie **410**, pas 404. Vérifier avec
`scripts/check_urls.py`, qui traite 404 et 410 comme mortes.
Mortes connues : `/search-everywhere/`, `/tarifs/`, `/llms.txt`.

**Contenu pas encore paru** — quand on produit un lot programmé sur plusieurs
semaines, un article ne doit lier que ceux **déjà en ligne le jour de sa
parution**. Concrètement : trier le lot par date de publication, et n'autoriser
que les prédécesseurs.

Le premier article du lot ne peut donc lier que des pages permanentes. C'est
normal, et c'est suffisant : il y a une vingtaine de cibles permanentes.

---

## 3. Comment poser les liens

Le mécanisme est un dictionnaire `URL → [expressions d'ancrage, par ordre de
préférence]`, parcouru dans l'ordre. Pour chaque URL autorisée et non encore
utilisée, on cherche la première occurrence libre d'une de ses expressions.

Les expressions vont du plus spécifique au plus générique :

```python
("/audit-geo/", ["audit GEO", "diagnostic initial", "audit de départ",
                 "relevé initial", "diagnostic", "audit", "le relevé"]),
```

L'expression générique n'est utilisée que si aucune expression spécifique n'a
été trouvée. Cela évite les ancres pauvres tout en garantissant le volume.

Le découpage doit être **conscient des balises** : on ne remplace que dans les
nœuds de texte situés hors des zones interdites (§1.3).

---

## 4. Cibles permanentes

Toujours vérifier avec `check_urls.py` avant un lot : la liste vieillit.

| URL | Bonnes ancres |
|---|---|
| `/audit-geo/` | audit GEO, diagnostic initial, relevé de départ |
| `/mesurer-sa-visibilite/` | taux de citation, mesure de départ |
| `/cartographie-ia/` | cartographie des citations, référentiel de formulations, prompts |
| `/app/` | outil automatisé, tableau de bord, outillage |
| `/reddit-pour-le-geo/` | espaces communautaires, forums, discussions |
| `/eeat-google/` | auteur identifiable, signature d'auteur, autorité |
| `/agence-seo/` | socle SEO, SEO classique, référencement naturel |
| `/playbook-geo/` | plan d'action, feuille de route, étapes |
| `/agence-geo/` | agence GEO, agence spécialisée, un prestataire |
| `/cas-clients/` | cas documentés, retours d'expérience, une mission |
| `/visibilite-llm/` | visibilité générative, modèles de langage |
| `/maillage-interne-wordpress/` | maillage interne, structure du site, vos pages |
| `/seo-ai-systems/` | moteurs génératifs, moteurs de réponse |
| `/agences-geo-france/` | classement des agences, palmarès, les acteurs |
| `/audit-geo-claude-code/` | automatisation, automatisable, scripter |
| `/claude-skills-repo-github/` | protocole documenté, contrat de mesure |
| `/seo-local/` | référencement local, zone desservie, marché local |
| `/agence-geo-nice/` | Nice |

---

## 5. Cluster GEO 2026 — ordre de parution

Un article ne lie que ceux situés au-dessus de lui.

```
agence-referencement-chatgpt        14/08 (publié)
agence-seo-ia                       17/08
referencement-chatgpt               19/08
agence-referencement-ia             21/08
agence-visibilite-ia                24/08
agence-aeo                          26/08
referencement-gemini                28/08
referencement-perplexity            31/08
seo-pour-chatgpt                    02/09
cest-quoi-le-geo                    04/09
expert-geo                          07/09
freelance-geo                       09/09
top-agences-geo-france              11/09
comment-apparaitre-dans-chatgpt     14/09
visibilite-chatgpt                  16/09
etre-cite-par-chatgpt               18/09
```

Ancres pour ces pages : le mot-clé exact de la cible, plus deux ou trois
expressions propres à son sujet (`GPTBot` → `/seo-pour-chatgpt/`, `Perplexity` →
`/referencement-perplexity/`, `part de voix` → `/visibilite-chatgpt/`).

---

## 6. Contrôle

`validate_page.py` vérifie : nombre de liens ≥ 8, aucun lien répété, aucune
cible inconnue, aucune cible paraissant après le contenu courant.

Le contrôle du **contexte négatif reste manuel** : afficher les ancres avec 50
caractères de contexte avant et après, et les relire.
