# -*- coding: utf-8 -*-
"""Blocs rediges — agence seo 06. Registre AGENCE. Page DEPARTEMENTALE.

Ce n'est pas une ville : elle agrege et renvoie vers les pages villes, sans
les cannibaliser (villes.json). Elle a donc son angle propre, qu'aucune page
ville ne peut porter : LE DECOUPAGE. Le 06 n'est pas un marche, c'en est
plusieurs — la metropole niçoise, le couloir cannois des salons, Antibes et
Sophia Antipolis, la filiere de Grasse, la frontiere mentonnaise, la
couronne de Cagnes, et l'arriere-pays des stations. Chaque bassin renvoie
vers sa page, dans le texte.

Parti pris assume : pas une page par commune (le departement en compte plus
de 160). Une page seulement la ou le marche change. C'est aussi la reponse a
Le Cannet (30 recherches, contigu a Cannes) : il est traite ici et dans la
page Cannes, pas dans une page jumelle.

Absorbe « agence seo alpes-maritimes » (30) et « agence seo paca » (70).
Grappe : 490/mois. A rediger en dernier : toutes les pages villes existent.
"""

BLOCS = {
    "pill": "Agence SEO 06 · Alpes-Maritimes",
    "h1": "Agence SEO 06 : les Alpes-Maritimes ne sont pas <em>un marché, "
          "mais sept</em>",
    "lead": [
        "Entre Mandelieu et Menton, il y a une heure de route environ, et "
        "pourtant rien ne se cherche de la même façon. Un restaurant du "
        "Vieux-Nice, un traiteur qui vit du MIPIM, un éditeur de Sophia "
        "Antipolis et un fournisseur d'absolus à Grasse n'ont ni les mêmes "
        "clients, ni les mêmes requêtes, ni les mêmes concurrents.",
        "Une agence SEO 06 qui applique la même recette partout se trompe au "
        "moins une fois sur deux. Depuis notre bureau du port de Nice, nous "
        "découpons le département en bassins, et nous travaillons chacun "
        "pour ce qu'il est, sur Google comme dans les réponses de ChatGPT, "
        "Claude, Gemini et Perplexity.",
    ],
    "cta1": "Réserver un audit offert",
    "cta2": "Voir notre offre SEO",
    "cta2_url": "https://decupler.com/machine-de-guerre-seo/",
    "micro": "30 minutes avec Nathan, en visio ou dans vos locaux. Sans "
             "engagement.",
    "visuel_photo": "hero-06",
    "visuel_alt": "La rade de Villefranche-sur-Mer — agence SEO 06 Décupler, à Nice",
    "visuel_badge": ("Un département", "Littoral · technopole · arrière-pays"),
    "hero_preuve": ("+46 %",
        "de clics sur les requêtes locales en 3 mois — Speed Inter",
        "https://decupler.com/etude-de-cas-seo-speed-inter/"),
    "cards": [
        ("Zone", "Alpes-Maritimes · de Mandelieu à Menton"),
        ("Bureau", "Nice · 10 avenue Lympia privée"),
        ("Méthode", "Un bassin, une stratégie"),
    ],
    "trust": [
        ("7", "bassins, sept façons de chercher"),
        ("1", "bureau, au port de Nice"),
        ("4", "moteurs IA suivis en plus de Google"),
        ("500 €", "point d'entrée en SEO local"),
    ],

    "h2_pourquoi": "Pourquoi le référencement dans le 06 se joue bassin par bassin ?",
    "pourquoi": [
        "Parce que la demande ne suit pas les limites administratives. Un "
        "habitant de Villeneuve-Loubet cherche un plombier « à Cagnes », un "
        "congressiste cherche un traiteur « à Cannes » depuis Londres, un "
        "ingénieur cherche un sous-traitant « Sophia Antipolis » sans jamais "
        "taper le nom d'une commune. Google, lui, répond à ces formulations, "
        "pas au découpage de la préfecture.",
        "Le département réunit aussi des économies qui n'ont presque rien en "
        "commun. Le littoral vit du tourisme et de l'événementiel, avec des "
        "pics violents. La technopole vend à des entreprises du monde "
        "entier. Grasse vit d'une filière. L'arrière-pays vit des saisons de "
        "ski et de randonnée. La frontière italienne change la langue de la "
        "moitié des clients mentonnais.",
        "Travailler le 06 comme un seul marché revient à écrire des pages "
        "qui ne parlent à personne. Nous commençons donc toujours par la "
        "même question : dans quel bassin êtes-vous, et d'où viennent vos "
        "clients ?",
    ],
    "cta_pourquoi": "Savoir dans quel bassin vous jouez",

    "h2_ranker": "Quels sont les sept marchés des Alpes-Maritimes ?",
    "ranker_intro": "Sept bassins, chacun avec ses requêtes et ses pièges. "
                    "Quand un bassin mérite une page à lui, elle est liée "
                    "ci-dessous.",
    "ranker": [
        ("Nice et sa métropole",
         "Commerce, santé, services, tech : le marché le plus dense et le "
         "plus concurrentiel, où chaque quartier compte. C'est là qu'est "
         "notre bureau — voir <a class=\"lnk\" "
         "href=\"https://decupler.com/agence-seo-nice/\">agence SEO "
         "Nice</a>."),
        ("Cannes, Le Cannet et Mandelieu",
         "Un calendrier plus qu'une ville : les salons, le Festival, la "
         "saison. Le Cannet se traite avec Cannes, pas à part — voir "
         "<a class=\"lnk\" href=\"https://decupler.com/agence-seo-cannes/\">"
         "agence SEO Cannes</a>."),
        ("Antibes, Juan-les-Pins et Sophia Antipolis",
         "Deux marchés sur une même commune : le yachting du port Vauban et "
         "les entreprises de la technopole — voir <a class=\"lnk\" "
         "href=\"https://decupler.com/agence-seo-antibes/\">agence SEO "
         "Antibes</a>."),
        ("Grasse et son pays",
         "Une filière, le parfum, qui vend au monde entier dans le "
         "vocabulaire du métier — voir <a class=\"lnk\" "
         "href=\"https://decupler.com/agence-seo-grasse/\">agence SEO "
         "Grasse</a>."),
        ("Cagnes-sur-Mer et sa couronne",
         "Villeneuve-Loubet, Saint-Laurent-du-Var, le Cros : des commerces "
         "qui doivent tenir leur territoire face à Nice — voir "
         "<a class=\"lnk\" href=\"https://decupler.com/agence-seo-cagnes-sur-mer/\">"
         "agence SEO Cagnes-sur-Mer</a>."),
        ("Menton et la frontière",
         "Une clientèle italienne, une saison d'hiver, la Fête du Citron — "
         "voir <a class=\"lnk\" href=\"https://decupler.com/agence-seo-menton/\">"
         "agence SEO Menton</a>."),
        ("L'arrière-pays et les stations",
         "Isola 2000, Auron, Valberg, les vallées du Mercantour : une demande "
         "saisonnière, souvent sur mobile, souvent la veille. Pas de page "
         "dédiée : chaque dossier se traite avec la commune qui l'entoure."),
    ],

    "h2_methode": "Comment travaillons-nous sur un dossier du 06 ?",
    "methode_intro": "Quatre étapes. La première situe votre entreprise "
                     "dans son bassin, avant de parler de mots-clés.",
    "methode": [
        ("On situe votre bassin.",
         "D'où viennent vos clients, dans quelle langue, à quel moment de "
         "l'année. La réponse décide de tout le reste."),
        ("On relève ce qui se cherche vraiment.",
         "Les formulations réelles, commune par commune et en plusieurs "
         "langues, et ce que les moteurs IA répondent sur votre métier."),
        ("On construit les pages qui manquent.",
         "Une page par besoin réel, jamais une page par commune. Nos agents "
         "IA préparent, Nathan relit et valide avant la mise en ligne."),
        ("On mesure les demandes.",
         "Appels, formulaires, itinéraires : un rapport mensuel qui dit ce "
         "que le référencement a rapporté."),
    ],
    "mock_k": "Question posée à ChatGPT par un acheteur étranger",
    "mock_q": "Which real estate agencies around Mougins and Valbonne speak "
              "English and handle villa sales?",
    "mock_ans": [
        (True, "Les agences dont le site anglais nomme les communes "
               "couvertes, les types de biens et l'équipe"),
        (True, "Celles qui sont citées par des sources tierces, en anglais, "
               "avec les mêmes informations"),
        (False, "Celles qui écrivent seulement « Côte d'Azur » sans jamais "
                "préciser où elles travaillent"),
    ],
    "mock_ft": "Illustration du mécanisme, pas une capture : le moteur "
               "répond commune par commune, jamais « Alpes-Maritimes ».",

    "h2_preuve": "Sur quoi nous juger ?",
    "preuve_intro": "Des études de cas publiées et chiffrées, choisies pour "
                    "ce qu'elles disent des marchés du 06 : la proximité, "
                    "la saison, la page qui compte.",
    "preuves": [
        ("Speed Inter — la proximité reprise mot à mot",
         "+46 % de clics organiques en trois mois (331 → 485 par mois) et un "
         "taux de clic passé de 0,61 % à 0,89 %. Des requêtes de quartier "
         "reprises une à une.",
         "https://decupler.com/etude-de-cas-seo-speed-inter/", "Lire le cas"),
        ("Decathlon Travel — une demande qui arrive par vagues",
         "+140 % de trafic organique en six mois (12 500 → 30 000 visites par "
         "mois) et +180 % de conversions. Le profil du littoral et des "
         "stations.",
         "https://decupler.com/etude-de-cas-seo-decathlon/", "Lire le cas"),
        ("Reux Travaux — une seule page de service",
         "+450 % de clics en trois mois sur la page stratégique (8 → 44). Ce "
         "qu'une page bien reprise rapporte à un artisan.",
         "https://decupler.com/etude-de-cas-seo-reux-travaux/", "Lire le cas"),
        ("Toutes nos études de cas",
         "Huit missions publiées, chacune avec sa source de mesure.",
         "https://decupler.com/cas-clients/", "Voir les études"),
    ],
    "preuve_note": "Chiffres issus de Google Search Console et de Semrush. "
                   "Ils racontent ces missions ; les vôtres dépendront de "
                   "votre bassin et de votre point de départ.",

    "photo_ville": {
        "cle": "bandeau-06",
        "alt": "Le Mercantour, l'arrière-pays des Alpes-Maritimes",
        "h2": "Du littoral aux sommets, en une heure de route",
        "p": "Le Mercantour, les stations, les villages perchés : le 06 ne "
             "s'arrête pas à la Promenade des Anglais. L'arrière-pays a ses "
             "propres clients, ses propres saisons, et des entreprises qu'on "
             "ne trouve pas quand on cherche mal.",
        "chips": ["Littoral", "Technopole", "Filière parfum", "Stations"],
    },

    "h2_zone": "Où intervenons-nous dans les Alpes-Maritimes ?",
    "zone_intro": "Une agence SEO 06 doit pouvoir venir partout dans "
                  "le département : nous le faisons depuis notre bureau du "
                  "port de Nice. Nous nous déplaçons pour le lancement et "
                  "les points importants, et nous travaillons à distance le "
                  "reste du temps. Nice est la seule ville où nous avons une "
                  "adresse.",
    "zone_note": "Au-delà du 06, nous intervenons aussi dans le Var et en "
                 "Principauté de Monaco, qui ont chacun leurs pages.",

    "ruban": [
        ("7 bassins", "sept façons de chercher dans un même département"),
        ("≈ 1 h", "de route entre Mandelieu et Menton"),
        ("FR · EN · IT", "les trois langues de la clientèle du 06"),
        ("1 mois", "de préavis, à tout moment"),
    ],

    "h2_budget": "Combien coûte une agence SEO dans le 06 ?",
    "budget_intro": "Nos fourchettes sont les mêmes dans tout le "
                    "département. Ce qui change le prix, c'est le nombre de "
                    "bassins et de langues à couvrir.",
    "budget": [
        ("À partir de 500 € / mois",
         "Un commerce ou un artisan dans un seul bassin : fiche "
         "d'établissement, pages principales, suivi mensuel."),
        ("1 000 à 2 000 € / mois",
         "Une entreprise B2B, un e-commerce ou un réseau présent dans "
         "plusieurs bassins, avec une version anglaise ou italienne."),
        ("Sur devis",
         "Plusieurs établissements, une clientèle internationale, ou un "
         "audit seul avant une refonte."),
    ],
    "budget_note": "Un conseil qui ne nous rapporte rien : si vos clients "
                   "viennent tous du bouche-à-oreille, commencez par votre "
                   "fiche d'établissement. Nous vous le dirons au premier "
                   "appel.",

    "h2_livrables": "Qu'est-ce qui arrive chaque mois sur un dossier du 06 ?",
    "livrables_intro": "Six livrables, adaptés à votre bassin plutôt qu'à "
                       "un modèle unique.",
    "livrables": [
        ("01", "Le rapport des demandes",
         "Appels, formulaires, itinéraires : ce que le référencement a "
         "rapporté ce mois-ci, et d'où.",
         "Chaque mois"),
        ("02", "Le relevé des positions, commune par commune",
         "Vos requêtes suivies dans chaque commune de votre bassin, pas une "
         "moyenne départementale.",
         "Chaque semaine"),
        ("03", "Les citations dans les moteurs IA",
         "Ce que répondent ChatGPT, Claude, Gemini et Perplexity sur votre "
         "métier dans votre bassin.",
         "Chaque semaine"),
        ("04", "Les pages créées ou reprises",
         "Rédigées pour un besoin réel, relues par Nathan avant la mise en "
         "ligne.",
         "2 à 6 par mois"),
        ("05", "Le calendrier des saisons",
         "Salons, saison d'été, saison d'hiver : ce qui doit être prêt, et "
         "à quelle date.",
         "Mis à jour chaque mois"),
        ("06", "Un point avec Nathan",
         "Trente minutes en visio, ou dans vos locaux quand le dossier le "
         "demande.",
         "Chaque mois"),
    ],
    "livrables_note": "Entre deux points, vous écrivez directement à "
                      "l'équipe. Pas de ticket, pas de commercial.",

    "bandeau": ("Une page par marché, jamais une page par commune",
        ["Le département compte plus de 160 communes. Créer une page par "
         "commune avec le même texte et un nom qui change, c'est ce que "
         "Google appelle des pages satellites : il les repère, et il "
         "pénalise le site entier.",
         "Nous créons une page seulement là où le marché change vraiment. "
         "C'est pour cela que Le Cannet est traité avec Cannes, et "
         "l'arrière-pays avec la commune qui l'entoure. Moins de pages, "
         "mais chacune a une raison d'exister."],
        (None, None, None, None, None)),
    "bandeau_photo": "nathan-bras",
    "bandeau_cap": "Nathan Fenina valide chaque page avant sa mise en ligne.",

    "h2_duo": "Ce que nous faisons, et ce que nous ne faisons pas",
    "duo_intro": "La seconde colonne compte autant que la première.",
    "duo": (
        "Ce que nous faisons",
        [
            "<b>Situer votre entreprise dans son bassin.</b> Avant tout "
            "mot-clé.",
            "<b>Suivre vos positions commune par commune.</b> Et en "
            "plusieurs langues.",
            "<b>Écrire les pages qui manquent.</b> Une par besoin réel.",
            "<b>Suivre votre visibilité dans les moteurs IA.</b> Chaque "
            "semaine.",
            "<b>Mesurer les demandes.</b> Pas seulement le trafic.",
        ],
        "Ce que nous ne faisons pas",
        [
            "<b>Une page par commune.</b> C'est la pénalité assurée.",
            "<b>De fausses adresses.</b> Nice est notre seule adresse, et "
            "nous le disons.",
            "<b>Des liens achetés.</b> Sur aucun dossier.",
            "<b>Promettre une position.</b> Personne ne contrôle Google.",
            "<b>Deux concurrents dans le même bassin.</b> Un seul client par "
            "métier et par bassin.",
        ],
    ),

    "parti_pill": "Mon parti pris",
    "h2_parti": "Pourquoi « Côte d'Azur » ne suffit jamais",
    "parti_pris": [
        "Presque toutes les entreprises du département écrivent « Côte "
        "d'Azur » sur leur site. C'est joli, et c'est inutile : personne ne "
        "cherche un plombier « Côte d'Azur », et aucun moteur IA ne "
        "recommande un prestataire sans savoir où il travaille.",
        "<strong>Ce qui fait ranker dans le 06, c'est la précision.</strong> "
        "Nommer les communes où l'on intervient, les quartiers, les langues "
        "parlées, les saisons de travail. Dire « nous livrons de Mandelieu à "
        "Villefranche », pas « sur toute la Côte ».",
        "C'est un travail modeste, presque administratif. Mais c'est celui "
        "qui fait la différence entre une entreprise qu'on trouve et une "
        "entreprise qu'on devine. <strong>Les moteurs, eux, ne devinent "
        "pas.</strong>",
    ],
    "parti_role": "Fondateur de Décupler · Nice",

    "h2_variantes": "Agence SEO 06, Alpes-Maritimes, PACA : quelle différence ?",
    "variantes": [
        "« Agence SEO 06 », « agence SEO Alpes-Maritimes » et « agence SEO "
        "PACA » désignent souvent la même recherche : un prestataire proche, "
        "qui connaît la région. La différence tient à l'échelle. Le 06 est "
        "un département ; la région PACA ajoute le Var, les "
        "Bouches-du-Rhône et les départements alpins.",
        "Dans le Var, nous intervenons à Fréjus et à Toulon, comme le "
        "décrit la page <a class=\"lnk\" "
        "href=\"https://decupler.com/agence-seo-toulon/\">agence SEO "
        "Toulon</a>. Au-delà, nous travaillons à distance, sans prétendre à "
        "une présence locale.",
        "Si votre priorité est d'apparaître dans les réponses des moteurs "
        "IA plutôt que dans Google, notre page <a class=\"lnk\" "
        "href=\"https://decupler.com/agence-geo-nice/\">agence GEO Nice</a> "
        "détaille cette partie du travail.",
    ],

    "h2_faq": "Questions fréquentes sur le SEO dans les Alpes-Maritimes",
    "faq": [
        ("Faut-il une page par commune où l'on intervient ?",
         "Non. Une page par marché réel suffit, avec la liste des communes "
         "couvertes écrite noir sur blanc. Des pages identiques qui ne "
         "changent que le nom de la ville sont repérées et pénalisées."),
        ("Mon entreprise est à Mougins ou à Valbonne : quelle page me "
         "concerne ?",
         "Celle du bassin où sont vos clients. Pour une entreprise de la "
         "technopole, c'est Antibes et Sophia Antipolis ; pour un commerce "
         "de proximité, c'est souvent Cannes ou Grasse. Nous le vérifions "
         "dans votre Search Console au premier appel."),
        ("Vous déplacez-vous dans tout le département ?",
         "Oui, pour le lancement et les points importants, de Mandelieu à "
         "Menton et dans l'arrière-pays. Le reste du travail se fait à "
         "distance, comme avec n'importe quelle agence."),
        ("Travaillez-vous en italien et en anglais ?",
         "Oui. Nous rédigeons en français et en anglais, et nous faisons "
         "appel à des rédacteurs natifs pour l'italien, relus avant "
         "publication."),
        ("Combien de temps avant les premiers résultats ?",
         "Les corrections de fiche et de technique produisent souvent un "
         "effet en quelques semaines. Les pages nouvelles demandent "
         "plusieurs mois : nous vous donnons une estimation après l'audit, "
         "pas avant."),
    ],

    "h2_voisines": "Vous êtes hors du 06 ?",
    "voisines_intro": "Chaque page décrit ce qui change d'une ville à "
                      "l'autre.",
    "voisines": [
        ("Agence SEO Monaco", "La Principauté, qui n'est pas le 06 : "
         "d'autres règles.", "https://decupler.com/agence-seo-monaco/"),
        ("Agence SEO Fréjus", "Par l'Esterel, à une demi-heure "
         "de Mandelieu.", "https://decupler.com/agence-seo-frejus/"),
        ("Consultant SEO Nice", "Un seul interlocuteur plutôt qu'une "
         "équipe.", "https://decupler.com/consultant-seo-nice/"),
        ("Consultant SEO Marseille", "Les Bouches-du-Rhône, à distance.",
         "https://decupler.com/consultant-seo-marseille/"),
    ],

    "photo_alt": "Nathan Fenina, fondateur de Décupler, agence SEO 06",
    "eeat": "Huit ans de SEO, plus de 70 entreprises accompagnées en SaaS, "
            "e-commerce et services B2B. Nathan dirige Décupler depuis Nice "
            "et connaît chacun des bassins du département.",
    "eeat_plus": [
        "Nathan Fenina a installé Décupler au port de Nice, à une heure "
        "au plus de chaque bassin du littoral. Il relit chaque page avant sa mise en ligne : dans "
        "un département où une commune voisine peut être un autre marché, "
        "c'est la relecture qui évite les erreurs.",
        "Ses analyses sur la visibilité dans les moteurs génératifs sont "
        "publiées sur ce site et sur LinkedIn : de quoi juger sa façon de "
        "travailler avant de lui confier un dossier.",
    ],

    "final_lien": ("https://decupler.com/audit-geo/", "Auditer ma visibilité dans les IA"),
    "h2_final": "Trente minutes pour situer votre entreprise dans son bassin",
    "final": "On ouvre votre Search Console, on regarde d'où viennent vos "
             "clients et ce que répondent les IA sur votre métier. Vous "
             "repartez avec votre bassin, vos concurrents réels et les "
             "trois pages à écrire en premier.",
}
