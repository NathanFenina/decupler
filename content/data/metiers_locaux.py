# -*- coding: utf-8 -*-
"""Cluster « création de site internet pour <métier> ».

Chaque entrée alimente une page fille de /site-internet-offert/.
Les volumes et difficultés viennent d'Ubersuggest (France, français), relevés
le 21 août 2026 — à revérifier avant d'arbitrer une priorité.

Le champ `exclus` est le plus important du fichier : il liste les agents du
catalogue qu'on REFUSE d'activer pour ce métier, et pourquoi. C'est ce qui
sépare une page de vente d'une page qui met le client en infraction.
"""

# (slug, mot-clé, volume/mois, difficulté SEO, CPC €)
CIBLES = [
    ('dentiste',           'création site internet dentiste',            320,  9, 14.72),
    ('plombier',           'création site internet plombier',            110, 14,  4.42),
    ('electricien',        'création site internet électricien',          90, 15,  8.22),
    ('institut-de-beaute', 'création site internet institut de beauté',   90, 15, 15.07),
    ('paysagiste',         'création site internet paysagiste',           20, 10,  6.80),
    ('artisan',            'création site internet artisan',             350, 30,  6.14),
]

PILIER = 'https://decupler.com/site-internet-offert/'
RDV = 'https://calendly.com/fenina-nathan/consultationstrategique'


