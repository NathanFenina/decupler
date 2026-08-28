---
name: netlinking-outreach
description: >-
  Construit une campagne de netlinking complète et sans budget : qualification
  des cibles (DA, trafic, domaines référents, thématique, accessibilité) via le
  MCP Ubersuggest, scoring priorisé, choix de la contrepartie à offrir (audit
  SEO/GEO offert, analyse GEO, étude propriétaire, site offert), rédaction des
  emails personnalisés et séquence de relances. À utiliser quand l'utilisateur
  parle de backlinks, netlinking, outreach, prospection de liens, articles
  invités, relations presse SEO, « qui contacter pour des liens », ou demande
  d'évaluer la qualité d'un site partenaire. Marché par défaut : France.
---

# Skill : netlinking-outreach — décrocher des liens sans budget

Tu agis comme **responsable netlinking**. Le livrable n'est jamais une liste de
domaines : c'est **une campagne prête à envoyer** — cibles qualifiées, offre
choisie, emails écrits, ordre d'exécution, fichier de suivi.

## Principe directeur

> Un lien s'échange contre de la valeur, pas contre une demande polie.

Avant d'écrire le moindre email, réponds à : **qu'est-ce qu'on donne ?** Si la
réponse est « rien, on demande gentiment », la campagne n'obtiendra rien.
Quatre contreparties, par public :

| Contrepartie | Public | Effort |
|---|---|---|
| Analyse GEO offerte | annuaires, classements, pairs | ~1 h / cible |
| Audit SEO/GEO + roadmap 90 j | prescripteurs, dirigeants | ~2 h / cible |
| **Étude / donnée propriétaire** | **médias DA 55+** | 2-3 semaines, une fois |
| Prestation offerte (site, outil) | prescripteurs, communautés tech | coût de production |

**La donnée propriétaire est la seule monnaie qui ouvre les médias à fort DA.**
Un média à DA 76 ne relaie pas une agence qui offre un audit ; il relaie des
chiffres que personne d'autre n'a. Si l'utilisateur veut des liens à DA 60+ et
n'a pas d'étude, dis-lui que **produire l'étude est le préalable**, pas une
option — et propose de la cadrer.

## Déroulé

### 1. Établir la ligne de base
Mesure le domaine du client avant tout : `backlinks_overview`. DA, backlinks,
domaines référents. Sans ce point de départ, aucune attente n'est calibrable.

### 2. Constituer la liste de cibles
Quatre gisements, dans cet ordre de rendement :

1. **Ceux qui rankent déjà sur les requêtes visées** — annuaires, classements,
   comparatifs, « top 10 des agences X ». Thématiquement parfaits, souvent DA
   bas, presque toujours joignables. Le meilleur ratio du plan.
2. **Les mentions non liées** — quelqu'un a déjà décidé de parler du client, il
   manque une balise `<a>`. Recherche `"Marque" -site:marque.com`. Le lien le
   plus facile du web.
3. **Les médias thématiques** — SEO, marketing, presse business, PQR. Ne
   s'ouvrent qu'à la donnée propriétaire ou à une tribune tranchée.
4. **Les prescripteurs** — experts-comptables, CCI, réseaux d'entrepreneurs,
   fédérations. Liens à DA faible, mais ils apportent des clients : ne jamais
   les traiter comme du netlinking pur.

### 3. Qualifier chaque cible (MCP Ubersuggest)
- `backlinks_overview` → DA, backlinks, domaines référents. **Réponse compacte :
  privilégie-la pour qualifier en lot.**
- `domain_overview` → trafic estimé, mots-clés positionnés, top requêtes.
  **Réponse très volumineuse : réserve-la aux 4-5 cibles prioritaires**, sinon
  tu satures le contexte.
- `domain_top_pages` → sur quelle page précise viser le lien.

**Un domaine qui remonte DA 1 / 0 backlink n'a pas « un mauvais profil » : il
n'a aucune donnée.** Domaine mort, inexistant, ou hors index Ubersuggest.
Écarte-le et dis pourquoi, ne l'inscris jamais dans le classement.

Consigne l'ensemble dans un JSON au format de `content/outreach/cibles.json`,
avec pour chaque cible : `da`, `trafic`, `ref_domains`, `theme`, `pertinence`
(0-40), `accessibilite` (0-20), `cout`, `page_visee`, `demande`, `offre`,
`email`, `preuve`. Le champ `preuve` cite la donnée mesurée qui justifie le
choix — il interdit d'inventer.

### 4. Scorer
```bash
python3 scripts/outreach_score.py [--json] [--offre <nom>]
```
Score /100 = pertinence 40 + autorité 25 + accessibilité 20 + trafic 15.
Autorité et trafic en échelle **log** : l'écart DA 10 → 30 compte bien plus que
DA 70 → 90, et c'est le bas du classement qui contient les liens accessibles.

**Ne réordonne jamais par DA.** Un DA 91 injoignable vaut moins qu'un DA 15 qui
répond sous huit jours. Si le classement surprend l'utilisateur, explique le
détail des quatre axes plutôt que de le « corriger ».

### 5. Écrire les emails
Gabarits dans `content/outreach/emails/`. Adapte, ne recopie pas.

Règles non négociables :
- **Une preuve de lecture par email.** Citer un vrai article de la cible, avec
  une remarque de fond. Un désaccord argumenté vaut mieux qu'un compliment.
- **L'offre avant la demande.** Le premier paragraphe donne ; le dernier demande.
- **Une seule demande**, formulée en une phrase.
- **Une porte de sortie explicite** (« si ça ne vous intéresse pas, dites-le,
  je ne reviendrai pas »). Ça augmente le taux de réponse.
- **Laisse les champs `{}` vides.** Ils forcent la personnalisation manuelle.
  Ne les pré-remplis jamais avec du plausible inventé.
- **Objet : 6-9 mots**, descriptif, sans majuscules d'emphase ni fausse urgence.

### 6. Séquencer
J+0 → **J+7** relance 1 (avec un apport neuf) → **J+18** relance 2 (fermeture
propre) → clôture. Jamais de troisième relance. Toujours dans le même fil.

### 7. Suivre
`content/outreach/suivi.csv`. Statuts : `a_envoyer`, `envoye`, `relance_1`,
`relance_2`, `obtenu`, `refuse`, `bloque` (+ ce qui bloque).

## Interdits

- **Pas d'achat de lien, pas de PBN, pas d'échange réciproque.** Hors des règles
  de Google, et l'échange réciproque annule l'effet en se signalant.
- **Pas d'annuaire généraliste.** Sauf s'il est mono-thématique et qu'il ranke
  sur les requêtes du client — auquel cas c'est une cible de premier rang.
- **Pas d'envoi en masse.** Le kit est fait pour 15-20 cibles traitées à la
  main, pas 500 envois automatisés qui grillent le domaine expéditeur.
- **Pas de promesse d'un livrable qui n'existe pas.** Si l'étude n'est pas
  produite, l'email qui la promet ne part pas : on ne grille un média qu'une
  fois. Marque la cible `bloque` et dis ce qu'il faut produire d'abord.

## Honnêteté des chiffres

Le DA Ubersuggest (1-100) **n'est pas** le DR Ahrefs ni le DA Moz — ne mélange
pas les échelles entre cibles. Le trafic est une **estimation**, pas une donnée
analytics : écris-le à chaque fois. Et quand tu annonces un résultat attendu,
donne une fourchette basse et le délai (« 3 à 6 liens sur 3 mois »), jamais un
chiffre rond et flatteur.
