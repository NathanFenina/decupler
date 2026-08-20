# -*- coding: utf-8 -*-
"""Source unique des 20 skills GSC : alimente .claude/skills/ ET la page publique.

Champs : (nom, groupe, question, triggers, donnees, methode[], sortie)
"""
S = [
# ---------- A · DIAGNOSTIQUER ----------
("gsc-quick-wins","Diagnostiquer",
 "Quelles pages sont juste sous le seuil de trafic, et lesquelles rapportent le plus vite si on les pousse ?",
 "quick wins, striking distance, pages en position 8-20, sur quoi travailler en priorité, gains rapides SEO",
 "`query` + `page`, 28 derniers jours : impressions, clics, CTR, position moyenne.",
 ["Filtrer les couples (requête, page) en **position 8 à 20** avec au moins 50 impressions sur la période.",
  "Estimer le gain : `impressions × (CTR attendu en position 3 − CTR actuel)`. Utiliser une courbe CTR/position de référence, pas une moyenne du site.",
  "Agréger par URL et trier par gain estimé décroissant.",
  "Écarter les requêtes de marque : elles gonflent le classement sans rien apprendre."],
 "Un tableau URL · requête principale · position · impressions · gain de clics estimé, trié par gain. Top 10 commenté."),

("gsc-chute-trafic","Diagnostiquer",
 "J'ai perdu du trafic : est-ce le classement, le CTR, ou la demande qui a baissé ?",
 "baisse de trafic, chute SEO, j'ai perdu des visites, mon trafic s'effondre, pourquoi moins de clics",
 "Deux périodes comparables (même longueur, mêmes jours de semaine) : clics, impressions, CTR, position.",
 ["Décomposer la variation de clics en trois causes : **position** (position moyenne dégradée), **CTR** (position stable mais moins de clics), **demande** (impressions en baisse à position constante).",
  "Chiffrer la part de chaque cause dans la perte totale — c'est le cœur du diagnostic.",
  "Descendre au niveau URL pour les 10 plus grosses pertes.",
  "Vérifier `gsc-saisonnalite` avant de conclure à un problème."],
 "Un verdict en une phrase (« 70 % de la perte vient du CTR, pas du classement ») + le détail par cause et par URL."),

("gsc-content-decay","Diagnostiquer",
 "Quelles pages déclinent lentement depuis plusieurs mois, avant qu'elles ne disparaissent ?",
 "content decay, pages qui déclinent, contenu qui s'essouffle, pages à rafraîchir, perte progressive",
 "12 derniers mois par `page` et par mois : clics, impressions, position.",
 ["Repérer les pages en baisse sur **3 mois consécutifs au minimum** — un mauvais mois isolé est du bruit, pas du déclin.",
  "Calculer la pente sur 6 mois et le pourcentage perdu depuis le pic.",
  "Croiser avec la date de dernière mise à jour de la page si elle est disponible.",
  "Classer par volume perdu en valeur absolue, pas en pourcentage : −20 % sur une grosse page vaut plus que −80 % sur une page morte."],
 "Liste des pages en déclin avec pente, clics perdus, mois de bascule, et une recommandation par page (rafraîchir / fusionner / laisser mourir)."),

("gsc-cannibalisation","Diagnostiquer",
 "Quelles pages de mon site se battent entre elles sur la même requête ?",
 "cannibalisation, deux pages même mot-clé, mes pages se concurrencent, quelle page garder",
 "`query` + `page` sur 3 mois : impressions, clics, position par couple.",
 ["Isoler les requêtes servies par **2 URLs ou plus** avec des impressions significatives sur chacune.",
  "Signaler les cas où Google **alterne** entre les URLs d'un mois sur l'autre : c'est le vrai symptôme, pas la simple co-présence.",
  "Désigner l'URL à garder : celle qui a la meilleure position moyenne ET les meilleurs signaux de conversion.",
  "Distinguer la vraie cannibalisation d'une couverture légitime (une page catégorie et une page produit peuvent coexister)."],
 "Par requête : les URLs en conflit, laquelle garder, et l'action (fusion + redirection, désoptimisation, ou différenciation d'intention)."),

("gsc-ctr-anormal","Diagnostiquer",
 "Quelles pages sous-performent en clics compte tenu de la position qu'elles occupent déjà ?",
 "CTR faible, beaucoup d'impressions peu de clics, mes titles ne donnent pas envie, taux de clic anormal",
 "`query` + `page`, 28 jours : impressions, clics, CTR, position.",
 ["Établir la **courbe CTR/position du site** (CTR médian observé pour chaque position) — c'est la référence, pas un standard générique.",
  "Repérer les pages dont le CTR est nettement sous la médiane de leur propre position.",
  "Filtrer sur un minimum d'impressions pour éviter les faux positifs statistiques.",
  "Vérifier la SERP : un AI Overview ou un featured snippet concurrent explique parfois tout le déficit."],
 "Les pages à fort potentiel de CTR, avec l'écart chiffré à la courbe. Passer la main à `gsc-reecriture-title`."),

("gsc-requetes-neuves","Diagnostiquer",
 "Sur quelles requêtes Google a-t-il commencé à me montrer, sans que j'aie de page dédiée ?",
 "nouvelles requêtes, requêtes émergentes, sur quoi je commence à sortir, nouveaux mots-clés",
 "Deux périodes de 28 jours consécutives, dimension `query`.",
 ["Isoler les requêtes présentes sur la période récente et **absentes** de la précédente.",
  "Écarter le bruit : exiger un seuil d'impressions.",
  "Pour chaque requête neuve, identifier la page qui la reçoit et juger si elle est la bonne.",
  "Regrouper les requêtes neuves par thème : un cluster émergent vaut une page, pas une ligne."],
 "Les requêtes émergentes groupées par thème, avec la page actuellement servie et un verdict : page adaptée / à enrichir / à créer."),

("gsc-gagnants-perdants","Diagnostiquer",
 "Qu'est-ce qui monte et qu'est-ce qui tombe depuis le mois dernier ?",
 "évolution mensuelle, gagnants perdants, comparaison mois précédent, qu'est-ce qui a bougé",
 "Deux périodes comparables, par `page` et par `query`.",
 ["Comparer clics, impressions et position sur des périodes de longueur identique.",
  "Classer séparément les gains et les pertes, en valeur absolue.",
  "Pour chaque mouvement important, donner la cause probable (renvoyer vers `gsc-chute-trafic`).",
  "Ne jamais présenter un pourcentage sans le volume associé."],
 "Deux tableaux (top gains / top pertes) avec volume, variation, et cause probable."),

("gsc-saisonnalite","Diagnostiquer",
 "Cette baisse est-elle un problème, ou mon creux annuel habituel ?",
 "saisonnalité, est-ce normal cette baisse, creux annuel, comparer à l'an dernier",
 "16 mois d'historique minimum, par mois.",
 ["Comparer le mois courant au **même mois de l'année précédente**, pas au mois précédent.",
  "Calculer l'indice saisonnier de chaque mois sur l'historique disponible.",
  "Décider si l'écart observé sort de la fourchette saisonnière normale.",
  "Le dire franchement quand il n'y a pas assez d'historique pour conclure."],
 "Un verdict : saisonnier attendu / anomalie réelle / historique insuffisant, avec le graphique année sur année."),

# ---------- B · PRODUIRE ----------
("gsc-sections-manquantes","Produire",
 "Quelles questions cette page reçoit-elle sans y répondre ?",
 "sections manquantes, ma page ne répond pas à tout, enrichir une page, que rajouter dans cet article",
 "Toutes les requêtes servies par UNE URL, 3 mois.",
 ["Récupérer l'intégralité des requêtes que la page reçoit, y compris celles à faibles impressions.",
  "Les regrouper en intentions distinctes.",
  "Confronter chaque intention au contenu réel de la page : la traite-t-elle explicitement, ou Google l'a-t-il servie par défaut ?",
  "Ne proposer que les sections **absentes** — ne jamais réécrire ce qui existe déjà."],
 "La liste des sections à ajouter, avec pour chacune les requêtes qui la justifient et le volume d'impressions en jeu."),

("gsc-brief-depuis-requetes","Produire",
 "Comment écrire un brief à partir de ce que les gens tapent vraiment, pas de ce qu'un outil suggère ?",
 "brief à partir de GSC, brief basé sur mes données, plan d'article depuis Search Console",
 "Requêtes d'une page ou d'un cluster, 6 mois.",
 ["Partir des requêtes réelles : elles portent le vocabulaire exact des acheteurs.",
  "Grouper par intention, puis ordonner les groupes par volume d'impressions — cet ordre devient le plan Hn.",
  "Extraire les formulations interrogatives : elles deviennent des H3 ou des entrées de FAQ.",
  "Compléter avec la SERP (via DataForSEO ou Firecrawl) uniquement pour ce que GSC ne peut pas dire : ce que couvrent les concurrents."],
 "Un brief : angle, plan Hn ordonné, vocabulaire imposé, questions à traiter, et le volume d'impressions qui justifie chaque section."),

("gsc-reecriture-title","Produire",
 "Comment réécrire mes titles et metas pour récupérer les clics que je laisse sur la table ?",
 "réécrire les titles, améliorer le CTR, optimiser meta description, mes titres ne cliquent pas",
 "Sortie de `gsc-ctr-anormal` + title/meta actuels des pages ciblées.",
 ["Reprendre les pages identifiées en déficit de CTR.",
  "Réécrire en intégrant **la formulation exacte** de la requête la plus porteuse de la page.",
  "Respecter les limites d'affichage (environ 60 caractères pour le title, 155 pour la meta).",
  "Proposer deux variantes par page pour permettre un test.",
  "Estimer le gain de clics si le CTR rejoint la médiane de sa position."],
 "Un tableau : URL, title actuel → 2 propositions, meta actuelle → 2 propositions, gain de clics estimé."),

("gsc-faq-depuis-requetes","Produire",
 "Quelles questions dois-je mettre en FAQ, en me basant sur ce qu'on me demande vraiment ?",
 "FAQ depuis GSC, questions fréquentes réelles, quelles questions ajouter, FAQ basée sur les données",
 "Requêtes interrogatives d'une page ou d'un site, 6 mois.",
 ["Isoler les requêtes qui commencent par un interrogatif (comment, pourquoi, combien, quel, est-ce que…) ou qui en ont la forme.",
  "Dédupliquer les reformulations d'une même question.",
  "Trier par impressions et retenir celles qui ne sont pas déjà traitées dans le corps de la page.",
  "Rédiger des réponses courtes et autonomes — c'est ce format que les moteurs génératifs citent."],
 "Le bloc FAQ rédigé + le JSON-LD `FAQPage` correspondant, prêt à coller."),

("gsc-page-a-creer","Produire",
 "Quels sujets méritent une page dédiée que je n'ai pas encore ?",
 "quelles pages créer, sujets sans page, opportunités de contenu, trous dans mon site",
 "Toutes les requêtes du site, 6 mois, avec leur page servie.",
 ["Regrouper les requêtes en clusters sémantiques.",
  "Repérer les clusters où **aucune page n'est vraiment dédiée** : les impressions sont dispersées sur des pages approximatives, avec des positions faibles.",
  "Estimer le potentiel du cluster : impressions cumulées et position moyenne actuelle.",
  "Vérifier l'absence de doublon avec l'inventaire interne avant de proposer une création."],
 "Les clusters orphelins classés par potentiel, avec pour chacun le mot-clé principal, les requêtes couvertes et la page à créer."),

("gsc-consolidation","Produire",
 "Comment fusionner mes pages qui se cannibalisent, sans perdre de trafic ?",
 "fusionner des pages, consolidation, plan de redirection, regrouper mes contenus",
 "Sortie de `gsc-cannibalisation` + contenu des pages concernées.",
 ["Désigner la page canonique : meilleure position, meilleure profondeur, meilleurs signaux business.",
  "Lister ce que les pages absorbées apportent d'unique et qui doit être **transféré** avant redirection.",
  "Produire le plan de redirection 301, une ligne par URL.",
  "Lister les liens internes à mettre à jour pour ne pas laisser de chaînes de redirection."],
 "Le plan de fusion : page cible, contenu à transférer, redirections 301, liens internes à corriger."),

("gsc-maillage","Produire",
 "Quels liens internes ajouter, et depuis quelles pages exactement ?",
 "maillage interne, liens internes, quelles pages lier, netlinking interne",
 "Requêtes par page sur tout le site.",
 ["Calculer la proximité sémantique entre pages à partir du recouvrement de leurs requêtes.",
  "Proposer un lien quand une page A reçoit des requêtes proches du sujet d'une page B mieux positionnée.",
  "Proposer l'ancre à partir de la requête réelle partagée, jamais une ancre générique.",
  "Prioriser les liens venant des pages qui reçoivent déjà du trafic — un lien depuis une page morte ne vaut rien."],
 "Un tableau : page source, page cible, ancre proposée, requête qui la justifie, trafic de la page source."),

# ---------- C · PILOTER ----------
("gsc-rapport-mensuel","Piloter",
 "À quoi ressemble le mois écoulé, et qu'est-ce que ça veut dire ?",
 "rapport mensuel, reporting client, bilan du mois, rapport SEO",
 "Mois courant vs M-1 vs même mois N-1. GA4 et PostHog si branchés.",
 ["Donner d'abord les chiffres clés : clics, impressions, position moyenne, avec les deux comparaisons.",
  "Nommer les 3 mouvements qui expliquent l'essentiel de la variation — pas une liste de 40 lignes.",
  "Croiser avec les conversions si GA4 est disponible : « le trafic monte sur les pages qui ne convertissent pas » est une information, « le trafic monte » n'en est pas une.",
  "Terminer par les actions du mois suivant, priorisées.",
  "Ne jamais inventer un chiffre absent des données."],
 "Un rapport structuré : chiffres clés, ce qui a bougé et pourquoi, actions du mois suivant."),

("gsc-alerte","Piloter",
 "Qu'est-ce qui vient de décrocher et que je n'ai pas vu ?",
 "alerte SEO, surveillance, prévenir si ça baisse, monitoring Search Console",
 "7 derniers jours vs les 4 semaines précédentes.",
 ["Définir les seuils avant de regarder les données, pour éviter de justifier après coup.",
  "Surveiller : chute de clics d'une URL importante, perte de position sur une requête stratégique, effondrement de CTR, disparition d'une page de l'index.",
  "Comparer à des jours équivalents — un lundi contre un dimanche ne veut rien dire.",
  "Ne remonter que ce qui dépasse le seuil : une alerte qui crie tout le temps n'est plus lue."],
 "Une liste d'alertes ou, mieux, la confirmation explicite qu'il n'y a rien à signaler."),

("gsc-panier-cibles","Piloter",
 "Où en sont les requêtes sur lesquelles j'ai décidé de me battre ?",
 "suivi de mots-clés, mes requêtes cibles, positions suivies, où j'en suis sur mes mots-clés",
 "Un panier de requêtes défini par le client, suivi mois par mois.",
 ["Suivre position, impressions et clics pour chaque requête du panier.",
  "Afficher la trajectoire sur 6 mois, pas seulement l'instantané.",
  "Signaler les requêtes qui franchissent un palier (entrée en page 1, entrée dans le top 3).",
  "Indiquer la page qui se positionne, et alerter si Google en change."],
 "Le tableau de suivi avec trajectoire, paliers franchis, et changements de page servie."),

("gsc-indexation","Piloter",
 "Qu'est-ce qui n'est pas indexé, et pourquoi ?",
 "indexation, pages non indexées, couverture, google n'indexe pas mes pages",
 "Rapport de couverture + inspection d'URL + sitemap.",
 ["Confronter les URLs du sitemap aux URLs réellement indexées.",
  "Classer les exclusions par motif : découverte sans indexation, explorée non indexée, canonique différente, 404, redirection.",
  "Traiter en priorité les pages qui comptent — une page de pagination non indexée n'est pas un problème.",
  "Pour chaque motif, donner la correction concrète, pas juste le constat."],
 "Les pages non indexées qui comptent, groupées par motif, avec l'action de correction."),

("gsc-google-vs-llm","Piloter",
 "Je suis bien placé sur Google — est-ce que les IA me citent pour autant ?",
 "visibilité IA vs Google, écart GEO, suis-je cité par ChatGPT, comparer position et citations",
 "Requêtes cibles GSC + interrogation des moteurs génératifs (Perplexity, ChatGPT).",
 ["Prendre les requêtes où le site est déjà bien positionné sur Google.",
  "Poser ces mêmes questions aux moteurs génératifs et relever qui est cité, et à quel rang.",
  "Mettre les deux colonnes face à face : l'écart est la feuille de route GEO.",
  "Identifier les sources que les moteurs citent à la place — c'est là qu'il faut aller se faire mentionner.",
  "Journaliser chaque relevé pour mesurer l'évolution d'un mois sur l'autre."],
 "Le tableau position Google / citation LLM par requête, l'écart chiffré, et les sources concurrentes à travailler."),
]



