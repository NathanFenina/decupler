# -*- coding: utf-8 -*-
"""Pages du cluster « avis Google » et « agents ».

Chaque page décrit ses sections : les guides (intention informationnelle) et
les pages agent (intention commerciale) n'ont pas la même architecture.
Volumes et difficultés relevés sur Ubersuggest (France, français) le
21 août 2026.
"""

RDV = 'https://calendly.com/fenina-nathan/consultationstrategique'
PILIER = 'https://decupler.com/site-internet-offert/'
MAJ = '21 août 2026'
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
    meta=("Supprimer un avis Google : les 6 motifs que Google accepte, la procédure de "
          "signalement, le recours en appel, et ce qui ne marche pas. Guide 2026."),
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

     ('tableau', dict(
       alt=True, eyebrow="Le tri",
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
       eyebrow="La procédure",
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
        "Concrètement, faites d'abord constater l'avis (capture horodatée, idéalement constat d'huissier si l'enjeu le "
        "justifie), puis prenez l'avis d'un avocat. Nous ne sommes pas juristes et cette page ne remplace pas une "
        "consultation&nbsp;— elle sert à ce que vous ne découvriez pas le délai le quatrième mois."],
       tip="Dans l'immense majorité des cas, l'avis qui vous ronge n'est ni diffamatoire ni supprimable. Il est "
           "simplement mal placé dans une liste trop courte. Le travail utile est ailleurs&nbsp;: en faire arriver "
           "d'autres.",
       tip_ic="📌")),

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
         "Oui, à condition de le demander à <strong>tous</strong> vos clients. Depuis 2026, Google interdit "
         "explicitement de trier les clients selon leur note avant de les envoyer sur la fiche, et sanctionne cette "
         "pratique jusqu'à la suspension du profil. Demander à tout le monde est autorisé&nbsp;; filtrer ne l'est pas."),
        ("Que faire pendant que le signalement est en cours&nbsp;?",
         "Répondez à l'avis, calmement et brièvement, sans détailler le dossier. Cette réponse est lue par tous les "
         "prospects suivants&nbsp;: c'est elle qui décide de l'effet réel de l'avis, bien plus que sa présence."),
        ("Vous proposez un service de suppression d'avis&nbsp;?",
         "Non, et méfiez-vous de ceux qui le proposent. On travaille sur ce qui est autorisé et durable&nbsp;: une "
         "fiche complète, un flux d'avis sincères, des réponses systématiques, et une alerte quand un client repart "
         "mécontent."),
       ])),
    ]),

# ══ 2. Répondre aux avis Google — 110/mois, difficulté 22 ═════════════════
"repondre-aux-avis-google": dict(
    mot_cle="répondre aux avis google",
    titre_seo="Répondre aux avis Google : la méthode en 4 temps",
    meta=("Répondre aux avis Google, positifs comme négatifs : la structure d'une bonne réponse, "
          "les erreurs qui coûtent cher, et ce que Google en fait vraiment."),
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

     ('etapes', dict(
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

     ('etapes', dict(
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
          "l'appel et pose le rendez-vous. Ce qu'il fait, ce qu'il ne fait pas, ce que ça coûte."),
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

}
