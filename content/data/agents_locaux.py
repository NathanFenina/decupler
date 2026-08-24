# -*- coding: utf-8 -*-
"""Catalogue des agents Décupler pour les entreprises locales.

Source unique : alimente la page offre ET les futures pages agent.
Champs : (slug, nom, etape, promesse, mecanique, preuve)
"""

ETAPES = [
 ("trouve",     "Être trouvé",        "Aujourd'hui, quand quelqu'un cherche votre métier dans votre ville, il tombe sur un concurrent."),
 ("capte",      "Ne rater aucun appel", "Le client qui n'obtient pas de réponse ne laisse pas de message. Il appelle le suivant."),
 ("transforme", "Transformer",         "Le devis part, et puis plus rien. C'est le trou le plus cher, et personne ne le bouche."),
 ("capitalise", "Capitaliser",         "Vous avez des centaines de clients satisfaits et une poignée d'avis."),
 ("pilote",     "Voir ce que ça rapporte", "Sans preuve chiffrée, un abonnement finit toujours par être résilié."),
]

AGENTS = [
 # --- Être trouvé ---
 ("fiche-google", "Optimisation de la fiche Google", "trouve",
  "Votre fiche passe de « remplie à moitié » à complète, sur tous les critères que Google regarde.",
  "On complète catégories, services, zones desservies, horaires, photos et description avec le vocabulaire que vos clients tapent réellement.",
  "Une fiche complète remonte devant une fiche vide, à distance égale."),
 ("posts-google", "Posts Google automatiques", "trouve",
  "Vous photographiez déjà vos chantiers. Envoyez la photo par SMS&nbsp;: le post part sur votre fiche, rédigé et optimisé.",
  "L'agent reçoit la photo, écrit le texte avec les mots-clés de votre métier et de votre ville, et publie.",
  "Zéro effort de votre côté : vous photographiez déjà vos chantiers."),
 ("citations-locales", "Citations locales", "trouve",
  "Votre nom, votre adresse et votre téléphone, écrits à l'identique sur les annuaires que Google recoupe.",
  "On crée et on aligne vos fiches sur les annuaires qui comptent dans votre secteur. La moindre variation d'adresse "
  "entre deux annuaires affaiblit votre fiche&nbsp;: on la corrige partout.",
  "C'est le socle du référencement local : sans citations cohérentes, une fiche Google plafonne."),
 ("seo-local", "SEO local", "trouve",
  "Le site est construit pour sortir sur votre métier dans votre ville, pas pour être joli sur une plaquette.",
  "Pages de zone, vocabulaire de votre secteur, structure des données, maillage interne&nbsp;: le travail de fond "
  "qui décide de votre place dans les résultats locaux, au-delà de la fiche Google.",
  "C'est notre métier de départ : on est agence SEO avant d'être fournisseur de sites."),
 ("mots-cles-locaux", "Recherche de mots-clés locaux", "trouve",
  "On arrête de se battre sur « plombier Paris » pour viser ce que vos clients tapent vraiment.",
  "Analyse des requêtes de votre zone pour isoler celles à forte intention et faible concurrence.",
  "Ce sont ces requêtes-là que le site et la fiche vont viser."),
 # --- Ne rater aucun appel ---
 ("sms-appel-manque", "SMS sur appel manqué", "capte",
  "Vous ne décrochez pas&nbsp;: le client reçoit un SMS dans la seconde, à votre nom, avant d'avoir composé le numéro suivant.",
  "Un numéro de suivi renvoie vers votre portable. S'il n'y a pas de réponse, le SMS part automatiquement avec le lien de votre formulaire.",
  "Sans lui, ce client appelle le concurrent suivant et vous ne saurez jamais qu'il a existé."),
 ("sms-formulaire", "SMS instantané sur formulaire", "capte",
  "Une demande arrive sur le site&nbsp;: vous avez le nom et le numéro par SMS, avant même d'avoir ouvert votre boîte mail.",
  "Vous recevez le nom et le numéro à rappeler. Le prospect reçoit une confirmation immédiate.",
  "Une demande envoyée par e-mail est lue le soir. Par SMS, elle est lue dans la minute."),
 ("chatbot", "Assistant de chat sur le site", "capte",
  "Il est 21&nbsp;h, un visiteur hésite. Il obtient une vraie réponse&nbsp;— pas un formulaire à remplir.",
  "L'assistant est entraîné sur vos prestations, vos horaires et votre zone. Il répond, qualifie, et vous transmet le contact.",
  "La majorité des recherches locales se font hors de vos heures d'ouverture."),
 ("messagerie-google", "Messagerie de la fiche Google", "capte",
  "Les messages envoyés depuis votre fiche Google reçoivent une réponse. Aujourd'hui, presque personne n'y répond.",
  "L'agent surveille la messagerie de la fiche, répond aux questions courantes — horaires, zone, disponibilité — "
  "et vous transmet le contact dès qu'il s'agit d'un vrai projet.",
  "Google affiche le délai de réponse moyen sur votre fiche. Un délai long se voit."),
 ("estimation-en-ligne", "Estimation en ligne", "capte",
  "Le visiteur obtient une fourchette de prix sur le site, et vous ne rappelez que des gens qui savent déjà à quoi "
  "s'attendre.",
  "Quelques questions sur le site donnent un ordre de grandeur calculé à partir de vos propres tarifs. Vous recevez "
  "la demande déjà chiffrée.",
  "Sans estimation, le premier échange sert à découvrir que le budget ne colle pas."),
 ("agent-vocal", "Agent vocal hors horaires", "capte",
  "Le téléphone sonne un samedi matin. Une voix décroche, comprend le besoin, et pose le rendez-vous dans votre agenda.",
  "L'agent ne se déclenche que si personne ne décroche. Il qualifie l'appel et pose le rendez-vous dans votre agenda.",
  "Il ne remplace personne : il prend le relais quand la ligne serait tombée dans le vide."),
 # --- Transformer ---
 ("relance-devis", "Relance de devis sans réponse", "transforme",
  "Vos devis restés sans réponse repartent à J+3 puis à J+7, poliment, sans que vous ayez à y penser.",
  "Dès qu'un devis est marqué envoyé, la séquence démarre. Elle s'arrête net si le client répond.",
  "C'est le plus rentable de tous : le prospect vous connaît déjà et a déjà dit qu'il était intéressé."),
 ("rappel-rdv", "Confirmation et rappel de rendez-vous", "transforme",
  "Le client confirme la veille. Vous ne vous déplacez plus pour rien.",
  "SMS de confirmation à la prise de rendez-vous, rappel automatique 24&nbsp;h avant.",
  "Un déplacement à vide coûte une demi-journée."),
 ("relance-facture", "Relance de facture impayée", "transforme",
  "Vos factures en retard sont relancées à échéance, poliment, sans que vous ayez à jouer le rôle du créancier.",
  "L'agent suit les échéances et envoie un rappel courtois à J+1, puis un second à J+15 avec le récapitulatif. "
  "La séquence s'arrête au paiement.",
  "Une facture relancée dans la semaine se paie ; une facture relancée au bout de deux mois se négocie."),
 ("reactivation", "Réactivation des clients dormants", "transforme",
  "Vos clients d'il y a deux ans reçoivent un mot. Il y en a toujours quelques-uns qui avaient un projet en tête.",
  "L'agent repère les clients sans contact depuis 12 mois et envoie un message adapté à votre métier.",
  "Ce sont vos prospects les moins chers : ils vous ont déjà payé une fois."),
 # --- Capitaliser ---
 ("demande-avis", "Demande d'avis Google", "capitalise",
  "Chaque client reçoit une demande d'avis au bon moment, sans exception et en un clic.",
  "SMS envoyé après l'intervention, avec le lien direct vers votre fiche. Relance unique si pas de réponse.",
  "La demande part à tous vos clients, sans filtre&nbsp;— c'est la seule méthode conforme, et c'est aussi celle qui rapporte le plus d'avis."),
 ("reponse-avis", "Réponse automatique aux avis", "capitalise",
  "Chaque avis reçoit une réponse personnalisée, y compris les mauvais.",
  "L'agent rédige une réponse qui reprend le contenu de l'avis. Les avis négatifs vous sont signalés avant publication de la réponse.",
  "Un avis à 2 étoiles bien traité en public rassure plus qu'un 5 étoiles de plus."),
 ("parrainage", "Demande de parrainage", "capitalise",
  "Un client qui vient de dire qu'il est content est le seul moment où demander s'il connaît quelqu'un ne coûte rien.",
  "Quand le suivi de satisfaction remonte un retour positif, l'agent propose au client de vous recommander, avec un "
  "message tout prêt qu'il n'a qu'à transférer.",
  "Le parrainage est le canal le moins cher qui existe, et celui qu'on oublie systématiquement de demander."),
 ("satisfaction", "Suivi de satisfaction", "capitalise",
  "Vous savez qu'un client est mécontent avant qu'il ne l'écrive sur Google.",
  "Un SMS de satisfaction part à la fin de l'intervention. S'il est négatif, vous êtes alerté pour rappeler.",
  "Ce message ne conditionne jamais l'accès à l'avis Google&nbsp;: c'est du service, pas du filtrage."),
 # --- Piloter ---
 ("rapport-mensuel", "Rapport mensuel de l'argent récupéré", "pilote",
  "Chaque mois, le compte exact de ce que le système a rattrapé pour vous.",
  "«&nbsp;Ce mois-ci&nbsp;: 19 appels rattrapés, 12 devis relancés, 7 nouveaux avis, 4 rendez-vous pris.&nbsp;»",
  "C'est le seul chiffre qui compte pour savoir si l'abonnement vaut son prix."),
]

CIBLES = [
 ("Paysagistes", "🌿", "Devis saisonniers, beaucoup d'appels en journée, personne au bureau."),
 ("Artisans du bâtiment", "🔧", "Sur un chantier, le téléphone dans la poche, les mains prises."),
 ("Dentistes et cabinets", "🦷", "Rendez-vous manqués, standard saturé aux heures de pointe."),
 ("Spas et instituts", "💆", "Réservations le soir et le week-end, quand personne ne décroche."),
 ("Agences immobilières", "🏠", "Un lead sur un bien part au premier qui rappelle."),
 ("Maisons d'hôtes", "🛏️", "Des demandes qui arrivent la nuit, souvent de l'étranger."),
]


def par_etape(cle):
    return [a for a in AGENTS if a[2] == cle]


# Agents qui renvoient vers une page existante du site. Les autres n'ont pas
# encore de page : ne rien mettre plutot qu'un lien mort.
LIENS = {
    'citations-locales': 'https://decupler.com/citations-locales/',
    'seo-local': 'https://decupler.com/seo-local/',
}
