# -*- coding: utf-8 -*-
"""Blocs rediges — agence seo nice. Registre AGENCE (entite Decupler).

Angle propre a Nice, et a aucune autre ville du lot : c'est la seule ou Decupler
a une adresse reelle (port Lympia). La page peut donc dire « notre bureau »,
ce qui est interdit partout ailleurs. Deuxieme particularite : la SERP y est
tenue par une page Digimood de 610 mots, sans FAQ ni adresse, non retouchee
depuis janvier 2021 — l'ecart se joue sur la fraicheur et la preuve, pas sur
le volume de texte.

Absorbe les variantes de meme intention plutot que d'en faire des pages :
agence referencement nice (480), agence referencement naturel nice (90),
referencement site internet nice (140), referencement google nice (10).
Volume cumule de la grappe : 2 320/mois.
"""

BLOCS = {
    "pill": "Agence SEO Nice · Port Lympia",
    "h1": "Agence SEO Nice : le référencement naturel "
          "<em>vu depuis le port Lympia</em>",
    "lead": [
        "Une agence SEO Nice qui n'est pas à Nice, ça se voit. Nos bureaux "
        "sont au 10 avenue Lympia privée, 06300, entre le port et le Vieux-Nice. "
        "C'est la seule ville de la Côte d'Azur où nous pouvons écrire cela, et ça "
        "change ce qu'on peut vous promettre : on connaît la saisonnalité niçoise, "
        "on sait quels quartiers se disputent quelles requêtes.",
        "Nous travaillons deux terrains à la fois : Google, et les réponses de "
        "ChatGPT, Claude, Gemini et Perplexity — où vos prospects niçois posent "
        "désormais une partie de leurs questions.",
    ],
    "cta1": "Réserver un audit offert",
    "cta2": "Voir notre page GEO Nice",
    "cta2_url": "https://decupler.com/agence-geo-nice/",
    "micro": "30 minutes avec Nathan, à Nice ou en visio. Sans engagement.",
    "cards": [
        ("Nos bureaux", "10 av. Lympia privée · 06300"),
        ("Zone", "Nice et Alpes-Maritimes"),
        ("Moteurs suivis", "Google · ChatGPT · Claude · Gemini"),
    ],
    "trust": [
        ("06300", "nos bureaux, port Lympia"),
        ("4", "moteurs IA suivis en plus de Google"),
        ("8", "études de cas publiées et chiffrées"),
        ("8 ans", "d'expertise SEO"),
    ],

    "h2_pourquoi": "Pourquoi une agence SEO à Nice, et pas une agence à distance ?",
    "pourquoi": [
        "Nice est la cinquième ville de France, mais son marché de la recherche ne "
        "se comporte pas comme celui d'une métropole classique. Il est saisonnier : "
        "la demande d'hôtellerie, de restauration, de location et de services "
        "touristiques monte d'avril à septembre, puis retombe. Un calendrier "
        "éditorial lissé sur douze mois publie ses meilleurs contenus en novembre, "
        "quand personne ne cherche.",
        "Il est aussi multilingue. Une part significative de la clientèle niçoise "
        "interroge Google en anglais et en italien, avec des formulations qui ne "
        "sont jamais la traduction littérale des vôtres. « Dentist Nice English "
        "speaking » n'est pas « dentiste anglophone Nice » : ce sont deux requêtes "
        "distinctes, et la seconde ne capte pas la première.",
        "Enfin, il est géographiquement resserré. Sur la Promenade des Anglais, à "
        "Jean-Médecin, dans le Vieux-Nice ou au port, des dizaines "
        "d'établissements se disputent les mêmes mots-clés à quelques centaines de "
        "mètres. À cette échelle, ce n'est plus le contenu qui départage, c'est "
        "le <a class=\"lnk\" href=\"https://decupler.com/seo-local/\">SEO "
        "local</a> : la cohérence de votre fiche d'établissement, vos avis, vos "
        "citations sur les annuaires azuréens.",
    ],
    "cta_pourquoi": "Voir où j'en suis sur Nice",

    "h2_ranker": "Qu'est-ce qui fait ranker une entreprise niçoise ?",
    "ranker_intro": "Cinq leviers, dans l'ordre où nous les traitons sur un projet "
                    "niçois. L'ordre compte : les trois premiers se règlent en "
                    "quelques semaines, les deux derniers demandent des mois.",
    "ranker": [
        ("La fiche d'établissement avant le site",
         "Sur une requête niçoise géolocalisée, le pack local occupe le haut de "
         "l'écran avant le premier lien bleu. Catégorie principale exacte, horaires "
         "à jour, photos récentes, questions-réponses remplies : c'est le levier le "
         "plus rapide. Notre guide : <a class=\"lnk\" "
         "href=\"https://decupler.com/fiche-gmb/\">optimiser sa fiche GMB</a>."),
        ("Les avis, en volume et en fraîcheur",
         "Un établissement niçois avec 12 avis ne tient pas face à un voisin qui en "
         "a 180. Ce qui compte n'est pas seulement la note, c'est le rythme : trois "
         "avis par mois pèsent plus que trente d'un coup l'an dernier. Méthode : "
         "<a class=\"lnk\" href=\"https://decupler.com/obtenir-des-avis-google/\">"
         "obtenir des avis Google</a> sans sortir du cadre autorisé."),
        ("La cohérence de vos coordonnées sur le web azuréen",
         "Nom, adresse et téléphone doivent être identiques partout — annuaires, "
         "réseaux, presse locale. Une ancienne adresse qui traîne dans dix "
         "annuaires envoie à Google un signal contradictoire. C'est le travail des "
         "<a class=\"lnk\" href=\"https://decupler.com/citations-locales/\">"
         "citations locales</a>."),
        ("Des pages par quartier, pas une page « Nice »",
         "Une seule page qui empile tous les quartiers ne se classe sur aucun. Une "
         "page par zone réelle d'intervention, avec ses repères propres, capte les "
         "requêtes « près de la gare », « Vieux-Nice », « Cimiez » que personne ne "
         "travaille sérieusement."),
        ("La citation dans les réponses IA",
         "Quand un visiteur demande à ChatGPT « un bon ostéopathe à Nice », la "
         "réponse ne cite pas dix sites : elle en cite deux ou trois. Être dans "
         "cette liste demande un contenu découpable, balisé, et des mentions hors "
         "de votre site. C'est l'objet de notre <a class=\"lnk\" "
         "href=\"https://decupler.com/mesurer-sa-visibilite/\">mesure de la visibilité IA</a>."),
    ],

    "h2_methode": "Comment on travaille sur un projet niçois ?",
    "methode_intro": "Quatre étapes, la première est gratuite et vous repartez avec "
                     "le diagnostic même si vous ne signez pas.",
    "methode": [
        ("Diagnostic local.", "On regarde votre Search Console, votre fiche "
         "d'établissement, vos avis, et les cinq concurrents niçois qui vous passent "
         "devant. On vous dit lesquels sont réellement forts et lesquels tiennent "
         "par inertie."),
        ("Fondations techniques.", "Vitesse, indexation, données structurées, "
         "maillage. Rien ne sert de produire du contenu sur un site que Google "
         "explore mal — on l'a vu chez Atoo Énergie, où 80 erreurs techniques "
         "corrigées ont suffi à débloquer la croissance."),
        ("Production et signaux locaux.", "Pages par quartier et par service, fiche "
         "d'établissement tenue, avis, citations sur les annuaires azuréens. Chaque "
         "livrable est relu par un expert avant mise en ligne."),
        ("Mesure et arbitrage.", "Un point mensuel sur données Search Console, pas "
         "sur un tableau de bord maison. On coupe ce qui ne produit rien et on "
         "renforce ce qui bouge."),
    ],
    "mock_k": "Requête posée à ChatGPT depuis Nice",
    "mock_q": "Quelle agence SEO me recommandes-tu à Nice ?",
    "mock_ans": [
        (True, "Décupler — agence SEO &amp; GEO, port Lympia"),
        (False, "Agence sans adresse vérifiable dans le 06"),
        (False, "Agence sans contenu structuré ni balisage"),
        (False, "Agence sans mentions hors de son propre site"),
    ],
    "mock_ft": "Illustration du mécanisme de sélection des sources. Ce n'est pas la "
               "capture d'une réponse réelle : les citations IA varient d'une "
               "formulation à l'autre et d'un jour à l'autre.",

    "h2_preuve": "Quels résultats, chiffres à l'appui ?",
    "preuve_intro": "Nous ne publions pas de moyenne de portefeuille. Chaque chiffre "
                    "ci-dessous renvoie à son étude de cas complète : période, "
                    "méthode, avant et après, source de mesure.",
    "preuves": [
        ("Artisanat local — Reux Travaux",
         "+450 % de clics sur la page de service stratégique en 3 mois (8 → 44), "
         "+16 % sur la page d'accueil, temps de chargement réduit de 40 %. Le cas le "
         "plus proche d'une PME niçoise de services.",
         "https://decupler.com/etude-de-cas-seo-reux-travaux/", "Lire le cas complet"),
        ("Installateur — Atoo Énergie",
         "+15 % de clics organiques en 3 mois (12 700 → 15 000/mois), CTR de 1 % à "
         "1,5 %, plus de 80 erreurs techniques corrigées. Mesuré dans Search Console.",
         "https://decupler.com/etude-de-cas-seo-atoo-energie/", "Lire le cas complet"),
        ("Dépannage — Speed Inter",
         "+46 % de clics organiques en 3 mois (331 → 485/mois), CTR de 0,61 % à "
         "0,89 %, mots-clés locaux repris un à un.",
         "https://decupler.com/etude-de-cas-seo-speed-inter/", "Lire le cas complet"),
        ("Les huit missions publiées",
         "Decathlon +140 %, Spigao +250 %, Le Point ×3,2, Double Trade +105 %, "
         "Allianz ROI ×3. Toutes chiffrées, toutes nommées.",
         "https://decupler.com/cas-clients/", "Voir tous les cas clients"),
    ],
    "preuve_note": "Mesures Google Search Console et Semrush. Les gains dépendent du "
                   "point de départ : un site à 300 clics et un site à 12 000 clics "
                   "ne progressent pas au même rythme, et nous vous le dirons avant "
                   "de signer, pas après.",

    "h2_zone": "Où intervenons-nous autour de Nice ?",
    "zone_intro": "Nos bureaux sont au port. En pratique nous couvrons Nice intra-"
                  "muros et la bande littorale des Alpes-Maritimes, avec des "
                  "déplacements sur site quand le projet le demande.",
    "zone_note": "Au-delà de cette zone, nous travaillons à distance — et nous le "
                 "disons plutôt que d'ouvrir une adresse de façade. Sur Cannes, "
                 "Antibes et Toulon nous intervenons depuis Nice.",

    "h2_budget": "Combien coûte une agence SEO à Nice ?",
    "budget_intro": "Les tarifs d'une agence niçoise sont rarement affichés. Voici "
                    "les nôtres, et les trois facteurs qui les font varier : le "
                    "nombre de pages à traiter, la difficulté des requêtes visées, "
                    "et la part de technique à reprendre.",
    "budget": [
        ("À partir de 500 € / mois",
         "SEO local : commerce, artisan, profession libérale, établissement unique à "
         "Nice. Fiche d'établissement, avis, citations, pages de service."),
        ("1 000 à 2 000 € / mois",
         "SEO B2B, SaaS, e-commerce : production de contenu régulière, technique, "
         "maillage, netlinking, suivi des citations IA."),
        ("Sur devis",
         "Multi-établissements, multilingue (anglais et italien pour la clientèle "
         "azuréenne), gros catalogue, refonte complète. Après audit, jamais avant."),
    ],
    "budget_note": "Et si après le diagnostic nous pensons que le SEO n'est pas votre "
                   "priorité du moment — parce que votre site convertit mal, ou "
                   "parce que votre marché niçois passe surtout par la "
                   "recommandation — nous vous le dirons. C'est arrivé, et c'est "
                   "moins cher pour vous qu'un an de contenu inutile.",

    "h2_variantes": "Agence SEO Nice, référencement naturel, référencement "
                    "Google : quelle différence ?",
    "variantes": [
        "Aucune, en réalité. « Agence SEO Nice », « agence de référencement "
        "naturel Nice », « agence référencement Google Nice » et « référencement de "
        "site internet Nice » désignent le même métier : faire apparaître votre "
        "site dans les résultats non payants de Google. SEO est l'acronyme anglais "
        "(<i>search engine optimization</i>), référencement naturel sa traduction "
        "française. Si vous cherchez avec l'une ou l'autre formulation, vous "
        "cherchez la même chose.",
        "La distinction utile est ailleurs : entre le <b>référencement naturel</b> "
        "(gratuit en clics, payant en travail, durable) et le <b>référencement "
        "payant</b> — Google Ads, souvent appelé SEA. Le premier construit un actif "
        "qui continue de produire quand vous arrêtez d'investir ; le second "
        "s'éteint le jour où vous coupez le budget. Les deux se complètent, et nous "
        "faisons les deux — voir l'<a class=\"lnk\" "
        "href=\"https://decupler.com/etude-de-cas-sea-allianz/\">étude de cas "
        "Allianz</a> pour la partie payante.",
        "Deuxième distinction, plus récente : entre le SEO et le <b>GEO</b>, "
        "l'optimisation pour les moteurs génératifs. Le SEO vise le lien bleu, le "
        "GEO vise la citation dans la réponse de ChatGPT ou de Perplexity. Le "
        "second s'appuie sur le premier : un site invisible sur Google a peu de "
        "chances d'être cité par une IA. Détail sur notre page "
        "<a class=\"lnk\" href=\"https://decupler.com/agence-geo/\">agence GEO</a>.",
        "Si vous cherchez un interlocuteur unique plutôt qu'une équipe, la page "
        "<a class=\"lnk\" href=\"https://decupler.com/consultant-seo-nice/\">"
        "consultant SEO à Nice</a> décrit l'accompagnement en direct avec Nathan.",
    ],

    "h2_faq": "Questions fréquentes sur le SEO à Nice",
    "faq": [
        ("Combien de temps avant de voir des résultats à Nice ?",
         "Sur des requêtes niçoises géolocalisées, la fiche d'établissement et les "
         "avis produisent un effet en <b>4 à 8 semaines</b> — c'est le levier le "
         "plus rapide du SEO local. Sur des requêtes de service concurrentielles "
         "(« avocat Nice », « dentiste Nice »), comptez <b>4 à 6 mois</b> pour un "
         "mouvement solide. Nous avons vu +450 % de clics sur une page de service en "
         "3 mois chez Reux Travaux, mais le point de départ était bas : un site déjà "
         "bien positionné progresse moins vite en pourcentage."),
        ("Vous êtes vraiment à Nice, ou c'est une adresse de domiciliation ?",
         "Vraiment à Nice. Une agence SEO Nice se vérifie à son adresse : la nôtre "
         "est au <b>10 avenue Lympia privée, 06300</b>, quartier du port. "
         "Vous pouvez venir, et nous pouvons venir chez vous. C'est aussi pour ça "
         "que nous n'avons pas ouvert de page « notre agence de Marseille » ou "
         "« notre agence de Lyon » : nous n'y avons pas de bureau, et l'écrire "
         "serait un faux signal local que Google finit par repérer."),
        ("Faut-il une page par quartier de Nice ?",
         "Seulement si vous y intervenez réellement et si la requête existe. Une "
         "page « plombier Vieux-Nice » a du sens pour un artisan qui s'y déplace "
         "vraiment ; dupliquée sur quinze quartiers avec le même texte, elle devient "
         "du contenu jumeau que Google ignore. La règle que nous appliquons : une "
         "page par zone où vous avez des clients et quelque chose de spécifique à "
         "dire."),
        ("Mes clients sont étrangers. Ça change quoi pour le référencement ?",
         "Beaucoup, et c'est propre à Nice. Un visiteur italien ou britannique "
         "n'écrit pas la traduction de votre requête française : il emploie ses "
         "propres formulations, souvent plus courtes et plus directes. Traduire "
         "votre site ne suffit donc pas — il faut refaire la recherche de mots-clés "
         "dans chaque langue, puis baliser correctement les versions "
         "(<code>hreflang</code>). C'est un chantier à part, chiffré à part."),
        ("Est-ce que l'IA rédige mes contenus ?",
         "Elle en produit la matière, un expert SEO la relit, la corrige et la "
         "valide — rien ne se publie sans cette relecture. Concrètement : six agents "
         "spécialisés prennent en charge l'analyse, les briefs, la rédaction, le "
         "maillage et la publication ; un humain décide de l'angle, coupe ce qui "
         "sonne générique et signe. C'est ce qui nous permet de produire du volume "
         "sans livrer du contenu interchangeable, que Google comme les moteurs IA "
         "apprennent justement à écarter."),
        ("Que se passe-t-il si je ne suis pas satisfait ?",
         "L'engagement est de six mois, parce que c'est le délai réel pour que le "
         "travail se voie. Si au bout de <b>trois mois</b> rien ne bouge, nous "
         "reprenons la stratégie ensemble sans frais supplémentaires. Et si un "
         "contenu ne correspond pas à vos standards, il est refait."),
    ],

    "photo_alt": "Nathan Fenina, fondateur de l'agence SEO Nice Décupler",
    "eeat": "Huit ans de SEO, plus de 70 entreprises accompagnées en SaaS, "
            "e-commerce et services B2B. Nathan dirige Décupler depuis Nice et "
            "suit personnellement les projets azuréens — c'est lui que vous aurez "
            "au premier rendez-vous, pas un commercial.",

    "final_lien": ("https://decupler.com/agence-seo/", "Notre expertise SEO"),
    "h2_final": "Trente minutes pour savoir où vous en êtes à Nice",
    "final": "Vous cherchez une agence SEO Nice et vous voulez un avis franc avant "
             "de signer quoi que ce soit ? On ouvre votre Search Console et votre "
             "fiche d'établissement, on "
             "regarde les cinq concurrents niçois qui vous passent devant, et on "
             "vous dit ce qui se joue vraiment. À nos bureaux du port ou en visio, "
             "sans engagement.",
}