# Prompts de production, copiables tels quels. Remplacer {domaine} et {page}.
GARDE = ("Ne jamais inventer un chiffre : si la donnée manque ou si le volume\n"
         "est trop faible pour conclure, dis-le explicitement.\n"
         "Indique toujours la période et le volume qui portent tes conclusions.")

PROMPTS = {

"gsc-quick-wins": """Contexte : site {domaine}, marché France.
Objectif : trouver où je gagne le plus de trafic pour le moins d'effort.

1. Récupère les couples (requête, page) sur les 28 derniers jours :
   impressions, clics, CTR, position moyenne.
2. Ne garde que la position 8 à 20, avec au moins 50 impressions.
3. Écarte les requêtes contenant ma marque : elles gonflent le
   classement sans rien m'apprendre.
4. Construis la courbe CTR/position de MON site — le CTR médian que
   j'observe à chaque position. N'utilise pas une courbe standard.
5. Estime le gain par couple :
   impressions × (CTR médian en position 3 − CTR actuel).
6. Agrège par URL, additionne, trie par gain décroissant.

Rends un tableau : URL | requête principale | position | impressions |
gain estimé en clics/mois. Puis commente le top 10 : pour chacune, une
phrase sur ce qui bloque probablement (intention mal servie, page trop
courte, title faible).

""" + GARDE,

"gsc-chute-trafic": """Contexte : site {domaine}. J'ai perdu du trafic organique.
Objectif : savoir de quoi vient la perte avant de corriger quoi que ce soit.

1. Prends les 28 derniers jours et les 28 précédents. Vérifie que les
   deux périodes contiennent le même nombre de chaque jour de semaine.
2. Décompose la variation de clics en trois causes :
   - POSITION : je suis moins bien classé qu'avant
   - CTR : je suis classé pareil mais on me clique moins
   - DEMANDE : mes impressions baissent à position constante
3. Chiffre la part de chaque cause dans la perte totale, en clics et en
   pourcentage. C'est le cœur de la réponse — commence par ça.
4. Descends au niveau URL pour les 10 plus grosses pertes et refais la
   même décomposition sur chacune.
5. Avant de conclure à un problème, vérifie la saisonnalité : compare
   au même mois de l'année précédente.

Rends d'abord un verdict en une phrase du type « 70 % de la perte vient
du CTR, pas du classement », puis le détail par cause et par URL.
Termine par ce que je dois corriger en premier.

""" + GARDE,

"gsc-content-decay": """Contexte : site {domaine}.
Objectif : repérer les pages qui s'éteignent lentement, avant qu'elles
ne disparaissent complètement.

1. Récupère 12 mois d'historique par page et par mois : clics,
   impressions, position moyenne.
2. Ne retiens une page que si elle baisse sur au moins 3 mois
   CONSÉCUTIFS. Un mauvais mois isolé est du bruit, pas du déclin.
3. Pour chaque page retenue, calcule la pente sur 6 mois, le pourcentage
   perdu depuis son pic, et le mois où la bascule commence.
4. Classe par clics perdus en VALEUR ABSOLUE, pas en pourcentage :
   −20 % sur une grosse page vaut plus que −80 % sur une page morte.
5. Si tu as la date de dernière mise à jour de chaque page, mets-la en
   face — une corrélation avec l'ancienneté oriente le diagnostic.

Rends un tableau : URL | pente 6 mois | clics perdus | mois de bascule |
recommandation. La recommandation doit trancher entre trois options
seulement : rafraîchir, fusionner, ou laisser mourir. Justifie en une
phrase pour chaque page.

""" + GARDE,

"gsc-cannibalisation": """Contexte : site {domaine}.
Objectif : trouver les pages qui se font concurrence entre elles.

1. Récupère les couples (requête, page) sur les 3 derniers mois.
2. Isole les requêtes servies par 2 URLs ou plus, avec des impressions
   significatives sur chacune (au moins 30).
3. Distingue deux situations, c'est essentiel :
   - VRAIE cannibalisation : Google ALTERNE entre mes URLs d'un mois
     sur l'autre. C'est le symptôme qui compte.
   - Couverture légitime : une page catégorie et une page produit
     peuvent coexister sur la même requête sans problème.
4. Pour chaque conflit réel, désigne l'URL à garder : celle qui a la
   meilleure position moyenne ET la meilleure intention business.
5. Mesure ce que le conflit coûte : compare la position moyenne quand
   les deux pages se battent à la meilleure position observée.

Rends, par requête : les URLs en conflit, leurs positions mois par mois,
laquelle garder, et l'action — fusion et redirection, désoptimisation de
la perdante, ou différenciation d'intention. Ne propose une fusion que
si les deux pages traitent réellement le même sujet.

""" + GARDE,

"gsc-ctr-anormal": """Contexte : site {domaine}.
Objectif : récupérer les clics que je laisse sur la table à position égale.

1. Récupère les couples (requête, page) sur 28 jours : impressions,
   clics, CTR, position.
2. Construis d'abord la courbe CTR/position de MON site : pour chaque
   position entière, le CTR médian que j'observe réellement. C'est la
   référence — un standard générique du marché ne vaut rien ici.
3. Repère les pages dont le CTR est nettement sous la médiane de leur
   PROPRE position. Exige au moins 200 impressions pour éviter les faux
   positifs statistiques.
4. Pour les 10 pires écarts, vérifie la SERP : un AI Overview, un
   featured snippet concurrent ou un bloc shopping expliquent parfois
   tout le déficit. Dans ce cas, dis-le — ce n'est pas un problème de
   title.
5. Chiffre le manque à gagner : impressions × (CTR médian − CTR actuel).

Rends un tableau : URL | requête | position | CTR actuel | CTR médian à
cette position | écart | clics perdus/mois. Sépare clairement les cas
« title à réécrire » des cas « la SERP me vole le clic ».

""" + GARDE,

"gsc-requetes-neuves": """Contexte : site {domaine}.
Objectif : attraper les sujets sur lesquels Google commence à me tester.

1. Compare les 28 derniers jours aux 28 précédents, dimension requête.
2. Isole les requêtes présentes sur la période récente et TOTALEMENT
   absentes de la précédente.
3. Écarte le bruit : exige au moins 20 impressions sur la période
   récente. Écarte aussi les requêtes de marque.
4. Pour chaque requête neuve, identifie la page qui la reçoit
   aujourd'hui et juge si c'est la bonne : Google me sert-il une page
   pertinente, ou une page par défaut faute de mieux ?
5. Regroupe les requêtes neuves par thème. Un cluster émergent mérite
   une page dédiée, une requête isolée ne mérite qu'une section.

Rends les clusters émergents triés par impressions cumulées, avec pour
chacun : les requêtes qui le composent, la page actuellement servie, sa
position, et un verdict en trois options — page adaptée, page à
enrichir, page à créer.

""" + GARDE,

"gsc-gagnants-perdants": """Contexte : site {domaine}.
Objectif : voir ce qui a bougé ce mois-ci, et de combien.

1. Compare le mois écoulé au précédent, sur des périodes de longueur
   strictement identique. Fais-le par page ET par requête.
2. Classe séparément les gains et les pertes, en VALEUR ABSOLUE de
   clics. Un +300 % sur 4 clics n'intéresse personne.
3. Pour chacun des 10 plus gros mouvements dans chaque sens, donne la
   cause probable : position, CTR, ou demande.
4. Ne présente jamais un pourcentage sans le volume à côté.
5. Signale à part les pages qui apparaissent ou disparaissent
   complètement — ce sont souvent des problèmes techniques, pas
   éditoriaux.

Rends deux tableaux (top 10 gains, top 10 pertes) : URL ou requête |
clics avant | clics après | variation absolue | variation % | cause
probable. Termine par les 3 mouvements qui expliquent l'essentiel de la
variation globale.

""" + GARDE,

"gsc-saisonnalite": """Contexte : site {domaine}. Mon trafic baisse et je ne sais pas
si je dois m'inquiéter.
Objectif : séparer le cycle normal de l'anomalie réelle.

1. Récupère au moins 16 mois d'historique mensuel : clics, impressions.
2. Compare le mois courant au MÊME MOIS de l'année précédente, pas au
   mois précédent. C'est toute la différence.
3. Calcule l'indice saisonnier de chaque mois sur l'historique
   disponible, et la fourchette normale de variation.
4. Situe l'écart observé : est-il dans la fourchette saisonnière, ou
   en sort-il ?
5. Si l'historique est trop court pour établir un cycle (moins de deux
   passages sur le même mois), dis-le franchement au lieu de conclure.

Rends un verdict clair en trois options : saisonnier attendu, anomalie
réelle, ou historique insuffisant. Appuie-le sur le tableau année contre
année, mois par mois. Si c'est une anomalie, enchaîne sur une
décomposition position / CTR / demande.

""" + GARDE,

"gsc-sections-manquantes": """Contexte : page {page} du site {domaine}.
Objectif : trouver ce que cette page reçoit comme questions sans y répondre.

1. Récupère TOUTES les requêtes servies par cette URL sur 3 mois, y
   compris celles à faibles impressions — c'est souvent là que se
   cachent les trous.
2. Regroupe-les en intentions distinctes (pas en mots-clés : en
   intentions).
3. Lis le contenu réel de la page. Pour chaque intention, tranche :
   la page la traite-t-elle EXPLICITEMENT, ou Google l'a-t-il servie
   par défaut faute de meilleure candidate ?
4. Ne propose que les sections ABSENTES. Ne réécris jamais ce qui
   existe déjà — ce n'est pas la mission.
5. Pour chaque section proposée, cite les requêtes qui la justifient et
   le total d'impressions en jeu.

Rends la liste des sections à ajouter, ordonnée par impressions
couvertes, avec pour chacune : le titre Hn proposé, les requêtes
justificatives, le volume, et deux lignes sur ce que la section doit
dire. Termine par le total d'impressions actuellement mal servies.

""" + GARDE,

"gsc-brief-depuis-requetes": """Contexte : site {domaine}, cluster ou page {page}.
Objectif : un brief bâti sur ce que les gens tapent vraiment, pas sur ce
qu'un outil de volume suggère.

1. Récupère les requêtes du cluster sur 6 mois : impressions, clics,
   position, page servie.
2. Groupe par intention, puis ordonne les groupes par impressions.
   Cet ordre devient le plan Hn — le sujet le plus cherché passe en
   premier, pas celui qui t'arrange.
3. Extrais les formulations interrogatives : elles deviennent des H3 ou
   des entrées de FAQ.
4. Relève le VOCABULAIRE EXACT des requêtes. C'est le langage de mes
   acheteurs : impose-le dans le brief, ne le reformule pas en jargon.
5. Complète avec la SERP (DataForSEO ou Firecrawl) UNIQUEMENT pour ce
   que Search Console ne peut pas dire : ce que couvrent les
   concurrents et que je ne couvre pas.

Rends un brief : angle éditorial, plan Hn ordonné avec le volume qui
justifie chaque section, vocabulaire imposé, questions à traiter, et
longueur cible. Précise pour chaque section si elle vient de mes
données ou de l'analyse SERP.

""" + GARDE,

"gsc-reecriture-title": """Contexte : site {domaine}.
Objectif : réécrire les titles et metas des pages qui sous-performent
en clics à position égale.

1. Pars de la sortie de gsc-ctr-anormal. Si tu ne l'as pas, lance
   d'abord l'analyse : courbe CTR/position du site, puis écart.
2. Pour chaque page ciblée, récupère le title et la meta actuels ainsi
   que sa requête la plus porteuse en impressions.
3. Réécris en intégrant la FORMULATION EXACTE de cette requête, pas une
   variante élégante. Google met en gras ce qui correspond.
4. Respecte les limites d'affichage : environ 60 caractères pour le
   title, 155 pour la meta. Compte-les et affiche le compte.
5. Produis DEUX variantes par page, avec des angles différents — une
   factuelle, une orientée bénéfice — pour permettre un test.
6. Estime le gain si le CTR rejoint la médiane de sa position.

Rends un tableau : URL | title actuel (nb caractères) | variante A |
variante B | meta actuelle | variante A | variante B | gain estimé.
Ajoute une phrase par page expliquant ton angle.

""" + GARDE,

"gsc-faq-depuis-requetes": """Contexte : page {page} du site {domaine}.
Objectif : une FAQ construite sur les vraies questions reçues.

1. Récupère les requêtes de cette page sur 6 mois.
2. Isole celles qui sont des questions : soit elles commencent par un
   interrogatif (comment, pourquoi, combien, quel, quand, est-ce que),
   soit elles en ont la forme implicite (« prix installation X »).
3. Déduplique les reformulations d'une même question — garde la
   formulation la plus recherchée comme intitulé.
4. Écarte celles qui sont DÉJÀ traitées dans le corps de la page : une
   FAQ qui répète le contenu ne sert à rien.
5. Rédige des réponses courtes et AUTONOMES : 2 à 4 phrases,
   compréhensibles hors contexte. C'est ce format que ChatGPT et
   Perplexity citent.
6. Trie par impressions décroissantes et garde les 8 meilleures.

Rends le bloc FAQ rédigé en HTML sémantique, puis le JSON-LD FAQPage
correspondant, prêt à coller. Indique en face de chaque question son
volume d'impressions.

""" + GARDE,

"gsc-page-a-creer": """Contexte : site {domaine}.
Objectif : trouver les sujets qui méritent une page et n'en ont pas.

1. Récupère toutes les requêtes du site sur 6 mois, avec la page qui
   les sert et la position obtenue.
2. Regroupe en clusters sémantiques.
3. Repère les clusters ORPHELINS : les impressions sont dispersées sur
   plusieurs pages approximatives, les positions sont faibles, et
   aucune page n'est vraiment dédiée au sujet.
4. Estime le potentiel de chaque cluster : impressions cumulées,
   position moyenne actuelle, et gain si une vraie page atteignait la
   position 5.
5. Avant de proposer une création, VÉRIFIE qu'il n'existe pas déjà une
   page sur le sujet dans l'inventaire du site. Une page en double fait
   plus de mal que pas de page.

Rends les clusters orphelins triés par potentiel, avec pour chacun : le
mot-clé principal, les requêtes couvertes, les impressions cumulées, les
pages qui les captent mal aujourd'hui, et le titre de la page à créer.
Signale explicitement les clusters où tu as un doute sur un doublon.

""" + GARDE,

"gsc-consolidation": """Contexte : site {domaine}.
Objectif : fusionner mes pages cannibales sans perdre de trafic.

1. Pars des conflits identifiés par gsc-cannibalisation.
2. Pour chaque groupe, désigne la page canonique selon trois critères,
   dans cet ordre : meilleure position moyenne, meilleure profondeur de
   contenu, meilleure intention business.
3. Lis les pages absorbées et liste ce qu'elles apportent d'UNIQUE et
   qui doit être transféré avant redirection — sections, exemples,
   données, visuels. C'est l'étape qu'on saute et qui coûte le trafic.
4. Produis le plan de redirections 301, une ligne par URL source.
5. Liste les liens internes pointant vers les URLs absorbées et qui
   doivent être repointés, pour ne pas laisser de chaînes de
   redirection.
6. Indique les requêtes à surveiller après la fusion et le délai
   raisonnable avant de juger (compte 4 à 6 semaines).

Rends : page cible, contenu à transférer section par section, tableau
de redirections, liens internes à corriger, requêtes à surveiller.

""" + GARDE,

"gsc-maillage": """Contexte : site {domaine}.
Objectif : ajouter les liens internes qui manquent, avec les bonnes ancres.

1. Récupère les requêtes par page sur l'ensemble du site, 6 mois.
2. Calcule la proximité entre pages à partir du RECOUVREMENT de leurs
   requêtes — pas d'une similarité de titre.
3. Propose un lien quand une page A reçoit des requêtes proches du sujet
   d'une page B mieux positionnée sur ces requêtes.
4. Déduis l'ancre de la requête réelle partagée. Jamais « cliquez ici »,
   jamais une ancre générique, jamais l'URL nue.
5. Ne pars QUE de pages qui reçoivent déjà du trafic : un lien depuis
   une page que personne ne visite ne transmet rien.
6. Vérifie que le lien n'existe pas déjà avant de le proposer.

Rends un tableau : page source | trafic de la source | page cible |
ancre proposée | requête qui justifie le lien | où l'insérer dans la
page source. Trie par impact attendu, et limite-toi à 20 liens pour
rester actionnable.

""" + GARDE,

"gsc-rapport-mensuel": """Contexte : site {domaine}, rapport pour le client.
Objectif : un rapport qui DIT quelque chose, pas qui aligne des courbes.

1. Récupère : mois courant, mois précédent, et même mois l'an dernier.
2. Ouvre sur les chiffres clés — clics, impressions, position moyenne —
   avec les DEUX comparaisons. Sans la comparaison annuelle, on
   confond un cycle avec une tendance.
3. Nomme les 3 mouvements qui expliquent l'essentiel de la variation.
   Trois, pas quarante lignes de tableau.
4. Si GA4 est branché, croise avec les conversions par page d'entrée.
   « Le trafic monte sur les pages qui ne convertissent pas » est une
   information ; « le trafic monte » n'en est pas une.
5. Si PostHog est branché, ajoute où les visiteurs organiques décrochent.
6. Termine par les actions du mois suivant, priorisées par impact
   attendu, avec la page concernée pour chacune.

Rends : chiffres clés, les 3 mouvements expliqués, le croisement
conversion, puis les actions. Ton factuel, pas de superlatifs. Si un
chiffre est absent des données, écris-le au lieu de l'estimer.

""" + GARDE,

"gsc-alerte": """Contexte : site {domaine}, surveillance hebdomadaire.
Objectif : ne remonter que ce qui mérite vraiment mon attention.

1. FIXE LES SEUILS AVANT de regarder les données. Sinon on justifie
   après coup ce qu'on a trouvé.
   Seuils proposés, à ajuster : −25 % de clics sur une URL qui pesait
   plus de 100 clics/mois ; −3 positions sur une requête stratégique ;
   −30 % de CTR à position stable ; disparition totale d'une page.
2. Compare les 7 derniers jours aux 4 semaines précédentes, sur des
   jours ÉQUIVALENTS. Un lundi contre un dimanche ne veut rien dire.
3. Écarte les variations explicables par la saisonnalité connue.
4. Ne remonte que ce qui dépasse un seuil. Une alerte qui se déclenche
   toutes les semaines n'est plus lue par personne.
5. Pour chaque alerte, donne la cause probable et l'action immédiate.

Rends soit la liste des alertes classées par gravité, soit — et c'est
une réponse parfaitement valable — la confirmation explicite qu'il n'y
a rien à signaler cette semaine, avec les seuils qui ont été testés.

""" + GARDE,

"gsc-panier-cibles": """Contexte : site {domaine}, panier de requêtes stratégiques.
Objectif : suivre les requêtes sur lesquelles j'ai décidé de me battre.

1. Prends le panier de requêtes défini (si je ne te l'ai pas donné,
   demande-le-moi avant de commencer — ne le devine pas).
2. Pour chaque requête : position, impressions, clics, et la PAGE qui
   se positionne.
3. Montre la trajectoire sur 6 mois, pas l'instantané. Une position 7
   qui vient de 15 et une position 7 qui vient de 3 n'appellent pas la
   même réaction.
4. Signale les franchissements de palier : entrée en page 1 (top 10),
   entrée dans le top 3, sortie de page 1.
5. Alerte si Google CHANGE la page qu'il positionne sur une requête —
   c'est souvent le signe d'une cannibalisation qui démarre.
6. Sépare les requêtes qui progressent, stagnent, et reculent.

Rends le tableau de suivi : requête | position M-5 à M | tendance |
page servie | changement de page | palier franchi. Termine par les 3
requêtes qui demandent une action ce mois-ci, et laquelle.

""" + GARDE,

"gsc-indexation": """Contexte : site {domaine}.
Objectif : savoir ce qui n'est pas indexé, et surtout si c'est grave.

1. Confronte les URLs du sitemap aux URLs réellement indexées.
2. Classe les exclusions par MOTIF : découverte sans indexation,
   explorée non indexée, canonique différente, 404, redirection,
   bloquée par robots.txt, balise noindex.
3. Trie par importance business, pas par volume. Une page de
   pagination non indexée n'est pas un problème ; ta page service
   principale non indexée en est un.
4. Pour chaque motif, donne la correction CONCRÈTE, pas le constat.
   « Explorée non indexée » veut souvent dire contenu trop faible ou
   trop proche d'une autre page : dis laquelle.
5. Signale les pages indexées qui NE sont PAS dans le sitemap —
   c'est l'angle mort habituel.

Rends : le compte par motif, puis les pages qui comptent vraiment,
groupées par motif, avec l'action de correction et sa priorité.
Distingue ce qui est normal de ce qui est cassé.

""" + GARDE,

"gsc-google-vs-llm": """Contexte : site {domaine}, marché France.
Objectif : mesurer l'écart entre ma visibilité Google et ma visibilité
dans les moteurs génératifs.

1. Prends mes requêtes cibles où je suis déjà bien placé sur Google
   (position 1 à 10 selon Search Console).
2. Pose ces mêmes questions à Perplexity, en langage naturel — pas en
   mots-clés. Un utilisateur d'IA écrit des phrases.
3. Pour chaque réponse, relève : mon domaine est-il cité ? à quel rang
   parmi les sources ? et QUI est cité à ma place ?
4. Mets les deux colonnes face à face : position Google contre présence
   LLM. L'écart est la feuille de route GEO — les requêtes où je suis
   1er sur Google et absent des IA sont les plus urgentes.
5. Analyse les sources citées à ma place : sont-elles des concurrents,
   des annuaires, des forums, des médias ? C'est là qu'il faut aller
   se faire mentionner.
6. Journalise le relevé avec sa date pour comparer d'un mois sur l'autre.

Rends le tableau requête | position Google | cité par Perplexity |
rang de citation | sources citées à ma place. Puis les 5 requêtes au
plus gros écart, avec pour chacune l'action concrète pour y entrer.

""" + GARDE,
}
