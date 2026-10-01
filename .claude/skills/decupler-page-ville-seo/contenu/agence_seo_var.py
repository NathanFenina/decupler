# -*- coding: utf-8 -*-
"""Blocs rediges — agence seo var. Registre AGENCE. Page DEPARTEMENTALE.

Meme role que la page 06 : elle agrege et renvoie vers les pages du Var
(Toulon, Frejus, consultant Toulon) sans les cannibaliser. Son angle propre :
LE VAR N'EST PAS UN MARCHE, C'EN EST SEPT. La rade de Toulon et son tissu
industriel et de defense ; Hyeres et les iles d'Or ; l'est varois et
l'Esterel ; le golfe de Saint-Tropez ; la Dracenie ; la Provence verte et
les vignobles ; le haut Var et le Verdon. Chaque bassin qui a sa page y
renvoie, dans le texte.

Parti pris : le Var n'est la banlieue ni de Marseille, ni de Nice. L'ouest
regarde vers Marseille, l'est vers Cannes, et le centre ne regarde que
lui-meme. Une page par marche, jamais une page par commune (plus de 150).

Decupler n'a pas d'adresse dans le Var : on intervient depuis Nice, a
distance, et on ne le cache pas.

Absorbe « agence referencement var » (90). Grappe : 180/mois.
"""

