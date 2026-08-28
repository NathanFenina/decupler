# Kit netlinking & outreach — Décupler

Mesures du **28 août 2026**, MCP Ubersuggest (`domain_overview`,
`backlinks_overview`, locId 2250, langue fr).

**Point de départ, sans fard :** `decupler.com` est à **DA 9, 116 backlinks,
90 domaines référents**. Les quatre sites qui nous devancent sur les requêtes
« agence GEO » sont à DA 10, 15, 23 et 27. L'écart est franchissable — ce n'est
pas Ahrefs contre nous, c'est un blog perso contre nous. Mais il ne se
franchira pas en un mois, et aucun des liens ci-dessous ne se paie : le plan
entier tient à zéro euro et à du travail.

---

## 1. Ce qu'on offre (quatre monnaies, quatre publics)

| Offre | Pour qui | Ce que ça coûte | Ce que ça rapporte |
|---|---|---|---|
| **Analyse GEO offerte** | annuaires, classements, pairs | ~1 h par cible | ouvre la porte, ne se refuse pas |
| **Audit SEO/GEO + roadmap 90 jours** | prescripteurs, dirigeants | ~2 h par cible | crée une dette de réciprocité |
| **Baromètre GEO France** | médias SEO, presse business | ~3 semaines, une fois | **le seul levier qui ouvre les DA 57-91** |
| **Site internet offert** | prescripteurs locaux | le coût de production | liens + clients réels |

**L'audit gratuit ouvre les portes. Le baromètre est ce qui décroche les gros
liens.** Un média à DA 76 ne publie pas une agence qui offre un audit — il
publie des chiffres que personne d'autre n'a. C'est la seule différence entre
un plan à 5 liens et un plan à 30.

### ⚠️ Le baromètre n'existe pas encore

Les emails 04 et 05 promettent des données. **Ne pas les envoyer avant que
l'étude soit réellement faite.** Griller Abondance, WebRankInfo, BDM et Siècle
Digital avec une promesse creuse, c'est perdre quatre contacts qu'on n'a
qu'une fois. Le baromètre était calé en novembre dans la feuille de route de
Morgane : **c'est à remonter, c'est la pièce maîtresse.**

---

## 2. Les cibles, classées

```bash
python3 scripts/outreach_score.py            # tableau lisible
python3 scripts/outreach_score.py --json     # sortie machine
python3 scripts/outreach_score.py --offre barometre
```

Score sur 100 = **pertinence 40** + **autorité 25** + **accessibilité 20** +
**trafic 15**. L'autorité et le trafic sont en échelle log : passer de DA 10 à
DA 30 change la vie, passer de DA 70 à DA 90 beaucoup moins. Et un DA 91
injoignable vaut moins qu'un DA 15 qui répond — d'où le poids de
l'accessibilité.

**Les seize cibles**, données réelles : voir `cibles.json`.
Quatre domaines ont été **écartés** faute de données (DA 1, zéro backlink) :
`journalducoinmarketing.com`, `lesitedelentrepreneur.fr`, `tribuneseo.com`, et
`cci.fr` (DA 19 — viser les CCI territoriales en direct, pas par email froid).

---

## 3. L'ordre d'exécution

### Vague 1 — cette semaine · 2 emails · 0 €
`agences-geo.com` (score 78,7) et `sebastien-vallat.com` (77,9).

Les deux meilleures cibles du plan sont aussi les deux plus faciles, et ce
n'est pas un hasard : ce sont les seules dont le métier consiste à lister des
agences GEO. Leur DA est bas (10 et 15) mais le lien est **thématiquement
parfait** et il vient d'une page qui ranke déjà sur nos requêtes.
→ `email-01-annuaire-geo.md`, `email-02-classement-agences.md`

### Vague 2 — sous 15 jours · 5 emails · 0 €
`seomix.fr`, `leblogdumarketing.com`, `codeur.com`, `journalducm.com`,
`dynamique-mag.com`. Articles invités et outil open source.
→ `email-03-article-invite.md`, `email-06-wordpress-outil.md`

### Vague 3 — en continu, dès maintenant · 0 €
**Les mentions non liées.** Le lien le plus facile du web : quelqu'un a déjà
décidé de parler de nous, il manque une balise `<a>`. Cherchez
`"Décupler" -site:decupler.com` et `"Nathan Fenina" -site:decupler.com`, et
pour Decathlon, Le Point, Société Générale, Sodexo, Allianz : demandez
directement aux interlocuteurs.
→ `email-09-mention-non-liee.md`

### Vague 4 — en continu · le vrai moteur commercial
**Les prescripteurs locaux** : experts-comptables, CCI territoriales, chambres
de métiers, BNI, coworkings, fédérations de commerçants. Ce n'est pas du
netlinking, c'est du partenariat qui produit un lien en passant. Le lien vaut
peu en DA ; il vaut beaucoup en chiffre d'affaires.
→ `email-07-prescripteur.md`

### Vague 5 — après le baromètre, pas avant
`webrankinfo.com`, `abondance.com`, `blogdumoderateur.com`, `siecledigital.fr`,
`journaldunet.com`, `chefdentreprise.com`, `nicematin.com`.
→ `email-04-media-data.md`, `email-05-tribune.md`, `email-08-presse-locale.md`

---

## 4. Ce qu'on ne fait pas

- **Pas d'achat de lien.** Hors budget, et hors des règles de Google.
- **Pas d'échange de liens réciproques.** L'effet s'annule et le motif se voit.
- **Pas de troisième relance.** Deux, puis on clôt. (`email-10-relances.md`)
- **Pas d'annuaires génériques.** Un lien depuis un annuaire fourre-tout ne
  pèse rien. `agences-geo.com` est l'exception : il est mono-thématique.
- **Pas d'envoi en masse.** Chaque email de ce kit contient au moins un champ
  `{}` qui exige d'avoir lu la cible. Un email non personnalisé ne reçoit pas
  de réponse — il grille le domaine expéditeur.

---

## 5. Attentes réalistes

Sur 16 cibles, avec des emails personnalisés et deux relances :
**3 à 6 liens obtenus sur 3 mois**, dont probablement les deux de la vague 1
sous quinze jours. Ça ne fera pas passer decupler.com de DA 9 à DA 30. Ça le
mettra à parité thématique avec les quatre sites qui nous devancent
aujourd'hui — ce qui, sur des requêtes à 614 impressions et 0 clic, est
exactement ce qui manque.

Le suivi se tient dans `suivi.csv`.
