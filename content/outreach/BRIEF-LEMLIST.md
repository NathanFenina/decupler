# Brief campagne — « Audit SEO/GEO offert », Alpes-Maritimes

> Document auto-portant. Il est fait pour être déposé tel quel dans un projet
> Claude Code connecté à lemlist, qui n'a aucun contexte sur Décupler.
> Tout ce qu'il faut est ici. Rien à aller chercher ailleurs.

---

## 1. Qui envoie

**Décupler**, agence SEO/GEO basée à Nice. Fondateur : **Nathan Fenina**.
Site : `https://decupler.com`. Répondre à : `projects@decupler.com`.

Décupler fait du référencement classique (Google) **et** du GEO — la visibilité
dans les réponses générées par ChatGPT, Perplexity, Gemini et les AI Overviews
de Google. C'est ce second volet qui porte toute la campagne : c'est nouveau,
personne ne l'a montré à ces prospects, et ça se démontre en une capture d'écran.

Références clients : Decathlon, Le Point, Société Générale, Sodexo, Allianz.
Utilisables dans les relances, pas dans le premier message — trop « vendeur »
en ouverture.

**À ne pas surjouer :** Décupler est une petite structure. Le message ne dit
jamais « leader », « expert n°1 », ni ne donne de chiffre de croissance inventé.
La crédibilité vient de la démonstration, pas de l'adjectif.

## 2. L'offre, en une phrase

> L'audit de votre visibilité — Google **et** moteurs IA — offert, avec une
> feuille de route sur 90 jours. Sans contrepartie et sans rendez-vous
> commercial obligatoire.

C'est un vrai audit, réellement produit, environ 2 h de travail par cible. **Si
la campagne convertit à 30 %, il faut être capable de livrer.** Caler le débit
d'envoi là-dessus : mieux vaut 8 emails par semaine tenus que 80 promis.

## 3. À qui — et à qui surtout pas

**Cible retenue : les cabinets d'expertise comptable et les réseaux
professionnels des Alpes-Maritimes.** Raison : ce sont les seuls prospects qui
sont **à la fois** client potentiel (ils ont un site qui se bat sur
« expert comptable nice ») **et** prescripteur (ils ont 200 clients TPE à qui
parler de nous). Toutes les autres cibles ne rapportent qu'une des deux choses.

**Cible secondaire** (campagne 2, plus tard) : dirigeants de TPE locales —
dentistes, plombiers, électriciens, instituts de beauté. Le site de Décupler a
déjà une page dédiée pour chacun de ces quatre métiers.

**À exclure formellement de toute liste :**

- **Les médias et blogs SEO** — Abondance, WebRankInfo, Blog du Modérateur,
  Siècle Digital, Journal du Net. Ils n'ont aucun besoin d'un audit SEO ; leur
  envoyer cette offre est ridicule et grille le contact définitivement. Ils
  relèvent d'une campagne séparée, adossée à une étude chiffrée.
- **Les agences qui font déjà du SEO** dans le 06 : Agence NOCTA, VCOMK,
  CKC-Net, Tendances.media. Ce sont des concurrents.
- Toute adresse en `@gmail`, `@orange`, `@wanadoo` : hors cadre B2B.

## 4. Le mécanisme du message

Une seule idée porte toute la campagne :

> On pose la vraie requête à ChatGPT et à Perplexity — « un expert-comptable à
> Nice pour une PME » — on regarde qui sort, et on le leur dit.

C'est concret, vérifiable, et personne d'autre ne le fait. Un email qui dit
« je peux améliorer votre référencement » finit à la corbeille. Un email qui dit
« j'ai posé la question hier, voilà les trois cabinets qui sortent, vous n'y
êtes pas » se lit jusqu'au bout.

**Cela impose une contrainte absolue : le test doit être réellement fait, pour
chaque lead, avant l'envoi.** Voir §6.

## 5. Le fichier de leads

`content/outreach/lemlist/leads-prescripteurs.csv` — 8 leads, adresses relevées
sur les sites publics des sociétés et vérifiées une par une. Aucune devinée.

Dans lemlist, **chaque en-tête de colonne devient une variable** utilisable
comme `{{nomDeColonne}}`.

| Colonne | Rôle |
|---|---|
| `email` | destinataire |
| `salutation` | **pré-calculée**, vaut `Bonjour` ou `Bonjour {Prénom}` |
| `firstName` | vide sur les adresses génériques — ne pas l'utiliser seul |
| `companyName` | nom du cabinet |
| `ville`, `metier`, `effectif` | personnalisation factuelle |
| `siteWeb` | domaine à auditer |
| `requeteTest` | **la requête exacte à poser aux IA** pour ce lead |
| `segment` | `prescripteur` ou `reseau` — pilote la variante d'email |
| `accroche` | **à remplir par l'agent** — voir §6 |
| `constatIA` | **à remplir par l'agent** — voir §6 |
| `notes` | matière première pour écrire l'accroche |

