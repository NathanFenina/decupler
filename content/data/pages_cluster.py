# -*- coding: utf-8 -*-
"""Pages du cluster « avis Google » et « agents ».

Chaque page décrit ses sections : les guides (intention informationnelle) et
les pages agent (intention commerciale) n'ont pas la même architecture.
Volumes et difficultés relevés sur Ubersuggest (France, français) le
21 août 2026.
"""

RDV = 'https://calendly.com/fenina-nathan/consultationstrategique'
PILIER = 'https://decupler.com/site-internet-offert/'
MAJ = '24 août 2026'
MAJ_ISO = '2026-08-24'
IMG = 'https://decupler.com/wp-content/uploads/2026/08/'

# (slug, mot-clé, volume/mois, difficulté SEO, CPC €)
CIBLES = [
    ('supprimer-un-avis-google',  'supprimer un avis google',   1300, 15,  2.51),
    ('agent-vocal-ia',            'agent vocal ia',              320, 13, 11.18),
    ('standard-telephonique-ia',  'standard téléphonique ia',    170, 15, 39.58),
    ('repondre-aux-avis-google',  'répondre aux avis google',    110, 22,  2.02),
    ('chatbot-wordpress',         'chatbot wordpress',           110, 15,  6.80),
    ('obtenir-des-avis-google',   'obtenir des avis google',      50, 20,  3.09),
]

G_REGLES = ('https://support.google.com/business/answer/7091?hl=fr',)
G_SIGNAL = ('https://support.google.com/business/answer/4596773?hl=fr',)

SIG_AVIS = ("On gère les fiches Google et les avis d'entreprises locales, et on refuse "
            "les méthodes qui font suspendre un profil.")
SIG_AGENT = ("On construit des sites d'entreprises locales et on branche derrière les agents "
             "qui rattrapent ce que la journée fait perdre.")