BLOCS = {
    "pill": "Agence SEO Var · 83",
    "h1": "Agence SEO Var : un seul département, <em>sept façons "
          "d'y chercher un prestataire</em>",
    "lead": [
        "Un sous-traitant de la rade de Toulon, un loueur de bateaux à "
        "Hyères, un domaine des Côtes de Provence et un gîte au bord du "
        "Verdon partagent un code postal en 83. Pour le reste, presque rien : "
        "ni les clients, ni les saisons, ni les mots tapés dans Google.",
        "Une agence SEO Var utile commence donc par une carte. Nous "
        "découpons le département en bassins, puis nous travaillons chacun "
        "avec ses propres requêtes, sur Google comme dans les réponses de "
        "ChatGPT, Claude, Gemini et Perplexity. Nous le faisons depuis Nice, "
        "sans adresse varoise, et nous l'écrivons dès la première ligne.",
    ],
    "cta1": "Réserver un audit offert",
    "cta2": "Découvrir notre offre SEO",
    "cta2_url": "https://decupler.com/machine-de-guerre-seo/",
    "micro": "30 minutes avec Nathan, en visio. Sans engagement.",
    "visuel_photo": "hero-var",
    "visuel_alt": "La plage Notre-Dame à Porquerolles — agence SEO Var "
                  "Décupler, depuis Nice",
    "visuel_badge": ("Le 83", "Rade · îles · vignes · Verdon"),
    "hero_preuve": ("+140 %",
        "de trafic organique en 6 mois sur une demande saisonnière — "
        "Decathlon Travel",
        "https://decupler.com/etude-de-cas-seo-decathlon/"),
    "cards": [
        ("Zone", "Var · de Saint-Cyr à l'Estérel, jusqu'au Verdon"),
        ("Depuis", "Nice · aucune adresse dans le Var"),
        ("Méthode", "Un bassin, des requêtes à lui"),
    ],
    "trust": [
        ("7", "bassins varois, sept demandes distinctes"),
        ("8", "ans de référencement naturel"),
        ("70+", "entreprises accompagnées"),
        ("500 €", "par mois pour démarrer en local"),
    ],

    "h2_pourquoi": "Pourquoi une agence SEO Var doit-elle raisonner par bassin ?",
    "pourquoi": [
        "Parce que le Var est plus grand qu'il n'en a l'air sur une carte "
        "de la côte. Il s'étend de Saint-Cyr-sur-Mer jusqu'à l'Estérel, et "
        "de la presqu'île de Giens jusqu'aux gorges du Verdon. Entre ces points, "
        "l'économie change plusieurs fois.",
        "Autour de Toulon, on vend à des donneurs d'ordre, sur des cycles "
        "longs. Sur les îles et dans le golfe, on vend à des visiteurs qui "
        "réservent quelques semaines avant l'été. Dans la Provence verte, "
        "un domaine vend du vin, des visites et parfois des chambres. Dans "
        "le haut Var, la saison se joue souvent sur un week-end de beau "
        "temps.",
        "Les requêtes suivent ces réalités, pas la carte administrative. "
        "Rares sont ceux qui cherchent un chantier naval « dans le Var ». On "
        "cherche « La Seyne », « Hyères » ou « près du lac de Sainte-Croix ». La "
        "première question d'un dossier est donc toujours la même : où sont "
        "vos clients, et comment nomment-ils l'endroit où ils vous "
        "cherchent ?",
    ],
    "cta_pourquoi": "Identifier mon bassin varois",

    "h2_ranker": "Quels sont les sept bassins économiques du Var ?",
    "ranker_intro": "Sept marchés, avec leurs requêtes et leurs erreurs "
                    "typiques. Quand un bassin a sa propre page, le lien est "
                    "dans le texte.",
    "ranker": [
        ("La rade de Toulon",
         "Toulon, La Seyne-sur-Mer, Six-Fours-les-Plages : la base navale, "
         "la sous-traitance de défense, la réparation et la plaisance. Des "
         "acheteurs précis, peu nombreux, qui comparent longtemps — voir "
         "<a class=\"lnk\" href=\"https://decupler.com/agence-seo-toulon/\">"
         "agence SEO Toulon</a>, ou <a class=\"lnk\" "
         "href=\"https://decupler.com/consultant-seo-toulon/\">consultant "
         "SEO Toulon</a> si vous préférez un seul interlocuteur."),
        ("Hyères et les îles d'Or",
         "Porquerolles, Port-Cros, la presqu'île de Giens : des traversées, "
         "des locations, de la restauration, sur une saison serrée. Tout se "
         "cherche sur mobile, souvent la veille du départ. Ce bassin se "
         "traite ici, avec la commune d'Hyères."),
        ("L'est varois et l'Estérel",
         "Fréjus, Saint-Raphaël et les roches rouges du massif : "
         "hébergement, campings, commerce, services aux résidents à "
         "l'année. Un marché qui déborde vers Cannes — voir "
         "<a class=\"lnk\" href=\"https://decupler.com/agence-seo-frejus/\">"
         "agence SEO Fréjus</a>."),
        ("Le golfe de Saint-Tropez",
         "Saint-Tropez, Sainte-Maxime, Grimaud, Cogolin : une clientèle "
         "internationale, des recherches en anglais et une saison courte. "
         "Pas de page dédiée pour l'instant : chaque dossier part de la "
         "commune où il se joue."),
        ("La Dracénie",
         "Draguignan et ses villages : commerces, artisans, professions "
         "libérales, et une ville de garnison avec ses écoles militaires. "
         "Une demande de proximité, stable toute l'année."),
        ("La Provence verte et les vignobles",
         "Brignoles, Saint-Maximin-la-Sainte-Baume, les domaines des Côtes "
         "de Provence : vente au caveau, œnotourisme, export. Le rosé se "
         "vend autant par sa réputation que par sa fiche en ligne."),
        ("Le haut Var et le Verdon",
         "Les gorges, le lac de Sainte-Croix, Aups et son marché aux "
         "truffes : gîtes, canoë, randonnée. Des recherches de dernière "
         "minute, souvent depuis un téléphone, une fois sur place."),
    ],

    "h2_methode": "Comment abordons-nous un dossier varois ?",
    "methode_intro": "Quatre temps. Le premier consiste à placer votre "
                     "entreprise sur la carte, avant tout mot-clé.",
    "methode": [
        ("Placer l'entreprise dans son bassin.",
         "Rade, îles, golfe, vignes ou Verdon : nous regardons d'où "
         "viennent vos demandes et à quelle période."),
        ("Écouter la demande réelle.",
         "Les formulations tapées commune par commune, en français et en "
         "anglais, et ce que les moteurs IA disent aujourd'hui de votre "
         "métier dans le Var."),
        ("Écrire uniquement les pages utiles.",
         "Une page quand un besoin distinct existe, aucune pour habiller une "
         "commune. Chaque texte est relu et validé par Nathan avant la mise "
         "en ligne."),
        ("Compter les demandes, pas les visites.",
         "Appels, réservations, formulaires, itinéraires : chaque mois, ce "
         "que le référencement a apporté, bassin par bassin."),
    ],
    "mock_k": "Question posée à ChatGPT par un visiteur",
    "mock_q": "Quels domaines des Côtes de Provence proposent une "
              "dégustation le dimanche près de Lorgues ?",
    "mock_ans": [
        (True, "Les domaines dont le site indique la commune, les jours "
               "d'ouverture et les langues parlées"),
        (True, "Ceux que citent aussi des sources extérieures, avec les "
               "mêmes informations"),
        (False, "Ceux qui écrivent seulement « en Provence » sans dire où "
                "se trouve le caveau"),
    ],
    "mock_ft": "Illustration du mécanisme, pas une capture : le moteur "
               "cherche une commune et des horaires, pas un slogan.",

    "h2_preuve": "Quels résultats pouvons-nous montrer ?",
    "preuve_intro": "Aucune de ces missions ne se passe dans le Var, et nous "
                    "ne le prétendons pas. Nous les avons choisies pour leur "
                    "ressemblance avec les marchés varois : la saison, le "
                    "site technique, l'artisan.",
    "preuves": [
        ("Decathlon Travel — préparer la saison",
         "Le trafic organique est passé de 12 500 à 30 000 visites par mois "
         "en six mois, soit +140 %, avec +180 % de conversions. C'est la "
         "logique des îles et du golfe : être prêt avant la vague.",
         "https://decupler.com/etude-de-cas-seo-decathlon/", "Lire le cas"),
        ("Atoo Énergie — réparer avant d'écrire",
         "Plus de 80 erreurs techniques corrigées, un chargement ramené de "
         "4,8 à 2,6 secondes, et +15 % de clics en trois mois. Le point de "
         "départ fréquent pour un site industriel.",
         "https://decupler.com/etude-de-cas-seo-atoo-energie/", "Lire le cas"),
        ("Reux Travaux — une page qui travaille",
         "La page de service stratégique est passée de 8 à 44 clics en trois "
         "mois, soit +450 %. Un profil proche de celui d'un artisan de la "
         "Dracénie ou de la Provence verte.",
         "https://decupler.com/etude-de-cas-seo-reux-travaux/", "Lire le cas"),
        ("L'ensemble de nos études",
         "Huit missions publiées, avec la source de chaque mesure.",
         "https://decupler.com/cas-clients/", "Consulter les études"),
    ],
    "preuve_note": "Mesures issues de Google Search Console et de Semrush. "
                   "Elles décrivent ces missions-là ; un dossier varois "
                   "partira de son propre point de départ.",

    "photo_ville": {
        "cle": "bandeau-var",
        "alt": "Le Var, les vignes des Côtes de Provence",
        "h2": "Derrière la côte, un département de vignes et de collines",
        "p": "On résume souvent le Var à ses plages. Autour de Cuers et "
             "de Pierrefeu-du-Var, ce sont pourtant des rangs de vigne à perte de vue, "
             "des caves coopératives et des domaines qui reçoivent des "
             "visiteurs. Ces entreprises-là aussi se cherchent en ligne, avec "
             "leur propre vocabulaire.",
        "chips": ["Rade", "Îles", "Vignobles", "Verdon"],
    },

    "h2_zone": "D'où intervenons-nous dans le Var ?",
    "zone_intro": "Décupler n'a pas d'adresse dans le Var. Notre agence SEO "
                  "Var travaille depuis Nice, au 10 avenue Lympia privée, à "
                  "une heure de route de l'Estérel, davantage pour la rade ou "
                  "le Verdon. Nous "
                  "travaillons à distance ; si le dossier le justifie, nous "
                  "pouvons venir pour le lancement, et nous l'organisons "
                  "ensemble.",
    "zone_note": "Au-delà du Var, les Alpes-Maritimes et la Principauté de "
                 "Monaco ont chacune leur page.",

    "ruban": [
        ("7 bassins", "de la rade de Toulon aux gorges du Verdon"),
        ("150+", "communes, et bien moins de pages à écrire"),
        ("FR · EN", "les deux langues du golfe et des îles"),
        ("0", "adresse dans le Var : nous venons de Nice"),
    ],

    "h2_budget": "Quel budget prévoir pour le SEO dans le Var ?",
    "budget_intro": "Les tarifs ne changent pas d'un bassin à l'autre. Ce "
                    "qui les fait varier, c'est le nombre de marchés "
                    "visés et de langues à couvrir.",
    "budget": [
        ("À partir de 500 € / mois",
         "Un artisan, un commerce ou un gîte dans un seul bassin : fiche "
         "d'établissement, pages clés, suivi chaque mois."),
        ("1 000 à 2 000 € / mois",
         "Une PME B2B de la rade, un domaine qui vend en ligne, un "
         "e-commerce ou une activité présente dans plusieurs bassins."),
        ("Sur devis",
         "Plusieurs sites, une clientèle étrangère, ou un audit avant "
         "refonte. Notre <a class=\"lnk\" "
         "href=\"https://decupler.com/faire-un-audit-seo/\">méthode d'audit "
         "SEO</a> décrit ce que couvre ce travail."),
    ],
    "budget_note": "Si votre activité vit d'une clientèle fidèle qui vous "
                   "connaît déjà, un abonnement n'est peut-être pas utile. "
                   "Une fiche d'établissement bien tenue peut suffire, et "
                   "nous vous le dirons dès le premier appel.",

    "h2_livrables": "Que recevez-vous chaque mois sur un dossier varois ?",
    "livrables_intro": "Six livrables, réglés sur votre bassin et sur son "
                       "calendrier.",
    "livrables": [
        ("01", "Le compte des demandes",
         "Appels, réservations, formulaires : ce que la recherche a "
         "réellement produit, et depuis quelles communes.",
         "Chaque mois"),
        ("02", "Les positions relevées sur place",
         "Vos requêtes mesurées depuis les communes de votre bassin : "
         "Hyères n'affiche pas les mêmes résultats que Draguignan.",
         "Chaque semaine"),
        ("03", "La présence dans les réponses IA",
         "Ce que ChatGPT, Claude, Gemini et Perplexity recommandent sur "
         "votre métier, et si votre nom y figure.",
         "Chaque semaine"),
        ("04", "Les pages écrites ou reprises",
         "Chacune répond à un besoin identifié, et Nathan la relit avant "
         "publication.",
         "2 à 6 par mois"),
        ("05", "Le calendrier du bassin",
         "Ouverture de la saison, vendanges, régates, rentrée : ce qui doit "
         "être en ligne avant chaque échéance.",
         "Revu chaque mois"),
        ("06", "Le point mensuel avec Nathan",
         "Trente minutes en visio sur ce qui a progressé, ce qui a stagné "
         "et la suite.",
         "Chaque mois"),
    ],
    "livrables_note": "Entre deux points, vous écrivez à l'équipe "
                      "directement, sans passer par un formulaire de support.",

    "bandeau": ("Une page par marché, jamais une page par commune",
        ["Le Var compte plus de 150 communes. Publier une page par commune, "
         "avec le même texte et seulement le nom qui change, produit ce que "
         "Google appelle des pages satellites. Il les détecte, et c'est tout "
         "le site qui en pâtit.",
         "Nous ouvrons une page seulement quand le marché change vraiment. "
         "Toulon et Fréjus en ont une ; le golfe, les îles et le Verdon sont "
         "traités à partir de la commune où se trouve votre activité. Moins "
         "de pages, et chacune a quelque chose à dire."],
        (None, None, None, None, None)),
    "bandeau_photo": "nathan-bras",
    "bandeau_cap": "Nathan Fenina valide chaque page avant sa mise en ligne.",

    "h2_duo": "Ce que nous faisons dans le Var, et ce que nous refusons",
    "duo_intro": "La colonne de droite compte autant que celle de gauche.",
    "duo": (
        "Ce que nous faisons",
        [
            "<b>Situer votre activité sur la carte.</b> Rade, îles, golfe, "
            "vignes ou Verdon.",
            "<b>Mesurer vos positions commune par commune.</b> En français "
            "et en anglais.",
            "<b>Écrire les pages qui manquent.</b> Seulement celles qui "
            "répondent à un besoin.",
            "<b>Suivre les moteurs IA.</b> Chaque semaine, sur votre métier.",
            "<b>Compter les demandes.</b> Le trafic seul ne paie personne.",
        ],
        "Ce que nous refusons",
        [
            "<b>Une page par village.</b> Google y voit des pages "
            "satellites.",
            "<b>Une adresse varoise inventée.</b> Nous sommes à Nice, et "
            "c'est écrit.",
            "<b>L'achat de liens.</b> Sur aucun dossier.",
            "<b>Garantir une première place.</b> Aucune agence ne la "
            "contrôle.",
            "<b>Une recette unique pour tout le 83.</b> Elle se trompe de "
            "marché une fois sur deux.",
        ],
    ),

    "parti_pill": "Mon parti pris",
    "h2_parti": "Le Var n'est la banlieue ni de Marseille, ni de Nice",
    "parti_pris": [
        "Vu de Marseille, le Var commence juste après La Ciotat et ressemble à une "
        "extension de la métropole. Vu de Nice, il commence à l'Estérel et "
        "ressemble à la suite de la Côte d'Azur. Les deux lectures sont "
        "fausses, et elles coûtent cher.",
        "<strong>L'ouest regarde vers Marseille, l'est regarde vers Cannes, "
        "et le centre ne regarde que lui-même.</strong> Un artisan de "
        "Brignoles n'a rien à gagner d'une page pensée pour la Côte. Un "
        "hôtel de Saint-Raphaël, lui, se bat aussi contre des adresses du "
        "06.",
        "Nous sommes installés à Nice, et nous le disons. C'est justement "
        "pour cela que nous refusons de traiter le Var comme un prolongement "
        "des Alpes-Maritimes. <strong>Chaque bassin se lit avec ses propres "
        "données, pas avec nos habitudes.</strong>",
    ],
    "parti_role": "Fondateur de Décupler · Nice",

    "h2_variantes": "Agence SEO Var ou agence référencement Var : est-ce la "
                    "même chose ?",
    "variantes": [
        "Oui. « Agence SEO Var » et « agence référencement Var » désignent "
        "le même métier : SEO est le sigle anglais, référencement naturel "
        "sa traduction. Les deux recherches attendent un prestataire qui "
        "connaît le département et qui sait le découper.",
        "La nuance porte sur l'échelle. Une recherche sur le Var vise le "
        "département entier, alors qu'une recherche sur Toulon ou Fréjus "
        "vise une ville. Si votre clientèle vient surtout des "
        "Alpes-Maritimes, notre page <a class=\"lnk\" "
        "href=\"https://decupler.com/agence-seo-06/\">agence SEO 06</a> "
        "décrit ce marché voisin.",
        "Si c'est la visibilité dans les assistants conversationnels qui "
        "vous préoccupe, notre guide du <a class=\"lnk\" "
        "href=\"https://decupler.com/referencement-chatgpt/\">référencement "
        "sur ChatGPT</a> explique comment une entreprise y est citée.",
    ],

    "h2_faq": "Quelles questions nous pose-t-on sur le SEO dans le Var ?",
    "faq": [
        ("Mon entreprise est à Sanary ou à Bandol : quelle page me "
         "concerne ?",
         "Tout dépend d'où viennent vos clients. S'ils sont dans "
         "l'agglomération toulonnaise, c'est le marché de la rade. S'ils "
         "arrivent de Marseille ou d'Aix, votre concurrence est aussi "
         "là-bas. Nous le vérifions ensemble dans votre Search Console."),
        ("Faut-il créer une page pour chaque commune varoise où l'on "
         "travaille ?",
         "Non. Une page par marché, avec les communes desservies écrites en "
         "clair, fait mieux qu'une série de pages presque identiques. Google "
         "repère ces séries et les déclasse."),
        ("Avez-vous un bureau dans le Var ?",
         "Non. Notre seule adresse est à Nice, au 10 avenue Lympia privée. "
         "Nous travaillons à distance ; si le dossier le justifie, nous "
         "pouvons venir pour le lancement, et nous l'organisons ensemble."),
        ("Mon activité ne tourne que l'été : le SEO a-t-il un intérêt ?",
         "Oui, à condition de s'y prendre tôt. Une page doit être en ligne "
         "et indexée des mois avant l'ouverture, parce que les visiteurs "
         "comparent bien avant de réserver. En juin, il est souvent trop "
         "tard pour la saison en cours."),
        ("Quand peut-on espérer les premiers effets ?",
         "Une fiche d'établissement corrigée ou un site réparé réagissent "
         "parfois en quelques semaines. Une page neuve demande en général "
         "plusieurs mois. Nous donnons une estimation après l'audit, jamais "
         "avant."),
    ],

    "h2_voisines": "Votre marché dépasse le Var ?",
    "voisines_intro": "Chaque page décrit un marché différent, pas le même "
                      "texte avec un autre nom.",
    "voisines": [
        ("Agence SEO 06", "Les Alpes-Maritimes, de l'autre côté de "
         "l'Estérel.", "https://decupler.com/agence-seo-06/"),
        ("Agence SEO Toulon", "La rade, la défense et les achats "
         "industriels.", "https://decupler.com/agence-seo-toulon/"),
        ("Agence SEO Fréjus", "L'est varois, entre Estérel et "
         "Méditerranée.", "https://decupler.com/agence-seo-frejus/"),
        ("Consultant SEO Marseille", "Pour l'ouest varois tourné vers les "
         "Bouches-du-Rhône.", "https://decupler.com/consultant-seo-marseille/"),
    ],

    "photo_alt": "Nathan Fenina, fondateur de Décupler, agence SEO Var "
                 "depuis Nice",
    "eeat": "Nathan Fenina pratique le référencement naturel depuis huit "
            "ans et a accompagné plus de 70 entreprises. Il dirige Décupler "
            "depuis Nice et relit chaque page varoise avant sa publication.",
    "eeat_plus": [
        "Dans le Var, une commune voisine peut appartenir à un autre marché. "
        "Cette relecture sert à vérifier qu'une page parle bien au bon "
        "bassin, avec les bons noms de lieux.",
        "Ses analyses sur la visibilité dans les moteurs génératifs sont en "
        "accès libre, sur ce site et sur LinkedIn. Vous pouvez juger sa "
        "méthode avant de lui confier quoi que ce soit.",
    ],

    "final_lien": ("https://decupler.com/audit-geo/", "Mesurer ma visibilité dans les IA"),
    "h2_final": "Dans quel bassin varois jouez-vous vraiment ?",
    "final": "En trente minutes, nous ouvrons votre Search Console et nous "
             "regardons d'où viennent vos visiteurs. Nous interrogeons aussi "
             "les moteurs IA sur votre métier. Vous repartez avec votre "
             "bassin, vos vrais concurrents et les trois premières pages à "
             "écrire.",
}