**Pourquoi une colonne `salutation` pré-calculée.** Sept des huit adresses sont
génériques (`contact@`, `secretariat@`) et n'ont pas de prénom associé. Un
`Bonjour {{firstName}}` produirait « Bonjour , » — la signature d'un
publipostage, sur le premier mot du message. Pré-calculer la salutation en
amont règle le problème sans dépendre de la syntaxe de valeur de repli de
lemlist, qui n'est pas la même partout. **Ne pas remplacer `{{salutation}}` par
`{{firstName}}` dans les gabarits.**

## 6. Le travail de l'agent, avant tout envoi

C'est le cœur de la campagne, et ce n'est pas automatisable à l'aveugle.
Pour **chaque ligne** du CSV, avant de charger la campagne :

**a) Poser la requête `requeteTest`** à ChatGPT et à Perplexity. Relever les
entreprises citées. Trois issues :

| Ce qu'on observe | Ce qu'on écrit dans `constatIA` |
|---|---|
| Le cabinet n'est cité nulle part | `Le vôtre n'en fait pas partie.` |
| Cité par un moteur, pas l'autre | `Vous sortez chez Perplexity mais pas chez ChatGPT.` |
| Cité par les deux | `Vous sortez chez les deux — c'est rare, et c'est fragile.` |

Le troisième cas n'est pas un échec : c'est la meilleure accroche des trois.
**Ne jamais écrire « vous n'y êtes pas » sans avoir vérifié.** Un prospect qui
teste et se voit cité répond pour le dire, et la campagne est morte.

**b) Ouvrir `siteWeb`** et écrire `accroche` : une phrase, factuelle,
spécifique, invérifiable ailleurs. Puisée dans `notes` ou sur le site.
Exemples corrects :

> `1988, Promenade des Anglais, 52 personnes — vous êtes un des rares cabinets du 06 à avoir passé la barre des 50.`
> `Trois bureaux entre Nice, Antibes et Mouans-Sartoux : vous avez donc trois fois le problème dont je vais vous parler.`

Exemples à rejeter : « J'espère que vous allez bien », « Je me permets de vous
contacter », « Votre cabinet a retenu mon attention ». Génériques, donc nuls.

**c) Contrôle avant envoi.** Aucun lead ne part si `accroche` ou `constatIA`
vaut encore `A REMPLIR`. Faire échouer le chargement plutôt que d'envoyer un
gabarit à trous.

## 7. La séquence lemlist

Trois étapes, dans le même fil, arrêt automatique à la première réponse.

| Étape | Délai | Objet | Corps |
|---|---|---|---|
| 1 | J+0 | voir §8 | Email 1 |
| 2 | J+7 ouvré | *(réponse au fil, pas de nouvel objet)* | Relance 1 |
| 3 | J+18 ouvré | *(réponse au fil)* | Relance 2 — clôture |

Puis **stop définitif**. Pas de quatrième message : ça ne convertit rien et ça
détruit la réputation du domaine.

**Réglages lemlist :**

- **Arrêt sur réponse** : activé (`stop on reply`).
- **Suivi des ouvertures** : **désactivé**. Le pixel de tracking dégrade la
  délivrabilité et, sur 8 leads, la statistique n'a aucune valeur. On mesure
  les réponses, rien d'autre.
- **Suivi des clics** : désactivé, pour la même raison — et parce qu'il
  réécrit les URL, ce qui déclenche les filtres.
- **Volume** : 20 envois/jour maximum sur le domaine, quel que soit le nombre
  de campagnes en parallèle.
- **Créneau** : mardi–jeudi, 8 h–10 h, heure de Paris. Un expert-comptable
  traite ses emails tôt.
- **Chauffe du domaine** : si `decupler.com` n'a jamais servi à de l'envoi en
  volume, lancer lemwarm **deux semaines avant** la campagne. Sinon les huit
  emails partent en spam et on ne le saura jamais.
- **Désinscription** : lien obligatoire dans chaque email (§10). Vérifier le
  token exact proposé par le compte lemlist plutôt que d'en supposer un —
  à défaut, la phrase « répondez stop » du gabarit tient lieu de mécanisme,
  et il faut alors traiter les « stop » à la main.

## 8. Les emails

### Étape 1 — J+0

**Objet :** `Ce que ChatGPT répond quand on cherche un {{metier}} à {{ville}}`

```
{{salutation}},

{{accroche}}

J'ai posé la question à ChatGPT et à Perplexity la semaine dernière :
« {{requeteTest}} ». Les deux citent trois cabinets. {{constatIA}}

Ce n'est pas un jugement sur votre travail — c'est un filtre technique, et la
plupart des cabinets ignorent qu'il existe. Il se corrige.

Je dirige Décupler, une agence SEO à Nice. Je vous propose l'audit de
{{siteWeb}}, gratuitement et sans contrepartie :

— votre visibilité réelle dans ChatGPT, Perplexity et les réponses IA de
  Google, requête par requête, captures à l'appui
— ce qui vous manque techniquement pour être cité, classé par ordre d'impact
— une feuille de route sur 90 jours, chiffrée en temps, que votre prestataire
  actuel peut exécuter — ou vous-même

