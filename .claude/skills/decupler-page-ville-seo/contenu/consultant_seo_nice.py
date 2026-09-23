# -*- coding: utf-8 -*-
"""Blocs rediges — consultant seo nice. Registre CONSULTANT (entite Nathan Fenina).

Deux regles qui tiennent toute la page :

1. Voix a la premiere personne. Ce n'est pas la page agence au singulier : c'est
   une autre offre. L'argument n'est pas « une equipe et six agents IA », c'est
   « un seul interlocuteur, qui vous repond lui-meme ».
2. Elle ne doit pas dupliquer agence-seo-nice. Aucun bloc n'y est repris :
   contexte, leviers, methode, preuves, budget et FAQ sont ecrits a part. Le
   controle de duplication du validateur est la pour ca — seuil d'alerte a
   6 phrases communes, on vise 0.

Absorbe « expert seo nice » (210) et « freelance seo nice » (140).
Volume cumule de la grappe : 1 230/mois.
"""

BLOCS = {
    "pill": "Consultant SEO Nice · Nathan Fenina",
    "h1": "Consultant SEO Nice : <em>un seul interlocuteur</em>, "
          "de l'audit à la mise en ligne",
    "lead": [
        "Je m'appelle Nathan Fenina. Je fais du référencement naturel depuis huit "
        "ans, j'ai accompagné plus de 70 entreprises, et je dirige Décupler depuis "
        "Nice — 10 avenue Lympia privée, quartier du port.",
        "On cherche un consultant SEO Nice pour deux raisons opposées : soit on veut "
        "quelqu'un de plus léger qu'une agence, soit on veut quelqu'un de plus "
        "impliqué. Cette page-ci n'est pas celle de l'agence. Certains projets n'ont pas "
        "besoin d'une équipe de six personnes : ils ont besoin de quelqu'un qui "
        "comprend le dossier, décide vite et rend des comptes. Quand c'est le cas, "
        "je prends le projet en direct. Vous m'écrivez, c'est moi qui réponds.",
    ],
    "cta1": "Échanger 30 minutes avec moi",
    "cta2": "Voir l'offre agence",
    "cta2_url": "https://decupler.com/agence-seo-nice/",
    "micro": "Je réponds moi-même. Pas de commercial, pas de qualification en trois "
             "appels.",
    # Visuel du hero : une photo reelle et un badge qui porte le fait
    # differenciant de la ville. Remplace les trois encadres de texte.
    "visuel": (
        "https://decupler.com/wp-content/uploads/2026/09/nathan-fenina-nice.jpg",
        "Nathan Fenina, consultant SEO à Nice, au-dessus de la baie des Anges",
        1000, 1332,
        "Votre interlocuteur", "Nathan Fenina · Nice, port Lympia"),
    "hero_preuve": ("×3,2",
        "le trafic d'un article en 12 semaines, sans nouveau contenu — Le Point",
        "https://decupler.com/etude-de-cas-seo-le-point/"),
    "cards": [
        ("Interlocuteur", "Nathan Fenina, en direct"),
        ("Basé à", "Nice · port Lympia · 06300"),
        ("Depuis", "8 ans · 70+ missions"),
    ],
    "trust": [
        ("8 ans", "de référencement naturel"),
        ("70+", "entreprises accompagnées"),
        ("1", "interlocuteur, du premier appel à la livraison"),
        ("06300", "basé à Nice, pas une adresse de façade"),
    ],

    "h2_pourquoi": "Consultant ou agence : lequel vous faut-il vraiment ?",
    "pourquoi": [
        "La question n'est pas de savoir lequel est meilleur, mais lequel "
        "correspond à votre situation. Un consultant a du sens quand la décision "
        "doit être rapide, quand le périmètre est clair, et quand vous avez déjà "
        "quelqu'un en interne capable d'exécuter. J'arbitre, je priorise, je forme "
        "votre équipe, et je ne facture pas une structure dont vous n'avez pas "
        "l'usage.",
        "Une agence a du sens quand il faut produire du volume en continu : "
        "quarante contenus par mois, du netlinking, de la technique et du suivi, "
        "sans mobiliser personne chez vous. Dans ce cas, c'est l'offre agence "
        "qu'il faut regarder — le bouton en haut de page y mène — et pas "
        "celle-ci.",
        "Le mauvais choix le plus fréquent : prendre un consultant en espérant "
        "qu'il produira comme une agence. Je conseille, j'audite, je forme et je "
        "supervise — mais je ne rédige pas quarante articles par mois tout seul. "
        "Autant le dire avant qu'après.",
    ],
    "cta_pourquoi": "En parler directement avec moi",

    "h2_ranker": "Sur quoi j'interviens concrètement ?",
    "ranker_intro": "Cinq missions, celles pour lesquelles on me contacte le plus "
                    "souvent. Elles se prennent séparément ou à la suite.",
    "ranker": [
        ("L'audit qui tranche",
         "Pas un rapport de 80 pages que personne ne lit. Une liste de dix actions "
         "classées par impact, avec ce que chacune coûte et ce qu'elle rapporte. "
         "C'est le livrable que je préfère : il se lit en vingt minutes et il se "
         "met en œuvre. Point de départ : <a class=\"lnk\" "
         "href=\"https://decupler.com/faire-un-audit-seo/\">ce que contient un "
         "audit SEO</a>."),
        ("L'arbitrage éditorial",
         "Le plus gros gâchis que je vois : des entreprises qui publient beaucoup "
         "sur des sujets sans demande. Je définis la carte des requêtes qui valent "
         "vraiment quelque chose pour vous, et j'écarte le reste — c'est souvent la "
         "moitié du plan initial."),
        ("La remise en état technique",
         "Indexation, vitesse, données structurées, redirections, contenus jumeaux. "
         "Un chantier ingrat, invisible en apparence, et souvent le seul qui "
         "débloque un site qui stagne."),
        ("La formation de votre équipe",
         "Une demi-journée avec votre responsable marketing vaut parfois mieux que "
         "six mois de prestation : elle rend l'équipe autonome sur les briefs, les "
         "balises et le maillage. Je le propose, même si c'est moins rentable pour "
         "moi."),
        ("La visibilité dans les moteurs IA",
         "Être cité par ChatGPT ou Perplexity ne s'achète pas et ne s'improvise "
         "pas : ça demande un contenu qu'un modèle peut découper, un balisage "
         "propre et des mentions ailleurs que chez vous. Je le traite comme une "
         "mission à part — voir <a class=\"lnk\" "
         "href=\"https://decupler.com/consultant-geo/\">consultant GEO</a>."),
        ("La reprise d'un site pénalisé ou décroché",
        "Une chute brutale après une mise à jour, un site piraté, une migration "
        "ratée. Ce sont les missions où un diagnostic rapide vaut le plus cher, "
        "et où l'erreur coûte des mois."),
    ],


    "bandeau": ("Pourquoi je limite le nombre de missions",
        ["« Un seul interlocuteur » ne veut rien dire si j'en prends quinze en "
         "parallèle. Je plafonne volontairement le nombre de projets que je "
         "suis en direct, ce qui veut dire que je refuse des dossiers — et que "
         "quand j'en accepte un, vous avez vraiment quelqu'un au bout du fil.",
         "Je travaille depuis Nice, au port Lympia. Pour les entreprises "
         "azuréennes on se voit ; ailleurs c'est la visio, et ça n'a jamais "
         "gêné une mission."],
        ("https://decupler.com/wp-content/uploads/2026/09/nathan-fenina-nice.jpg", "Nathan Fenina, consultant SEO à Nice, au-dessus de la baie "
         "des Anges", 1000, 1332, "Nathan Fenina — Nice, port Lympia.")),

    "h2_voisines": "Vous êtes ailleurs sur la Côte d'Azur ?",
    "voisines_intro": "Je prends des missions dans tout le 06 et le 83. Voici "
                      "les pages qui décrivent chaque marché — et l'offre "
                      "agence, si c'est du volume qu'il vous faut.",
    "voisines": [
        ("Agence SEO Nice", "L'offre complète : l'équipe, les six agents IA, la "
         "production en continu.",
         "https://decupler.com/agence-seo-nice/"),
        ("Agence SEO Cannes", "Le marché cannois, calé sur le calendrier du "
         "Palais des Festivals.",
         "https://decupler.com/agence-seo-cannes/"),
        ("Agence SEO Toulon", "Le B2B industriel varois : arsenal, logistique, "
         "BTP.",
         "https://decupler.com/agence-seo-toulon/"),
        ("Consultant GEO", "Se faire citer par ChatGPT et Perplexity : je le "
         "traite comme une mission distincte.",
         "https://decupler.com/consultant-geo/"),
    ],

    "h2_methode": "Comment se passe une mission avec moi ?",
    "methode_intro": "Quatre temps. Le premier est gratuit, et vous repartez avec "
                     "quelque chose d'utile même si la suite ne se fait pas.",
    "methode": [
        ("Un appel de trente minutes.", "Vous me montrez votre Search Console, je "
         "vous dis ce que j'y vois. Si je pense que le SEO n'est pas votre priorité "
         "du moment, je vous le dis à ce moment-là — ça m'est arrivé, et c'est plus "
         "honnête que de vendre un an de contenu."),
        ("L'audit.", "Dix jours. Je remets une liste d'actions priorisées, chiffrées "
         "en effort et en gain attendu. Vous en faites ce que vous voulez, y compris "
         "l'exécuter sans moi."),
        ("La mise en œuvre, à votre main ou à la mienne.", "Soit je pilote et votre "
         "équipe exécute, soit je prends l'exécution — et dans ce second cas je "
         "m'appuie sur l'équipe de Décupler, en vous le disant."),
        ("Un point mensuel, court.", "Une heure sur données Search Console. Ce qui a "
         "bougé, ce qui n'a pas bougé, ce qu'on change. Pas de tableau de bord "
         "décoratif."),
    ],
    "mock_k": "Ce qu'on me demande le plus au premier appel",
    "mock_q": "Pourquoi mon site ne décolle pas alors que je publie chaque semaine ?",
    "mock_ans": [
        (True, "Les sujets publiés n'ont pas de demande réelle"),
        (True, "Le site est mal exploré : le contenu n'est pas vu"),
        (False, "Il faut publier davantage"),
        (False, "Il faut refaire le site"),
    ],
    "mock_ft": "Les deux premières causes expliquent la majorité des cas que je vois. "
               "Les deux suivantes sont les réflexes les plus coûteux, et les plus "
               "souvent inutiles.",

    "h2_preuve": "Quels résultats est-ce que je peux montrer ?",
    "preuve_intro": "Des missions signées, chiffrées et publiées. Chaque lien mène à "
                    "l'étude de cas complète, avec la période, la méthode et la "
                    "source de mesure.",
    "preuves": [
        ("Le Point — optimiser sans rien réécrire",
         "Trafic d'un article multiplié par 3,2 (+218 %) en 12 semaines, de 2 000 à "
         "6 360 visites mensuelles, sans créer un seul nouveau contenu. La mission "
         "qui illustre le mieux ce qu'un arbitrage bien fait produit.",
         "https://decupler.com/etude-de-cas-seo-le-point/", "Lire le cas complet"),
        ("Spigao — un SaaS B2B en six mois",
         "+250 % de trafic organique (5 200 → 16 250 sessions), +180 % de leads "
         "organiques, coût d'acquisition payant réduit de 45 %.",
         "https://decupler.com/etude-de-cas-seo-spigao/", "Lire le cas complet"),
        ("Reux Travaux — une page, +450 %",
         "Une seule page de service reprise : 8 → 44 clics en trois mois. Le "
         "contre-exemple parfait de la stratégie « publions plus ».",
         "https://decupler.com/etude-de-cas-seo-reux-travaux/", "Lire le cas complet"),
        ("Allianz — quand le payant est le bon levier",
         "ROI multiplié par 3 (1,8× → 5,4×) et coût par lead réduit de 42 % à budget "
         "constant. Parfois la réponse n'est pas le SEO, et il faut savoir le dire.",
         "https://decupler.com/etude-de-cas-sea-allianz/", "Lire le cas complet"),
    ],
    "preuve_note": "Mesures Google Search Console et Semrush. Ces résultats sont ceux "
                   "de ces missions, dans leur contexte — je ne les présente pas comme "
                   "une promesse pour la vôtre. Le point de départ change tout, et "
                   "nous le regarderons ensemble au premier appel.",

    "h2_zone": "D'où je travaille, et jusqu'où je me déplace",
    "zone_intro": "Je suis basé à Nice, au port. Je me déplace sur Nice et la bande "
                  "littorale des Alpes-Maritimes ; au-delà, je travaille en visio — "
                  "ce qui n'a jamais gêné une mission.",
    "zone_note": "Pour les entreprises hors du 06, la visio est la règle et elle "
                 "fonctionne : la moitié de mes missions se sont faites sans que je "
                 "mette les pieds chez le client.",

    "h2_budget": "Combien coûte un consultant SEO à Nice ?",
    "budget_intro": "Affichés, parce qu'un consultant qui refuse de donner un ordre "
                    "de grandeur avant l'appel vous fait perdre votre temps. Ce qui "
                    "les fait varier : la taille du site, la difficulté des requêtes, "
                    "et l'état de la technique.",
    "budget": [
        ("À partir de 500 € / mois",
         "Accompagnement d'une entreprise locale niçoise : arbitrage mensuel, fiche "
         "d'établissement, avis, priorisation des pages."),
        ("1 000 à 2 000 € / mois",
         "Accompagnement d'un site B2B, SaaS ou e-commerce : stratégie, briefs, "
         "supervision de la production, technique, suivi des citations IA."),
        ("Sur devis",
         "Audit ponctuel, formation d'équipe, mission multilingue, ou expertise sur "
         "un chantier précis (migration, refonte, pénalité). Chiffré après l'appel."),
    ],
    "budget_note": "Un audit seul est possible, sans suite obligatoire. C'est souvent "
                   "la meilleure façon de commencer : vous voyez comment je "
                   "travaille, et vous gardez le livrable quoi qu'il arrive.",

    "h2_variantes": "Consultant SEO Nice, expert, freelance : c'est le même métier ?",
    "variantes": [
        "Oui, à quelques nuances de vocabulaire près. « Consultant SEO Nice », "
        "« expert SEO Nice » et « freelance SEO Nice » désignent la même chose : "
        "une personne, pas une structure, qui prend en charge votre référencement "
        "naturel. Les trois mots traduisent surtout une nuance de posture — le "
        "consultant conseille et arbitre, l'expert est convoqué sur un problème "
        "précis, le freelance exécute en indépendant. En pratique je fais les trois, "
        "selon ce dont le projet a besoin.",
        "Une différence est réelle, en revanche : je ne suis pas freelance au sens "
        "strict. Je dirige Décupler, une agence avec une équipe. Quand vous me "
        "prenez en direct, vous avez un consultant ; si la mission demande de la "
        "production en volume, je peux m'appuyer sur l'équipe — et je vous le dis "
        "plutôt que de faire semblant de tout écrire moi-même à trois heures du "
        "matin.",
        "Dernier point de vocabulaire : « consultant en référencement naturel » et "
        "« consultant SEO » sont strictement équivalents, l'un étant la version "
        "française de l'autre. Si vous cherchez plutôt une équipe complète, l'offre "
        "agence est décrite en haut de cette page ; et si votre enjeu est d'abord "
        "local — fiche d'établissement, avis, citations — commencez par le guide "
        "<a class=\"lnk\" href=\"https://decupler.com/seo-local/\">SEO "
        "local</a>.",
    ],

    "h2_faq": "Ce qu'on me demande avant de travailler ensemble : vos questions",
    "faq": [
        ("C'est vous qui suivez mon projet, ou quelqu'un d'autre ?",
         "Moi. Prendre un consultant SEO Nice et se retrouver avec un junior qu'on "
         "n'a pas choisi est le reproche le plus courant fait à la profession : ici "
         "ça n'arrive pas. C'est le sens de cette page : vous avez un interlocuteur, du premier "
         "appel jusqu'aux points mensuels. Si la mission demande de la production en "
         "volume, une partie de l'exécution passe par l'équipe de Décupler — mais "
         "l'arbitrage, la stratégie et la relation restent de mon côté, et je vous "
         "dis toujours qui fait quoi."),
        ("Quel est l'engagement minimum ?",
         "Pour un accompagnement, <b>six mois</b> : c'est le délai réel avant que le "
         "travail se voie dans les positions. Pour un audit seul ou une formation, "
         "aucun engagement — c'est une mission ponctuelle, livrée et terminée."),
        ("Vous travaillez avec quels types d'entreprises ?",
         "Surtout des PME et ETI de 5 à 100 personnes, en tech, SaaS, e-commerce et "
         "services B2B, plus des entreprises locales niçoises. Je décline les projets "
         "où je ne suis pas utile : sites illégaux ou trompeurs, secteurs où je n'ai "
         "aucune compétence, et budgets où mon intervention coûterait plus qu'elle ne "
         "rapporterait. Pour les entreprises de la construction et de l'artisanat, "
         "voir aussi <a href=\"https://decupler.com/seo-btp/\">SEO BTP</a>."),
        ("Est-ce que vous utilisez l'IA pour produire ?",
         "Oui, et sans faire mystère : Décupler s'appuie sur six agents IA "
         "spécialisés pour l'analyse, les briefs, la rédaction et la publication. Ce "
         "qui ne change pas, c'est qu'un humain relit, corrige et valide avant mise "
         "en ligne — et sur les missions que je prends en direct, cet humain c'est "
         "moi. Un contenu qui sonne générique ne part pas."),
        ("Que se passe-t-il si les résultats ne viennent pas ?",
         "Au bout de trois mois, si rien ne bouge, on reprend la stratégie ensemble "
         "sans frais supplémentaires. Et si j'estime que le problème n'est pas le SEO "
         "— site qui convertit mal, offre pas assez claire, marché qui passe par la "
         "recommandation — je vous le dirai, même si ça met fin à la mission."),
    ],

    "photo_alt": "Nathan Fenina, consultant SEO Nice et fondateur de Décupler",
    "eeat": "Huit ans de référencement naturel, plus de 70 entreprises "
            "accompagnées en SaaS, e-commerce et services B2B. Basé à Nice, au "
            "port Lympia. Je prends un nombre limité de missions en direct — c'est "
            "la condition pour que « un seul interlocuteur » veuille dire quelque "
            "chose.",

    "final_lien": ("https://decupler.com/cas-clients/", "Voir mes missions"),
    "h2_final": "Trente minutes, et vous saurez si j'ai quelque chose à vous apporter",
    "final": "On regarde votre Search Console ensemble, je vous dis ce que je ferais "
             "à votre place et dans quel ordre. Si la réponse est « rien pour "
             "l'instant », vous l'entendrez aussi.",
}