PAGES = {

# ══ 1. Supprimer un avis Google — 1 300/mois, difficulté 15 ═══════════════
"supprimer-un-avis-google": dict(
    mot_cle="supprimer un avis google",
    titre_seo="Supprimer un avis Google : ce qui marche vraiment",
    meta=("Supprimer un avis Google : les motifs que Google accepte, la procédure, le recours "
          "en appel — et comment retirer un avis que vous avez laissé vous-même."),
    signature=SIG_AVIS,
    sections=[
     ('hero', dict(
       kicker="Supprimer un avis Google",
       h1="Un avis injuste ne se supprime pas parce qu'il est <em>injuste</em>.",
       leads=[
         "<strong>Google ne supprime pas un avis négatif&nbsp;: il supprime un avis qui enfreint ses règles.</strong> "
         "La nuance décide de tout. Un client mécontent qui raconte une vraie mauvaise expérience restera en ligne, "
         "quoi que vous fassiez. Un avis faux, hors sujet, injurieux ou déposé par un concurrent peut partir&nbsp;— "
         "à condition de le signaler sur le bon motif.",
         "Ce guide donne les six motifs que Google accepte, la procédure exacte, le recours quand le signalement est "
         "refusé, et les quatre méthodes qui aggravent votre cas."],
       cta="Faire auditer ma fiche Google",
       sous_cta="Gratuit · sans engagement",
       image=(IMG + 'guide-supprimer-avis.jpg',
              "Une gérante de commerce consulte son ordinateur portable, contrariée par un avis"))),

     ('reponse', dict(
       eyebrow="La réponse courte",
       h2="Google supprime-t-il un avis négatif&nbsp;?",
       reponse="Non. Google ne supprime jamais un avis au seul motif qu'il est négatif, ni parce qu'il est faux "
               "selon vous. Il supprime un avis qui enfreint ses règles sur le contenu&nbsp;: faux avis, contenu hors "
               "sujet, propos injurieux ou haineux, informations personnelles, conflit d'intérêts, ou contenu "
               "promotionnel. Le signalement passe par l'outil de gestion des avis de votre fiche d'établissement, et "
               "une décision de refus peut faire l'objet d'un appel.",
       paras=["Autrement dit&nbsp;: la question à se poser n'est pas «&nbsp;cet avis est-il mérité&nbsp;?&nbsp;» mais "
              "«&nbsp;quelle règle enfreint-il&nbsp;?&nbsp;». Si vous ne trouvez pas la règle, le signalement sera "
              "refusé, et vous aurez perdu votre seule cartouche."])),

     ('qr', dict(
       alt=True, eyebrow="En une phrase",
       h2="Les questions auxquelles vous cherchez une réponse tout de suite",
       items=[
        ("Combien de temps Google met-il à supprimer un avis&nbsp;?",
         "De quelques jours à quelques semaines. Google ne s'engage sur aucun délai et n'envoie pas toujours de "
         "notification&nbsp;: c'est l'outil de gestion des avis qui affiche l'état du signalement. Relancer ne "
         "l'accélère pas."),
        ("Combien de signalements faut-il pour faire retirer un avis&nbsp;?",
         "Aucun nombre ne déclenche une suppression. Un seul signalement bien motivé vaut mieux que trente identiques. "
         "Une vague de signalements venant de comptes liés ressemble à une manipulation, et se retourne contre le "
         "profil signalé."),
        ("Qui peut supprimer un avis Google&nbsp;?",
         "Deux personnes seulement&nbsp;: <strong>son auteur</strong>, à tout moment, depuis ses contributions&nbsp;; "
         "et <strong>Google</strong>, quand l'avis enfreint ses règles. Le propriétaire de la fiche ne le peut pas, "
         "et aucun prestataire ne le peut à sa place."),
        ("Une entreprise peut-elle faire retirer un avis qu'elle juge injuste&nbsp;?",
         "Pas au motif qu'il est injuste. Un avis négatif sincère laissé par un vrai client reste en ligne, même "
         "sévère, même exagéré. Seule une infraction aux règles de contenu ouvre un retrait."),
        ("Pourquoi un avis Google disparaît-il parfois tout seul&nbsp;?",
         "Le plus souvent parce que les filtres anti-spam de Google l'ont retiré après coup, parce que son auteur a "
         "supprimé son compte Google, ou parce que la fiche a été fusionnée avec un doublon. Un avis peut aussi "
         "revenir&nbsp;: un retrait automatique n'est pas définitif."),
        ("Peut-on supprimer seulement la photo jointe à un avis&nbsp;?",
         "Oui, une photo se signale indépendamment du texte, depuis la photo elle-même. C'est utile quand le "
         "commentaire est acceptable mais que l'image montre un salarié, une plaque d'immatriculation ou un document."),
       ])),

     ('tableau', dict(
       alt=True, eyebrow="Le tri", verdict=True,
       h2="Ce que Google retire, et ce qu'il laisse en ligne",
       paras=["Cette distinction est la seule qui compte. Ainsi, avant de signaler quoi que ce soit, situez votre avis dans "
              "la bonne colonne."],
       colonnes=["Ce qui peut être retiré", "Ce qui reste en ligne"],
       lignes=[
        ["<strong>Faux avis</strong>&nbsp;: personne qui n'a jamais été cliente, avis acheté, campagne coordonnée.",
         "<strong>Avis négatif sincère</strong> d'un vrai client, même sévère, même exagéré."],
        ["<strong>Hors sujet</strong>&nbsp;: propos sans rapport avec l'expérience vécue chez vous.",
         "<strong>Avis sans commentaire</strong>&nbsp;: une étoile seule, sans texte, n'enfreint aucune règle."],
        ["<strong>Injures, propos haineux, contenu sexuel</strong> ou violent.",
         "<strong>Désaccord sur les faits</strong>&nbsp;: votre version contre la sienne, sans preuve d'infraction."],
        ["<strong>Informations personnelles</strong>&nbsp;: nom d'un salarié, adresse, numéro, plaque.",
         "<strong>Avis ancien</strong>&nbsp;: l'ancienneté n'est pas un motif de retrait."],
        ["<strong>Conflit d'intérêts</strong>&nbsp;: avis d'un concurrent, d'un ancien salarié, de vous-même.",
         "<strong>Client difficile</strong> qui n'a pas eu gain de cause&nbsp;: ce n'est pas une infraction."],
        ["<strong>Contenu promotionnel</strong> ou spam déposé sur votre fiche.",
         "<strong>Avis sur un fait réel</strong> que vous préféreriez oublier."],
       ])),

     ('etapes', dict(
       eyebrow="La procédure", howto=True,
       h2="Comment signaler un avis, étape par étape",
       paras=["Comptez ensuite quelques jours à quelques semaines. En revanche, rien n'accélère le traitement&nbsp;: relancer ne sert à rien "
              "et signaler deux fois le même avis non plus."],
       items=[
        ("Identifiez la règle enfreinte",
         "Reprenez le tableau ci-dessus et nommez précisément l'infraction. Faites une capture d'écran de l'avis avec "
         "sa date et le pseudo de l'auteur&nbsp;: si vous devez aller plus loin, elle vous servira."),
        ("Signalez depuis l'outil de gestion des avis",
         "Depuis votre fiche d'établissement, ouvrez l'outil de gestion des avis, sélectionnez l'établissement, puis "
         "«&nbsp;Signaler un nouvel avis à supprimer&nbsp;». Choisissez le motif qui correspond exactement à "
         "l'infraction identifiée, pas celui qui vous arrange."),
        ("Suivez le statut",
         "Le même outil affiche l'état du signalement&nbsp;: décision en attente, signalement examiné, ou remonté. "
         "Un «&nbsp;examiné, aucune règle enfreinte&nbsp;» n'est pas la fin de l'histoire."),
        ("Faites appel si c'est refusé",
         "En bas de l'outil, «&nbsp;Faire appel pour les avis éligibles&nbsp;» permet de sélectionner jusqu'à dix avis "
         "et de demander un réexamen. C'est là que se gagnent la plupart des retraits obtenus&nbsp;: apportez un "
         "élément neuf, pas la même demande reformulée."),
       ])),

     ('cartes', dict(
       eyebrow="L'autre cas", id="mon-avis",
       h2="Et si c'est vous qui avez laissé l'avis&nbsp;?",
       paras=["Une bonne partie des gens qui cherchent à supprimer un avis Google cherchent à supprimer "
              "<strong>le leur</strong>&nbsp;: un coup de sang, une erreur d'établissement, un litige réglé depuis. "
              "Dans ce cas, c'est simple et immédiat&nbsp;— vous êtes la seule personne, avec Google, à pouvoir le "
              "faire. Il n'y a ni signalement, ni délai, ni justification à fournir."],
       items=[
        ("chatbot", "Sur Android",
         "Ouvrez Google Maps, touchez votre photo de profil en haut à droite, puis "
         "«&nbsp;Vos contributions&nbsp;» et l'onglet «&nbsp;Avis&nbsp;». À côté de l'avis, les trois points "
         "donnent «&nbsp;Modifier l'avis&nbsp;» et «&nbsp;Supprimer l'avis&nbsp;»."),
        ("agent-vocal", "Sur iPhone et iPad",
         "Le chemin est le même dans l'application Google Maps. Si vous passez par Safari, connectez-vous sur "
         "google.com/maps et demandez la version pour ordinateur&nbsp;: le menu mobile du navigateur n'expose pas "
         "toujours les contributions."),
        ("fiche-google", "Sur ordinateur",
         "Allez sur google.com/maps, ouvrez le menu en haut à gauche, puis «&nbsp;Vos contributions&nbsp;» et "
         "«&nbsp;Avis&nbsp;». Le menu à trois points de chaque avis contient la suppression. Vous pouvez aussi passer "
         "par votre compte Google, rubrique «&nbsp;Données et confidentialité&nbsp;»."),
        ("satisfaction", "Ce qui se passe ensuite",
         "L'avis disparaît de la fiche tout de suite, mais il peut rester visible quelques heures dans les résultats "
         "de recherche, le temps que le cache se mette à jour. La note moyenne de l'établissement, elle, est "
         "recalculée immédiatement."),
       ],
       tip="Si un commerçant vous demande de retirer votre avis en échange d'un geste commercial, sachez que vous "
           "n'y êtes pas tenu&nbsp;— et que lui n'a pas le droit de conditionner un remboursement à ce retrait.",
       tip_ic="🙋")),

     ('cartes', dict(
       alt=True, eyebrow="Les fausses pistes",
       h2="Quatre méthodes qui aggravent votre situation",
       classe='non',
       items=[
        ("demande-avis", "Acheter la suppression",
         "Des prestataires promettent de faire disparaître n'importe quel avis contre paiement. Soit ils font ce que "
         "vous pouviez faire seul, soit ils utilisent de faux signalements en masse&nbsp;— et c'est votre profil qui "
         "est sanctionné, pas le leur."),
        ("posts-google", "Noyer sous de faux avis positifs",
         "Les faux avis sont explicitement interdits par les règles de Google. Ses systèmes détectent les rafales "
         "d'avis venant d'appareils ou de comptes liés. Le résultat le plus courant n'est pas une meilleure note&nbsp;: "
         "c'est une purge qui emporte aussi vos vrais avis."),
        ("chatbot", "Répondre à chaud",
         "Une réponse agressive ou qui donne des détails sur le dossier du client fait deux dégâts&nbsp;: elle reste "
         "en ligne bien plus longtemps que l'avis, et elle est lue par tous les prospects suivants. Elle peut aussi "
         "vous exposer si elle révèle des informations sur la personne."),
        ("satisfaction", "Demander à ses proches de signaler l'avis",
         "Le nombre de signalements ne pèse pas sur la décision&nbsp;: c'est le motif qui compte. Une vague de "
         "signalements identiques ressemble surtout à une manipulation."),
       ],
       tip="La seule vraie parade contre un avis injuste qui reste en ligne, c'est le volume d'avis sincères qui "
           "l'entoure. Un avis à une étoile sur douze fait tache&nbsp;; sur cent quarante, il ne se voit plus.",
       tip_ic="⚖️",
       sources=[("règles de Google sur le contenu des avis", G_REGLES[0]),
                ("procédure de signalement des avis inappropriés", G_SIGNAL[0])])),

     ('etapes', dict(
       eyebrow="Le plan B", id="refuse",
       h2="«&nbsp;Signalement examiné, aucune règle enfreinte&nbsp;»&nbsp;: la suite",
       paras=["C'est la réponse la plus fréquente, et c'est là que la plupart des gens abandonnent. Il reste pourtant "
              "quatre choses à faire, dans cet ordre&nbsp;— chacune coûte plus cher que la précédente, alors ne "
              "sautez pas d'étape."],
       items=[
        ("Faites appel avec un élément neuf",
         "L'appel n'est pas une deuxième chance sur le même dossier&nbsp;: reformuler la même demande donne le même "
         "refus. Ce qui fait bouger un réexamen, c'est une preuve que vous n'aviez pas jointe&nbsp;— l'absence de "
         "l'auteur dans votre fichier client, la date de son avis comparée à celle de votre fermeture annuelle, une "
         "capture de son profil montrant dix avis à une étoile déposés le même jour dans votre secteur."),
        ("Reprenez contact avec l'auteur",
         "Quand le litige est réglé, un client satisfait retire souvent son avis de lui-même&nbsp;: c'est la voie la "
         "plus rapide et la seule qui soit à 100&nbsp;% entre vos mains. Écrivez-lui hors de la fiche, réglez le "
         "fond, et demandez le retrait sans le conditionner à un geste commercial&nbsp;— une contrepartie explicite "
         "vous exposerait."),
        ("Notifiez l'hébergeur si le contenu est manifestement illicite",
         "Google est hébergeur au sens de la loi pour la confiance dans l'économie numérique du 21&nbsp;juin 2004. "
         "Une notification en bonne et due forme, avec les mentions exigées par son article&nbsp;6, fait courir sa "
         "responsabilité s'il laisse en ligne un contenu manifestement illicite. Ce n'est pas le même canal que le "
         "signalement&nbsp;: c'est une mise en demeure, et elle se rédige avec un avocat."),
        ("Passez au juge, ou arrêtez",
         "Le référé permet de faire cesser un trouble manifestement illicite en quelques semaines. C'est efficace et "
         "coûteux. En dessous d'un certain enjeu, la réponse honnête est d'arrêter là et de basculer le budget sur ce "
         "qui fait vraiment baisser le poids d'un avis&nbsp;: le volume d'avis sincères qui arrivent après."),
       ])),

     ('texte', dict(
       alt=True, eyebrow="Les disparitions",
       h2="Pourquoi un avis disparaît sans que personne ne l'ait signalé",
       paras=[
        "Il arrive qu'un avis s'efface tout seul, en bien comme en mal&nbsp;: le mauvais avis que vous guettiez "
        "s'évapore, ou dix bons avis manquent à l'appel un lundi matin. Ce n'est presque jamais une décision humaine.",
        "<strong>Les filtres automatiques</strong> passent après coup&nbsp;: Google analyse en continu les schémas de "
        "dépôt et retire rétroactivement ce qu'il classe comme faux ou coordonné. C'est la cause la plus fréquente, "
        "et c'est aussi celle qui emporte de vrais avis au passage&nbsp;— typiquement quand plusieurs clients ont "
        "laissé leur avis depuis le même réseau Wi-Fi, dans la même heure, sur une tablette de l'accueil.",
        "<strong>Le compte de l'auteur a été supprimé.</strong> Un compte Google fermé emporte ses contributions. "
        "L'avis disparaît sans que rien n'ait été signalé, et il ne reviendra pas.",
        "<strong>La fiche a bougé.</strong> Une fusion de doublons, un changement de catégorie, une adresse modifiée, "
        "une suspension temporaire du profil&nbsp;: chacun de ces mouvements peut faire disparaître des avis, parfois "
        "le temps de la vérification seulement.",
        "Un point important&nbsp;: <strong>un retrait automatique n'est pas définitif</strong>. Un avis filtré peut "
        "revenir si l'algorithme se ravise. Ne comptez donc pas une disparition comme un dossier clos, et ne "
        "reconstruisez pas votre moyenne sur un avis qui n'est peut-être parti que pour quinze jours."],
       tip="Si vous perdez plusieurs avis d'un coup, vérifiez d'abord que votre fiche n'a pas été fusionnée avec un "
           "doublon&nbsp;: c'est l'explication la plus courante, et la plus réparable.",
       tip_ic="🔍")),

     ('texte', dict(
       eyebrow="Le recours juridique",
       h2="Le recours juridique, et sa fenêtre de trois mois",
       paras=[
        "Un avis peut sortir du champ de la critique et tomber dans le <strong>dénigrement</strong> (propos qui "
        "jettent le discrédit sur vos produits ou services) ou la <strong>diffamation</strong> (imputation d'un fait "
        "précis portant atteinte à l'honneur). Ce sont deux qualifications différentes, avec deux régimes différents.",
        "D'abord, le point à connaître&nbsp;: <strong>l'action en diffamation se prescrit par trois mois à compter "
        "de la publication</strong>, en application de la loi du 29 juillet 1881 sur la liberté de la presse. Passé ce "
        "délai, la voie est fermée. C'est court, et c'est la raison pour laquelle un avis manifestement diffamatoire "
        "se traite tout de suite, pas «&nbsp;quand on aura le temps&nbsp;».",
        "Le dénigrement, lui, relève de la responsabilité civile de droit commun&nbsp;: article&nbsp;1240 du code "
        "civil, et une prescription de cinq ans. C'est une différence décisive&nbsp;— un avis qui dénigre vos "
        "prestations sans imputer de fait précis reste attaquable longtemps après qu'un avis diffamatoire soit devenu "
        "intouchable. La qualification n'est donc pas un détail de vocabulaire&nbsp;: elle décide de la porte qui "
        "vous reste ouverte.",
        "Concrètement, la séquence est toujours la même. <strong>Faites constater</strong> l'avis&nbsp;: capture "
        "horodatée avec l'URL complète, et constat de commissaire de justice si l'enjeu le justifie&nbsp;— une "
        "capture d'écran seule se conteste facilement. <strong>Mettez en demeure</strong>, l'auteur s'il est "
        "identifiable, l'hébergeur sinon. Puis <strong>choisissez la voie</strong>&nbsp;: le référé pour faire "
        "retirer vite, le fond pour obtenir des dommages et intérêts.",
        "Un mot sur l'anonymat, parce que c'est la question qui bloque tout le monde&nbsp;: un pseudonyme n'empêche "
        "pas d'agir. Le juge peut ordonner à l'hébergeur de communiquer les données d'identification de l'auteur. "
        "C'est une procédure de plus, donc du temps et de l'argent, mais ce n'est pas une impasse.",
        "Nous ne sommes pas juristes et cette page ne remplace pas une consultation. Elle sert à ce que vous ne "
        "découvriez pas le délai de trois mois au quatrième."],
       tip="Dans l'immense majorité des cas, l'avis qui vous ronge n'est ni diffamatoire ni supprimable. Il est "
           "simplement mal placé dans une liste trop courte. Le travail utile est ailleurs&nbsp;: en faire arriver "
           "d'autres.",
       tip_ic="📌")),

     ('texte', dict(
       alt=True, eyebrow="Le marché parallèle", id="prestataires",
       h2="Ce que vendent vraiment les services de suppression d'avis",
       paras=[
        "Tapez la requête et vous tomberez sur une dizaine de sites qui promettent de faire disparaître n'importe "
        "quel avis, au forfait ou au résultat. Il faut savoir ce que vous achetez, parce qu'aucun d'eux ne dispose "
        "d'un canal que vous n'auriez pas&nbsp;: <strong>seul Google décide</strong>, et il ne vend pas cet accès.",
        "Dans le meilleur des cas, le prestataire fait à votre place ce que décrit cette page&nbsp;: il qualifie "
        "l'infraction, signale proprement, fait appel avec un dossier. C'est un vrai travail, il peut le facturer, "
        "et le taux de réussite reste celui de la procédure officielle.",
        "Dans le pire, il déclenche des signalements en masse depuis des comptes fabriqués, ou compense en faisant "
        "déposer de faux avis positifs. Les deux enfreignent les règles de Google, et la sanction ne tombe pas sur "
        "le prestataire&nbsp;: elle tombe sur votre fiche, jusqu'à la suspension du profil et la perte de tous les "
        "avis accumulés.",
        "Il y a aussi un risque que peu de gens mesurent&nbsp;: faire publier de faux avis est une "
        "<strong>pratique commerciale trompeuse</strong>, punie par l'article&nbsp;L132-2 du code de la consommation "
        "de deux ans d'emprisonnement et 300&nbsp;000&nbsp;euros d'amende, montant pouvant être porté à un "
        "pourcentage du chiffre d'affaires. Le donneur d'ordre est l'entreprise, pas l'agence.",
        "La question à poser à un prestataire tient en une phrase&nbsp;: «&nbsp;par quel canal signalez-vous, et "
        "que se passe-t-il si Google refuse&nbsp;?&nbsp;» Une réponse qui parle de contacts internes chez Google est "
        "une réponse qui devrait mettre fin à la conversation."],
       tip="Une promesse de résultat sur une suppression d'avis est, en soi, un signal d'alarme&nbsp;: personne ne "
           "peut garantir une décision qui n'est pas la sienne.",
       tip_ic="🚩")),

     ('visuel', dict(
       eyebrow="Le seul levier qui tient", viz='capitalise',
       h2="Un avis pèse ce que pèse le silence autour de lui",
       paras=["Un avis à une étoile sur douze commande la lecture. Sur cent quarante, il devient une ligne parmi "
              "d'autres, et le prospect regarde la moyenne. Vous ne pouvez pas décider du sort d'un avis&nbsp;; vous "
              "décidez du nombre d'avis qui arrivent après lui, et de la vitesse à laquelle ils arrivent.",
              "C'est la seule variable de cette page que vous contrôlez entièrement, et c'est aussi la seule qui "
              "continue de produire de l'effet une fois le litige oublié."])),

     ('agents', dict(
       alt=True, eyebrow="Ce qu'on met en place",
       h2="Ce qui protège vraiment une fiche Google",
       paras=["On ne vend pas de suppression d'avis. On branche les mécaniques qui font qu'un mauvais avis pèse moins, "
              "et qu'on le voit venir avant qu'il ne soit écrit. Le catalogue complet est sur la "
              f"<a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["satisfaction", "demande-avis", "reponse-avis", "fiche-google"])),

     ('relance', dict(
       texte="On regarde votre fiche ensemble, avis compris, et je vous dis franchement ce qui est récupérable.",
       libelle="Prendre 15 minutes")),

     ('faq', dict(
       eyebrow="FAQ", h2="Les questions qu'on nous pose",
       items=[
        ("Combien de temps Google met-il à traiter un signalement&nbsp;?",
         "De quelques jours à quelques semaines, sans engagement de délai. L'outil de gestion des avis affiche l'état "
         "d'avancement&nbsp;: décision en attente, signalement examiné, ou remonté en appel. Relancer n'accélère rien."),
        ("Puis-je supprimer un avis Google moi-même&nbsp;?",
         "Vous ne pouvez pas supprimer un avis déposé par quelqu'un d'autre&nbsp;: seuls son auteur et Google le "
         "peuvent. Vous pouvez le signaler, faire appel d'un refus, et demander à l'auteur de le retirer lui-même — "
         "ce qui reste, quand le litige est réglé, la voie la plus rapide."),
        ("Un avis sans commentaire, juste une étoile, peut-il être retiré&nbsp;?",
         "Non, sauf s'il provient d'un faux compte ou d'une personne en conflit d'intérêts. Une note seule n'enfreint "
         "aucune règle de contenu&nbsp;: il n'y a pas de contenu à incriminer."),
        ("Est-ce que je peux demander à mes clients contents de laisser un avis pour compenser&nbsp;?",
         "Oui, à condition de le demander à <strong>tous</strong> vos clients. Google interdit explicitement de trier "
         "les clients selon leur satisfaction avant de les envoyer sur la fiche, et sanctionne cette pratique "
         "jusqu'à la suspension du profil. Demander à tout le monde est autorisé&nbsp;; filtrer ne l'est pas."),
        ("Que faire pendant que le signalement est en cours&nbsp;?",
         "Répondez à l'avis, calmement et brièvement, sans détailler le dossier. Cette réponse est lue par tous les "
         "prospects suivants&nbsp;: c'est elle qui décide de l'effet réel de l'avis, bien plus que sa présence."),
        ("Mon signalement est refusé et l'appel aussi. C'est vraiment fini&nbsp;?",
         "Pour la voie Google, oui. Il reste la notification à l'hébergeur si le contenu est manifestement illicite, "
         "et le juge si l'avis est diffamatoire — dans les trois mois — ou dénigrant. En dessous de cet enjeu, la "
         "suite utile n'est plus juridique&nbsp;: <a href=\"#refuse\">c'est le plan B</a>."),
        ("Mon propre avis a été supprimé par Google, pourquoi&nbsp;?",
         "Le plus souvent parce que les filtres l'ont classé comme suspect&nbsp;: compte récent, avis déposé depuis "
         "le même réseau qu'un autre, texte proche d'un avis existant, ou lien commercial supposé avec "
         "l'établissement. Vous pouvez le republier, mais un deuxième retrait est probable si la cause n'a pas changé."),
        ("Puis-je modifier mon avis au lieu de le supprimer&nbsp;?",
         "Oui, et c'est souvent préférable&nbsp;: un avis modifié conserve son ancienneté et remplace le texte "
         "précédent. Le chemin est le même que pour la suppression&nbsp;— vos contributions, l'onglet avis, puis "
         "«&nbsp;Modifier l'avis&nbsp;»."),
        ("Un concurrent a laissé un faux avis. Qu'est-ce qui marche&nbsp;?",
         "Le conflit d'intérêts est un motif de retrait explicite dans les règles de Google, et c'est l'un des mieux "
         "traités&nbsp;— à condition de le prouver. Signalez sur ce motif précis, et joignez ce qui rend le lien "
         "visible&nbsp;: le profil de l'auteur, les autres avis qu'il a déposés dans votre secteur, les dates."),
        ("Vous proposez un service de suppression d'avis&nbsp;?",
         "Non, et méfiez-vous de ceux qui le proposent. On travaille sur ce qui est autorisé et durable&nbsp;: une "
         "fiche complète, un flux d'avis sincères, des réponses systématiques, et une alerte quand un client repart "
         "mécontent."),
       ])),
    ]),

# ══ 2. Répondre aux avis Google — 110/mois, difficulté 22 ═════════════════
"repondre-aux-avis-google": dict(
    mot_cle="répondre aux avis google",
    titre_seo="Répondre aux avis Google : la méthode et 6 exemples",
    meta=("Répondre aux avis Google, positifs comme négatifs : la méthode en 4 temps, 6 exemples de "
          "réponses à copier, et quoi faire quand le bouton n'apparaît pas."),
    signature=SIG_AVIS,
    sections=[
     ('hero', dict(
       kicker="Répondre aux avis Google",
       h1="Votre réponse est lue <em>plus</em> que l'avis auquel elle répond.",
       leads=[
         "<strong>Répondre aux avis Google n'est pas un exercice de politesse&nbsp;: c'est de la vente.</strong> "
         "Le prospect qui lit un avis à une étoile ne cherche pas à savoir qui a raison. Il cherche à savoir comment "
         "vous réagissez quand quelque chose se passe mal — parce que ça lui arrivera peut-être.",
         "Une réponse posée sous un avis sévère convertit mieux qu'une fiche sans aucun avis négatif. Voici la "
         "structure qui marche, et les quatre erreurs qui transforment un incident en dossier."],
       cta="Faire auditer ma fiche Google",
       sous_cta="Gratuit · sans engagement",
       image=(IMG + 'guide-repondre-avis.jpg',
              "Un restaurateur répond posément aux avis depuis le comptoir de son établissement fermé"))),

     ('reponse', dict(
       eyebrow="La réponse courte",
       h2="Faut-il répondre à tous les avis Google&nbsp;?",
       reponse="Oui, aux positifs comme aux négatifs, et sans délai excessif. Répondre montre à vos futurs clients "
               "que quelqu'un est présent derrière la fiche, et une fiche dont tous les avis reçoivent une réponse "
               "inspire davantage confiance qu'une fiche mieux notée mais muette. Sur un avis négatif, la réponse est "
               "courte, factuelle, sans détailler le dossier, et propose de poursuivre hors ligne.",
       paras=["Un point souvent mal compris&nbsp;: la réponse n'a pas pour cible l'auteur de l'avis. Il a déjà son "
              "opinion. Elle a pour cible les dizaines de personnes qui liront l'échange dans les mois qui viennent."])),

     ('etapes', dict(howto=True, id="methode", 
       alt=True, eyebrow="La structure",
       h2="Une réponse à un avis négatif tient en quatre temps",
       paras=["Cinq lignes maximum. Au-delà, on lit un plaidoyer, et un plaidoyer donne raison à l'autre."],
       items=[
        ("Remercier, sans ironie",
         "«&nbsp;Merci d'avoir pris le temps de nous écrire&nbsp;». Cette première ligne n'est pas de la politesse "
         "vide&nbsp;: elle installe le ton pour tout ce qui suit et désamorce la lecture en mode conflit."),
        ("Reconnaître ce qui est vrai",
         "Il y a presque toujours un élément exact dans un avis négatif&nbsp;: le délai, l'attente, un manque "
         "d'information. Le reconnaître explicitement vous crédibilise plus que n'importe quelle justification, et "
         "coupe court à la surenchère."),
        ("Donner un fait, pas une défense",
         "Une phrase factuelle suffit&nbsp;: ce qui s'est passé, ou ce qui a changé depuis. Sans détailler le dossier "
         "du client, sans le contredire point par point, et sans révéler la moindre information sur lui."),
        ("Proposer de continuer ailleurs",
         "«&nbsp;Appelez-nous au 01&nbsp;xx, on regarde ça ensemble&nbsp;». Ça clôt l'échange public, ça montre que "
         "vous ne fuyez pas, et ça laisse une porte ouverte à une modification de l'avis par son auteur — la seule "
         "façon rapide de le voir disparaître."),
       ])),

     ('qr', dict(
       alt=True, eyebrow="En une phrase",
       h2="Ce que les gérants nous demandent avant de se lancer",
       items=[
        ("Faut-il répondre à tous les avis Google&nbsp;?",
         "Oui, aux négatifs comme aux positifs. Google indique lui-même que répondre aux avis améliore la visibilité "
         "locale, et un profil où le gérant répond systématiquement rassure davantage qu'un profil sans une seule "
         "réponse, quelle que soit la note."),
        ("Sous quel délai faut-il répondre&nbsp;?",
         "Sous 48&nbsp;heures pour un avis négatif, une semaine pour les autres. Passé un mois, la réponse ne sert "
         "plus le client qui l'a écrit&nbsp;— elle sert encore les prospects qui liront la fiche, donc elle vaut "
         "toujours d'être écrite."),
        ("Qui peut répondre aux avis d'une fiche&nbsp;?",
         "Seuls les comptes ayant le rôle propriétaire ou gestionnaire sur la fiche d'établissement. Un employé "
         "connecté à son compte Google personnel ne verra pas le bouton, même sur place et même sur le bon appareil."),
        ("Peut-on modifier ou supprimer une réponse déjà publiée&nbsp;?",
         "Oui, à tout moment et sans limite. C'est une différence importante avec l'avis lui-même&nbsp;: une réponse "
         "écrite à chaud se corrige, et il vaut mieux la corriger tard que la laisser."),
        ("Pourquoi le bouton «&nbsp;Répondre&nbsp;» n'apparaît-il pas&nbsp;?",
         "Trois causes, dans l'ordre de fréquence&nbsp;: la fiche n'est pas vérifiée, l'avis se trouve sur une fiche "
         "en doublon dont vous n'êtes pas gestionnaire, ou votre compte n'a pas les droits. Une fiche suspendue "
         "bloque également les réponses."),
        ("Peut-on répondre aux avis avec une IA&nbsp;?",
         "Rien ne l'interdit, et Google propose lui-même des suggestions de réponse. Ce qui se voit et se retourne "
         "contre vous, c'est la réponse générique&nbsp;: quatre avis différents qui reçoivent la même formule, "
         "lisibles à la suite sur la même fiche."),
       ])),

     ('cartes', dict(
       eyebrow="Les erreurs",
       h2="Quatre réponses qui font plus de dégâts que l'avis",
       classe='non',
       items=[
        ("chatbot", "Contredire point par point",
         "Reprendre chaque phrase pour la réfuter donne à l'échange l'allure d'une dispute, et à vous celle de "
         "quelqu'un qui a besoin d'avoir raison. Le lecteur ne tranche pas&nbsp;: il passe au concurrent suivant."),
        ("satisfaction", "Donner des détails sur le client",
         "«&nbsp;Vous êtes arrivé avec 40 minutes de retard et vous n'aviez pas votre ordonnance&nbsp;» : même quand "
         "c'est vrai, ça se retourne toujours contre vous, et selon votre métier ça peut vous exposer bien au-delà "
         "de l'image."),
        ("posts-google", "Copier-coller la même réponse partout",
         "Dix avis positifs qui reçoivent le même «&nbsp;Merci beaucoup pour votre retour&nbsp;!&nbsp;» se voient au "
         "premier coup d'œil et annulent l'effet recherché. Deux mots repris de l'avis suffisent à personnaliser."),
        ("reponse-avis", "Répondre trois mois plus tard",
         "Une réponse tardive sous un avis négatif ressemble à une réaction de crise. Sous un avis positif, elle ne "
         "sert plus à rien&nbsp;: le client a tourné la page."),
       ],
       tip="Sur un avis positif, la réponse la plus utile n'est pas «&nbsp;merci&nbsp;» : c'est une phrase qui reprend "
           "la prestation citée. Elle ajoute du vocabulaire réel à votre fiche, celui que vos futurs clients tapent.",
       tip_ic="💡")),

     ('cartes', dict(
       alt=True, eyebrow="Le blocage", id="ou-repondre",
       h2="Où répondre&nbsp;— et pourquoi le bouton n'apparaît pas",
       paras=["On répond depuis la fiche d'établissement, jamais depuis Google Maps en tant que simple visiteur. "
              "Sur ordinateur, cherchez votre entreprise dans Google en étant connecté au bon compte&nbsp;: le "
              "panneau de gestion s'affiche directement dans les résultats, avec l'onglet «&nbsp;Avis&nbsp;». Sur "
              "mobile, l'application Google Maps expose la même chose dans l'onglet «&nbsp;Entreprise&nbsp;». Si le "
              "bouton reste introuvable, c'est l'une de ces quatre raisons."],
       items=[
        ("fiche-google", "La fiche n'est pas vérifiée",
         "Tant que la validation n'est pas allée à son terme, la fiche existe pour les visiteurs mais vous n'en êtes "
         "pas officiellement gestionnaire. Vous voyez les avis, vous ne pouvez pas y répondre. C'est la cause "
         "numéro un, et la plus longue à corriger."),
        ("citations-locales", "L'avis est sur un doublon",
         "Une même entreprise peut exister deux fois&nbsp;: ancienne adresse, ancienne raison sociale, fiche créée "
         "par un tiers. Les avis se répartissent entre les deux, et vous ne gérez que l'une. Demandez la fusion "
         "plutôt que de créer une troisième fiche."),
        ("messagerie-google", "Votre compte n'a pas les droits",
         "Seuls les rôles propriétaire et gestionnaire peuvent répondre. Un salarié ajouté en simple accès, ou "
         "connecté à son compte personnel, ne verra rien. Vérifiez avec quel compte vous êtes connecté avant de "
         "chercher plus loin&nbsp;: c'est l'erreur la plus fréquente, et la plus vite réglée."),
        ("reponse-avis", "La fiche est suspendue",
         "Une suspension gèle tout&nbsp;: réponses, modifications, photos. Elle fait souvent suite à un changement "
         "d'informations massif, à une catégorie interdite, ou à une vague d'avis jugée suspecte. Il faut demander "
         "le rétablissement avant de pouvoir répondre à quoi que ce soit."),
       ],
       tip="Un avis qui date de plus de trois ans reste répondable&nbsp;: il n'y a pas de délai de forclusion. Si "
           "vous reprenez une fiche laissée à l'abandon, commencez par les avis les plus lus, pas les plus récents.",
       tip_ic="🔑")),

     ('texte', dict(
       eyebrow="Le vrai enjeu", id="pourquoi",
       h2="À qui s'adresse vraiment une réponse",
       paras=[
        "L'erreur de cadrage la plus courante&nbsp;: écrire à la personne qui a laissé l'avis. Elle est déjà partie, "
        "elle a dit ce qu'elle avait à dire, et dans la plupart des cas elle ne reviendra pas lire. "
        "<strong>Votre réponse est écrite pour les gens qui liront cette fiche dans six mois.</strong> Ce sont eux "
        "qui décideront d'appeler ou pas.",
        "Ça change tout à la manière d'écrire. Un prospect qui tombe sur un avis à une étoile ne cherche pas à savoir "
        "qui avait raison&nbsp;— il cherche à savoir ce qui se passe quand ça se passe mal chez vous. La réponse "
        "lui donne exactement cette information. Un gérant qui reconnaît, explique et propose une solution vaut mieux "
        "qu'un gérant sans un seul avis négatif&nbsp;: le premier a été mis à l'épreuve, le second est une inconnue.",
        "Google, de son côté, indique dans sa documentation que répondre aux avis contribue à la visibilité locale, "
        "au même titre que la complétude de la fiche et la régularité de l'activité. On ne connaît pas le poids exact "
        "de ce signal, et personne ne le connaît&nbsp;— méfiez-vous de qui vous annonce un pourcentage. Ce qu'on "
        "observe en revanche sur les fiches qu'on gère, c'est qu'une fiche où le gérant répond systématiquement "
        "reçoit des avis plus longs et plus détaillés&nbsp;: les gens écrivent davantage quand ils savent qu'on lit.",
        "Le corollaire est désagréable&nbsp;: <strong>répondre à un avis sur trois est pire que ne jamais "
        "répondre</strong>. Une fiche où seuls les avis positifs ont une réponse raconte au lecteur exactement ce "
        "que vous n'aviez pas prévu de lui dire."],
       tip="Si vous devez choisir par manque de temps, répondez aux avis à deux et trois étoiles avant les autres. "
           "Ce sont ceux que les prospects lisent en premier pour se faire une idée&nbsp;: ni dithyrambe, ni "
           "règlement de comptes.",
       tip_ic="🎯")),

     ('tableau', dict(
       eyebrow="Les modèles", id="exemples",
       h2="Six situations, et ce que vous écrivez dans chacune",
       paras=["Ces réponses sont courtes volontairement. Une réponse longue à un avis négatif donne du poids à "
              "l'avis&nbsp;: le lecteur y passe plus de temps, et vous avez l'air de vous justifier. Remplacez ce qui "
              "est entre crochets, et rien d'autre."],
       colonnes=["La situation", "Ce que vous écrivez"],
       lignes=[
        ["<strong>Avis négatif justifié</strong>&nbsp;— le client a raison, vous le savez.",
         "«&nbsp;Bonjour [prénom], vous avez raison et je suis désolé pour [le fait précis]. Nous avons changé "
         "[ce qui a changé] depuis. Si vous voulez qu'on répare ça, je suis joignable au [numéro].&nbsp;»"],
        ["<strong>Avis négatif injuste</strong>&nbsp;— votre version diffère de la sienne.",
         "«&nbsp;Bonjour [prénom], notre relevé indique [le fait, sans polémique]. Je comprends que l'expérience "
         "vous ait déçu. Appelez-moi au [numéro], je reprends le dossier avec vous.&nbsp;» Aucune contradiction "
         "frontale&nbsp;: le lecteur tranche, pas vous."],
        ["<strong>Avis d'une personne qui n'est pas cliente.</strong>",
         "«&nbsp;Bonjour, nous ne retrouvons pas de passage à votre nom dans nos dossiers. Il s'agit peut-être d'une "
         "confusion d'établissement. Écrivez-nous à [adresse], nous vérifierons ensemble.&nbsp;» Signalez en "
         "parallèle&nbsp;: la réponse ne remplace pas le signalement."],
        ["<strong>Avis à trois étoiles</strong>&nbsp;— ni bon ni mauvais, souvent ignoré.",
         "«&nbsp;Merci [prénom]. Vous avez apprécié [ce qui est cité], et il manquait [ce qui est reproché]&nbsp;: "
         "c'est noté. Dites-nous si [action corrective] vous conviendrait mieux la prochaine fois.&nbsp;»"],
        ["<strong>Avis positif détaillé</strong>&nbsp;— le plus rentable, et le plus bâclé.",
         "«&nbsp;Merci [prénom]. [Le collaborateur cité] sera content de le lire. Au plaisir pour "
         "[la prochaine prestation].&nbsp;» Reprenez un mot de l'avis&nbsp;: c'est ce qui prouve que vous l'avez lu."],
        ["<strong>Cinq étoiles sans commentaire.</strong>",
         "«&nbsp;Merci pour ces cinq étoiles. Si vous avez deux minutes pour dire ce qui vous a plu, ça aide "
         "beaucoup les personnes qui hésitent.&nbsp;» Une note seule pèse peu&nbsp;; un texte pèse."],
       ])),

     ('texte', dict(
       eyebrow="L'IA dans la boucle", id="ia",
       h2="Répondre avec une IA&nbsp;: ce qui marche, et ce qui se voit",
       paras=[
        "La question revient à chaque rendez-vous, et la réponse honnête n'est ni oui ni non. Rien n'interdit "
        "d'utiliser un modèle pour rédiger une réponse&nbsp;— Google propose lui-même des suggestions dans son "
        "interface. Ce qui pose problème, c'est la manière.",
        "<strong>Ce qui se voit immédiatement</strong>&nbsp;: la réponse qui commence par «&nbsp;Nous vous "
        "remercions chaleureusement pour votre retour&nbsp;» quatre fois de suite sur la même page. Un visiteur qui "
        "fait défiler vos avis lit vos réponses à la file. La répétition est le seul indice dont il a besoin, et "
        "elle transforme une preuve d'attention en preuve d'automatisme.",
        "<strong>Ce qui marche</strong>&nbsp;: donner au modèle ce qu'il ne peut pas deviner. Le nom du "
        "collaborateur concerné, la date du passage, ce qui a été corrigé depuis, votre façon de parler. Une réponse "
        "générée qui cite un fait vérifiable ne ressemble plus à une réponse générée&nbsp;— parce qu'elle n'en est "
        "plus vraiment une.",
        "<strong>Ce qu'on ne délègue jamais</strong>&nbsp;: l'avis négatif sérieux, celui qui touche à la sécurité, "
        "à la santé, à l'argent ou à une personne nommée. Là, une formule polie mais à côté de la plaque coûte plus "
        "cher que l'avis. Notre règle chez Décupler est simple&nbsp;: l'IA propose sur les positifs et les tièdes, "
        "un humain écrit les négatifs.",
        "Un dernier point, souvent oublié&nbsp;: ne mettez jamais dans une réponse publique une information que le "
        "client ne vous a pas donnée publiquement. Son numéro de dossier, son adresse, le détail de son "
        "intervention. Vous répondez à une personne devant tout le monde."],
       tip="Test simple avant de publier&nbsp;: relisez vos six dernières réponses à la suite. Si elles pourraient "
           "être interverties sans que rien ne cloche, elles ne disent rien.",
       tip_ic="🪞")),

     ('agents', dict(
       alt=True, eyebrow="Ce qu'on met en place",
       h2="Répondre systématiquement, sans y passer vos soirées",
       paras=["Le problème n'est pas de savoir répondre&nbsp;: c'est de le faire à chaque fois, dans la semaine, "
              "pendant deux ans. C'est exactement ce qu'un agent fait bien. Le catalogue complet est sur la "
              f"<a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["reponse-avis", "satisfaction", "demande-avis"])),

     ('relance', dict(
       texte="On regarde vos avis et vos réponses ensemble, et je vous dis ce qui se joue vraiment sur votre fiche.",
       libelle="Prendre 15 minutes")),

     ('faq', dict(
       eyebrow="FAQ", h2="Les questions qu'on nous pose",
       items=[
        ("Peut-on répondre à un avis Google depuis un téléphone&nbsp;?",
         "Oui, dans l'application Google Maps, onglet «&nbsp;Entreprise&nbsp;» puis «&nbsp;Avis&nbsp;», avec le "
         "compte gestionnaire. C'est le plus rapide au quotidien&nbsp;— mais écrivez les réponses délicates sur un "
         "clavier d'ordinateur, on se relit mieux."),
        ("Que répondre à un avis positif qui n'a pas de texte&nbsp;?",
         "Remerciez en une ligne et demandez deux mots. Une note seule pèse peu dans la décision d'un prospect&nbsp;: "
         "c'est le texte qu'on lit. Votre réponse est la seule occasion polie de le demander."),
        ("Combien de temps la réponse met-elle à s'afficher&nbsp;?",
         "Quelques minutes en général, parfois quelques heures. Si elle n'apparaît toujours pas au bout d'un jour, "
         "vérifiez qu'elle ne contient pas de numéro de téléphone ou de lien&nbsp;: c'est ce qui déclenche le plus "
         "souvent un filtrage."),
        ("Faut-il répondre à un avis manifestement faux, ou seulement le signaler&nbsp;?",
         "Les deux, et dans cet ordre&nbsp;: signalez d'abord, répondez ensuite. Le signalement peut échouer&nbsp;; "
         "la réponse, elle, sera lue quoi qu'il arrive. Restez factuel et court&nbsp;— accuser publiquement l'auteur "
         "d'être un faux client se retourne contre vous s'il ne l'est pas."),
        ("Répondre aux avis améliore-t-il mon référencement local&nbsp;?",
         "Google indique que répondre aux avis contribue à la confiance accordée à un établissement, et une fiche "
         "active envoie un signal de vitalité. Ne comptez pas dessus comme sur un levier de position&nbsp;: comptez "
         "dessus comme sur un levier de conversion, qui est mesurable et immédiat."),
        ("Dois-je répondre aux avis à une étoile sans commentaire&nbsp;?",
         "Oui, en une ligne&nbsp;: «&nbsp;Nous ne retrouvons pas votre passage, écrivez-nous pour qu'on comprenne ce "
         "qui s'est passé.&nbsp;» Ça montre au lecteur suivant que la note isolée n'a jamais été explicitée."),
        ("Puis-je demander à un client de modifier son avis&nbsp;?",
         "Oui, si le litige a été réglé. Un client dont le problème a été résolu modifie souvent son avis "
         "spontanément&nbsp;— c'est de loin la voie la plus rapide, puisque son auteur est la seule personne, avec "
         "Google, à pouvoir le retirer. Ce qui est interdit, c'est de lui offrir une contrepartie."),
        ("Et si l'avis est manifestement faux&nbsp;?",
         "Répondez quand même, brièvement et sans accusation, puis signalez-le. Voir notre guide sur "
         "<a href=\"https://decupler.com/supprimer-un-avis-google/\">la suppression d'un avis Google</a> pour les "
         "motifs que Google accepte et la procédure."),
        ("Une IA peut-elle répondre à ma place&nbsp;?",
         "Pour les avis positifs, oui, et le gain de temps est réel. Pour les négatifs, l'agent rédige une proposition "
         "et vous alerte&nbsp;: c'est vous qui validez. Une réponse automatique sous un avis grave se voit, et se paie."),
        ("Combien de temps pour répondre&nbsp;?",
         "Dans la semaine pour les avis positifs, sous 48 heures pour les négatifs. Un avis négatif sans réponse "
         "pendant un mois est lu comme un aveu."),
       ])),
    ]),

# ══ 3. Obtenir des avis Google — 50/mois, difficulté 20 ═══════════════════
"obtenir-des-avis-google": dict(
    mot_cle="obtenir des avis google",
    titre_seo="Obtenir des avis Google : la méthode qui reste autorisée",
    meta=("Obtenir des avis Google sans se faire suspendre : ce que Google interdit depuis 2026, "
          "le bon moment pour demander, et la mécanique qui tient dans la durée."),
    signature=SIG_AVIS,
    sections=[
     ('hero', dict(
       kicker="Obtenir des avis Google",
       h1="Vos clients sont contents.<br>Ils ne l'écrivent <em>nulle part</em>.",
       leads=[
         "<strong>Obtenir des avis Google ne tient pas à une astuce&nbsp;: ça tient à demander, à tout le monde, au "
         "bon moment.</strong> La plupart des entreprises locales ont des centaines de clients satisfaits et une "
         "poignée d'avis. La raison est presque toujours la même&nbsp;: personne n'a jamais demandé. Ou bien on a "
         "demandé une fois, à la mauvaise minute.",
         "Et depuis 2026, une bonne partie des méthodes vendues sur le sujet est devenue interdite. On commence par "
         "là&nbsp;: ce que vous ne pouvez plus faire."],
       cta="Faire auditer ma fiche Google",
       sous_cta="Gratuit · sans engagement",
       image=(IMG + 'guide-obtenir-avis.jpg',
              "Une coiffeuse tend son téléphone à une cliente pour lui demander un avis"))),

     ('reponse', dict(
       eyebrow="La réponse courte",
       h2="Comment obtenir des avis Google sans enfreindre les règles&nbsp;?",
       reponse="En demandant à tous vos clients, sans exception, avec un lien direct vers votre fiche, juste après la "
               "prestation. Ce qui est interdit&nbsp;: trier les clients selon leur satisfaction avant de les envoyer "
               "sur Google, offrir une contrepartie contre un avis, et acheter des avis. Google sanctionne ces "
               "pratiques jusqu'à la suspension complète du profil.",
       paras=["Le tri préalable — souvent vendu sous le nom de «&nbsp;filtrage&nbsp;» ou de «&nbsp;portail de "
              "satisfaction&nbsp;» — est le point qui a changé. Beaucoup d'outils le proposent encore. Le fait qu'un "
              "logiciel le fasse pour vous ne le rend pas conforme&nbsp;: c'est votre fiche qui saute, pas la sienne."])),

     ('qr', dict(
       alt=True, eyebrow="En une phrase",
       h2="Les six questions qui reviennent à chaque rendez-vous",
       items=[
        ("Où trouver le lien pour demander un avis Google&nbsp;?",
         "Dans votre fiche d'établissement, section «&nbsp;Demander des avis&nbsp;»&nbsp;: Google génère un lien "
         "court en <code>g.page/r/…/review</code> qui ouvre directement la fenêtre de notation. C'est ce lien-là "
         "qu'on envoie, jamais l'adresse de la fiche&nbsp;— qui oblige le client à chercher le bouton."),
        ("Comment créer un QR code d'avis Google&nbsp;?",
         "Encodez ce même lien court dans n'importe quel générateur de QR code. Google en propose un dans les "
         "supports téléchargeables de la fiche. Sur un comptoir ou une facture, le QR code convertit mieux qu'une "
         "adresse à recopier&nbsp;— mais moins bien qu'un SMS reçu deux heures après le passage."),
        ("Peut-on demander un avis à ses clients&nbsp;?",
         "Oui, c'est explicitement autorisé et encouragé par Google. Ce qui est interdit, c'est de choisir à qui "
         "vous le demandez selon sa satisfaction supposée, et d'offrir une contrepartie. Demandez à tout le "
         "monde&nbsp;: c'est la seule règle qui compte."),
        ("Peut-on offrir une réduction contre un avis&nbsp;?",
         "Non. Toute contrepartie — remise, cadeau, tirage au sort, point de fidélité — enfreint les règles de "
         "Google, et un avis obtenu contre rémunération relève en France de la pratique commerciale trompeuse. "
         "Le risque n'est pas seulement la purge des avis&nbsp;: c'est la suspension du profil."),
        ("Combien d'avis faut-il pour que ça change quelque chose&nbsp;?",
         "Il n'y a pas de seuil publié par Google. Ce qu'on observe, c'est qu'en dessous d'une quinzaine d'avis un "
         "seul avis négatif commande la lecture, et qu'au-delà de la centaine la moyenne prend le dessus. Le rythme "
         "compte autant que le total&nbsp;: une fiche dont le dernier avis date de deux ans inquiète."),
        ("Pourquoi mes nouveaux avis disparaissent-ils&nbsp;?",
         "Presque toujours les filtres anti-spam&nbsp;: plusieurs avis déposés depuis le même réseau Wi-Fi dans la "
         "même heure, depuis une tablette posée à l'accueil, ou par des comptes sans historique. Faites déposer les "
         "avis plus tard, depuis chez le client, sur son propre téléphone."),
       ])),

     ('cartes', dict(
       alt=True, eyebrow="Les interdits",
       h2="Trois méthodes qui font suspendre un profil",
       classe='non',
       items=[
        ("demande-avis", "Le tri avant redirection",
         "Envoyer d'abord un sondage, puis n'envoyer sur Google que ceux qui ont mis une bonne note. C'est la "
         "définition du filtrage d'avis, et c'est explicitement interdit. La sanction va du masquage des avis à la "
         "suspension du profil."),
        ("satisfaction", "La contrepartie",
         "Une remise, un café offert, un tirage au sort contre un avis&nbsp;: l'incitation est interdite. Même "
         "quand elle est offerte à tout le monde. Même quand vous ne demandez pas un avis positif."),
        ("posts-google", "L'achat d'avis",
         "Au-delà de l'interdiction par Google, la publication de faux avis de consommateurs est une pratique "
         "commerciale trompeuse. Le risque ne se limite pas à la fiche."),
       ],
       tip="Ce qui reste parfaitement autorisé, et que presque personne ne fait sérieusement&nbsp;: demander à "
           "<strong>chaque</strong> client, à chaque fois, avec un lien qui ouvre directement le formulaire.",
       tip_ic="⚖️",
       sources=[("règles de Google sur le contenu des avis", G_REGLES[0])])),

     ('etapes', dict(howto=True, id="methode", 
       eyebrow="La méthode",
       h2="Ce qui fait passer une fiche de 12 avis à 140",
       items=[
        ("Demander dans l'heure qui suit",
         "La satisfaction a en effet une durée de vie très courte. Un SMS envoyé dans l'heure après l'intervention obtient un taux "
         "de réponse sans commune mesure avec un e-mail envoyé le lendemain, qui sera lu le soir et oublié."),
        ("Envoyer un lien direct, pas «&nbsp;cherchez-nous sur Google&nbsp;»",
         "Chaque étape supplémentaire divise le nombre de retours. Le lien court de votre fiche ouvre directement la "
         "fenêtre de rédaction&nbsp;: le client écrit deux phrases sans jamais quitter son téléphone."),
        ("Demander à tout le monde, y compris à ceux dont vous doutez",
         "C'est d'abord la condition de conformité. C'est ensuite ce qui rend la note crédible. Une fiche à 5,0 sur 200 avis "
         "n'inspire pas confiance&nbsp;; une fiche à 4,7 avec deux avis moyens et vos réponses dessous, si."),
        ("Relancer une fois, jamais deux",
         "Une relance à 48 heures récupère en effet une part significative des non-réponses. La deuxième relance n'apporte "
         "presque rien et transforme une demande en harcèlement."),
       ])),

     ('texte', dict(
       eyebrow="Le vrai blocage", id="pourquoi",
       h2="Pourquoi un client content n'écrit rien",
       paras=[
        "Il n'y a pas de mystère à résoudre&nbsp;: la satisfaction ne produit pas d'action. Un client mécontent a "
        "quelque chose à obtenir en écrivant&nbsp;— réparation, exutoire, mise en garde. Un client content, lui, a "
        "déjà eu ce qu'il voulait. L'affaire est close de son point de vue, et écrire un avis est un service qu'il "
        "vous rend, pas un besoin qu'il satisfait.",
        "C'est pour ça que le déséquilibre est structurel, et pas une malchance qui vous frappe vous. Sur une fiche "
        "laissée à elle-même, la proportion d'avis négatifs est mécaniquement plus forte que la proportion de "
        "clients mécontents. Vous ne lisez pas votre qualité de service&nbsp;: vous lisez qui a eu une raison "
        "d'écrire.",
        "La conséquence pratique est nette&nbsp;: <strong>tant que vous ne demandez pas, vous ne collectez que les "
        "mécontents</strong>. Et demander une fois, à l'occasion, quand on y pense, ne suffit pas — c'est la "
        "régularité qui renverse la pente, pas l'intensité.",
        "Le deuxième blocage est le frottement. Entre l'envie vague de laisser un avis et l'avis publié, il y a "
        "chercher l'entreprise, trouver le bouton, se connecter au bon compte, écrire. Chaque étape perd du monde. "
        "Un lien direct reçu par SMS supprime les trois premières&nbsp;: c'est toute la différence entre "
        "«&nbsp;laissez-nous un avis sur Google&nbsp;» sur une facture et un message qui ouvre directement la "
        "fenêtre de notation.",
        "Le troisième, plus banal&nbsp;: on n'ose pas demander. C'est pourtant la demande explicite, faite de vive "
        "voix par la personne qui a réalisé la prestation, qui obtient le meilleur taux — largement devant "
        "n'importe quel automatisme envoyé seul. L'automatisation ne remplace pas la demande, elle la rend "
        "systématique."],
       tip="Une fiche de douze avis dont deux négatifs affiche 3,8. La même entreprise, avec la même qualité de "
           "service et cent quarante avis demandés à tout le monde, affiche 4,7. Rien n'a changé dans le travail.",
       tip_ic="⚖️")),

     ('cartes', dict(
       alt=True, eyebrow="La mise en œuvre", id="erreurs",
       h2="Quatre façons de saboter une collecte pourtant autorisée",
       classe='non',
       paras=["Ces erreurs-là ne sont pas des infractions&nbsp;: elles font simplement perdre les avis qu'on vient "
              "de collecter, ou les font filtrer par Google. On les voit sur presque toutes les fiches qu'on reprend."],
       items=[
        ("demande-avis", "La tablette posée à l'accueil",
         "Dix avis déposés le même jour, depuis la même adresse IP, souvent depuis des comptes créés sur place&nbsp;: "
         "c'est le schéma que les filtres anti-spam repèrent le mieux. Les avis partent, et parfois les précédents "
         "avec. Faites déposer l'avis plus tard, depuis le téléphone du client."),
        ("sms-formulaire", "Le mailing groupé à tout le fichier",
         "Trois cents demandes envoyées le même matin produisent une rafale d'avis anormale sur une fiche qui en "
         "recevait deux par mois. Étalez&nbsp;: la demande doit suivre la prestation, pas le calendrier marketing."),
        ("rappel-rdv", "La demande trois semaines après",
         "Passé quelques jours, le souvenir s'est émoussé et la reconnaissance aussi. L'avis, s'il arrive, est court "
         "et générique — donc peu utile au prospect qui le lira. La fenêtre utile se compte en heures, pas en mois."),
        ("citations-locales", "Le QR code sans phrase",
         "Un carré noir sans contexte ne se scanne pas. Il faut dire ce qu'il y a derrière et combien de temps ça "
         "prend. «&nbsp;Votre avis en 30 secondes&nbsp;» au-dessus du code change tout, et coûte une ligne "
         "d'impression."),
       ])),

     ('tableau', dict(
       eyebrow="Les messages", id="modeles",
       h2="Ce qu'on écrit pour demander un avis, selon le canal",
       paras=["Trois règles avant les modèles. <strong>Le lien direct</strong>, jamais l'adresse de la "
              "fiche. <strong>Le bon moment</strong>&nbsp;: entre deux heures et un jour après la prestation, "
              "quand le souvenir est net et la reconnaissance encore vive. <strong>Une seule relance</strong>, "
              "quatre jours plus tard, et on s'arrête là."],
       colonnes=["Le canal", "Le message"],
       lignes=[
        ["<strong>SMS, deux heures après</strong>&nbsp;— le plus efficace, et de loin.",
         "«&nbsp;Bonjour [prénom], [prénom du technicien] de [entreprise]. Content d'avoir pu vous dépanner "
         "aujourd'hui. Si vous avez trente secondes, votre avis nous aide beaucoup&nbsp;: [lien]. Merci&nbsp;!&nbsp;»"],
        ["<strong>E-mail, le lendemain</strong>&nbsp;— pour les prestations longues.",
         "Objet&nbsp;: «&nbsp;Un mot sur [la prestation]&nbsp;?&nbsp;» — Corps&nbsp;: «&nbsp;Bonjour [prénom], "
         "j'espère que [le résultat] vous convient. Un avis en deux lignes aide les personnes qui hésitent à nous "
         "appeler&nbsp;: [lien]. Et s'il y a quoi que ce soit à reprendre, répondez-moi directement.&nbsp;»"],
        ["<strong>De vive voix, à la fin du rendez-vous.</strong>",
         "«&nbsp;Si vous êtes content, je vous envoie un lien par SMS&nbsp;— un avis Google, c'est ce qui nous "
         "amène nos clients.&nbsp;» Annoncer le SMS double son taux d'ouverture&nbsp;: il n'arrive plus par surprise."],
        ["<strong>QR code au comptoir ou sur la facture.</strong>",
         "«&nbsp;Votre avis en 30 secondes&nbsp;» au-dessus du code. Un QR code sans phrase ne se scanne pas. "
         "Précisez ce qui se passe après le scan&nbsp;: personne ne scanne dans le vide."],
        ["<strong>La relance, quatre jours plus tard.</strong>",
         "«&nbsp;Bonjour [prénom], je me permets un dernier message&nbsp;: si vous avez un instant pour un avis, "
         "c'est ici [lien]. Sinon, aucun souci, bonne journée.&nbsp;» La porte de sortie explicite fait passer la "
         "relance de harcèlement à politesse."],
        ["<strong>Ce qu'on n'écrit jamais.</strong>",
         "«&nbsp;Laissez-nous 5&nbsp;étoiles&nbsp;», «&nbsp;10&nbsp;% de remise contre un avis&nbsp;», "
         "«&nbsp;Si vous n'êtes pas satisfait, appelez-nous plutôt que d'écrire&nbsp;». Les trois enfreignent les "
         "règles de Google, et la dernière est celle qui fait suspendre les profils."],
       ])),

     ('texte', dict(
       eyebrow="Le marché noir", id="acheter",
       h2="Acheter des avis Google&nbsp;: ce que vous achetez vraiment",
       paras=[
        "La requête existe, les offres aussi&nbsp;: une dizaine d'euros l'avis, livré en quarante-huit heures, "
        "avec des «&nbsp;comptes réels et vieillis&nbsp;». Il faut savoir ce qu'on achète, parce que ce n'est pas "
        "ce qui est annoncé.",
        "<strong>Sur le plan technique</strong>, ces avis proviennent de comptes qui déposent des dizaines d'avis "
        "sans lien géographique cohérent. C'est exactement le motif que les filtres de Google détectent le mieux. "
        "La purge arrive rarement le jour même&nbsp;— souvent quelques mois plus tard, et elle emporte au passage "
        "les vrais avis déposés dans la même période.",
        "<strong>Sur le plan légal</strong>, c'est plus lourd que ce que la plupart des gérants imaginent. Publier "
        "ou faire publier de faux avis de consommateurs est une pratique commerciale trompeuse, punie par "
        "l'article&nbsp;L132-2 du code de la consommation de deux ans d'emprisonnement et 300&nbsp;000&nbsp;euros "
        "d'amende, montant pouvant être porté à un pourcentage du chiffre d'affaires. La DGCCRF contrôle ce terrain "
        "et publie ses sanctions. Le donneur d'ordre est l'entreprise, pas le prestataire.",
        "<strong>Sur le plan commercial</strong>, enfin&nbsp;: cinq avis élogieux sans détail, déposés la même "
        "semaine, sur une fiche qui n'en avait aucun, ne convainquent personne. Un prospect lit les avis dans "
        "l'ordre chronologique. Le contraste saute aux yeux avant même la lecture.",
        "La vraie alternative n'est pas plus lente qu'on ne croit. Une entreprise locale qui demande un avis à "
        "chaque client, systématiquement et par SMS, passe de quelques avis à plusieurs dizaines en un "
        "trimestre&nbsp;— avec des textes qui parlent de vraies prestations, et qui restent en ligne."],
       tip="Le test&nbsp;: si un prestataire ne vous demande pas votre fichier client, c'est qu'il ne compte pas "
           "s'en servir. Il n'y a que deux façons d'obtenir un avis&nbsp;— le demander à un client, ou le fabriquer.",
       tip_ic="🚫")),

     ('agents', dict(
       alt=True, eyebrow="Ce qu'on met en place",
       h2="La demande d'avis qui tourne sans vous",
       paras=["Demander à chaque client, à chaque fois, pendant deux ans&nbsp;: personne ne le tient à la main. C'est "
              "le genre de tâche pour laquelle un agent existe. Le catalogue complet est sur la "
              f"<a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["demande-avis", "satisfaction", "reponse-avis", "citations-locales"])),

     ('relance', dict(
       texte="On regarde votre fiche, votre nombre d'avis et ce que font vos trois concurrents les plus proches.",
       libelle="Prendre 15 minutes")),

     ('faq', dict(
       eyebrow="FAQ", h2="Les questions qu'on nous pose",
       items=[
        ("Comment récupérer le lien d'avis si je n'ai pas accès à la fiche&nbsp;?",
         "Il faut d'abord récupérer la fiche&nbsp;: revendiquez-la depuis Google, la procédure passe par une "
         "vérification par courrier, téléphone ou vidéo. Sans accès gestionnaire, pas de lien court, pas de "
         "réponses aux avis, pas de statistiques."),
        ("Peut-on demander un avis à un client mécontent&nbsp;?",
         "Oui, et il faut le faire&nbsp;— c'est même toute la logique de la règle. Ce qui est interdit, c'est de "
         "l'écarter. En pratique, un client mécontent recontacté avant la demande d'avis écrit rarement un avis "
         "négatif&nbsp;: c'est le suivi de satisfaction qui règle ça, pas le filtrage."),
        ("Les avis sur d'autres plateformes comptent-ils pour Google&nbsp;?",
         "Pas dans la note de votre fiche, qui ne reflète que les avis Google. Mais ils comptent pour la décision "
         "du prospect, qui compare souvent deux ou trois sources, et pour les moteurs génératifs, qui puisent "
         "largement hors de Google."),
        ("Faut-il répondre aux avis qu'on vient de recevoir&nbsp;?",
         "Oui, systématiquement, et c'est ce qui entretient le flux&nbsp;: les clients suivants voient qu'on lit. "
         "La méthode est détaillée sur notre page <a href=\"https://decupler.com/repondre-aux-avis-google/\">"
         "répondre aux avis Google</a>."),
        ("Combien d'avis faut-il pour être crédible&nbsp;?",
         "Il n'y a pas de seuil officiel, mais la comparaison est locale&nbsp;: ce qui compte, c'est votre nombre "
         "d'avis face à celui des trois établissements que Google affiche à côté de vous. Regardez-les, c'est votre "
         "objectif réel."),
        ("Un client peut-il laisser un avis sans compte Google&nbsp;?",
         "Non, un compte Google est nécessaire pour publier un avis. En pratique, la quasi-totalité des utilisateurs "
         "d'Android en ont un, et une grande partie des utilisateurs d'iPhone aussi via Gmail."),
        ("Puis-je proposer une remise contre un avis&nbsp;?",
         "Non. L'incitation est interdite, même sans exiger un avis positif et même si l'offre est faite à tous. "
         "C'est un motif de suppression des avis concernés, et de sanction du profil."),
        ("Et si je reçois un avis négatif après avoir demandé&nbsp;?",
         "C'est le risque, et c'est aussi le prix de la conformité. En pratique, un SMS de satisfaction envoyé en "
         "parallèle vous alerte quand un client repart mécontent&nbsp;— vous le rappelez avant qu'il n'écrive. C'est "
         "du service, et rien ne l'interdit."),
        ("Les avis anciens comptent-ils autant&nbsp;?",
         "Google met en avant la fraîcheur&nbsp;: une fiche avec cinquante avis dont le dernier date de deux ans "
         "rassure moins qu'une fiche avec trente avis dont trois de ce mois-ci. C'est un flux, pas un stock."),
        ("Vous garantissez un nombre d'avis&nbsp;?",
         "Non, et personne ne peut le garantir honnêtement&nbsp;: ça dépend de votre volume de clients et de leur "
         "satisfaction. Ce qu'on garantit, c'est que la demande part à chaque fois, ce qui n'est le cas chez presque "
         "personne aujourd'hui."),
       ])),
    ]),

# ══ 4. Agent vocal IA — 320/mois, difficulté 13, CPC 11,18 € ══════════════
"agent-vocal-ia": dict(
    mot_cle="agent vocal ia",
    titre_seo="Agent vocal IA : décrocher quand vous ne pouvez pas",
    meta=("Agent vocal IA pour entreprise locale : il décroche quand personne ne répond, qualifie "
          "l'appel et pose le rendez-vous. Ce qu'il fait, et ce qu'il coûte."),
    signature=SIG_AGENT,
    sections=[
     ('hero', dict(
       kicker="Agent vocal IA",
       h1="Une voix décroche <em>quand vous ne pouvez pas</em>.",
       leads=[
         "<strong>Un agent vocal IA est un répondant automatique qui prend l'appel quand personne ne décroche</strong>, "
         "comprend la demande, la qualifie, et pose le rendez-vous dans votre agenda. Il ne remplace pas votre accueil "
         "— il se déclenche uniquement dans le silence qui, aujourd'hui, coûte le client.",
         "Chez Décupler il n'est pas vendu seul&nbsp;: il fait partie des agents branchés autour du site, dans une "
         f"<a href=\"{PILIER}\">offre où la création du site est offerte</a> et où vous ne payez qu'un abonnement."],
       cta="Écouter ce que ça donnerait chez moi",
       sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois",
       image=(IMG + 'agent-vocal-ia.jpg',
              "Un artisan travaille des deux mains, son téléphone posé à côté de lui sur l'établi"),
       phone=[("call", "06 44 •• •• 12", "Appel entrant · 19:41"),
              ("miss", "Vous ne décrochez pas", "3 sonneries, personne"),
              ("sms", "L'agent a pris l'appel", "Fuite sous évier · rappel demandé demain 8&nbsp;h", "RDV posé")])),

     ('bande', dict(
       lbl_g="Sans agent vocal", ic_g="sms-appel-manque",
       lbl_d="Avec", ic_d="agent-vocal",
       cnt=("L'appel tombe sur la boîte vocale",
            "Moins d'un appelant sur trois laisse un message. Les autres composent le numéro suivant, et vous ne "
            "saurez jamais qu'ils ont appelé.",
            "Une voix répond et note la demande",
            "Nom, motif, urgence, créneau souhaité. Vous recevez tout par SMS et vous rappelez quand vous êtes "
            "disponible."))),

     ('reponse', dict(
       eyebrow="La réponse courte",
       h2="Qu'est-ce qu'un agent vocal IA, concrètement&nbsp;?",
       reponse="C'est un système qui répond au téléphone à votre place lorsque l'appel n'est pas décroché. Il tient "
               "une vraie conversation, comprend le motif de l'appel, pose les questions utiles à votre métier, "
               "propose un créneau dans votre agenda et vous transmet le résumé par SMS. Il ne se déclenche que "
               "lorsque personne n'a répondu&nbsp;: si vous décrochez, il ne se passe rien.",
       paras=["Techniquement, il combine la reconnaissance vocale, un modèle de langage et une synthèse vocale. "
              "Commercialement, ce qui compte est ailleurs&nbsp;: ce n'est ni un serveur vocal à touches, ni un "
              "répondeur. L'appelant parle normalement et obtient une réponse, pas un menu."])),

     ('texte', dict(
       alt=True, eyebrow="Le vrai problème",
       h2="Ce n'est pas le standard qui coûte cher, c'est le silence",
       paras=[
        "Il est 19&nbsp;h&nbsp;41. Vous rangez le camion, vous êtes en cabine, vous dînez. Quelqu'un a un problème "
        "maintenant, cherche votre métier dans votre ville, et compose le premier numéro. "
        "<strong>Ça sonne trois fois et ça bascule sur la boîte vocale.</strong> Il raccroche et appelle le suivant.",
        "Le coût de cet appel n'apparaît nulle part dans votre comptabilité. Il n'y a pas de ligne «&nbsp;clients "
        "perdus faute de réponse&nbsp;», et c'est précisément pour ça qu'on ne s'en occupe jamais&nbsp;: on ne peut "
        "pas regretter ce qu'on n'a pas vu.",
        "Un agent vocal ne résout pas un problème de qualité de service. Il résout un problème d'heures ouvrables — "
        "et pour une entreprise locale, la demande arrive rarement pendant les heures ouvrables."],
       tip="Le seul chiffre à regarder pour savoir si ça vaut le coup&nbsp;: combien vaut, chez vous, un client "
           "moyen. Un seul rattrapé dans le mois paie généralement l'abonnement entier.",
       tip_ic="🧮")),

     ('etapes', dict(
       eyebrow="Comment ça marche",
       h2="Quatre étapes, et rien à installer",
       items=[
        ("Un numéro de suivi renvoie sur votre ligne",
         "Vous gardez votre numéro et votre téléphone. Le numéro de suivi est un numéro géographique normal, non "
         "surtaxé&nbsp;: pour l'appelant, rien ne change."),
        ("L'agent ne se déclenche que dans le silence",
         "Après un nombre de sonneries que vous choisissez, et seulement si personne n'a décroché. Vous fixez aussi "
         "les plages horaires&nbsp;: soirs et week-ends seulement, ou en permanence."),
        ("Il qualifie selon votre métier",
         "Il est entraîné sur vos prestations, votre zone d'intervention et vos horaires. Il pose les questions qui "
         "comptent chez vous — la nature de la panne, la surface, le type de soin — et pas un questionnaire générique."),
        ("Vous recevez le résumé et le rendez-vous",
         "SMS immédiat avec le nom, le numéro, le motif et le degré d'urgence. Si vous avez branché l'agenda, le "
         "créneau est déjà posé."),
       ])),

     ('cartes', dict(
       alt=True, eyebrow="Ce qu'il ne fait pas",
       h2="Les limites, dites avant la vente",
       classe='non',
       items=[
        ("agent-vocal", "Il ne remplace pas votre accueil",
         "Si vous avez une secrétaire ou un accueil, l'agent ne prend jamais sa place&nbsp;: il prend le relais quand "
         "la ligne est occupée, en dehors des horaires, ou pendant les pics. Quelqu'un qui vous vend le remplacement "
         "d'un humain par une voix synthétique vous vend surtout un problème d'image."),
        ("relance-devis", "Il ne s'engage jamais sur un prix",
         "Ni sur un tarif, ni sur un délai d'intervention. Il note la demande, il ne négocie pas. Le chiffrage reste "
         "le vôtre, et c'est aussi ce qui vous protège."),
        ("satisfaction", "Il dit qu'il est un assistant",
         "L'appelant n'est jamais laissé à croire qu'il parle à une personne. C'est une question de loyauté "
         "commerciale, et en pratique ça se passe mieux&nbsp;: les gens acceptent très bien de parler à un assistant "
         "qui les rappelle, beaucoup moins de découvrir qu'on les a trompés."),
       ])),

     ('agents', dict(
       eyebrow="Ce qui va avec",
       h2="L'agent vocal ne travaille jamais seul",
       paras=["Il couvre l'appel décroché. Restent la demande arrivée par le formulaire, celle arrivée à 21&nbsp;h "
              "sur le site, et le devis qui dort. Le catalogue complet des quinze agents est sur la "
              f"<a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["sms-appel-manque", "sms-formulaire", "chatbot", "rappel-rdv"])),

     ('relance', dict(
       texte="Quinze minutes en visio&nbsp;: je vous fais entendre ce que l'agent répondrait à vos appels, avec votre "
             "métier et votre zone.",
       libelle="Prendre 15 minutes")),

     ('faq', dict(
       alt=True, eyebrow="FAQ", h2="Les questions qu'on nous pose",
       items=[
        ("Est-ce que ça s'entend que c'est une IA&nbsp;?",
         "Oui, et c'est voulu&nbsp;: l'agent se présente comme un assistant dès la première phrase. La voix est "
         "naturelle, mais l'objectif n'est pas de faire illusion — il est de ne pas laisser un appel sans réponse."),
        ("Que se passe-t-il si l'appelant ne veut pas parler à un robot&nbsp;?",
         "Il raccroche, exactement comme il aurait raccroché devant la boîte vocale. Vous n'êtes pas plus mal qu'avant. "
         "En pratique, la plupart des gens acceptent de laisser leur demande dès lors qu'on leur promet un rappel."),
        ("Ça marche pour les urgences&nbsp;?",
         "C'est le cas où ça rapporte le plus, parce que l'urgence n'attend pas et que vos concurrents ne décrochent "
         "pas non plus à 22&nbsp;h. L'agent qualifie le degré d'urgence et vous alerte différemment selon le niveau."),
        ("Je dois changer de téléphone ou d'opérateur&nbsp;?",
         "Non. Vous gardez votre numéro, votre téléphone et votre forfait. Le numéro de suivi se pose devant, et il "
         "renvoie sur votre ligne existante."),
        ("Combien coûte un agent vocal IA&nbsp;?",
         "Chez nous il n'est pas facturé à l'unité&nbsp;: il fait partie de l'abonnement mensuel qui démarre à "
         "199&nbsp;€ et qui monte selon le nombre d'agents branchés. La création du site, elle, est offerte&nbsp;— "
         f"voir <a href=\"{PILIER}\">le détail de l'offre</a>."),
        ("Et si je préfère juste un SMS automatique&nbsp;?",
         "C'est un autre agent, plus simple et souvent suffisant pour démarrer&nbsp;: l'appelant reçoit un message "
         "à votre nom dans la seconde. Beaucoup de clients commencent par là et ajoutent la voix ensuite."),
       ])),
    ]),

# ══ 5. Standard téléphonique IA — 170/mois, difficulté 15, CPC 39,58 € ════
"standard-telephonique-ia": dict(
    mot_cle="standard téléphonique ia",
    titre_seo="Standard téléphonique IA : le comparatif honnête",
    meta=("Standard téléphonique IA ou permanence téléphonique humaine : ce que chacun sait faire, "
          "ce que ça coûte vraiment, et dans quels cas l'IA ne suffit pas."),
    signature=SIG_AGENT,
    sections=[
     ('hero', dict(
       kicker="Standard téléphonique IA",
       h1="Un standard qui répond à 20&nbsp;h,<br>sans <em>embaucher</em> pour 20&nbsp;h.",
       leads=[
         "<strong>Un standard téléphonique IA prend les appels que votre accueil ne peut pas prendre&nbsp;:</strong> "
         "hors horaires, pendant les pics, quand la ligne est occupée. Il tient une conversation, qualifie la demande "
         "et pose le rendez-vous — sans menu à touches et sans musique d'attente.",
         "Cette page n'est pas un argumentaire. C'est la comparaison avec la permanence téléphonique humaine, y "
         "compris les cas où elle reste le bon choix."],
       cta="Comparer sur mon cas",
       sous_cta="Gratuit · sans engagement",
       image=(IMG + 'standard-telephonique-ia.jpg',
              "L'accueil vide et soigné d'un cabinet, téléphone posé sur le comptoir"))),

     ('reponse', dict(
       eyebrow="La réponse courte",
       h2="Standard IA ou permanence téléphonique humaine&nbsp;?",
       reponse="Un standard téléphonique IA est disponible en permanence, prend un nombre illimité d'appels "
               "simultanés et coûte un forfait fixe. Une permanence humaine comprend mieux les situations "
               "inhabituelles, gère l'émotion et sait sortir du cadre. Le partage raisonnable&nbsp;: l'IA en débordement "
               "et hors horaires, l'humain sur les heures ouvrées et les sujets sensibles.",
       paras=["La question n'est presque jamais «&nbsp;l'un ou l'autre&nbsp;». Elle est «&nbsp;qui prend l'appel de "
              "19&nbsp;h&nbsp;41&nbsp;», parce qu'aujourd'hui la réponse est «&nbsp;personne&nbsp;»."])),

     ('tableau', dict(
       alt=True, eyebrow="Le comparatif",
       h2="Ce que chacun sait faire",
       colonnes=["", "Standard IA", "Permanence humaine"],
       lignes=[
        ["<strong>Disponibilité</strong>", "24&nbsp;h/24, tous les jours", "Plages contractuelles, souvent heures ouvrées"],
        ["<strong>Appels simultanés</strong>", "Sans limite", "Limité au nombre d'opérateurs"],
        ["<strong>Coût</strong>", "Forfait fixe, indépendant du volume", "À l'appel ou au forfait, monte avec le volume"],
        ["<strong>Situations inhabituelles</strong>", "Transfère ou prend note", "Comprend, adapte, rassure"],
        ["<strong>Client en colère</strong>", "Note et alerte&nbsp;: à éviter", "C'est là que l'humain vaut son prix"],
        ["<strong>Connaissance de votre métier</strong>", "Entraîné sur vos prestations et votre zone", "Dépend de la formation du prestataire"],
        ["<strong>Mise en route</strong>", "Quelques jours", "Contrat, formation, scripts"],
       ])),

     ('cartes', dict(
       eyebrow="Les limites",
       h2="Trois situations où on vous dira non",
       classe='non',
       items=[
        ("satisfaction", "Les appels d'urgence vitale",
         "Santé, sécurité, incident grave&nbsp;: un assistant vocal note et alerte, il ne juge pas une situation "
         "critique. Si votre activité en reçoit régulièrement, il vous faut une astreinte humaine, pas un agent."),
        ("chatbot", "Les conversations à forte charge émotionnelle",
         "Un client furieux, un litige en cours, une annonce difficile&nbsp;: l'agent transfère ou prend note, mais "
         "il ne désamorce rien. Sur ces appels-là, une voix synthétique aggrave presque toujours."),
        ("relance-devis", "La vente complexe au téléphone",
         "Si la conversion se joue sur un échange long, avec objections et négociation, l'agent sert à capter le "
         "contact&nbsp;— pas à vendre. Ce qu'il vous fait gagner, c'est le rendez-vous."),
       ],
       tip="Formulé autrement&nbsp;: l'agent est excellent sur les appels qui, aujourd'hui, ne sont pas décrochés du "
           "tout. Il est médiocre sur ceux où votre présence fait la différence. Ce sont rarement les mêmes.",
       tip_ic="⚖️")),

     ('etapes', dict(
       alt=True, eyebrow="La mise en place",
       h2="De la ligne existante au premier appel traité",
       items=[
        ("On garde votre numéro",
         "Un numéro de suivi non surtaxé se pose devant votre ligne actuelle. Aucun changement d'opérateur, aucun "
         "matériel, rien à installer."),
        ("Vous fixez la règle de bascule",
         "Nombre de sonneries, plages horaires, ligne occupée. C'est vous qui décidez quand l'agent prend la main, "
         "et il ne le fait jamais si quelqu'un décroche."),
        ("On l'entraîne sur votre activité",
         "Prestations, zone d'intervention, horaires, questions à poser, ce qu'il ne doit jamais dire. C'est cette "
         "étape qui fait la différence entre un agent utile et un répondeur bavard."),
        ("Vous écoutez avant de brancher",
         "On vous fait entendre des appels de test sur vos cas réels. Si le résultat ne vous convient pas, on ne "
         "branche pas."),
       ])),

     ('agents', dict(
       eyebrow="Ce qui va avec",
       h2="Le standard n'est qu'une porte d'entrée",
       paras=["Un appel capté qui n'aboutit pas à un rendez-vous confirmé ne sert à rien. Le catalogue complet des "
              f"quinze agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["agent-vocal", "rappel-rdv", "sms-appel-manque", "rapport-mensuel"])),

     ('relance', dict(
       texte="Donnez-moi vos trois questions les plus fréquentes au téléphone&nbsp;: je vous fais entendre ce que "
             "l'agent répondrait.",
       libelle="Prendre 15 minutes")),

     ('faq', dict(
       alt=True, eyebrow="FAQ", h2="Les questions qu'on nous pose",
       items=[
        ("Combien coûte un standard téléphonique IA&nbsp;?",
         "Chez nous, il n'est pas facturé à l'appel&nbsp;: il fait partie de l'abonnement mensuel qui démarre à "
         "199&nbsp;€ et qui monte selon le nombre d'agents branchés. L'intérêt du forfait fixe est qu'un mois chargé "
         "ne coûte pas plus cher, contrairement à une facturation à l'appel."),
        ("Est-ce que je peux le limiter aux heures de fermeture&nbsp;?",
         "Oui, et beaucoup de clients commencent ainsi&nbsp;: soirs, week-ends et jours fériés uniquement. On élargit "
         "ensuite si le rapport vous convient."),
        ("Il peut transférer un appel à un humain&nbsp;?",
         "Oui, selon des règles que vous définissez&nbsp;: mot-clé prononcé, degré d'urgence, ou simple demande de "
         "l'appelant. Le transfert est ce qui évite les mauvaises surprises."),
        ("Mes clients vont-ils accepter&nbsp;?",
         "L'expérience est comparée à ce qu'il y avait avant, pas à un idéal. Face à une boîte vocale, un assistant "
         "qui note la demande et promet un rappel passe très bien. Face à une secrétaire disponible, non — c'est "
         "pour ça qu'on ne le met pas là."),
        ("Ça remplace un télésecrétariat&nbsp;?",
         "Sur le débordement et le hors horaires, oui, et à un coût très inférieur. Sur la gestion d'agenda complexe "
         "et les appels sensibles, non. Beaucoup de cabinets gardent les deux, chacun sur son terrain."),
        ("Quelle différence avec l'agent vocal&nbsp;?",
         "C'est le même agent, présenté sous l'angle qui vous parle. Si vous n'avez pas d'accueil, lisez plutôt "
         "<a href=\"https://decupler.com/agent-vocal-ia/\">la page agent vocal</a>&nbsp;; si vous en avez un et que "
         "vous cherchez à le soulager, vous êtes au bon endroit."),
       ])),
    ]),

# ══ 6. Chatbot WordPress — 110/mois, difficulté 15, CPC 6,80 € ════════════
"chatbot-wordpress": dict(
    mot_cle="chatbot wordpress",
    titre_seo="Chatbot WordPress : lequel installer, et comment",
    meta=("Chatbot WordPress pour une entreprise locale : plugin ou script, ce qu'il faut lui "
          "apprendre, l'impact sur la vitesse du site, et ce qu'il ne doit jamais faire."),
    signature=SIG_AGENT,
    sections=[
     ('hero', dict(
       kicker="Chatbot WordPress",
       h1="Il est 21&nbsp;h.<br>Votre site répond, ou il <em>attend</em>.",
       leads=[
         "<strong>Un chatbot WordPress bien posé répond aux questions que vos visiteurs se posent le soir</strong>, "
         "quand personne ne décroche. Vos horaires, votre zone, vos tarifs, un rendez-vous. Mal posé, en revanche, "
         "il ralentit le site, dit n'importe quoi, et fait fuir.",
         "Cette page explique laquelle des deux versions vous obtenez, selon comment il est installé et sur quoi il "
         "est entraîné."],
       cta="Voir ce que ça donnerait sur mon site",
       sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois",
       image=(IMG + 'chatbot-wordpress.jpg',
              "Une visiteuse consulte un site sur son téléphone à 21 h, chez elle"),
       phone=[("call", "Visiteur · 21:07", "Page « Tarifs »"),
              ("miss", "Sans assistant", "Il referme l'onglet"),
              ("sms", "Avec l'assistant", "«&nbsp;Vous intervenez à Vitry&nbsp;? — Oui, et samedi matin.&nbsp;»",
               "Contact obtenu")])),

     ('reponse', dict(
       eyebrow="La réponse courte",
       h2="Comment ajouter un chatbot sur WordPress&nbsp;?",
       reponse="Par un plugin depuis l'administration, ou par un script fourni par le service et collé dans le pied "
               "de page du thème. Le script est en général plus léger&nbsp;: il ne charge rien tant que le visiteur "
               "n'ouvre pas la fenêtre. Beaucoup de plugins, eux, en ajoutent sur toutes les pages. Or sur un "
               "site d'entreprise locale, la différence se voit sur la vitesse de chargement mobile.",
       paras=["Le choix technique est secondaire. Ce qui décide du résultat, c'est ce que le chatbot sait de votre "
              "activité. Un assistant branché sur un modèle générique répond poliment à côté du sujet. Et un "
              "visiteur qui reçoit une réponse à côté ne revient pas."])),

     ('texte', dict(
       alt=True, eyebrow="Le vrai problème",
       h2="Ce n'est pas la conversation qui manque, c'est l'horaire",
       paras=[
        "La demande d'une entreprise locale n'arrive pas entre 9&nbsp;h et 18&nbsp;h. Elle arrive le soir, quand la "
        "personne a enfin cinq minutes, ou le dimanche. À cette heure-là, votre site est la seule chose ouverte, et "
        "il ne dit rien de plus que ce qui est écrit dessus.",
        "Trois questions reviennent partout&nbsp;: <strong>est-ce que vous intervenez chez moi</strong>, "
        "<strong>combien ça coûte à peu près</strong>, <strong>sous combien de temps</strong>. Un formulaire ne "
        "répond à aucune des trois. Il demande au visiteur de laisser ses coordonnées pour obtenir une réponse qu'il "
        "veut maintenant.",
        "Un assistant entraîné sur votre zone, vos prestations et vos délais répond aux trois en dix secondes, puis "
        "demande le contact. Dans cet ordre&nbsp;: la réponse d'abord, le formulaire ensuite."],
       tip="Le meilleur indicateur d'un assistant utile n'est pas le nombre de conversations&nbsp;: c'est le nombre "
           "de contacts obtenus la nuit et le week-end, quand vous n'auriez rien eu.",
       tip_ic="🌙")),

     ('etapes', dict(
       eyebrow="Ce qu'il doit savoir",
       h2="Quatre choses, et il devient utile",
       paras=["Un assistant qui ne sait que ce qui est déjà écrit sur le site ne sert à rien&nbsp;: le visiteur "
              "l'a lu."],
       items=[
        ("Votre zone d'intervention, à la commune près",
         "«&nbsp;Vous venez à Vitry&nbsp;?&nbsp;» est la question la plus posée et celle qui fait le plus fuir quand "
         "la réponse est floue. La liste des communes se donne une fois."),
        ("Vos ordres de grandeur de prix",
         "Pas un devis&nbsp;: une fourchette, et les cas où elle ne s'applique pas. Un visiteur qui repart sans "
         "aucun ordre d'idée va le chercher ailleurs, et il le trouve."),
        ("Vos délais réels, par saison",
         "«&nbsp;Sous quel délai&nbsp;?&nbsp;» n'a pas la même réponse en février et en avril. Un assistant qui "
         "annonce un délai que vous ne tiendrez pas vous crée un problème au lieu d'en régler un."),
        ("Ce qu'il ne doit jamais faire",
         "S'engager sur un prix ferme, promettre une intervention, donner un conseil technique risqué. La liste des "
         "interdits compte autant que celle des réponses."),
       ])),

     ('cartes', dict(
       alt=True, eyebrow="Les erreurs",
       h2="Trois façons de rendre un chatbot nuisible",
       classe='non',
       items=[
        ("chatbot", "Le brancher sans rien lui apprendre",
         "Un assistant générique répond avec assurance à côté du sujet. C'est pire que pas d'assistant du tout&nbsp;: "
         "le visiteur repart avec une information fausse et l'impression d'avoir été mal reçu."),
        ("mots-cles-locaux", "Le laisser ralentir le site",
         "Beaucoup de plugins chargent leurs scripts sur toutes les pages, y compris pour les visiteurs qui "
         "n'ouvriront jamais la fenêtre. Sur mobile, ça se paie en secondes de chargement, donc en visiteurs perdus "
         "avant même la première ligne."),
        ("satisfaction", "Le faire passer pour un humain",
         "Un prénom, une photo, aucune mention d'assistant&nbsp;: quand le visiteur comprend, il ne retient qu'une "
         "chose, c'est qu'on lui a menti. L'assistant se présente comme tel, et ça ne coûte rien en conversion."),
       ])),

     ('agents', dict(
       eyebrow="Ce qui va avec",
       h2="Le chat couvre le soir. Il ne couvre pas le téléphone",
       paras=["Un visiteur qui préfère appeler appellera. Le catalogue complet des quinze agents est sur la "
              f"<a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["chatbot", "sms-formulaire", "agent-vocal", "rappel-rdv"])),

     ('relance', dict(
       texte="Donnez-moi les trois questions qu'on vous pose le plus&nbsp;: je vous montre ce que l'assistant "
             "répondrait sur votre site.",
       libelle="Prendre 15 minutes")),

     ('faq', dict(
       eyebrow="FAQ", h2="Les questions qu'on nous pose",
       items=[
        ("Un chatbot ralentit-il un site WordPress&nbsp;?",
         "Il peut, et c'est le principal reproche à faire à beaucoup de plugins&nbsp;: ils chargent leurs ressources "
         "sur toutes les pages. Un script qui ne charge la fenêtre qu'au clic a un impact quasi nul. C'est le premier "
         "critère à vérifier avant d'installer quoi que ce soit."),
        ("Plugin ou script&nbsp;?",
         "Le plugin est plus simple à poser depuis l'administration&nbsp;; le script est en général plus léger et plus "
         "facile à contrôler. Sur les sites qu'on construit, on met un script chargé à la demande&nbsp;— pour la "
         "vitesse et pour ne pas ajouter une extension de plus à maintenir."),
        ("Il faut lui écrire toutes les réponses à la main&nbsp;?",
         "Non. Il apprend à partir de votre site, de vos prestations et de vos horaires. Ce qu'on écrit à la main, "
         "c'est la liste courte de ce qu'il ne doit jamais dire&nbsp;— et c'est cette liste qui fait la qualité."),
        ("Que se passe-t-il s'il ne sait pas répondre&nbsp;?",
         "Il le dit et propose de vous transmettre la question, avec le contact du visiteur. Un assistant qui invente "
         "plutôt que d'avouer son ignorance est un assistant à débrancher."),
        ("Et le RGPD&nbsp;?",
         "L'assistant ne collecte que ce que le visiteur donne volontairement pour être rappelé&nbsp;: nom, contact, "
         "motif. Selon votre métier, on restreint davantage&nbsp;— dans un cabinet de santé, par exemple, il ne pose "
         "aucune question médicale et ne conserve aucun élément clinique."),
        ("Combien coûte un chatbot WordPress&nbsp;?",
         "Chez nous il fait partie de l'abonnement mensuel qui démarre à 199&nbsp;€ et qui monte selon le nombre "
         f"d'agents branchés, la création du site étant offerte&nbsp;— voir <a href=\"{PILIER}\">le détail de "
         "l'offre</a>. Ailleurs, comptez un abonnement mensuel par assistant, souvent facturé au nombre de "
         "conversations."),
       ])),
    ]),

# ══ Pages agent (vente) — pas de volume de recherche, maillées depuis l'offre ══

"agent-fiche-google": dict(
    mot_cle="optimisation fiche google",
    titre_seo="Optimisation de la fiche Google : l'agent Décupler",
    meta=("On complète votre fiche Google sur tous les critères que Google regarde, avec le "
          "vocabulaire que vos clients tapent. Inclus dans l'offre site offert."),
    signature=SIG_AVIS,
    sections=[
     ('hero', dict(
       kicker="Agent · Optimisation de la fiche Google",
       h1="Une fiche remplie à moitié<br>ne remonte <em>jamais</em>.",
       leads=["<strong>À distance égale, c'est la fiche la plus complète qui passe devant.</strong> Catégories, "
              "services, zones desservies, horaires, photos, description&nbsp;: chaque champ vide est un point que "
              "votre concurrent a et que vous n'avez pas.",
              "On remplit les seize critères que Google regarde, avec le vocabulaire que vos clients tapent "
              "réellement&nbsp;— pas celui de votre plaquette."],
       cta="Faire auditer ma fiche", sous_cta="Gratuit · sans engagement", viz="trouve")),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="Concrètement, qu'est-ce qui change sur la fiche&nbsp;?",
       reponse="On complète les champs que presque personne ne remplit&nbsp;: les services détaillés un par un, les "
               "zones desservies commune par commune, les attributs, la description longue, et les catégories "
               "secondaires. Puis on maintient&nbsp;: horaires exceptionnels, nouvelles photos, nouveaux services.",
       paras=["La catégorie principale est le champ qui pèse le plus lourd, et c'est celui qui est le plus souvent "
              "mal choisi. Un « entrepreneur général » qui pose des fenêtres ne sortira jamais sur « menuisier »."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que cet agent ne fera pas", classe='non',
       items=[
        ("mots-cles-locaux", "Vous promettre une position",
         "Personne ne peut garantir une place dans le pack local&nbsp;: la distance entre le chercheur et vous compte, "
         "et vous ne pouvez pas la changer. Ce qu'on peut faire, c'est ne plus perdre sur les critères qui dépendent "
         "de vous."),
        ("demande-avis", "Fabriquer des avis",
         "Une fiche complète sans avis plafonne, mais la solution n'est pas d'en inventer. On branche la demande "
         "d'avis à tous vos clients&nbsp;— voir "
         "<a href=\"https://decupler.com/obtenir-des-avis-google/\">obtenir des avis Google</a>."),
        ("citations-locales", "Ignorer le reste de votre présence",
         "Une fiche parfaite avec une adresse écrite différemment sur trois annuaires reste bancale. C'est le travail "
         "des <a href=\"https://decupler.com/citations-locales/\">citations locales</a>, qu'on branche en même temps."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="La fiche n'est qu'une porte",
       paras=["Être trouvé ne sert à rien si l'appel qui suit n'est pas décroché. Le catalogue complet des quinze "
              f"agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["citations-locales", "posts-google", "mots-cles-locaux", "demande-avis"])),
     ('relance', dict(texte="Je regarde votre fiche en direct et je vous dis ce qui manque, champ par champ.",
                      libelle="Prendre 15 minutes")),
     ('faq', dict(alt=True, eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Ma fiche existe déjà, vous la refaites&nbsp;?",
         "Non, on la complète. On ne crée une fiche que si vous n'en avez pas, ou si un doublon traîne&nbsp;— auquel "
         "cas on fait fusionner, ce qui est souvent la première chose à régler."),
        ("Combien de temps avant de voir un effet&nbsp;?",
         "Les modifications sont visibles en quelques jours, l'effet sur les positions se juge sur quelques semaines. "
         "C'est un des rares leviers locaux où le travail est fini une fois pour toutes, et non à recommencer."),
        ("Vous avez besoin des accès à ma fiche&nbsp;?",
         "Oui, en tant que gestionnaire&nbsp;— vous restez propriétaire et vous pouvez nous retirer l'accès à tout "
         "moment. On ne demande jamais le transfert de propriété."),
        ("C'est facturé combien&nbsp;?",
         f"Rien à l'unité&nbsp;: cet agent fait partie de l'abonnement mensuel qui démarre à 199&nbsp;€, la création "
         f"du site étant offerte. Voir <a href=\"{PILIER}\">le détail de l'offre</a>."),
       ])),
    ]),

"agent-posts-google": dict(
    mot_cle="posts google my business automatiques",
    titre_seo="Posts Google automatiques : une photo, un post publié",
    meta=("Vous photographiez déjà vos chantiers. Envoyez la photo par SMS : le post part sur votre "
          "fiche Google, rédigé et optimisé. Inclus dans l'offre site offert."),
    signature=SIG_AVIS,
    sections=[
     ('hero', dict(
       kicker="Agent · Posts Google automatiques",
       h1="Vous prenez déjà les photos.<br>Elles dorment dans votre <em>téléphone</em>.",
       leads=["<strong>Une fiche Google qui publie est une fiche vivante&nbsp;;</strong> une fiche muette depuis huit "
              "mois envoie le signal inverse, à Google comme au client qui hésite.",
              "Le geste demandé tient en dix secondes&nbsp;: vous envoyez une photo de chantier par SMS. L'agent "
              "écrit le texte avec le vocabulaire de votre métier et de votre ville, et publie."],
       cta="Voir ce que ça donnerait", sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois",
       phone=[("call", "Vous · 17:22", "📷 Photo du chantier"),
              ("sms", "Post publié", "«&nbsp;Terrasse bois posée cette semaine à Vitry — 24&nbsp;m², essence "
                                     "douglas.&nbsp;»", "En ligne")])),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="Comment un post part depuis un SMS&nbsp;?",
       reponse="Vous envoyez la photo à un numéro dédié, avec deux mots si vous voulez préciser. L'agent identifie la "
               "prestation, écrit un texte court intégrant votre métier et votre commune, ajoute un bouton d'appel, "
               "et publie sur votre fiche. Vous recevez le post en retour&nbsp;: un mot suffit à le faire retirer.",
       paras=["Ce que ça vaut&nbsp;: chaque post ajoute à votre fiche du vocabulaire réel — un nom de prestation, une "
              "commune, un matériau — que vous n'aviez nulle part ailleurs."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que cet agent ne fera pas", classe='non',
       items=[
        ("posts-google", "Publier sans vos photos",
         "On ne va pas chercher d'images en banque. Si vous n'envoyez rien pendant deux mois, la fiche ne publie rien "
         "— et c'est mieux que de publier des photos qui ne sont pas les vôtres."),
        ("satisfaction", "Publier des avant/après dans tous les métiers",
         "Dans la santé et l'esthétique, les avant/après tombent sous des règles strictes. Selon votre activité, "
         "l'agent est configuré pour ne publier que du factuel&nbsp;: prestation, lieu, matériel."),
        ("mots-cles-locaux", "Remplacer un vrai travail de mots-clés",
         "Le post reprend le vocabulaire qu'on lui a donné. C'est la recherche de mots-clés locaux qui décide de ce "
         "vocabulaire, pas l'agent de publication."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="Publier ne suffit pas à être trouvé",
       paras=[f"Le catalogue complet des quinze agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["fiche-google", "citations-locales", "mots-cles-locaux", "demande-avis"])),
     ('relance', dict(texte="Envoyez-moi une photo de votre dernier chantier&nbsp;: je vous montre le post qui en sortirait.",
                      libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Je dois envoyer une photo tous les combien&nbsp;?",
         "Une à deux par mois suffisent à tenir une fiche vivante. Il n'y a aucune obligation&nbsp;: le reste du "
         "système tourne même si vous n'envoyez jamais rien."),
        ("Je peux relire avant publication&nbsp;?",
         "Par défaut le post part directement et vous le recevez en retour. Si vous préférez valider avant, on bascule "
         "l'agent en mode relecture&nbsp;— ça se règle en une minute."),
        ("Et si la photo est ratée&nbsp;?",
         "L'agent le dit et ne publie pas. Une photo floue ou mal cadrée sur une fiche fait plus de mal qu'une fiche "
         "sans photo récente."),
        ("Ça marche aussi pour les réseaux sociaux&nbsp;?",
         "L'agent publie sur la fiche Google, qui est l'endroit où la décision se prend en recherche locale. On peut "
         "brancher d'autres destinations, mais on ne commence jamais par là."),
       ])),
    ]),

"agent-mots-cles-locaux": dict(
    mot_cle="recherche de mots-clés locaux",
    titre_seo="Mots-clés locaux : viser ce que vos clients tapent",
    meta=("On arrête de se battre sur « plombier Paris » pour viser les requêtes de votre zone à "
          "forte intention et faible concurrence. Inclus dans l'offre site offert."),
    signature=SIG_AVIS,
    sections=[
     ('hero', dict(
       kicker="Agent · Recherche de mots-clés locaux",
       h1="« Plombier Paris » ne vous<br>amènera <em>jamais</em> un client.",
       leads=["<strong>Le mot-clé évident est celui sur lequel tout le monde se bat, et personne de votre taille ne "
              "gagne.</strong> Pendant ce temps, des dizaines de requêtes précises, à forte intention et à faible "
              "concurrence, sont libres dans votre zone.",
              "L'agent isole ces requêtes-là, et c'est elles que le site et la fiche vont viser."],
       cta="Voir mes requêtes libres", sous_cta="Gratuit · sans engagement", viz="pilote")),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="Qu'est-ce qu'un mot-clé local qui vaut le coup&nbsp;?",
       reponse="Trois conditions&nbsp;: il est tapé dans votre zone, il exprime une intention d'achat et non une "
               "curiosité, et sa difficulté est à votre portée. Une requête à 40 recherches par mois que vous prenez "
               "vaut mieux qu'une requête à 3 000 sur laquelle vous serez toujours en page trois.",
       paras=["C'est exactement le raisonnement qu'on applique à notre propre site&nbsp;: on ne vise que ce qu'on peut "
              "prendre, et on le dit quand une requête est hors de portée."])),
     ('etapes', dict(
       alt=True, eyebrow="La méthode", h2="Comment on trie",
       items=[
        ("On part de vos prestations réelles",
         "Pas d'une liste générique de métier. Ce que vous facturez vraiment, dans l'ordre de ce qui vous rapporte."),
        ("On mesure volume, difficulté et intention",
         "Chaque requête reçoit ses trois chiffres. Une requête sans intention commerciale est écartée même si le "
         "volume est beau."),
        ("On compare à votre autorité réelle",
         "Un site neuf ne prend pas les mêmes requêtes qu'un site installé depuis dix ans. On vous dit franchement "
         "ce qui est hors de portée, et pour combien de temps."),
        ("On répartit sur les pages",
         "Une requête par page, jamais deux pages sur la même&nbsp;: c'est comme ça qu'on évite de se cannibaliser "
         "soi-même."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="Savoir quoi viser, puis le viser",
       paras=[f"Le catalogue complet des quinze agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["fiche-google", "citations-locales", "posts-google", "rapport-mensuel"])),
     ('relance', dict(texte="Donnez-moi votre métier et votre ville&nbsp;: je vous sors les requêtes libres dans votre zone.",
                      libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Vous garantissez la première page&nbsp;?",
         "Non, et personne ne le peut honnêtement. Ce qu'on garantit, c'est de ne viser que des requêtes à votre "
         "portée et de vous montrer chaque mois où vous en êtes."),
        ("C'est un travail à refaire souvent&nbsp;?",
         "Le socle tient des années. On le revoit quand vous ajoutez une prestation, quand vous élargissez votre zone, "
         "ou quand les données montrent qu'une requête neuve est apparue."),
        ("Vous utilisez quels outils&nbsp;?",
         "Les données de volume et de difficulté viennent d'Ubersuggest, et les requêtes réelles de votre Search "
         "Console une fois le site en ligne. Les deuxièmes valent mieux que les premières&nbsp;: ce sont vos clients."),
        ("Et pour la visibilité dans les IA&nbsp;?",
         "C'est un autre exercice, avec d'autres requêtes&nbsp;— voir notre approche de la "
         "<a href=\"https://decupler.com/visibilite-llm/\">visibilité dans les LLM</a>."),
       ])),
    ]),

"agent-sms-appel-manque": dict(
    mot_cle="sms sur appel manqué",
    titre_seo="SMS sur appel manqué : rattraper l'appel qu'on rate",
    meta=("Vous ne décrochez pas : le client reçoit un SMS dans la seconde, à votre nom, avant "
          "d'avoir composé le numéro suivant. Inclus dans l'offre site offert."),
    signature=SIG_AGENT,
    sections=[
     ('hero', dict(
       kicker="Agent · SMS sur appel manqué",
       h1="Il ne laisse pas de message.<br>Il appelle le <em>suivant</em>.",
       leads=["<strong>Moins d'un appelant sur trois laisse un message sur une boîte vocale.</strong> Les autres "
              "raccrochent et composent le numéro d'après. Cet appel-là n'apparaît nulle part dans votre journée&nbsp;: "
              "vous ne saurez jamais qu'il a existé.",
              "L'agent envoie un SMS à votre nom dans la seconde qui suit, avec le lien de votre formulaire. Le client "
              "vous attend au lieu d'appeler ailleurs."],
       cta="Voir ce que ça donnerait", sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois",
       phone=[("call", "06 12 •• •• 41", "Appel entrant · 14:32"),
              ("miss", "Appel manqué", "Vous êtes sur un chantier"),
              ("sms", "SMS envoyé", "«&nbsp;Ici Dupont Paysage. Je vous rappelle très vite.&nbsp;»",
               "Client retenu")])),
     ('bande', dict(
       lbl_g="Sans l'agent", ic_g="sms-appel-manque", lbl_d="Avec", ic_d="sms-formulaire",
       cnt=("L'appel manqué ne laisse aucune trace",
            "Ni message, ni rappel, ni ligne dans une statistique. Le client est parti et vous n'avez rien vu.",
            "Le SMS part avant qu'il ait raccroché",
            "À votre nom, avec le lien de votre formulaire. Vous rappelez quand vous descendez du toit."))),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="Comment un appel manqué déclenche un SMS&nbsp;?",
       reponse="Un numéro de suivi, géographique et non surtaxé, se pose devant votre ligne et renvoie sur votre "
               "portable. Si personne ne décroche après le nombre de sonneries que vous choisissez, le SMS part "
               "automatiquement à l'appelant, signé de votre nom. Vous gardez votre numéro, votre téléphone et votre "
               "forfait.",
       paras=["C'est l'agent le plus simple du catalogue et souvent le premier qu'on branche&nbsp;: il ne demande "
              "aucune décision, aucun apprentissage, et il travaille dès le premier appel raté."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que cet agent ne fera pas", classe='non',
       items=[
        ("agent-vocal", "Répondre à la place de quelqu'un",
         "Il envoie un message écrit, il ne tient pas de conversation. Si vous voulez qu'une voix décroche et pose le "
         "rendez-vous, c'est <a href=\"https://decupler.com/agent-vocal-ia/\">l'agent vocal</a>."),
        ("relance-devis", "Qualifier la demande",
         "Le SMS annonce que vous rappelez. Il ne demande ni le motif ni l'adresse&nbsp;: un message trop long ou "
         "trop curieux fait fuir. La qualification, c'est le rôle du vocal ou de l'assistant du site."),
        ("satisfaction", "Vous faire gagner du temps",
         "Il ne réduit pas votre charge d'appels, il l'augmente&nbsp;— parce que vous rappelez des gens qui seraient "
         "partis. C'est du chiffre d'affaires, pas du confort. Autant le dire avant."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="Le SMS rattrape. Il ne convertit pas",
       paras=[f"Le catalogue complet des quinze agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["agent-vocal", "sms-formulaire", "chatbot", "rappel-rdv"])),
     ('relance', dict(texte="Quinze minutes&nbsp;: on regarde combien d'appels vous ratez vraiment dans une semaine.",
                      libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Le numéro de suivi est-il surtaxé&nbsp;?",
         "Non. C'est un numéro géographique classique&nbsp;: l'appelant paie un appel local. C'est l'inverse des "
         "réseaux de dépannage qui facturent la mise en relation."),
        ("Je dois changer de numéro sur mes devis et mon camion&nbsp;?",
         "Non. Le numéro de suivi ne sert que sur le site et la fiche Google, là où on peut mesurer. Votre numéro "
         "historique continue de fonctionner exactement comme avant."),
        ("Et si l'appelant est un démarcheur&nbsp;?",
         "Il reçoit un SMS et ça s'arrête là. Le coût est négligeable et le filtrage automatique ferait plus de dégâts "
         "qu'il n'en éviterait&nbsp;: un vrai client mal classé, c'est un client perdu."),
        ("Ça marche la nuit et le week-end&nbsp;?",
         "Oui, et c'est là que ça rapporte le plus, parce que vos concurrents ne décrochent pas non plus. Vous pouvez "
         "adapter le texte du message selon l'horaire."),
       ])),
    ]),

"agent-sms-formulaire": dict(
    mot_cle="alerte sms formulaire de contact",
    titre_seo="SMS instantané sur formulaire : rappeler avant les autres",
    meta=("Une demande arrive sur le site : vous avez le nom et le numéro par SMS, avant même "
          "d'avoir ouvert votre boîte mail. Inclus dans l'offre site offert."),
    signature=SIG_AGENT,
    sections=[
     ('hero', dict(
       kicker="Agent · SMS instantané sur formulaire",
       h1="Une demande par mail<br>se lit le soir. Trop <em>tard</em>.",
       leads=["<strong>Celui qui rappelle en premier signe.</strong> Une demande envoyée à 10&nbsp;h et lue à "
              "19&nbsp;h a eu le temps d'aller chez deux concurrents, qui ont peut-être déjà rappelé.",
              "L'agent vous envoie le nom et le numéro par SMS dans la seconde. Le prospect, lui, reçoit une "
              "confirmation immédiate&nbsp;: il sait que sa demande est arrivée quelque part."],
       cta="Voir ce que ça donnerait", sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois",
       phone=[("call", "Formulaire · 10:04", "Nouvelle demande"),
              ("sms", "À rappeler", "Claire M. · 06 71 •• •• 09 · Devis salle de bain · Vitry",
               "Reçu en 4 s")])),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="Pourquoi un SMS plutôt qu'un e-mail&nbsp;?",
       reponse="Parce qu'un SMS est lu dans les minutes qui suivent, et un e-mail professionnel le soir. Sur une "
               "demande de devis, ce décalage décide souvent de qui obtient le rendez-vous. L'agent vous transmet le "
               "nom, le numéro et le motif&nbsp;; le prospect reçoit une confirmation à votre nom.",
       paras=["Le message qui part au prospect compte autant que celui qui vous arrive&nbsp;: il évite le doute — "
              "« est-ce que ça a marché&nbsp;? » — qui pousse à remplir le formulaire du concurrent d'à côté."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que cet agent ne fera pas", classe='non',
       items=[
        ("chatbot", "Qualifier à votre place",
         "Il transmet ce que le formulaire a collecté. Si votre formulaire pose trois questions, vous recevez trois "
         "réponses. La qualification fine, c'est l'assistant du site&nbsp;— voir "
         "<a href=\"https://decupler.com/chatbot-wordpress/\">chatbot WordPress</a>."),
        ("relance-devis", "Relancer si vous ne rappelez pas",
         "L'agent vous prévient une fois. Si la demande reste sans suite, c'est un autre agent qui prend le relais, "
         "et il faut le brancher volontairement."),
        ("satisfaction", "Trier les demandes sérieuses",
         "Vous recevrez aussi des demandes creuses. On préfère vous laisser juger&nbsp;: un filtre automatique finit "
         "toujours par écarter un vrai client."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="Recevoir vite, puis ne pas laisser retomber",
       paras=[f"Le catalogue complet des quinze agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["sms-appel-manque", "chatbot", "relance-devis", "rappel-rdv"])),
     ('relance', dict(texte="On regarde votre formulaire actuel et ce qu'il devient une fois envoyé.",
                      libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Je reçois le SMS sur combien de numéros&nbsp;?",
         "Autant que vous voulez&nbsp;: vous, votre associé, votre assistante. Chacun peut avoir sa règle selon le "
         "type de demande."),
        ("Et si je suis en congés&nbsp;?",
         "Le message envoyé au prospect s'adapte&nbsp;: on annonce un délai de rappel réaliste plutôt que de le "
         "laisser attendre. Une attente annoncée fait beaucoup moins de dégâts qu'un silence."),
        ("Ça remplace mon logiciel de devis&nbsp;?",
         "Non, ça se pose devant. Vous continuez à travailler avec vos outils&nbsp;; l'agent ne fait que raccourcir le "
         "délai entre la demande et votre rappel."),
        ("Le prospect reçoit quoi exactement&nbsp;?",
         "Un message court à votre nom qui confirme la réception et annonce quand vous rappelez. Pas de publicité, pas "
         "de lien de suivi&nbsp;: juste ce qui le rassure."),
       ])),
    ]),

"agent-relance-devis": dict(
    mot_cle="relance de devis automatique",
    titre_seo="Relance de devis : le trou le plus cher, et personne ne le bouche",
    meta=("Vos devis restés sans réponse repartent à J+3 puis à J+7, poliment, sans que vous ayez "
          "à y penser. Inclus dans l'offre site offert."),
    signature=SIG_AGENT,
    sections=[
     ('hero', dict(
       kicker="Agent · Relance de devis",
       h1="Le devis part.<br>Et puis plus <em>rien</em>.",
       leads=["<strong>C'est le trou le plus cher de votre activité, et le seul que personne ne bouche.</strong> "
              "Vous avez passé deux heures à chiffrer, le client a dit qu'il regardait, et trois semaines plus tard "
              "vous n'osez plus rappeler.",
              "L'agent relance à J+3 puis à J+7, à votre nom, sur un ton neutre. Et il s'arrête net dès que le client "
              "répond."],
       cta="Voir ce que ça donnerait", sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois", viz="transforme")),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="À quoi ressemble une relance qui ne braque pas&nbsp;?",
       reponse="Trois lignes, à votre nom&nbsp;: le devis est toujours valable, vous restez disponible pour les "
               "questions, et vous demandez simplement si le projet suit son cours. Aucune remise, aucune urgence "
               "fabriquée, aucun rappel du montant. La séquence s'arrête dès la première réponse.",
       paras=["La réponse la plus fréquente n'est pas un refus&nbsp;: c'est « ah oui, pardon, j'avais oublié de vous "
              "répondre ». C'est exactement le devis que vous aviez perdu."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que cet agent ne fera pas", classe='non',
       items=[
        ("relance-devis", "Relancer indéfiniment",
         "Deux relances, puis plus rien. Une troisième n'apporte presque aucune réponse supplémentaire et transforme "
         "un suivi en harcèlement&nbsp;— ce qui vous coûte le client suivant, pas seulement celui-là."),
        ("satisfaction", "Négocier ou baisser le prix",
         "L'agent ne propose jamais de remise. Une relance qui s'accompagne d'une réduction apprend à vos clients à "
         "attendre pour payer moins cher."),
        ("chatbot", "Écrire à votre place la première fois",
         "Vous relisez et validez le texte des deux relances avant qu'elles ne partent la première fois. Ensuite, "
         "elles tournent seules."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="Relancer, puis ne pas rater le rendez-vous",
       paras=[f"Le catalogue complet des quinze agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["rappel-rdv", "reactivation", "sms-formulaire", "rapport-mensuel"])),
     ('relance', dict(texte="Combien de devis avez-vous envoyés le mois dernier sans jamais avoir de réponse&nbsp;? "
                            "On regarde ensemble ce que ça représente.",
                      libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Comment l'agent sait qu'un devis est parti&nbsp;?",
         "Soit vous le marquez envoyé dans votre outil, soit vous mettez l'agent en copie de l'e-mail. Les deux "
         "fonctionnent&nbsp;; le second ne demande aucun changement d'habitude."),
        ("Et si le client a déjà répondu par téléphone&nbsp;?",
         "Vous marquez le devis comme traité et la séquence s'arrête. C'est le seul geste demandé, et il évite la "
         "relance embarrassante."),
        ("Le message vient de mon adresse&nbsp;?",
         "Oui, à votre nom et depuis votre adresse. Le client ne voit jamais passer d'outil tiers."),
        ("Ça marche pour les devis papier&nbsp;?",
         "Oui, à condition d'avoir le contact du client dans le système. La relance part par e-mail ou par SMS selon "
         "ce dont vous disposez."),
       ])),
    ]),

"agent-rappel-rdv": dict(
    mot_cle="rappel de rendez-vous automatique",
    titre_seo="Rappel de rendez-vous : ne plus se déplacer pour rien",
    meta=("SMS de confirmation à la prise de rendez-vous, rappel automatique 24 h avant. Le client "
          "confirme la veille. Inclus dans l'offre site offert."),
    signature=SIG_AGENT,
    sections=[
     ('hero', dict(
       kicker="Agent · Confirmation et rappel de rendez-vous",
       h1="Un créneau libéré la veille<br>se <em>recase</em>. Pas celui qu'on découvre vide.",
       leads=["<strong>Un rendez-vous oublié coûte deux fois&nbsp;:</strong> l'heure perdue, et le client qui aurait "
              "pu la prendre. Dans un cabinet, c'est un fauteuil vide&nbsp;; chez un artisan, ce sont trente "
              "kilomètres pour rien.",
              "L'agent confirme à la prise du rendez-vous, puis rappelle la veille avec la possibilité de décaler en "
              "un mot. C'est le poste où le retour se voit le plus vite, parce qu'il se chiffre."],
       cta="Voir ce que ça donnerait", sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois",
       phone=[("call", "Confirmation", "Mardi 14&nbsp;h · noté"),
              ("sms", "Rappel · la veille", "«&nbsp;Rendez-vous demain 14&nbsp;h. Répondez OK, ou DECALER.&nbsp;»",
               "Confirmé")])),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="Pourquoi deux messages et pas un&nbsp;?",
       reponse="Le premier, à la prise du rendez-vous, ancre la date et donne une trace écrite&nbsp;: c'est lui qui "
               "évite l'erreur de créneau. Le second, la veille, sert à décider&nbsp;— il propose explicitement de "
               "décaler, parce qu'un client qui décale la veille vaut infiniment mieux qu'un client qui ne vient pas.",
       paras=["La formulation compte&nbsp;: proposer le report ne fait pas annuler davantage. Ça fait annuler "
              "<em>plus tôt</em>, ce qui est exactement ce qu'on cherche."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que cet agent ne fera pas", classe='non',
       items=[
        ("rappel-rdv", "Remplir le créneau libéré",
         "Il vous prévient qu'un créneau se libère, il ne trouve pas le remplaçant. C'est la réactivation des clients "
         "en attente qui fait ce travail, et il faut la brancher volontairement."),
        ("satisfaction", "Rappeler indéfiniment",
         "Une confirmation, un rappel. Un troisième message la veille au soir agace, et un client agacé annule."),
        ("chatbot", "Gérer votre agenda à votre place",
         "Il lit votre agenda, il ne le réorganise pas. Les arbitrages de planning restent les vôtres."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="Le rendez-vous tenu n'est qu'une étape",
       paras=[f"Le catalogue complet des quinze agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["agent-vocal", "relance-devis", "satisfaction", "reactivation"])),
     ('relance', dict(texte="Combien de rendez-vous non honorés par mois&nbsp;? Multipliez par votre panier moyen&nbsp;: "
                            "on regarde ce chiffre ensemble.",
                      libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Ça se branche sur mon agenda&nbsp;?",
         "Sur les agendas courants, oui. Sinon l'agent fonctionne sur les rendez-vous saisis dans son propre "
         "calendrier, ce qui reste plus simple que de changer d'outil."),
        ("SMS ou e-mail&nbsp;?",
         "SMS par défaut&nbsp;: le taux de lecture n'a rien à voir. L'e-mail vient en complément quand le rendez-vous "
         "demande des documents à préparer."),
        ("Et si le client répond au SMS&nbsp;?",
         "La réponse vous arrive. « OK » confirme automatiquement, « DECALER » vous alerte, et tout autre message "
         "vous est transmis tel quel."),
        ("Ça convient à un cabinet de santé&nbsp;?",
         "Oui, et c'est là que ça rapporte le plus. Le message ne contient jamais le motif de la consultation&nbsp;: "
         "date, heure, nom du praticien, rien d'autre."),
       ])),
    ]),

"agent-reactivation": dict(
    mot_cle="réactivation clients dormants",
    titre_seo="Réactivation des clients dormants : le fichier qu'on oublie",
    meta=("Vos clients d'il y a deux ans reçoivent un mot. Il y en a toujours quelques-uns qui "
          "avaient un projet en tête. Inclus dans l'offre site offert."),
    signature=SIG_AGENT,
    sections=[
     ('hero', dict(
       kicker="Agent · Réactivation des clients dormants",
       h1="Le client le moins cher<br>est celui que vous avez <em>déjà</em>.",
       leads=["<strong>Vous avez un fichier de clients satisfaits que personne n'a rappelés depuis deux ans.</strong> "
              "Ils n'ont pas changé de maison, ni de dents, ni de jardin. Certains ont un projet en tête et ne pensent "
              "simplement plus à vous.",
              "L'agent repère ceux qui n'ont pas eu de contact depuis douze mois et leur envoie un mot adapté à votre "
              "métier. C'est le canal le moins cher de tous&nbsp;: la confiance est déjà faite."],
       cta="Voir ce que ça donnerait", sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois", viz="capitalise")),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="Qu'est-ce qu'on écrit à un client de 2024&nbsp;?",
       reponse="Rien qui ressemble à une newsletter. Un message court, à votre nom, qui rappelle la prestation faite "
               "chez lui et propose la suite logique&nbsp;: le contrôle annuel, l'entretien de saison, la reprise du "
               "chantier laissé de côté. Un seul envoi, sans relance.",
       paras=["Le taux de réponse d'une réactivation bien écrite dépasse celui de n'importe quelle campagne vers des "
              "inconnus, pour une raison simple&nbsp;: ces gens vous connaissent et vous ont déjà payé."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que cet agent ne fera pas", classe='non',
       items=[
        ("reactivation", "Écrire à des gens qui ne vous connaissent pas",
         "L'agent ne travaille que sur vos clients. Il n'achète aucun fichier et n'envoie rien à des contacts qui "
         "n'ont jamais eu affaire à vous&nbsp;— c'est du démarchage, et ce n'est ni notre métier ni sans risque."),
        ("satisfaction", "Relancer plusieurs fois",
         "Un envoi, une fois par an au maximum. Un client dormant qui reçoit trois messages devient un client qui se "
         "désabonne."),
        ("posts-google", "Remplacer votre mémoire",
         "L'agent envoie ce que vos données lui permettent d'envoyer. Si vos fiches clients sont vides, le message "
         "sera générique — et un message générique ne réactive personne."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="Réveiller, puis ne pas laisser retomber",
       paras=[f"Le catalogue complet des quinze agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["relance-devis", "rappel-rdv", "demande-avis", "rapport-mensuel"])),
     ('relance', dict(texte="Combien de clients avez-vous servis il y a deux ans et jamais recontactés depuis&nbsp;?",
                      libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Et le RGPD&nbsp;?",
         "Il s'agit de vos propres clients, contactés au sujet d'une prestation comparable à celle qu'ils ont déjà "
         "achetée&nbsp;: c'est le cadre habituel de la prospection vers une clientèle existante. Chaque message porte "
         "un moyen simple de ne plus être contacté, et l'agent le respecte."),
        ("Je n'ai pas de fichier client propre.",
         "C'est le cas le plus fréquent. On part de ce que vous avez&nbsp;— factures, agenda, carnet — et on construit "
         "la base au fur et à mesure. Le premier envoi est souvent partiel&nbsp;; le deuxième ne l'est plus."),
        ("Quel message pour mon métier&nbsp;?",
         "Il change du tout au tout&nbsp;: contrôle annuel pour un cabinet, entretien de printemps pour un paysagiste, "
         "révision de chaudière pour un chauffagiste. On l'écrit avec vous la première fois."),
        ("À quelle fréquence&nbsp;?",
         "Une fois par an et par client, pas plus. La réactivation est un levier puissant précisément parce qu'on ne "
         "s'en sert pas souvent."),
       ])),
    ]),

"agent-satisfaction": dict(
    mot_cle="suivi de satisfaction client sms",
    titre_seo="Suivi de satisfaction : savoir avant que ce soit écrit",
    meta=("Un SMS de satisfaction part à la fin de l'intervention. S'il est négatif, vous êtes "
          "alerté pour rappeler. Inclus dans l'offre site offert."),
    signature=SIG_AVIS,
    sections=[
     ('hero', dict(
       kicker="Agent · Suivi de satisfaction",
       h1="Le rappeler le soir même,<br>ou le lire sur Google <em>samedi</em>.",
       leads=["<strong>Un client mécontent qui n'a rien dit finit toujours par l'écrire quelque part.</strong> Entre "
              "le moment où il repart contrarié et celui où il publie, il y a souvent deux ou trois jours&nbsp;: c'est "
              "la seule fenêtre où vous pouvez encore agir.",
              "L'agent envoie un SMS de satisfaction en fin d'intervention. S'il est négatif, vous êtes alerté "
              "immédiatement. Rien n'est publié, rien n'est filtré&nbsp;: c'est du service."],
       cta="Voir ce que ça donnerait", sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois",
       phone=[("call", "Intervention terminée", "Mardi · 16:40"),
              ("miss", "Retour reçu", "«&nbsp;Bof, la finition m'a déçu.&nbsp;»"),
              ("sms", "Vous êtes alerté", "Rappelez M. Perrin aujourd'hui", "Avant Google")])),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="En quoi c'est différent du filtrage d'avis&nbsp;?",
       reponse="Le filtrage consiste à sonder d'abord et à n'envoyer sur Google que les clients contents&nbsp;: c'est "
               "interdit, et sanctionné jusqu'à la suspension du profil. Ici, la demande d'avis part à tout le monde, "
               "sans exception. Le SMS de satisfaction est un canal séparé, qui revient chez vous et ne conditionne "
               "rien.",
       paras=["La différence n'est pas cosmétique&nbsp;: dans un cas vous triez vos clients avant de les exposer, dans "
              "l'autre vous rattrapez un mécontent. Beaucoup d'outils vendent le premier en l'appelant le second."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que cet agent ne fera pas", classe='non',
       items=[
        ("demande-avis", "Empêcher un avis négatif",
         "Le client reste libre d'écrire ce qu'il veut, quand il veut. L'agent vous donne quelques jours d'avance, "
         "pas un droit de veto."),
        ("satisfaction", "Décider à votre place de rappeler",
         "Il alerte. Le rappel, c'est vous, et c'est lui qui fait toute la valeur du dispositif. Un agent branché sans "
         "personne pour rappeler ne sert à rien."),
        ("reponse-avis", "Servir de conditionnement à la demande d'avis",
         "Les deux agents sont indépendants par construction. On refuse de les enchaîner, même quand on nous le "
         "demande&nbsp;— voir <a href=\"https://decupler.com/obtenir-des-avis-google/\">obtenir des avis Google</a>."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="Savoir, répondre, et faire venir les bons avis",
       paras=[f"Le catalogue complet des quinze agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["demande-avis", "reponse-avis", "rappel-rdv", "rapport-mensuel"])),
     ('relance', dict(texte="On regarde vos derniers avis négatifs&nbsp;: combien auraient pu être rattrapés avant "
                            "d'être écrits&nbsp;?",
                      libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Le SMS demande une note&nbsp;?",
         "Une question simple, en une ligne, avec une réponse en un mot ou une note courte. Plus le message est "
         "court, plus il obtient de réponses."),
        ("Le client comprend que ça ne va pas sur Google&nbsp;?",
         "Le message le dit&nbsp;: c'est un retour direct à l'entreprise. Aucune ambiguïté, aucun lien vers une "
         "plateforme."),
        ("Et si personne ne répond&nbsp;?",
         "C'est fréquent, et ce n'est pas grave&nbsp;: le dispositif ne coûte rien de plus. Ce sont les retours "
         "négatifs qui font sa valeur, et ceux-là arrivent."),
        ("Vous conservez les réponses&nbsp;?",
         "Elles vous appartiennent et vous restent accessibles. Selon votre métier, on restreint ce qui peut être "
         "demandé&nbsp;— dans la santé, par exemple, aucune question sur le soin lui-même."),
       ])),
    ]),

"agent-rapport-mensuel": dict(
    mot_cle="rapport mensuel agents",
    titre_seo="Rapport mensuel : le compte de ce qui a été rattrapé",
    meta=("Chaque mois, le compte exact de ce que le système a récupéré : appels rattrapés, devis "
          "relancés, avis, rendez-vous. Inclus dans l'offre site offert."),
    signature=SIG_AGENT,
    sections=[
     ('hero', dict(
       kicker="Agent · Rapport mensuel",
       h1="Sans preuve chiffrée,<br>un abonnement finit <em>résilié</em>.",
       leads=["<strong>C'est vrai, et c'est sain.</strong> Un service qu'on paie tous les mois sans jamais voir ce "
              "qu'il rapporte finit toujours par sauter, souvent au mauvais moment.",
              "Chaque mois, vous recevez le compte&nbsp;: appels rattrapés, devis relancés, avis obtenus, rendez-vous "
              "pris. Pas un tableau de bord à consulter&nbsp;— quatre chiffres, dans un message."],
       cta="Voir un rapport type", sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois", viz="pilote")),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="Qu'est-ce qu'on compte, exactement&nbsp;?",
       reponse="Des événements, pas des impressions&nbsp;: le nombre d'appels manqués qui ont reçu un SMS, le nombre "
               "de devis relancés et ceux qui ont obtenu une réponse, le nombre d'avis nouveaux, le nombre de "
               "rendez-vous posés par l'agent vocal. Chaque chiffre correspond à une action datée, vérifiable dans "
               "le détail.",
       paras=["Ce qu'on ne compte pas&nbsp;: les « vues », les « impressions » et tout ce qui gonfle un rapport sans "
              "rien prouver. Le seul chiffre qui compte est celui que vous pouvez rapprocher de votre chiffre "
              "d'affaires."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que ce rapport ne prétend pas être", classe='non',
       items=[
        ("rapport-mensuel", "Une attribution parfaite",
         "Un appel rattrapé qui devient un chantier trois semaines plus tard, personne ne peut le tracer "
         "honnêtement. On compte ce qu'on peut compter et on vous dit où s'arrête la mesure."),
        ("mots-cles-locaux", "Un rapport de positionnement",
         "Il ne dit pas où vous êtes classé sur telle requête. C'est un autre sujet, qu'on traite ailleurs et qui "
         "bouge trop pour figurer dans un compte mensuel."),
        ("satisfaction", "Une raison de rester",
         "Si les chiffres sont mauvais deux mois de suite, c'est qu'il faut changer quelque chose ou arrêter. Le "
         "rapport sert autant à ça qu'à justifier l'abonnement."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="Il ne mesure que ce qui tourne",
       paras=["Un rapport sur un système sans agents branchés est une page vide. Le catalogue complet est sur la "
              f"<a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["sms-appel-manque", "relance-devis", "demande-avis", "agent-vocal"])),
     ('relance', dict(texte="Je vous montre un rapport réel, avec les chiffres d'un mois entier.",
                      libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Je reçois ça comment&nbsp;?",
         "Par SMS et par e-mail, le même jour chaque mois. Quatre chiffres dans le message, le détail dans le lien "
         "si vous voulez creuser."),
        ("Je peux voir le détail d'un chiffre&nbsp;?",
         "Oui, ligne par ligne&nbsp;: quel appel, quel jour, quel devis. C'est ce qui distingue un compte d'une "
         "estimation."),
        ("Et si un mois est mauvais&nbsp;?",
         "Vous le verrez, et nous aussi. On regarde ce qui a changé&nbsp;— saison, volume d'appels, agent débranché — "
         "et on ajuste. Un rapport qui n'est jamais mauvais est un rapport qui ne mesure rien."),
        ("Vous comptez les chantiers signés&nbsp;?",
         "Seulement si vous nous les remontez. On ne va pas dans votre comptabilité, et on préfère un chiffre "
         "incomplet mais vrai à une estimation flatteuse."),
       ])),
    ]),

"agent-relance-facture": dict(
    mot_cle="relance de facture impayée",
    titre_seo="Relance de facture impayée : sans jouer le créancier",
    meta=("Vos factures en retard sont relancées à échéance, poliment, sans que vous ayez à jouer "
          "le rôle du créancier. Inclus dans l'offre site offert."),
    signature=SIG_AGENT,
    sections=[
     ('hero', dict(
       kicker="Agent · Relance de facture impayée",
       h1="Vous avez fait le travail.<br>Reste à vous faire <em>payer</em>.",
       leads=["<strong>Relancer une facture est le geste que personne n'a envie de faire.</strong> On repousse, on "
              "se dit qu'on verra la semaine prochaine, et deux mois plus tard on négocie ce qui était dû.",
              "L'agent relance à J+1 puis à J+15, poliment, à votre nom. Vous ne passez jamais pour le créancier "
              "qui court après son argent&nbsp;— et la séquence s'arrête au paiement."],
       cta="Voir ce que ça donnerait", sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois",
       phone=[("call", "Facture 2418 · 3 240 €", "Échéance dépassée · J+1"),
              ("miss", "Sans relance", "Vous n'osez pas rappeler"),
              ("sms", "Rappel envoyé", "«&nbsp;Bonjour, la facture 2418 arrive à échéance. Merci d'avance.&nbsp;»",
               "Payée à J+3")])),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="Quel ton pour une relance qui ne casse pas la relation&nbsp;?",
       reponse="Neutre et court. Le premier message rappelle simplement que l'échéance est passée et joint la "
               "facture&nbsp;: dans la majorité des cas, c'est un oubli. Le second, quinze jours plus tard, "
               "récapitule le montant et propose de vous appeler. Aucune menace, aucune pénalité annoncée&nbsp;: "
               "c'est vous qui décidez si l'affaire doit monter d'un cran.",
       paras=["Ce que ça change vraiment&nbsp;: le premier rappel part le lendemain de l'échéance, pas six semaines "
              "après. Une facture relancée dans la semaine se paie&nbsp;; une facture relancée au bout de deux mois "
              "se négocie."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que cet agent ne fera pas", classe='non',
       items=[
        ("relance-facture", "Faire du recouvrement",
         "Deux rappels courtois, et il s'arrête. Mise en demeure, pénalités, injonction de payer&nbsp;: ce sont des "
         "actes juridiques, avec des formes à respecter. L'agent vous signale le dossier, il ne l'engage pas."),
        ("satisfaction", "Décider à votre place quand ça se tend",
         "À partir du deuxième rappel sans réponse, vous êtes alerté. Certains clients valent qu'on décroche son "
         "téléphone plutôt que d'envoyer un troisième message&nbsp;: ce jugement reste le vôtre."),
        ("rapport-mensuel", "Remplacer votre comptabilité",
         "Il lit les échéances que vous lui donnez. Si vos factures ne sont pas suivies quelque part, il n'a rien à "
         "relancer&nbsp;— et c'est souvent le vrai problème à régler d'abord."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="Du devis à l'encaissement",
       paras=[f"Le catalogue complet des vingt agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["relance-devis", "estimation-en-ligne", "rappel-rdv", "rapport-mensuel"])),
     ('relance', dict(texte="Combien avez-vous en attente de paiement en ce moment&nbsp;? On regarde ce que la relance "
                            "automatique changerait.", libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Ça se branche sur mon logiciel de facturation&nbsp;?",
         "Sur les outils courants, oui. Sinon l'agent travaille sur les échéances que vous lui transmettez, ce qui "
         "reste plus simple que de changer de logiciel pour ça."),
        ("Le message part de mon adresse&nbsp;?",
         "Oui, à votre nom et depuis votre adresse. Le client ne voit jamais passer d'outil tiers, ce qui compte "
         "beaucoup sur ce sujet-là."),
        ("Et si le client a payé entre-temps&nbsp;?",
         "Vous marquez la facture réglée et la séquence s'arrête. Relancer un client qui a déjà payé fait plus de "
         "dégâts que de ne pas relancer du tout."),
        ("Vous ajoutez les pénalités de retard&nbsp;?",
         "Non, pas automatiquement. Elles sont dues de plein droit, mais les faire apparaître dans un rappel change "
         "complètement le ton. On vous laisse ce choix, dossier par dossier."),
       ])),
    ]),

"agent-messagerie-google": dict(
    mot_cle="messagerie fiche google",
    titre_seo="Messagerie de la fiche Google : répondre aux messages",
    meta=("Les messages envoyés depuis votre fiche Google reçoivent une réponse. Aujourd'hui, "
          "presque personne n'y répond. Inclus dans l'offre site offert."),
    signature=SIG_AVIS,
    sections=[
     ('hero', dict(
       kicker="Agent · Messagerie de la fiche Google",
       h1="Il y a une boîte de réception<br>que vous n'ouvrez <em>jamais</em>.",
       leads=["<strong>Votre fiche Google a une messagerie, et des gens y écrivent.</strong> Des questions simples&nbsp;: "
              "« vous êtes ouverts samedi », « vous venez jusqu'à Vitry », « vous prenez de nouveaux clients ». "
              "Presque aucune entreprise locale n'y répond.",
              "Google affiche votre délai de réponse moyen sur la fiche. Un délai long se voit, et il ne donne pas "
              "envie d'écrire."],
       cta="Faire auditer ma fiche", sous_cta="Gratuit · sans engagement", viz="capte")),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="Qui répond aux messages de la fiche&nbsp;?",
       reponse="L'agent surveille la messagerie, répond aux questions courantes à partir de ce qu'il sait de votre "
               "activité — horaires, zone d'intervention, prestations, disponibilité — et vous transmet le contact "
               "dès qu'il s'agit d'un vrai projet. Vous récupérez la conversation avec le nom et le numéro, sans "
               "avoir ouvert l'application.",
       paras=["C'est le pendant, sur Google, de l'assistant du site. Même logique, même liste d'interdits, mais sur "
              "un canal que la plupart des entreprises laissent en friche&nbsp;— donc avec beaucoup moins de "
              "concurrence sur la rapidité de réponse."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que cet agent ne fera pas", classe='non',
       items=[
        ("messagerie-google", "S'engager sur un prix ou un délai",
         "Il donne des ordres de grandeur si vous lui en avez fourni, jamais un devis. Un chiffre annoncé dans une "
         "messagerie Google se retrouve dans un avis six semaines plus tard."),
        ("satisfaction", "Se faire passer pour vous",
         "Il se présente comme un assistant. Sur un canal que le client croit direct, découvrir qu'il parlait à un "
         "robot sans le savoir se paie cher."),
        ("chatbot", "Remplacer l'assistant du site",
         "Ce sont deux canaux distincts avec deux publics&nbsp;: celui qui écrit depuis Google Maps ne fait pas la "
         "même démarche que celui qui a ouvert votre site. Voir "
         "<a href=\"https://decupler.com/chatbot-wordpress/\">chatbot WordPress</a>."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="La fiche complète, vivante, et qui répond",
       paras=[f"Le catalogue complet des vingt agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["fiche-google", "posts-google", "reponse-avis", "chatbot"])),
     ('relance', dict(texte="Je regarde si votre fiche a des messages en attente&nbsp;— il y en a presque toujours.",
                      libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Je ne savais pas que ma fiche avait une messagerie.",
         "C'est le cas de la plupart des gens, et c'est bien le problème. Si elle est activée et sans réponse depuis "
         "des mois, mieux vaut la désactiver que de laisser des messages sans réponse&nbsp;— on regarde ça ensemble."),
        ("Je reçois quoi, moi&nbsp;?",
         "Un SMS avec la question, le nom et le numéro dès que la conversation devient un vrai projet. Les questions "
         "d'horaires ne vous dérangent pas."),
        ("Le délai de réponse affiché sur ma fiche va changer&nbsp;?",
         "Oui, et c'est un des effets les plus visibles. Google met ce délai en avant&nbsp;; passer de « répond en "
         "quelques jours » à « répond en quelques minutes » se remarque."),
        ("Et pour un cabinet de santé&nbsp;?",
         "L'agent est restreint&nbsp;: aucune question médicale, aucun élément clinique conservé. Il oriente vers la "
         "prise de rendez-vous, rien d'autre."),
       ])),
    ]),

"agent-parrainage": dict(
    mot_cle="demande de parrainage client",
    titre_seo="Demande de parrainage : le canal qu'on oublie de demander",
    meta=("Quand un client vient de dire qu'il est content, l'agent lui propose de vous "
          "recommander, avec un message tout prêt. Inclus dans l'offre site offert."),
    signature=SIG_AGENT,
    sections=[
     ('hero', dict(
       kicker="Agent · Demande de parrainage",
       h1="Le meilleur moment pour demander,<br>c'est <em>maintenant</em>.",
       leads=["<strong>Un client qui vient d'écrire qu'il est content est dans le seul état d'esprit où demander ne "
              "coûte rien.</strong> Trois jours plus tard, la fenêtre est fermée&nbsp;: il est passé à autre chose.",
              "Quand le suivi de satisfaction remonte un retour positif, l'agent propose au client de vous "
              "recommander, avec un message tout prêt qu'il n'a qu'à transférer à qui il veut."],
       cta="Voir ce que ça donnerait", sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois",
       phone=[("call", "Retour reçu", "«&nbsp;Très content, merci&nbsp;!&nbsp;»"),
              ("sms", "Proposition envoyée", "«&nbsp;Ravi&nbsp;! Si quelqu'un autour de vous en a besoin, voici un "
                                             "message tout prêt à transférer.&nbsp;»", "1 filleul")])),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="Pourquoi le parrainage marche là où la publicité échoue&nbsp;?",
       reponse="Parce que la confiance est déjà faite. Un client qui vous recommande transfère sa propre "
               "crédibilité&nbsp;: la personne qui reçoit le message ne compare plus trois devis, elle appelle. "
               "C'est le canal le moins cher qui existe, et celui qu'on oublie systématiquement de demander.",
       paras=["Le déclencheur compte plus que le message. L'agent ne demande jamais à froid&nbsp;: il ne se déclenche "
              "qu'après un retour de satisfaction positif, donc auprès de gens qui viennent de dire du bien de vous."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que cet agent ne fera pas", classe='non',
       items=[
        ("parrainage", "Promettre une récompense à votre place",
         "Si vous voulez offrir quelque chose au parrain, c'est votre décision et on l'écrit noir sur blanc. Sans "
         "instruction de votre part, l'agent demande simplement, sans contrepartie&nbsp;— ce qui marche mieux qu'on "
         "ne le croit."),
        ("demande-avis", "Servir de demande d'avis déguisée",
         "Parrainage et avis Google sont deux choses différentes et deux agents distincts. Mélanger les deux dans un "
         "même message fait perdre les deux."),
        ("reactivation", "Demander deux fois",
         "Une proposition par client, après une intervention réussie. Un client relancé sur le parrainage devient un "
         "client qui ne répond plus au suivi de satisfaction."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="Il ne se déclenche jamais seul",
       paras=["Sans suivi de satisfaction, l'agent de parrainage n'a aucun signal pour se déclencher au bon moment. "
              f"Le catalogue complet des vingt agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["satisfaction", "demande-avis", "reactivation", "rapport-mensuel"])),
     ('relance', dict(texte="Combien de vos clients de l'an dernier vous ont amené quelqu'un&nbsp;? Et combien "
                            "auraient pu&nbsp;?", libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Ça ne fait pas insistant&nbsp;?",
         "Le message part une fois, juste après un retour positif, et il propose sans rien demander en retour. C'est "
         "le moment qui fait tout&nbsp;: la même phrase envoyée à froid serait déplacée."),
        ("Je peux offrir une remise au parrain&nbsp;?",
         "Oui, si vous le décidez, et l'agent l'écrira clairement. Attention à ne pas confondre avec la demande "
         "d'avis&nbsp;: là, la contrepartie est interdite."),
        ("Comment je sais qu'un client vient d'un parrainage&nbsp;?",
         "Le message transféré porte un lien qui vous le dit. Ça n'a l'air de rien, mais c'est ce qui vous permet de "
         "remercier le parrain&nbsp;— et c'est ce qui fait qu'il recommence."),
        ("Ça marche dans tous les métiers&nbsp;?",
         "Partout où le bouche-à-oreille compte déjà, donc dans presque tous les métiers locaux. Dans la santé, on "
         "l'écarte&nbsp;: la recommandation de patients relève de règles particulières."),
       ])),
    ]),

"agent-estimation-en-ligne": dict(
    mot_cle="estimation de prix en ligne",
    titre_seo="Estimation en ligne : ne rappeler que des gens qui savent",
    meta=("Le visiteur obtient une fourchette de prix sur le site, et vous ne rappelez que des "
          "gens qui savent déjà à quoi s'attendre. Inclus dans l'offre site offert."),
    signature=SIG_AGENT,
    sections=[
     ('hero', dict(
       kicker="Agent · Estimation en ligne",
       h1="Le premier appel sert<br>à découvrir que ça ne <em>colle pas</em>.",
       leads=["<strong>Sans ordre de grandeur, vous passez vos rappels à qualifier des budgets.</strong> Le visiteur, "
              "lui, n'ose pas demander le prix et va le chercher chez un concurrent qui l'affiche.",
              "L'agent pose quelques questions sur le site et donne une fourchette calculée à partir de vos propres "
              "tarifs. Vous recevez la demande déjà chiffrée."],
       cta="Voir ce que ça donnerait", sous_cta="Site 0&nbsp;€ · puis dès 199&nbsp;€/mois", viz="transforme")),
     ('reponse', dict(
       eyebrow="Ce que fait l'agent", h2="Une estimation, ce n'est pas un devis&nbsp;?",
       reponse="Non, et la page le dit explicitement au visiteur. C'est une fourchette calculée à partir de vos "
               "tarifs et de quelques paramètres&nbsp;: surface, type de prestation, urgence, zone. Elle sert à "
               "écarter les malentendus, pas à vous engager. Le devis reste le vôtre, après visite ou échange.",
       paras=["L'effet le plus net n'est pas le nombre de demandes&nbsp;— il baisse souvent. C'est leur qualité&nbsp;: "
              "vous rappelez des gens qui ont vu un ordre de grandeur et qui appellent quand même."])),
     ('cartes', dict(
       alt=True, eyebrow="Les limites", h2="Ce que cet agent ne fera pas", classe='non',
       items=[
        ("estimation-en-ligne", "Vous engager sur le montant affiché",
         "La fourchette est présentée comme telle, avec les cas où elle ne s'applique pas. Un chiffre présenté comme "
         "ferme sur un site vous suit ensuite dans toutes les négociations."),
        ("relance-devis", "Remplacer la visite",
         "Sur un chantier, aucun outil ne remplace le fait d'aller voir. L'estimation sert à décider si le "
         "déplacement vaut le coup, des deux côtés."),
        ("satisfaction", "Vous amener plus de demandes",
         "Elle en amène souvent moins. Ce sont les demandes hors budget qui disparaissent&nbsp;— celles qui vous "
         "faisaient perdre une heure au téléphone."),
       ])),
     ('agents', dict(
       eyebrow="Ce qui va avec", h2="Qualifier avant, relancer après",
       paras=[f"Le catalogue complet des vingt agents est sur la <a href=\"{PILIER}\">page de l'offre</a>."],
       slugs=["chatbot", "sms-formulaire", "relance-devis", "relance-facture"])),
     ('relance', dict(texte="Donnez-moi vos trois prestations les plus demandées et leurs tarifs&nbsp;: je vous montre "
                            "l'estimation qui en sortirait.", libelle="Prendre 15 minutes")),
     ('faq', dict(eyebrow="FAQ", h2="Les questions qu'on nous pose", items=[
        ("Je ne veux pas afficher mes prix.",
         "Une fourchette n'est pas un tarif public&nbsp;: elle dépend des réponses du visiteur et elle s'affiche à "
         "lui seul. Cela dit, si vous faites du dépannage à domicile, l'affichage de certains prix vous est de toute "
         "façon imposé&nbsp;— voir <a href=\"https://decupler.com/creation-site-internet-plombier/\">la page "
         "plombier</a>."),
        ("Mes concurrents vont voir mes prix.",
         "Ils les connaissent déjà&nbsp;: ils appellent, comme tout le monde. Ce que vous perdez en discrétion, vous "
         "le gagnez en temps sur des rappels qui n'aboutissaient pas."),
        ("Et si mon métier ne se chiffre pas comme ça&nbsp;?",
         "Alors on ne le branche pas. Certaines activités n'ont aucun paramètre exploitable&nbsp;; forcer une "
         "estimation y produit un chiffre faux, ce qui est pire que pas de chiffre du tout."),
        ("Le visiteur reçoit l'estimation par mail&nbsp;?",
         "Elle s'affiche à l'écran, et il peut la recevoir s'il laisse son contact. On ne conditionne jamais "
         "l'affichage à la saisie d'une adresse&nbsp;: c'est le meilleur moyen de le faire partir."),
       ])),
    ]),

}