Aucune condition. Vous le lisez, vous en faites ce que vous voulez. Je le fais
parce que c'est le meilleur moyen de vous montrer comment on travaille.

Trois jours de mon côté. Vous me dites juste oui.

Nathan Fenina
Décupler — https://decupler.com
```

**Variante `segment = reseau`** — remplacer les deux derniers paragraphes par :

```
Je vous propose de le faire pour trois de vos adhérents, gratuitement, ceux
que vous choisissez. S'ils trouvent ça utile, vous en parlez aux autres. S'ils
trouvent ça creux, vous n'en parlez à personne et on en reste là.

Et je peux venir présenter les résultats à vos adhérents, sur une heure, sans
rien vendre à la fin.
```

### Étape 2 — J+7 : on apporte quelque chose

```
{{salutation}},

Je remonte mon message, il est sûrement passé sous une pile.

Depuis, j'ai fait tourner le test sur les dix premiers cabinets du 06 : trois
seulement sont cités par ChatGPT, et ce ne sont pas les trois plus gros. Je
vous mets le détail dans l'audit si vous le voulez.

Si le sujet ne vous intéresse pas, dites-le-moi franchement — je ne reviendrai
pas dessus.

Nathan
```

> ⚠️ Cette relance affirme un résultat chiffré. **Faire réellement le test sur
> dix cabinets avant de l'activer**, et remplacer les chiffres par ce qui sort.
> Si le test n'est pas fait, retirer le paragraphe et relancer sur autre chose.

### Étape 3 — J+18 : on ferme proprement

```
{{salutation}},

Dernier message de ma part, promis.

L'audit reste offert et le restera encore quelques semaines. Si un jour ça
devient utile, mon adresse ne change pas.

Bonne continuation, et merci d'avoir lu.

Nathan
```

## 9. Ce qu'on ne fait jamais

- **Pas de fausse urgence** (« offre valable jusqu'à vendredi »). Sur un
  expert-comptable, ça détruit la crédibilité en une ligne.
- **Pas de chiffre inventé.** Aucun « +250 % de trafic », aucun « 40 clients
  accompagnés » qui ne soit vrai et vérifiable.
- **Pas de pièce jointe** au premier message : dégrade la délivrabilité.
- **Pas de lien de prise de rendez-vous** en étape 1. La seule action demandée
  est de répondre « oui ». Un lien Calendly transforme un cadeau en tunnel de
  vente.
- **Pas de quatrième message.**
- **Pas d'envoi si `accroche` ou `constatIA` vaut `A REMPLIR`.**

## 10. RGPD

La prospection B2B par email est licite en France sur la base de l'intérêt
légitime, à trois conditions cumulatives :

1. **l'objet du message est en rapport avec la fonction** du destinataire — un
   expert-comptable démarché sur la visibilité de son cabinet : conforme ;
2. **l'identité de l'expéditeur est visible** — nom, société, site : présents
   dans la signature ;
3. **un moyen de refus simple et gratuit** figure dans chaque message.

Le point 3 est le seul qui puisse manquer par négligence. Soit le lien de
désinscription lemlist, soit, à défaut, la mention « répondez *stop* et je vous
retire définitivement de ma liste » — auquel cas les « stop » doivent être
traités manuellement sous 48 h. **Ne pas retirer cette mention des gabarits.**

Conserver la trace de la source de chaque adresse : ici, le site public de la
société, colonne `notes`. C'est ce qui est demandé en cas de réclamation.

## 11. Ce qu'on mesure

Sur 8 leads, aucun taux n'a de valeur statistique. On compte des réponses.

| Repère | Seuil |
|---|---|
| Réponses | 2 ou plus sur 8 → le message fonctionne, on élargit |
| | 0 sur 8 après l'étape 3 → le message ou la cible est à revoir, pas à répéter |
| Audits livrés | 100 % de ceux acceptés, sous 5 jours ouvrés |
| Désinscriptions | 1 seule → relire les gabarits avant d'élargir |

Élargir avant d'avoir livré les premiers audits est la seule vraie façon de
rater cette campagne.

## 12. Étendre la liste

Sept cibles sont identifiées mais sans adresse publique : Panacée Expertise,
NOVACEA, CONSEILIANCE, Bosphore Sense, ANECS/CJEC Côte d'Azur, et les associés
nominatifs du Groupe Ferrua Ribes (Jerome Ribes, Geoffrey Benmergui). Elles
sont dans `content/outreach/suivi-prospection.csv` au statut `bloque`.
Récupérables par enrichissement, ~1 crédit par contact.

**Hors campagne email : Cédric Messina**, fondateur de l'Agence Comback (36
personnes, Nice) — agence qui ne fait pas de SEO — et **vice-président de la
CCI Nice Côte d'Azur**, ex-vice-président Comex40 du MEDEF, ambassadeur French
Tech. Un seul rendez-vous ouvre l'agence, la CCI et le réseau local.
**À contacter par LinkedIn ou par introduction, jamais par email froid.** Le
mettre dans une séquence automatisée serait le gâchis le plus coûteux du plan.