# ── Ajouts du 22/09 (soir) ────────────────────────────────────────────────
# Registre CONSULTANT : voix « je », entite Nathan Fenina. Le point de vue
# n'est pas celui d'une structure qui livre, mais d'une personne dont le
# temps est la ressource rare. Les livrables sont donc formules comme des
# engagements personnels, et la colonne « ce que je ne fais pas » porte sur
# la disponibilite — c'est la vraie difference avec la page agence.
BLOCS.update({
    "photo_ville": {
        "src": "https://decupler.com/wp-content/uploads/2026/09/bandeau-nice.jpg",
        "alt": "Nice vue d'en haut : la baie des Anges et le Vieux-Nice, où "
               "travaille Nathan Fenina",
        "w": 2000, "h": 858,
        "k": "Là où je travaille",
        "h2": "Je vis ici, et ça change deux choses à votre dossier",
        "p": "La première : je peux passer vous voir. Un commerce du "
             "Vieux-Nice, un cabinet à Cimiez, une PME dans la plaine du Var — "
             "j'y vais, et je comprends en une heure ce que trois visios ne "
             "montrent pas. La seconde : je connais vos concurrents, parce que "
             "je passe devant leurs vitrines.",
        "chips": ["Basé au port de Nice", "Rendez-vous sur place",
                  "06000 · 06100 · 06200 · 06300", "8 ans de SEO"],
        "credit": "Nice, la baie des Anges et le Vieux-Nice — photo Décupler",
    },
    "ruban": [
        ("1 interlocuteur", "vous n'êtes jamais transféré à un junior"),
        ("6 clients", "le maximum que je suis capable de suivre sérieusement"),
        ("48 h", "mon délai de réponse maximum sur un dossier en cours"),
        ("1 mois", "de préavis, sans pénalité, à tout moment"),
    ],

    "h2_livrables": "Sur quoi est-ce que je m'engage, chaque mois ?",
    "livrables_intro": "Un consultant indépendant vend du temps et du "
                       "jugement. Voici où passe ce temps, pour que vous "
                       "puissiez vérifier que je tiens ma part.",
    "livrables": [
        ("01", "Je relève vos positions depuis Nice",
         "Vos requêtes, géolocalisées ici, chaque semaine. Et je vous dis ce "
         "qui a bougé dans le classement de vos trois concurrents directs — pas "
         "seulement le vôtre.",
         "Chaque semaine"),
        ("02", "J'interroge les IA sur votre métier",
         "Les questions que vos clients posent à ChatGPT, Perplexity, Gemini et "
         "Claude, avec la liste de qui est cité. Quand vous n'y êtes pas, je "
         "vous dis pourquoi et ce qui manque.",
         "Chaque mois"),
        ("03", "J'écris et je publie",
         "Deux à quatre contenus par mois, de ma main, mis en ligne dans votre "
         "site. Je ne sous-traite pas la rédaction : c'est là que se joue la "
         "différence, donc c'est moi qui le fais.",
         "2 à 4 par mois"),
        ("04", "Je corrige la technique",
         "Vitesse, balises, données structurées, erreurs d'exploration. "
         "J'interviens directement dans le site quand j'y ai accès, ou je "
         "transmets un correctif prêt à appliquer à votre développeur.",
         "En continu"),
        ("05", "Je tiens votre fiche Google",
         "Photos, horaires, catégories, questions-réponses, avis. Sur une "
         "recherche faite dans la rue, à Nice, c'est cette fiche qui décide et "
         "elle se néglige vite.",
         "Chaque mois"),
        ("06", "Je vous appelle 45 minutes",
         "Tous les mois, en visio ou autour d'un café. Je vous dis aussi ce qui "
         "n'a pas marché : c'est la moitié utile de la conversation.",
         "Chaque mois"),
    ],
    "livrables_note": "Entre deux points mensuels, vous m'écrivez directement. "
                      "Je réponds sous 48 heures ouvrées, et je le tiens parce "
                      "que je limite volontairement le nombre de dossiers.",

    "h2_duo": "Qu'est-ce que je fais, et qu'est-ce que je refuse ?",
    "duo_intro": "La colonne de droite est la plus utile des deux : elle vous "
                 "évite de me confier un travail pour lequel je ne suis pas le "
                 "bon choix.",
    "duo": (
        "Ce dont je m'occupe",
        [
            "<b>La stratégie et l'exécution.</b> Je ne rends pas un audit de "
            "quarante pages à faire appliquer par quelqu'un d'autre : "
            "j'applique.",
            "<b>Le contenu, de ma main.</b> Recherche, plan, rédaction, "
            "publication. L'IA m'aide à défricher, elle n'écrit pas la version "
            "publiée.",
            "<b>Votre visibilité dans les IA autant que dans Google.</b> C'est "
            "le même travail de fond, et c'est là que l'écart se creuse en ce "
            "moment.",
            "<b>Vous former si vous voulez reprendre la main.</b> Certains "
            "clients veulent être autonomes au bout d'un an. C'est une réussite, "
            "pas une perte.",
            "<b>Vous dire non.</b> Quand votre problème n'est pas le SEO — un "
            "site illisible, une offre floue, un prix hors marché — je le dis "
            "avant de prendre un centime.",
        ],
        "Ce que je ne fais pas",
        [
            "<b>Plus de six dossiers à la fois.</b> Au-delà je fais du mauvais "
            "travail sur tous. Si je suis complet, je le dis et je vous donne "
            "une date.",
            "<b>Du référencement payant.</b> Google Ads est un autre métier ; "
            "je vous oriente vers quelqu'un plutôt que d'improviser.",
            "<b>Des liens achetés.</b> Jamais, sur aucun dossier. C'est votre "
            "site qui encaisserait la sanction, pas moi.",
            "<b>Des promesses de position.</b> Je m'engage sur le travail livré "
            "et sur les demandes entrantes mesurées, pas sur un rang que "
            "personne ne contrôle.",
            "<b>Deux clients concurrents à Nice.</b> Un seul par métier : je ne "
            "peux pas faire gagner deux entreprises sur la même requête.",
        ],
    ),

    "parti_pill": "Mon parti pris",
    "h2_parti": "Pourquoi plafonner à six clients quand on pourrait en "
                "prendre vingt ?",
    "parti_pris": [
        "C'est la question qu'on me pose le plus souvent, et la réponse est "
        "moins noble qu'elle en a l'air : <strong>je sais ce que je vaux quand "
        "je suis débordé</strong>. Au-delà de six dossiers suivis "
        "personnellement, je commence à rendre du travail correct au lieu de "
        "travail utile, et le client ne s'en aperçoit qu'au bout de quatre mois.",
        "La sortie classique de ce problème, c'est de recruter et de devenir "
        "une agence : un junior produit, je relis, je facture le double. Ça "
        "fonctionne, beaucoup le font bien. Mais ce n'est plus la prestation "
        "que j'ai envie de vendre, parce que ce qui fait la différence sur un "
        "dossier, c'est justement <strong>l'heure où l'on comprend le "
        "métier du client</strong> — et cette heure ne se délègue pas.",
        "Concrètement, ça veut dire que je suis parfois complet et que je vous "
        "donne une date au lieu d'un devis. Ça veut dire aussi que quand je "
        "prends votre dossier, vous avez la même personne du premier appel à la "
        "dernière publication, qui se souvient de ce qu'on a essayé en mars et "
        "pourquoi ça n'a pas marché. À Nice, où la recommandation fait plus de "
        "chiffre d'affaires que Google, c'est le seul modèle qui tient.",
    ],
    "parti_role": "Consultant SEO indépendant · Nice, quartier du port",
})