METIERS = {

"dentiste": dict(
    mot_cle="création site internet dentiste",
    titre_prix="création d'un site internet pour un dentiste",
    dans_ce_metier="dans un cabinet dentaire",
    titre_seo="Création de site internet pour dentiste : le site offert",
    meta=("Création de site internet pour dentiste : on construit le site du cabinet, "
          "vous le voyez terminé, puis vous décidez. Site 0 €, agents dès 199 €/mois."),
    kicker="Création de site internet pour dentiste",
    h1="Votre site, <em>offert</em>.<br>Vous ne payez que les rendez-vous qu'il vous ramène.",
    lead=("<strong>La création du site de votre cabinet ne vous est pas facturée&nbsp;:</strong> on le construit, "
          "vous le voyez terminé, puis vous décidez. Vous ne payez ensuite qu'un abonnement mensuel — hébergement "
          "et agents — à partir de 199&nbsp;€. Pour un cabinet dentaire, l'enjeu n'est pas d'avoir un site&nbsp;: "
          "c'est de ne plus perdre les patients qui appellent pendant que vous êtes en soin."),
    lead2=("Et de ne pas se retrouver en infraction avec le code de déontologie en cherchant à le faire. "
           "Une bonne partie de ce qu'on vend ailleurs aux cabinets dentaires vous est interdit&nbsp;: "
           "<a href=\"#deonto\">on vous dit lequel, et on ne le branche pas</a>."),
    image=("https://decupler.com/wp-content/uploads/2026/08/metier-dentiste-hero.jpg",
           "Une chirurgienne-dentiste consulte son téléphone à l'accueil de son cabinet, entre deux patients"),

    # Le téléphone du hero rejoue la scène propre au métier.
    phone=[("call", "01 42 •• •• 07", "Appel entrant · 15:42"),
           ("miss", "Appel manqué", "Vous êtes au fauteuil"),
           ("sms",  "SMS envoyé",
            "«&nbsp;Cabinet du Dr Meyer. Laissez votre numéro, on vous rappelle.&nbsp;»",
            "Patient retenu")],

    bande=("Le patient rappelle le cabinet suivant",
           "Le fauteuil est occupé, le standard sonne dans le vide. Il cherche « dentiste qui prend de nouveaux "
           "patients » et appelle le troisième résultat.",
           "Il laisse son numéro sans vous déranger",
           "Le SMS part au nom du cabinet. Vous rappelez entre deux patients, sans avoir interrompu un soin."),

    probleme_titre="Un cabinet ne manque pas de patients. Il manque les appels.",
    probleme=("Il est 15&nbsp;h&nbsp;42. Vous êtes sur une reprise de carie, gants aux mains, champ opératoire posé. "
              "Le téléphone sonne à l'accueil&nbsp;: quelqu'un cherche un praticien qui prend de nouveaux patients. "
              "<strong>Personne ne décroche. Il ne laisse pas de message. Il appelle le suivant.</strong> "
              "Vous ne saurez jamais qu'il a existé."),
    probleme2=("La création d'un site internet pour un dentiste ne règle donc pas que la vitrine&nbsp;: elle règle le standard. Et ce n'est pas qu'une affaire d'appels. Le rendez-vous que le patient a oublié et qui laisse "
               "quarante-cinq minutes de fauteuil vide. Le plan de traitement accepté oralement puis jamais reprogrammé. "
               "Les patients de contrôle qui ne sont pas revenus depuis trois ans et que personne n'a rappelés."),
    legende="Le patient le moins cher de votre année, c'est celui qui vous appelait déjà.",

    # Ordre du catalogue partagé : ce sont des slugs de content/data/agents_locaux.py
    agents=["agent-vocal", "sms-appel-manque", "rappel-rdv", "fiche-google",
            "chatbot", "reactivation", "mots-cles-locaux", "rapport-mensuel"],

    # Ce qu'on refuse de brancher, et pourquoi. Avec la source.
    deonto_titre="Ce qu'on ne branchera pas chez vous",
    deonto=[
      ("demande-avis", "Les demandes d'avis Google",
       "C'est l'agent le plus vendu aux cabinets dentaires, et c'est une faute. Le code de déontologie interdit "
       "la communication qui « fait appel à des témoignages de tiers », et l'Ordre considère l'envoi systématique "
       "d'un SMS après consultation comme une sollicitation de témoignages. On ne l'active pas, quel que soit "
       "le métier de votre voisin de palier à qui on l'a vendu."),
      ("posts-google", "Les avant/après et les témoignages de patients",
       "Même logique&nbsp;: pas de témoignages de tiers, pas de comparaison avec d'autres praticiens, et rien qui "
       "incite à un recours inutile aux soins. Votre site parle de votre parcours, de vos compétences et de vos "
       "conditions d'exercice&nbsp;— ce que le décret de décembre 2020 vous autorise explicitement à faire."),
      ("chatbot", "Les données de santé dans le chatbot",
       "L'assistant du site prend un nom, un créneau souhaité et un motif en une ligne. Il ne pose aucune question "
       "médicale et ne conserve aucun élément clinique. C'est un secrétariat qui répond à 21&nbsp;h, pas un dossier patient."),
    ],
    deonto_source=("Décret n° 2020-1658 du 22 décembre 2020",
                   "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042730959",
                   "recommandations de l'Ordre national des chirurgiens-dentistes",
                   "https://www.ordre-chirurgiens-dentistes.fr/pour-le-chirurgien-dentiste/communication-professionnelle-des-chirurgiens-dentistes/"),

    remplace=("À la place, on branche un SMS de satisfaction qui revient <strong>au cabinet</strong>, pas sur Google. "
              "Vous savez qui est reparti mécontent avant qu'il n'écrive quoi que ce soit, et vous rappelez. "
              "C'est du service&nbsp;: ça, rien ne l'interdit."),

    faq=[
      ("Est-ce que tout ça respecte le code de déontologie&nbsp;?",
       "C'est la première question qu'on se pose avant de brancher quoi que ce soit. Depuis le décret de décembre 2020, "
       "vous êtes libre de communiquer au public, y compris sur un site internet, sur vos compétences, votre parcours "
       "et vos conditions d'exercice. Les limites sont claires&nbsp;: pas de témoignages de tiers, pas de comparaison "
       "avec d'autres praticiens, rien qui incite à un recours inutile aux soins. Le site qu'on construit tient dans "
       "ces limites, et les agents qui n'y tiennent pas ne sont pas installés."),
      ("Vous demandez des avis Google à mes patients&nbsp;?",
       "Non. L'Ordre traite l'envoi systématique d'un SMS après consultation comme une sollicitation de témoignages, "
       "donc comme une infraction. On ne le fait pas chez un chirurgien-dentiste, même si l'agent existe pour "
       "d'autres métiers. Ce qui reste autorisé et utile&nbsp;: rendre votre fiche Google complète et trouvable, "
       "et répondre aux avis existants dans les limites du secret professionnel."),
      ("L'agent vocal va-t-il remplacer mon assistante&nbsp;?",
       "Non. Il ne se déclenche que si personne ne décroche&nbsp;— hors horaires, pendant un soin, ou quand la ligne "
       "est déjà occupée. Si votre assistante répond, il ne se passe rien. Il prend le relais uniquement quand "
       "l'appel serait tombé dans le vide."),
      ("Et les rendez-vous non honorés&nbsp;?",
       "C'est le poste où le retour se voit le plus vite, parce qu'un fauteuil vide se chiffre. Le patient reçoit "
       "une confirmation à la prise du rendez-vous, puis un rappel la veille avec la possibilité de décaler en un mot. "
       "Un créneau libéré la veille se recase&nbsp;; un patient qui ne vient pas, non."),
      ("La création d'un site internet pour un dentiste, gratuite&nbsp;? Où est le piège&nbsp;?",
       "Il n'y en a pas. La création du site ne vous coûte rien et vous ne payez rien tant que vous ne l'avez pas vu. "
       "On se rémunère sur l'abonnement mensuel, qui couvre l'hébergement et les agents. Si le site ne vous plaît pas, "
       "vous nous le dites et on en reste là."),
      ("Combien de temps avant d'avoir le site en ligne&nbsp;?",
       "Vous le voyez en visio avant toute décision. Une fois que vous dites oui, la mise en ligne et le branchement "
       "des agents se font dans la foulée."),
    ],
),
"plombier": dict(
    mot_cle="création site internet plombier",
    titre_prix="création d'un site internet pour un plombier",
    dans_ce_metier="chez un plombier",
    titre_seo="Création de site internet pour plombier : le site offert",
    meta=("Création de site internet pour plombier : on construit votre site, vous le voyez terminé, "
          "puis vous décidez. Site 0 €, agents dès 199 €/mois."),
    kicker="Création de site internet pour plombier",
    h1="Votre site, <em>offert</em>.<br>Vous ne payez que les interventions qu'il vous ramène.",
    lead=("<strong>La création de votre site ne vous est pas facturée&nbsp;:</strong> on le construit, vous le voyez "
          "terminé, puis vous décidez. Vous ne payez ensuite qu'un abonnement mensuel — hébergement et agents — "
          "à partir de 199&nbsp;€. Pour un plombier, l'enjeu n'est pas d'avoir un site&nbsp;: c'est de décrocher "
          "quand ça fuit chez quelqu'un, ou d'être rappelé avant qu'il compose le numéro suivant."),
    lead2=("Et d'être en règle sur l'affichage de vos prix, ce que la plupart des sites de plombiers ne sont pas. "
           "<a href=\"#deonto\">On vous explique pourquoi, et on le corrige</a>."),
    image=("https://decupler.com/wp-content/uploads/2026/08/metier-plombier-hero.jpg",
           "Un plombier consulte son téléphone entre deux interventions, agenouillé devant un meuble de salle de bain"),
    phone=[("call", "06 44 •• •• 12", "Appel entrant · 21:07"),
           ("miss", "Appel manqué", "Vous êtes sous un évier"),
           ("sms", "SMS envoyé", "«&nbsp;Ici Martin Plomberie. Décrivez la panne, je rappelle.&nbsp;»", "Chantier retenu")],
    bande=("Il appelle les trois suivants dans la minute",
           "Une fuite ne patiente pas. Le client compose les numéros de la liste jusqu'à ce que quelqu'un décroche, "
           "et c'est celui-là qui facture.",
           "Il vous décrit la panne par SMS",
           "Vous savez si c'est urgent avant même de rappeler, et vous arrivez avec la bonne pièce dans le camion."),
    probleme_titre="Un plombier ne manque pas de travail. Il manque les appels.",
    probleme=("Il est 21&nbsp;h&nbsp;07. Un chauffe-eau lâche à deux rues de chez vous. La personne cherche "
              "« plombier + votre ville », tombe sur trois numéros et appelle le premier. "
              "<strong>Vous êtes sous un évier, les mains dans l'eau. Ça sonne dans le vide.</strong> "
              "Elle ne laisse pas de message, elle appelle le deuxième."),
    probleme2=("La création d'un site internet pour un plombier ne règle donc pas que la vitrine&nbsp;: elle règle "
               "le standard. Et ce n'est pas qu'une affaire d'appels. Le devis de salle de bain parti il y a dix "
               "jours qui n'a jamais reçu de réponse. Le client d'entretien de chaudière qu'on n'a pas rappelé cette "
               "année. Les deux cents interventions réussies qui n'ont laissé aucune trace publique."),
    legende="Le chantier le moins cher de votre année, c'est celui qui vous appelait déjà.",
    agents=["sms-appel-manque", "agent-vocal", "fiche-google", "relance-devis",
            "sms-formulaire", "reactivation", "mots-cles-locaux", "rapport-mensuel"],
    deonto_titre="Ce qu'on corrige, et ce qu'on refuse de vous vendre",
    deonto=[
      ("mots-cles-locaux", "Vos tarifs seront affichés sur le site",
       "Ce n'est pas une option de confort. Depuis le 1<sup>er</sup> avril 2017, un professionnel du dépannage à "
       "domicile doit communiquer, <strong>avant</strong> la conclusion du contrat, son taux horaire de main-d'œuvre "
       "TTC, ses frais de déplacement, le prix des forfaits et le caractère gratuit ou payant du devis. La plupart "
       "des sites de plombiers ne l'affichent nulle part. Le vôtre, si&nbsp;— et c'est aussi ce qui vous distingue "
       "des faux dépanneurs au premier coup d'œil."),
      ("demande-avis", "Aucun avis fabriqué, aucun tri des clients",
       "Google interdit depuis 2026 de trier les clients selon leur note avant de les envoyer sur la fiche, et "
       "sanctionne jusqu'à la suspension complète du profil. On demande l'avis à tous vos clients, sans exception. "
       "Un profil suspendu, pour un métier qui vit de la recherche locale, c'est le robinet coupé."),
      ("agent-vocal", "Aucun numéro surtaxé",
       "Le numéro de suivi qui permet de détecter les appels manqués est un numéro géographique normal, non surtaxé, "
       "qui renvoie sur votre portable. Le client paie un appel local. C'est exactement l'inverse des réseaux de "
       "dépannage qui facturent la mise en relation."),
    ],
    deonto_source=("Arrêté du 24 janvier 2017 sur la publicité des prix du dépannage",
                   "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033935513",
                   "fiche pratique de la DGCCRF sur le dépannage à domicile",
                   "https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/plomberie-serrurerie-chauffage-choisir-le-bon-professionnel-pour-un-depannage-domicile"),
    remplace=("Afficher ses prix fait peur à beaucoup d'artisans. Dans les faits, ça filtre les curieux et ça rassure "
              "ceux qui ont déjà été échaudés par un dépanneur à 600&nbsp;€. Vous recevez moins d'appels, et une plus "
              "grande part d'entre eux se transforment."),
    faq=[
      ("Je dois vraiment afficher mes tarifs&nbsp;?",
       "Pour les prestations de dépannage, de réparation et d'entretien chez un particulier, oui&nbsp;: l'arrêté du "
       "24 janvier 2017 impose de communiquer le taux horaire TTC, les frais de déplacement, le prix des forfaits et "
       "le caractère gratuit ou payant du devis avant la conclusion du contrat. Le site est l'endroit le plus simple "
       "pour le faire une fois pour toutes."),
      ("L'agent vocal va-t-il répondre à ma place&nbsp;?",
       "Seulement si personne ne décroche. S'il se déclenche, il prend le motif, l'adresse et le degré d'urgence, "
       "puis vous envoie tout par SMS. Il ne s'engage jamais sur un prix ni sur un délai à votre place."),
      ("Et les appels de nuit ou le week-end&nbsp;?",
       "C'est là que le système rapporte le plus, parce que c'est là que vos concurrents ne décrochent pas non plus. "
       "Vous choisissez les plages où l'agent prend le relais, et celles où il se contente d'envoyer un SMS."),
      ("La création d'un site internet pour un plombier, gratuite&nbsp;? Où est le piège&nbsp;?",
       "Il n'y en a pas. La création ne vous coûte rien et vous ne payez rien tant que vous ne l'avez pas vu. On se "
       "rémunère sur l'abonnement mensuel, qui couvre l'hébergement et les agents. Si le site ne vous plaît pas, "
       "vous nous le dites et on en reste là."),
      ("Je travaille déjà par le bouche-à-oreille.",
       "Tant mieux, et ça ne change rien à ce qui se passe quand quelqu'un cherche un plombier à 21&nbsp;h. Le "
       "bouche-à-oreille amène des clients qui vous connaissent&nbsp;; la recherche locale amène ceux qui ne vous "
       "connaissent pas encore. Les deux se cumulent."),
      ("Combien de temps avant d'avoir le site en ligne&nbsp;?",
       "Vous le voyez en visio avant toute décision. Une fois que vous dites oui, la mise en ligne et le branchement "
       "des agents se font dans la foulée."),
    ],
),

"electricien": dict(
    mot_cle="création site internet électricien",
    titre_prix="création d'un site internet pour un électricien",
    dans_ce_metier="chez un électricien",
    titre_seo="Création de site internet pour électricien : le site offert",
    meta=("Création de site internet pour électricien : on construit votre site, vous le voyez terminé, "
          "puis vous décidez. Site 0 €, agents dès 199 €/mois."),
    kicker="Création de site internet pour électricien",
    h1="Votre site, <em>offert</em>.<br>Vous ne payez que les chantiers qu'il vous ramène.",
    lead=("<strong>La création de votre site ne vous est pas facturée&nbsp;:</strong> on le construit, vous le voyez "
          "terminé, puis vous décidez. Vous ne payez ensuite qu'un abonnement mensuel — hébergement et agents — "
          "à partir de 199&nbsp;€. Pour un électricien, le site ne sert pas à montrer des photos de tableaux&nbsp;: "
          "il sert à capter la demande de rénovation, de mise aux normes et de borne de recharge."),
    lead2=("Et à mettre en avant ce qui décide vraiment le client&nbsp;: vos qualifications et votre décennale. "
           "<a href=\"#deonto\">Ce qu'on affiche, et ce qu'on n'écrira jamais à votre place</a>."),
    image=("https://decupler.com/wp-content/uploads/2026/08/metier-electricien-hero.jpg",
           "Une électricienne consulte son téléphone devant un tableau électrique ouvert, en fin de journée"),
    phone=[("call", "07 61 •• •• 88", "Appel entrant · 17:34"),
           ("miss", "Appel manqué", "Vous êtes sur un tableau"),
           ("sms", "SMS envoyé", "«&nbsp;Ici Lemoine Élec. Je vous rappelle en descendant.&nbsp;»", "Client retenu")],
    bande=("Le devis part, et puis plus rien",
           "Une rénovation électrique se compare. Sans relance, votre devis se fait oublier derrière deux autres "
           "arrivés après le vôtre.",
           "Il repart tout seul à J+3 et J+7",
           "Poliment, à votre nom. Le client vous rappelle sans que vous ayez eu à demander deux fois."),
    probleme_titre="Un électricien ne manque pas de demandes. Il manque de suivi.",
    probleme=("Il est 17&nbsp;h&nbsp;34. Quelqu'un cherche un électricien pour une mise aux normes avant une vente. "
              "Il appelle trois numéros dans l'ordre. <strong>Vous êtes les deux mains dans un tableau, vous ne "
              "décrochez pas.</strong> Il ne laisse pas de message, il prend le deuxième rendez-vous de sa liste."),
    probleme2=("La création d'un site internet pour un électricien ne règle donc pas que la vitrine&nbsp;: elle règle "
               "le suivi. Et le trou le plus cher n'est pas l'appel manqué, c'est le devis de rénovation parti la "
               "semaine dernière, jamais relancé, sur lequel vous avez passé deux heures de chiffrage."),
    legende="Le chantier le moins cher de votre année, c'est le devis que vous avez déjà chiffré.",
    agents=["relance-devis", "sms-appel-manque", "fiche-google", "sms-formulaire",
            "rappel-rdv", "chatbot", "mots-cles-locaux", "rapport-mensuel"],
    deonto_titre="Ce qu'on affiche, et ce qu'on n'écrira pas",
    deonto=[
      ("fiche-google", "Vos qualifications, telles qu'elles sont",
       "Qualifelec, RGE, IRVE, décennale&nbsp;: on affiche vos numéros et vos dates de validité, pas des logos "
       "décoratifs. Un client qui compare trois électriciens regarde ça en premier, et une qualification affichée "
       "sans être détenue est une pratique commerciale trompeuse. On ne remplit que ce que vous nous confirmez."),
      ("mots-cles-locaux", "Vos tarifs de dépannage, si vous en faites",
       "Si vous intervenez en dépannage chez des particuliers, l'arrêté du 24 janvier 2017 vous impose de "
       "communiquer votre taux horaire TTC, vos frais de déplacement et le caractère gratuit ou payant du devis "
       "avant la conclusion du contrat. Sur les chantiers de rénovation sur devis, cette obligation ne s'applique "
       "pas de la même façon&nbsp;— on distingue les deux sur le site."),
      ("demande-avis", "Aucun avis fabriqué, aucun tri des clients",
       "Google interdit depuis 2026 de trier les clients selon leur note avant de les envoyer sur la fiche, et "
       "sanctionne jusqu'à la suspension du profil. On demande l'avis à tous vos clients, sans exception."),
    ],
    deonto_source=("Arrêté du 24 janvier 2017 sur la publicité des prix du dépannage",
                   "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033935513",
                   "règles de Google sur les avis",
                   "https://support.google.com/business/answer/7091"),
    remplace=("À la place des faux avis, on branche la relance de devis. Sur un métier où le panier moyen se compte "
              "en milliers d'euros, un devis récupéré vaut plus que dix avis."),
    faq=[
      ("Mes devis sont relancés automatiquement&nbsp;— ça ne fait pas insistant&nbsp;?",
       "Deux relances, à J+3 et J+7, écrites à votre nom, sur un ton neutre&nbsp;: on rappelle que le devis est "
       "toujours valable et on propose de répondre aux questions. Vous les relisez avant qu'elles partent la "
       "première fois. Ensuite, elles tournent seules."),
      ("Vous affichez mes qualifications sans vérifier&nbsp;?",
       "Non. On n'affiche que ce que vous nous confirmez, avec le numéro et la date de validité. Une qualification "
       "affichée sans être détenue vous expose, et nous aussi."),
      ("Je fais surtout du neuf et de la rénovation, pas du dépannage.",
       "Alors le site est construit là-dessus&nbsp;: rénovation complète, mise aux normes avant vente, borne de "
       "recharge, domotique. Ce sont des recherches à forte intention et à panier élevé, et elles se jouent presque "
       "toutes sur la recherche locale."),
      ("La création d'un site internet pour un électricien, gratuite&nbsp;? Où est le piège&nbsp;?",
       "Il n'y en a pas. La création ne vous coûte rien et vous ne payez rien tant que vous ne l'avez pas vu. On se "
       "rémunère sur l'abonnement mensuel. Si le site ne vous plaît pas, on en reste là."),
      ("L'assistant du site va-t-il chiffrer à ma place&nbsp;?",
       "Jamais. Il qualifie&nbsp;: type de logement, surface, nature des travaux, délai souhaité. Le chiffrage reste "
       "le vôtre. Vous recevez une demande déjà cadrée, pas un « bonjour, c'est combien&nbsp;?&nbsp;»."),
      ("Combien de temps avant d'avoir le site en ligne&nbsp;?",
       "Vous le voyez en visio avant toute décision. Ensuite, la mise en ligne et le branchement des agents se font "
       "dans la foulée."),
    ],
),

"institut-de-beaute": dict(
    mot_cle="création site internet institut de beauté",
    titre_prix="création d'un site internet pour institut de beauté",
    dans_ce_metier="dans un institut",
    titre_seo="Création de site internet pour institut de beauté : offert",
    meta=("Création de site internet pour institut de beauté : on construit votre site, vous le voyez terminé, "
          "puis vous décidez. Site 0 €, agents dès 199 €/mois."),
    kicker="Création de site internet pour institut de beauté",
    h1="Votre site, <em>offert</em>.<br>Vous ne payez que les rendez-vous qu'il vous remplit.",
    lead=("<strong>La création du site de votre institut ne vous est pas facturée&nbsp;:</strong> on le construit, "
          "vous le voyez terminé, puis vous décidez. Vous ne payez ensuite qu'un abonnement mensuel — hébergement "
          "et agents — à partir de 199&nbsp;€. Dans un institut, l'enjeu n'est pas la vitrine&nbsp;: c'est la cabine "
          "vide de 14&nbsp;h et la cliente qui n'est pas venue sans prévenir."),
    lead2=("Et c'est de ne pas écrire sur votre site des promesses qui vous exposent à un contrôle. "
           "<a href=\"#deonto\">On vous dit lesquelles</a>."),
    image=("https://decupler.com/wp-content/uploads/2026/08/metier-institut-de-beaute-hero.jpg",
           "La gérante d'un institut de beauté consulte son téléphone à l'accueil, entre deux soins"),
    phone=[("call", "06 78 •• •• 30", "Appel entrant · 14:12"),
           ("miss", "Appel manqué", "Vous êtes en cabine"),
           ("sms", "SMS envoyé", "«&nbsp;Institut Lina. Réservez ici, je vous rappelle après.&nbsp;»", "Cliente retenue")],
    bande=("La cabine reste vide et personne ne prévient",
           "Un rendez-vous oublié, c'est une heure de cabine perdue qui ne se rattrape pas. Et une cliente qui "
           "n'ose plus rappeler.",
           "Elle confirme la veille, en un mot",
           "Le créneau libéré la veille se recase. Celui qu'on découvre vide à 14&nbsp;h, non."),
    probleme_titre="Un institut ne manque pas de clientes. Il manque des créneaux.",
    probleme=("Il est 14&nbsp;h&nbsp;12. Vous êtes en cabine, gants aux mains, sur un soin d'une heure. Le téléphone "
              "sonne à l'accueil&nbsp;: quelqu'un cherche un institut pour un rendez-vous cette semaine. "
              "<strong>Personne ne décroche. Elle ne laisse pas de message. Elle appelle l'institut d'à côté.</strong>"),
    probleme2=("La création de site internet pour institut de beauté ne règle donc pas que la vitrine&nbsp;: "
               "elle règle le planning. Et ce n'est pas qu'une affaire d'appels. La cliente qui a oublié son "
               "rendez-vous de 16&nbsp;h. Les cartes cadeaux vendues en décembre et jamais utilisées. Les trois cents "
               "clientes satisfaites qui n'ont jamais laissé le moindre avis."),
    legende="La cliente la moins chère de votre année, c'est celle qui vous appelait déjà.",
    agents=["rappel-rdv", "sms-appel-manque", "fiche-google", "posts-google",
            "reactivation", "demande-avis", "chatbot", "rapport-mensuel"],
    deonto_titre="Ce qu'on n'écrira pas sur votre site",
    deonto=[
      ("satisfaction", "Aucune promesse de résultat chiffrée",
       "« Perdez deux tailles », « élimine la cellulite », « moins 5&nbsp;cm garantis »&nbsp;: ces formulations sont "
       "des allégations que la DGCCRF contrôle régulièrement, et qui doivent être prouvées scientifiquement pour "
       "être employées. Sans preuve, c'est une publicité trompeuse. Votre site décrit vos soins, votre matériel et "
       "votre façon de travailler&nbsp;— pas un résultat garanti."),
      ("posts-google", "Aucun avant/après retouché",
       "Une photo de soin retouchée ou choisie pour montrer un résultat qui n'est pas représentatif tombe dans la "
       "même catégorie. On préfère montrer votre cabine, votre matériel et votre équipe&nbsp;: c'est ce que les "
       "clientes regardent vraiment avant de réserver un premier soin."),
      ("chatbot", "Aucun faux label",
       "« Testé cliniquement », « validé par des dermatologues », des logos de certification qu'on ne détient pas&nbsp;: "
       "la DGCCRF met explicitement en garde contre ces mentions. On n'affiche que vos vraies formations, vos vraies "
       "marques partenaires et vos vraies certifications."),
    ],
    deonto_source=("fiche pratique de la DGCCRF sur les méthodes amincissantes",
                   "https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/methodes-amincissantes-attention-aux-publicites-mensongeres",
                   "règles de Google sur les avis",
                   "https://support.google.com/business/answer/7091"),
    remplace=("Ce qui remplit un planning d'institut, ce n'est pas la promesse de résultat&nbsp;: c'est la "
              "réservation en deux clics, le rappel la veille et la relance des clientes qui ne sont pas revenues "
              "depuis six mois. Trois mécaniques, aucune allégation."),
    faq=[
      ("Je ne peux vraiment pas parler de résultats&nbsp;?",
       "Vous pouvez décrire précisément ce que fait un soin, sur quelle zone, avec quel appareil, en combien de "
       "séances. Ce qui est encadré, c'est la promesse de résultat chiffrée et non prouvée. La différence est nette, "
       "et elle rend d'ailleurs le texte plus crédible."),
      ("Vous demandez des avis à mes clientes&nbsp;?",
       "Oui, à toutes, sans les trier selon leur humeur du jour&nbsp;— c'est ce que Google exige depuis 2026. En "
       "parallèle, un SMS de satisfaction revient à l'institut&nbsp;: vous savez qui est repartie déçue avant "
       "qu'elle n'écrive quoi que ce soit."),
      ("Et les rendez-vous non honorés&nbsp;?",
       "C'est le poste où le retour se voit le plus vite. Confirmation à la réservation, rappel la veille avec la "
       "possibilité de décaler en un mot. Un créneau libéré la veille se recase&nbsp;; une cliente qui ne vient pas, "
       "non."),
      ("La création d'un site internet pour institut de beauté, gratuite&nbsp;? Où est le piège&nbsp;?",
       "Il n'y en a pas. La création ne vous coûte rien et vous ne payez rien tant que vous ne l'avez pas vu. On se "
       "rémunère sur l'abonnement mensuel. Si le site ne vous plaît pas, on en reste là."),
      ("J'ai déjà un logiciel de réservation.",
       "Parfait, on branche le site dessus plutôt que de le remplacer. Les agents travaillent autour&nbsp;: appels "
       "manqués, rappels, relances, avis. On ne vous fait pas changer d'outil pour le plaisir."),
      ("Combien de temps avant d'avoir le site en ligne&nbsp;?",
       "Vous le voyez en visio avant toute décision. Ensuite, la mise en ligne et le branchement des agents se font "
       "dans la foulée."),
    ],
),

"paysagiste": dict(
    mot_cle="création site internet paysagiste",
    titre_prix="création d'un site internet pour un paysagiste",
    dans_ce_metier="chez un paysagiste",
    titre_seo="Création de site internet pour paysagiste : le site offert",
    meta=("Création de site internet pour paysagiste : on construit votre site, vous le voyez terminé, "
          "puis vous décidez. Site 0 €, agents dès 199 €/mois."),
    kicker="Création de site internet pour paysagiste",
    h1="Votre site, <em>offert</em>.<br>Vous ne payez que les chantiers qu'il vous ramène.",
    lead=("<strong>La création de votre site ne vous est pas facturée&nbsp;:</strong> on le construit, vous le voyez "
          "terminé, puis vous décidez. Vous ne payez ensuite qu'un abonnement mensuel — hébergement et agents — "
          "à partir de 199&nbsp;€. Pour un paysagiste, tout se joue sur deux mois de l'année&nbsp;: si le téléphone "
          "sonne dans le vide en avril, la saison est déjà entamée."),
    lead2=("Et sur ce que devient le devis d'aménagement chiffré en mars, qu'on relance rarement. "
           "<a href=\"#deonto\">Ce qu'on branche, et ce qu'on refuse de vous vendre</a>."),
    image=("https://decupler.com/wp-content/uploads/2026/08/metier-paysagiste-hero.jpg",
           "Un paysagiste consulte son téléphone dans un jardin qu'il vient de tailler"),
    phone=[("call", "06 12 •• •• 41", "Appel entrant · 14:32"),
           ("miss", "Appel manqué", "Vous êtes sur un chantier"),
           ("sms", "SMS envoyé", "«&nbsp;Ici Dupont Paysage. Je vous rappelle très vite.&nbsp;»", "Client retenu")],
    bande=("La saison passe et le téléphone sonne dans le vide",
           "En avril, vos journées sont dehors. Chaque appel manqué est un contrat d'entretien annuel qui part "
           "chez quelqu'un d'autre.",
           "Le SMS part avant qu'il ait raccroché",
           "À votre nom, avec le lien de votre formulaire. Vous rappelez le soir, la demande est toujours là."),
    probleme_titre="Un paysagiste ne manque pas de demandes. Il manque la fenêtre.",
    probleme=("Il est 14&nbsp;h&nbsp;32, un mardi d'avril. Quelqu'un regarde sa haie et décide enfin de faire appel "
              "à un professionnel. Il cherche « paysagiste + votre ville » et appelle le premier numéro. "
              "<strong>Vous êtes sur un chantier, taille-haie en main. Ça sonne dans le vide.</strong> "
              "Il appelle le suivant, et cette demande-là ne reviendra pas avant l'an prochain."),
    probleme2=("La création d'un site internet pour un paysagiste ne règle donc pas que la vitrine&nbsp;: elle règle "
               "la saison. Et ce n'est pas qu'une affaire d'appels. Le devis d'aménagement à 6&nbsp;000&nbsp;€ chiffré "
               "en mars et jamais relancé. Les clients d'entretien de l'an dernier que personne n'a rappelés en "
               "février. Les jardins réussis dont aucune photo n'est jamais sortie du téléphone."),
    legende="Le chantier le moins cher de votre année, c'est celui qui vous appelait déjà.",
    agents=["sms-appel-manque", "relance-devis", "fiche-google", "posts-google",
            "reactivation", "sms-formulaire", "mots-cles-locaux", "rapport-mensuel"],
    deonto_titre="Ce qu'on refuse de vous vendre",
    deonto=[
      ("demande-avis", "Aucun avis fabriqué, aucun tri des clients",
       "Google interdit depuis 2026 de trier les clients selon leur note avant de les envoyer sur la fiche, et "
       "sanctionne jusqu'à la suspension complète du profil. Pour un métier qui vit à 100&nbsp;% de la recherche "
       "locale, un profil suspendu en avril, c'est la saison perdue. On demande l'avis à tous vos clients."),
      ("mots-cles-locaux", "Aucune promesse de première page",
       "Personne ne peut garantir une position sur Google, et qui vous la vend vous vend du vent. Ce qu'on peut "
       "faire, c'est viser les requêtes que vos clients tapent vraiment dans votre zone plutôt que « paysagiste » "
       "tout court, et vous montrer chaque mois où vous en êtes."),
      ("posts-google", "Aucune photo qui n'est pas la vôtre",
       "Pas de banque d'images de jardins anglais. Vos chantiers, vos photos, envoyées par SMS depuis le terrain "
       "quand vous en avez une belle. C'est plus long à alimenter et c'est la seule chose qui convainc un voisin "
       "qui vous a vu travailler."),
    ],
    deonto_source=("règles de Google sur les avis",
                   "https://support.google.com/business/answer/7091",
                   "notre approche du référencement local",
                   "https://decupler.com/seo-local/"),
    remplace=("À la place de la promesse de position, vous recevez chaque mois le compte de ce qui est entré&nbsp;: "
              "appels rattrapés, devis relancés, rendez-vous pris. C'est vérifiable, contrairement à une place dans "
              "un classement que vous ne voyez jamais vous-même."),
    faq=[
      ("Mon activité est très saisonnière, ça vaut le coup toute l'année&nbsp;?",
       "C'est justement l'argument. Le système travaille en février pour remplir mars, et relance en octobre les "
       "clients d'entretien de l'an dernier. Sans lui, vous démarrez chaque saison à zéro."),
      ("Je n'ai pas le temps d'envoyer des photos.",
       "C'est optionnel, et ça prend dix secondes quand vous en avez envie&nbsp;: une photo par SMS, le post part "
       "rédigé sur votre fiche Google. Si vous n'en envoyez jamais, le reste tourne quand même."),
      ("Les devis d'aménagement, vous les relancez comment&nbsp;?",
       "Deux relances écrites à votre nom, à J+3 et J+7, sur un ton neutre&nbsp;: le devis est toujours valable, on "
       "reste disponible pour les questions. Vous les relisez la première fois, ensuite elles tournent seules."),
      ("La création d'un site internet pour un paysagiste, gratuite&nbsp;? Où est le piège&nbsp;?",
       "Il n'y en a pas. La création ne vous coûte rien et vous ne payez rien tant que vous ne l'avez pas vu. On se "
       "rémunère sur l'abonnement mensuel. Si le site ne vous plaît pas, on en reste là."),
      ("J'ai déjà une page Facebook qui marche bien.",
       "Elle ne vous rend pas trouvable quand quelqu'un cherche « paysagiste + votre ville » sur Google, et elle ne "
       "rattrape aucun appel manqué. Les deux ne font pas le même travail."),
      ("Combien de temps avant d'avoir le site en ligne&nbsp;?",
       "Vous le voyez en visio avant toute décision. Ensuite, la mise en ligne et le branchement des agents se font "
       "dans la foulée."),
    ],
),

"artisan": dict(
    mot_cle="création site internet artisan",
    titre_prix="création d'un site internet pour un artisan",
    dans_ce_metier="chez un artisan",
    titre_seo="Création de site internet pour artisan : le site offert",
    meta=("Création de site internet pour artisan : on construit votre site, vous le voyez terminé, "
          "puis vous décidez. Site 0 €, agents dès 199 €/mois."),
    kicker="Création de site internet pour artisan",
    h1="Votre site, <em>offert</em>.<br>Vous ne payez que les chantiers qu'il vous ramène.",
    lead=("<strong>La création de votre site ne vous est pas facturée&nbsp;:</strong> on le construit, vous le voyez "
          "terminé, puis vous décidez. Vous ne payez ensuite qu'un abonnement mensuel — hébergement et agents — "
          "à partir de 199&nbsp;€. Pour un artisan, le problème n'a jamais été d'avoir un site&nbsp;: c'est que "
          "personne ne peut décrocher quand on a les mains prises."),
    lead2=("Et que le devis chiffré un dimanche soir finit trop souvent sans réponse. "
           "<a href=\"#deonto\">Ce qu'on branche, ce qu'on affiche, et ce qu'on refuse</a>."),
    image=("https://decupler.com/wp-content/uploads/2026/08/metier-artisan-hero.jpg",
           "Un artisan menuisier consulte son téléphone dans son atelier, le matin"),
    phone=[("call", "06 33 •• •• 09", "Appel entrant · 10:48"),
           ("miss", "Appel manqué", "Vous êtes à l'atelier, machine en route"),
           ("sms", "SMS envoyé", "«&nbsp;Ici l'atelier Perrin. Je vous rappelle ce soir.&nbsp;»", "Client retenu")],
    bande=("Vous ne saurez jamais qu'il a appelé",
           "Le client ne laisse pas de message. Il compose le numéro suivant, et l'appel manqué ne laisse aucune "
           "trace dans votre journée.",
           "Il a votre réponse avant d'avoir raccroché",
           "À votre nom, avec le lien de votre formulaire. Vous rappelez quand la machine est arrêtée."),
    probleme_titre="Un artisan ne manque pas de travail. Il perd des clients en route.",
    probleme=("Il est 10&nbsp;h&nbsp;48. Quelqu'un cherche votre métier dans votre ville et appelle le premier numéro "
              "de la liste&nbsp;: le vôtre. <strong>Vous êtes à l'atelier, machine en route, ou sur un chantier à "
              "vingt kilomètres. Ça sonne dans le vide.</strong> Il ne laisse pas de message. Il appelle le suivant."),
    probleme2=("La création d'un site internet pour un artisan ne règle donc pas que la vitrine&nbsp;: elle règle ce "
               "qui se passe autour. Et ce n'est pas qu'une affaire d'appels. Le devis chiffré un dimanche soir et "
               "jamais relancé. Le rendez-vous que le client a oublié et qui vous a fait faire trente kilomètres pour "
               "rien. Les deux cents clients satisfaits qui n'ont jamais laissé d'avis."),
    legende="Le chantier le moins cher de votre année, c'est celui qui vous appelait déjà.",
    agents=["sms-appel-manque", "relance-devis", "fiche-google", "rappel-rdv",
            "sms-formulaire", "posts-google", "reactivation", "rapport-mensuel"],
    deonto_titre="Ce qu'on affiche, et ce qu'on refuse de vous vendre",
    deonto=[
      ("mots-cles-locaux", "Vos tarifs, si vous faites du dépannage",
       "Pour les prestations de dépannage, de réparation et d'entretien chez un particulier, l'arrêté du "
       "24 janvier 2017 impose de communiquer le taux horaire TTC, les frais de déplacement, le prix des forfaits et "
       "le caractère gratuit ou payant du devis <strong>avant</strong> la conclusion du contrat. Sur les chantiers "
       "sur devis, cette obligation ne s'applique pas de la même façon&nbsp;— on distingue les deux sur le site."),
      ("demande-avis", "Aucun avis fabriqué, aucun tri des clients",
       "Google interdit depuis 2026 de trier les clients selon leur note avant de les envoyer sur la fiche, et "
       "sanctionne jusqu'à la suspension complète du profil. On demande l'avis à tous vos clients, sans exception."),
      ("posts-google", "Aucune photo qui n'est pas la vôtre",
       "Pas de banque d'images de chantiers qui ne sont pas les vôtres. Vos réalisations, vos photos, envoyées par "
       "SMS depuis le terrain. C'est la seule chose qui convainc quelqu'un qui hésite entre trois devis."),
    ],
    deonto_source=("Arrêté du 24 janvier 2017 sur la publicité des prix du dépannage",
                   "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033935513",
                   "règles de Google sur les avis",
                   "https://support.google.com/business/answer/7091"),
    remplace=("Ce qui fait la différence sur un devis d'artisan, ce n'est pas la note moyenne&nbsp;: c'est d'être le "
              "seul des trois à avoir rappelé, relancé et confirmé le rendez-vous. C'est exactement ce que font les "
              "agents."),
    faq=[
      ("Mon métier n'est pas dans votre liste.",
       "La liste n'a rien de limitatif. La mécanique est la même dès que vos clients vous trouvent à moins de trente "
       "kilomètres et que vous ne pouvez pas décrocher pendant que vous travaillez. Menuisier, maçon, couvreur, "
       "carreleur, peintre&nbsp;: c'est le même système."),
      ("Je dois afficher mes tarifs&nbsp;?",
       "Seulement si vous intervenez en dépannage, réparation ou entretien chez des particuliers&nbsp;— dans ce cas "
       "l'arrêté de 2017 vous y oblige avant la conclusion du contrat. Sur les chantiers sur devis, non. On fait la "
       "distinction sur le site plutôt que de tout afficher ou rien."),
      ("Mes devis sont relancés automatiquement&nbsp;— ça ne fait pas insistant&nbsp;?",
       "Deux relances, à J+3 et J+7, écrites à votre nom, sur un ton neutre. Vous les relisez avant qu'elles partent "
       "la première fois. La plupart des clients répondent qu'ils avaient simplement oublié."),
      ("La création d'un site internet pour un artisan, gratuite&nbsp;? Où est le piège&nbsp;?",
       "Il n'y en a pas. La création ne vous coûte rien et vous ne payez rien tant que vous ne l'avez pas vu. On se "
       "rémunère sur l'abonnement mensuel, qui couvre l'hébergement et les agents. Si le site ne vous plaît pas, "
       "on en reste là."),
      ("Je n'ai pas le temps de m'occuper de tout ça.",
       "C'est exactement le point. Les agents tournent sans vous. Le seul geste qu'on vous demande, c'est d'envoyer "
       "de temps en temps une photo de chantier par SMS&nbsp;— et encore, c'est optionnel."),
      ("Combien de temps avant d'avoir le site en ligne&nbsp;?",
       "Vous le voyez en visio avant toute décision. Ensuite, la mise en ligne et le branchement des agents se font "
       "dans la foulée."),
    ],
),

}
