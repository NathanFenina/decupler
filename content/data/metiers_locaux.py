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

}