# Registre consultant : la biographie est a la premiere personne, et ce
# qu'elle promet est un acces direct — c'est le seul argument qu'une agence
# ne peut pas copier.
BLOCS["eeat_plus"] = [
    "Je travaille depuis le quartier du port de Nice et je me déplace dans "
    "toute la commune — Vieux-Nice, Libération, Cimiez, l'Ouest, la plaine "
    "du Var. Vous aurez mon numéro direct, pas celui d'un standard.",
    "J'écris publiquement sur le référencement dans les moteurs génératifs, "
    "ici et sur LinkedIn. Lisez-moi avant de m'appeler : c'est la façon la "
    "plus rapide de savoir si ma manière de travailler vous convient.",
]

# ── Visuels réels (23/09) ───────────────────────────────────────────────
# La même photo apparaissait trois fois sur cette page (hero, bandeau,
# bande auteur). Page consultant : Nathan en hero, sa ville dans le
# bandeau, la photo studio dans la bande auteur (choisie par l'assembleur).
BLOCS["visuel_photo"] = "nathan-nice"
BLOCS["visuel_badge"] = BLOCS["visuel"][4:6]
BLOCS["visuel_alt"] = "Nathan Fenina, consultant SEO à Nice"
BLOCS["bandeau_photo"] = "hero-nice"
BLOCS["bandeau_cap"] = "Le cours Saleya, dans le Vieux-Nice"
