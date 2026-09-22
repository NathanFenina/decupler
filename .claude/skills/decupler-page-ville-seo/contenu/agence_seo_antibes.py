# -*- coding: utf-8 -*-
"""Blocs rediges — agence seo antibes. Registre AGENCE.

Angle propre a Antibes, et a aucune autre ville : la commune contient DEUX
marches qui n'ont rien en commun.
  - le littoral : Port Vauban (plus grande marina d'Europe), yachting,
    tourisme, immobilier du Cap.
  - Sophia Antipolis : la premiere technopole europeenne, du B2B, du SaaS, de
    la recherche. Cycles longs, acheteurs techniques, requetes en anglais.
Une page qui traite Antibes comme « une ville de la Cote d'Azur » rate l'un
des deux. C'est le seul endroit du lot ou la page doit assumer deux publics.

Absorbe « agence referencement antibes » (90) et « agence seo sophia
antipolis » (110) — cette derniere est un quartier d'Antibes-Juan-les-Pins et
de Valbonne, pas une commune a part. Grappe : 410/mois.
"""

BLOCS = {
    "pill": "Agence SEO Antibes · Sophia Antipolis",
    "h1": "Agence SEO Antibes : <em>deux marchés</em> dans une seule commune",
    "lead": [
        "Antibes, c'est Port Vauban et le Cap d'un côté — yachting, tourisme, "
        "immobilier de prestige, saisonnalité forte. Et Sophia Antipolis de "
        "l'autre — SaaS, électronique, recherche, cycles d'achat de six à dix-huit "
        "mois et des acheteurs qui cherchent en anglais.",
        "Les deux ne se travaillent pas du tout pareil. Une agence SEO Antibes qui "
        "applique la même méthode aux deux fait la moitié du travail. Nous "
        "traitons chaque marché sur son propre terrain — Google d'abord, et les "
        "réponses de ChatGPT, Claude, Gemini et Perplexity, déjà bien installées "
        "dans la présélection fournisseur à Sophia.",
    ],
    "cta1": "Réserver un audit offert",
    "cta2": "Voir nos études de cas",
    "cta2_url": "https://decupler.com/cas-clients/",
    "micro": "30 minutes avec Nathan. Antibes est à vingt minutes de nos bureaux "
             "de Nice.",
    # Visuel du hero : une photo reelle et un badge qui porte le fait
    # differenciant de la ville. Remplace les trois encadres de texte.
    "visuel": (
        "https://decupler.com/wp-content/uploads/2026/09/decupler-equipe-seo-ia.jpg",
        "Experts de l'agence SEO Antibes Décupler devant un tableau de bord de trafic organique",
        1400, 933,
        "Deux marchés", "Port Vauban · Sophia Antipolis"),
    "hero_preuve": ("+250 %",
        "de trafic et +180 % de leads en 6 mois — Spigao, SaaS B2B",
        "https://decupler.com/etude-de-cas-seo-spigao/"),
    "cards": [
        ("Zone", "Antibes · Juan-les-Pins · 06600 · 06160"),
        ("Deux marchés", "Littoral et yachting · Sophia Antipolis"),
        ("Depuis", "Nice, à 20 minutes"),
    ],
    "trust": [
        ("2", "marchés distincts dans une seule commune"),
        ("06600", "Antibes, Juan-les-Pins et le Cap"),
        ("4", "moteurs IA suivis en plus de Google"),
        ("20 min", "depuis nos bureaux de Nice"),
    ],

    "h2_pourquoi": "Pourquoi une agence SEO à Antibes doit choisir son camp ?",
    "pourquoi": [
        "Commençons par le littoral. Port Vauban est la plus grande marina "
        "d'Europe, et autour d'elle vit une économie entière : courtage de "
        "bateaux, avitaillement, chantiers, équipages, conciergerie. La demande y "
        "est saisonnière — elle monte au printemps, culmine en été, retombe — et "
        "largement anglophone : un propriétaire de yacht britannique ou italien "
        "cherche « yacht refit Antibes », pas « chantier naval Antibes ».",
        "Puis Sophia Antipolis. Deux mille entreprises, trente mille emplois, et "
        "un profil de recherche à l'opposé : pas de saisonnalité, pas de "
        "proximité, des requêtes techniques à faible volume et à très forte "
        "valeur. Un éditeur de logiciel de Sophia ne vend pas à Antibes, il vend "
        "à Paris, Munich ou Boston. Le mot « Antibes » n'a alors qu'un intérêt : "
        "l'ancrage de la fiche d'établissement et le recrutement.",
        "Ce grand écart explique pourquoi tant de sites antibois plafonnent. Ils "
        "empilent les deux discours sur les mêmes pages, avec des mots-clés qui "
        "se contredisent, et Google n'arrive pas à décider de quoi le site parle. "
        "La première décision d'un projet antibois n'est donc pas technique : "
        "c'est de choisir quel marché la page adresse, et de le tenir.",
    ],
    "cta_pourquoi": "Savoir lequel des deux vous concerne",

    "h2_ranker": "Qu'est-ce qui fait ranker une entreprise antiboise ?",
    "ranker_intro": "Six leviers. Les trois premiers valent surtout pour le "
                    "littoral, les trois suivants pour Sophia — regardez d'abord "
                    "ceux de votre marché.",
    "ranker": [
        ("Littoral : l'anglais comme langue principale",
         "Sur le yachting et l'immobilier du Cap, une part majoritaire de la "
         "demande est anglophone. Une version anglaise construite sur ses propres "
         "mots-clés, pas traduite, capte un marché que vos concurrents laissent "
         "vide. C'est le levier le plus rentable du littoral antibois."),
        ("Littoral : le calendrier avant le contenu",
         "La demande nautique se prépare en février-mars pour une saison qui "
         "démarre en mai. Un contenu publié en juin arrive trop tard : Google met "
         "des semaines à l'indexer et à lui faire confiance. Le calendrier "
         "éditorial se cale sur les salons et l'ouverture de saison, pas sur "
         "l'année civile."),
        ("Littoral : la fiche d'établissement et les avis",
         "Sur les requêtes de service géolocalisées, le pack local passe avant le "
         "premier lien bleu. Catégorie exacte, photos récentes du port, avis "
         "réguliers — y compris en anglais, qui pèsent double ici. Méthode : "
         "<a class=\"lnk\" href=\"https://decupler.com/fiche-gmb/\">la fiche "
         "GMB</a> et <a class=\"lnk\" "
         "href=\"https://decupler.com/obtenir-des-avis-google/\">les avis</a>."),
        ("Sophia : une page par cas d'usage, pas par fonctionnalité",
         "Un acheteur technique ne cherche pas votre module, il cherche son "
         "problème. Une page par cas d'usage réel, avec le vocabulaire de son "
         "métier, capte une demande précise que personne ne travaille. C'est le "
         "socle de notre approche <a class=\"lnk\" "
         "href=\"https://decupler.com/seo-saas/\">SEO SaaS</a>."),
        ("Sophia : la documentation comme actif SEO",
         "Sur les éditeurs de logiciel, la documentation technique attire souvent "
         "plus de qualifiés que le site vitrine — et presque personne ne "
         "l'optimise. La rendre indexable et structurée est le gisement le plus "
         "sous-exploité de la technopole."),
        ("Sophia : être cité en présélection",
         "Avant d'appeler trois fournisseurs, un acheteur demande une liste à un "
         "assistant. Y figurer suppose un contenu découpable, un balisage propre "
         "et des mentions hors de votre site — voir <a class=\"lnk\" "
         "href=\"https://decupler.com/agence-geo/\">notre pôle GEO</a>."),
    ],

    "h2_methode": "Comment on travaille sur un projet antibois ?",
    "methode_intro": "Quatre étapes. La première est gratuite, et elle sert "
                     "surtout à trancher la question des deux marchés.",
    "methode": [
        ("Cadrage : quel marché, quelle langue.", "Une heure pour établir d'où "
         "viennent vos clients, dans quelle langue ils cherchent, et si votre site "
         "essaie de parler à deux publics à la fois. Cette réponse commande tout "
         "le reste."),
        ("Fondations techniques.", "Indexation, vitesse, données structurées, et "
         "balisage <code>hreflang</code> si le site est multilingue — l'erreur la "
         "plus fréquente sur les sites antibois qui ont une version anglaise."),
        ("Production sur le vocabulaire réel.", "Pages par service ou par cas "
         "d'usage selon votre marché, dans chaque langue de travail. Chaque "
         "livrable est relu et validé par un expert avant mise en ligne."),
        ("Mesure et arbitrage.", "Un point mensuel sur données Search Console, "
         "segmenté par langue et par pays. Sans cette segmentation, on optimise "
         "en ne voyant que la moitié du marché."),
    ],
    "mock_k": "Deux requêtes, deux marchés, un même code postal",
    "mock_q": "yacht refit Antibes  ·  logiciel de supervision industrielle",
    "mock_ans": [
        (True, "Site qui assume un seul des deux marchés"),
        (True, "Site avec une version anglaise pensée, pas traduite"),
        (False, "Site qui empile yachting et B2B sur les mêmes pages"),
        (False, "Site dont la documentation n'est pas indexable"),
    ],
    "mock_ft": "Illustration du mécanisme : deux intentions aussi éloignées ne "
               "peuvent pas se traiter sur les mêmes pages. Ce n'est pas la "
               "capture d'une réponse réelle.",

    "h2_preuve": "Quels résultats sur ces deux profils ?",
    "preuve_intro": "Deux missions côté B2B technique, deux côté service et "
                    "commerce. Chaque lien mène à l'étude complète : période, "
                    "méthode, avant et après, source de mesure.",
    "preuves": [
        ("Spigao — le SaaS B2B, profil Sophia",
         "+250 % de trafic organique en 6 mois (5 200 → 16 250 sessions), +180 % "
         "de leads organiques (120 → 336/mois), coût d'acquisition payant réduit "
         "de 45 %. Le cas le plus proche d'un éditeur de la technopole.",
         "https://decupler.com/etude-de-cas-seo-spigao/", "Lire le cas"),
        ("Double Trade — le sprint technique",
         "+105 % de trafic organique en 3 mois (8 400 → 17 220 sessions) et "
         "+130 % de leads, dont +22 % dès le premier mois par les seules "
         "corrections techniques.",
         "https://decupler.com/etude-de-cas-seo-double-trade/", "Lire le cas"),
        ("Decathlon Travel — le service saisonnier",
         "+140 % de trafic organique en 6 mois (12 500 → 30 000 visites/mois) et "
         "+180 % de conversions. Une demande saisonnière, comme sur le littoral.",
         "https://decupler.com/etude-de-cas-seo-decathlon/", "Lire le cas"),
        ("Reux Travaux — le service de proximité",
         "+450 % de clics sur la page de service stratégique en 3 mois (8 → 44). "
         "Ce qu'une seule page bien reprise peut produire.",
         "https://decupler.com/etude-de-cas-seo-reux-travaux/", "Lire le cas"),
    ],
    "preuve_note": "Mesures Google Search Console et Semrush. Ces résultats sont "
                   "ceux de ces missions dans leur contexte, pas une promesse pour "
                   "la vôtre : le point de départ et la concurrence changent tout. "
                   "Nous chiffrons l'attendu avant de signer, pas après.",

    "h2_zone": "Où intervenons-nous autour d'Antibes ?",
    "zone_intro": "Nos bureaux sont à Nice, à vingt minutes d'Antibes par le bord "
                  "de mer. Nous nous déplaçons sur la commune, à Juan-les-Pins et "
                  "à Sophia Antipolis. Nous n'avons pas de bureau antibois et nous "
                  "ne le prétendons pas.",
    "zone_note": "Précision utile : Sophia Antipolis n'est pas une commune. La "
                 "technopole s'étend sur Antibes, Valbonne, Biot, Mougins et "
                 "Vallauris. Si votre siège est à Valbonne, c'est bien cette page "
                 "qui vous concerne — et votre fiche d'établissement doit porter "
                 "votre commune réelle, pas « Sophia Antipolis ».",

    "h2_budget": "Combien coûte une agence SEO à Antibes ?",
    "budget_intro": "Affichés. Trois facteurs font varier le prix : le nombre de "
                    "marchés à couvrir, le nombre de langues, et l'état technique "
                    "du site.",
    "budget": [
        ("À partir de 500 € / mois",
         "Commerce, artisan, profession libérale antiboise, en français. Fiche "
         "d'établissement, avis, citations locales, pages de service."),
        ("1 000 à 2 000 € / mois",
         "SaaS, éditeur, B2B technique, e-commerce : pages par cas d'usage, "
         "documentation indexable, technique, suivi des citations IA."),
        ("Sur devis",
         "Version anglaise complète pour le yachting ou l'international, deux "
         "marchés menés en parallèle, gros catalogue. Après audit, jamais avant."),
    ],
    "budget_note": "Le conseil qui nous rapporte le moins et qui vous fait gagner "
                   "le plus : si votre site essaie aujourd'hui de parler aux deux "
                   "marchés, commencez par en séparer un. Ça coûte moins cher "
                   "qu'un an de contenu et ça débloque souvent la situation à soi "
                   "seul.",

    "h2_variantes": "Agence SEO Antibes, Sophia Antipolis, Juan-les-Pins : "
                    "faut-il une page par zone ?",
    "variantes": [
        "Non, et c'est une erreur fréquente. Antibes, Juan-les-Pins et le Cap "
        "d'Antibes forment une seule commune : trois pages qui répètent le même "
        "contenu avec le nom changé ne se classent sur aucune, Google les traite "
        "comme du contenu jumeau. Une page qui couvre honnêtement la commune vaut "
        "mieux que trois qui se cannibalisent.",
        "« Agence SEO Sophia Antipolis » est un cas à part, et c'est pour ça que "
        "cette page l'absorbe plutôt que d'en faire une page séparée. La "
        "technopole n'est pas une commune : elle s'étend sur Antibes, Valbonne, "
        "Biot, Mougins et Vallauris. Une page dédiée ne pourrait s'appuyer sur "
        "aucun code postal propre ni aucune fiche d'établissement — elle serait "
        "faible par construction. Le bon réflexe est de traiter Sophia comme un "
        "<b>marché</b>, pas comme un lieu.",
        "Quant à « agence référencement Antibes », c'est strictement la même chose "
        "qu'« agence SEO Antibes » : SEO est l'acronyme anglais, référencement "
        "naturel sa traduction française. Les deux formulations mènent au même "
        "besoin.",
        "Si vous cherchez un interlocuteur unique plutôt qu'une équipe, la page "
        "<a class=\"lnk\" href=\"https://decupler.com/consultant-seo-antibes/\">"
        "consultant SEO à Antibes</a> décrit l'accompagnement en direct.",
    ],

    "h2_faq": "Questions fréquentes sur le SEO à Antibes",
    "faq": [
        ("Je suis à Sophia Antipolis. Le SEO local m'intéresse-t-il ?",
         "Moins que vous ne le pensez, et c'est une bonne nouvelle pour votre "
         "budget. Si vous vendez à Paris, Munich ou Boston, la géolocalisation ne "
         "vous apporte rien : ce qui compte, ce sont des pages par cas d'usage, une "
         "documentation indexable et des mentions dans votre filière. Le local ne "
         "vous sert que sur deux points — la fiche d'établissement, utile pour la "
         "confiance et le recrutement, et les requêtes de vos prestataires locaux."),
        ("Faut-il un site en anglais pour le yachting ?",
         "Sur le yachting antibois, oui, et pas une traduction : une <b>version</b> "
         "anglaise avec sa propre recherche de mots-clés. Un propriétaire de bateau "
         "britannique tape « yacht refit Antibes » ou « berth Port Vauban », "
         "formulations qui n'ont aucun équivalent littéral en français. C'est le "
         "chantier le plus rentable de ce marché, et celui que vos concurrents "
         "négligent le plus souvent."),
        ("Mon site parle du yachting ET du B2B. Que faire ?",
         "Séparer. Deux silos distincts, avec leur propre arborescence, leur propre "
         "vocabulaire et, si possible, leur propre page d'entrée. Tant que les deux "
         "discours cohabitent sur les mêmes pages, Google n'arrive pas à décider de "
         "quoi votre site parle, et vous restez au milieu du classement sur les deux "
         "sujets. C'est le premier arbitrage qu'on fait sur un projet antibois."),
        ("Combien de temps avant des résultats ?",
         "Sur la fiche d'établissement et les avis : <b>4 à 8 semaines</b>. Sur des "
         "requêtes de service locales : <b>4 à 6 mois</b>. Sur du B2B technique à "
         "Sophia, comptez <b>6 mois</b> avant un mouvement solide — les volumes sont "
         "faibles, donc chaque position gagnée se voit lentement dans les chiffres "
         "mais vite dans les demandes entrantes."),
        ("Vous avez des clients à Sophia Antipolis ?",
         "Pas de mission Sophia publiée à ce jour, et nous préférons le dire. On "
         "ne choisit pas une agence SEO Antibes sur ses promesses mais sur ses "
         "chiffres publiés. Ce que "
         "nous avons, ce sont des missions SaaS et B2B de même profil — Spigao, "
         "Double Trade — dont les études de cas sont publiées et chiffrées. Vous "
         "pouvez juger sur celles-là."),
        ("Est-ce que l'IA rédige mes contenus techniques ?",
         "Elle produit la matière, un expert relit, corrige et valide. Sur du "
         "contenu technique nous vous faisons en plus valider le vocabulaire métier "
         "avant publication : une approximation sur un procédé ou une norme vous "
         "discrédite auprès du seul lecteur qui compte, et aucun gain de temps ne "
         "vaut ça."),
    ],

    "bandeau": ("Un marché, une méthode",
        ["Le premier livrable d'un projet antibois n'est pas un calendrier "
         "éditorial : c'est une décision. Quel marché votre site adresse, dans "
         "quelle langue, et ce qu'on arrête de faire. Nous la prenons avec vous "
         "au premier rendez-vous, et elle est souvent la partie la plus utile de "
         "tout l'accompagnement.",
         "Ensuite l'équipe produit — six agents IA sur l'analyse, les briefs, la "
         "rédaction, le maillage et la publication — et un expert SEO valide "
         "chaque page. Rien ne part en ligne sans cette relecture."],
        ("https://decupler.com/wp-content/uploads/2026/09/"
         "decupler-equipe-seo-ia.jpg",
         "Experts de l'agence SEO Antibes Décupler devant un tableau de bord de "
         "trafic organique", 1400, 933,
         "IA + humain : l'agent produit, l'expert valide et publie.")),

    "h2_voisines": "Nos autres zones d'intervention",
    "voisines_intro": "Chaque page décrit le marché réel de sa ville. Sur la Côte "
                      "d'Azur, deux communes voisines peuvent avoir des économies "
                      "sans rapport — Antibes en est la démonstration.",
    "voisines": [
        ("Agence SEO Nice", "Notre siège, au port Lympia. Marché saisonnier, "
         "multilingue, très dense.",
         "https://decupler.com/agence-seo-nice/"),
        ("Agence SEO Cannes", "Événementiel, luxe et yachting, au rythme du "
         "Palais des Festivals.",
         "https://decupler.com/agence-seo-cannes/"),
        ("Agence SEO Monaco", "Finance et immobilier de prestige, en plusieurs "
         "langues, hors de France.",
         "https://decupler.com/agence-seo-monaco/"),
        ("Agence SEO Toulon", "Le B2B industriel varois : arsenal, logistique "
         "portuaire, BTP.",
         "https://decupler.com/agence-seo-toulon/"),
    ],

    "photo_alt": "Nathan Fenina, fondateur de l'agence SEO Antibes Décupler",
    "eeat": "Huit ans de SEO, plus de 70 entreprises accompagnées en SaaS, "
            "e-commerce et services B2B. Basé à Nice, à vingt minutes d'Antibes "
            "et de Sophia Antipolis. Nathan prend lui-même le premier rendez-vous "
            "— c'est là que se joue l'arbitrage entre vos deux marchés.",

    "final_lien": ("https://decupler.com/faire-un-audit-seo/",
                   "Ce que contient l'audit"),
    "h2_final": "Trente minutes pour trancher entre vos deux marchés",
    "final": "On ouvre votre Search Console, on regarde d'où viennent vos "
             "visiteurs et dans quelle langue ils cherchent, et on vous dit lequel "
             "des deux marchés votre site tient réellement aujourd'hui. La réponse "
             "surprend souvent.",
}
