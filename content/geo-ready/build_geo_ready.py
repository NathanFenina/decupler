# -*- coding: utf-8 -*-
"""Page /geo-ready/ — optimisation GEO et simulateur GEO Ready.

Page OUVERTE : aucun formulaire, aucun contenu masqué. La capture d'email se
fait dans le simulateur (app.decupler.com/geo-ready), qui la transmet à
Airtable et Substack. La page sert de lead magnet partagé tel quel : on y lit
la méthode entière, puis on teste sa propre page.

Sources — rien en dehors :
  - le référentiel GEO Ready v0.2 (26 règles, points, blocs, statuts,
    bloquants, pondérations), tel qu'il est publié dans l'outil de Nathan et
    dans le simulateur ;
  - le comportement du simulateur, lu dans son code publié le 23/09/2026 ;
  - trois sources externes, vérifiées le 23/09/2026 :
      Aggarwal et al., « GEO: Generative Engine Optimization », KDD 2024
        (arXiv 2311.09735) — jusqu'à +40 % de visibilité ; +30 à 40 % pour
        les citations de sources, citations et statistiques ; le bourrage de
        mots-clés ne fonctionne pas ;
      Google Search Central, « Fonctionnalités d'IA et votre site Web »
        (mise à jour 31/12/2025) — aucune exigence technique supplémentaire ;
      France Num, guide GEO (publié 09/02/2026, mis à jour 24/04/2026).
Aucun chiffre client : les audits Gestalt / Apogea / HiFolks du brief ne sont
pas accessibles dans ce dépôt.

    python3 content/geo-ready/build_geo_ready.py
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", ".."))
sys.path.insert(0, os.path.join(RACINE, ".claude", "skills",
                                "decupler-page-ville-seo", "scripts"))
import build_ville as bv  # noqa: E402  (charte, typo, révélation)

SIM = ("https://app.decupler.com/geo-ready?utm_source=decupler"
       "&utm_medium=page&utm_campaign=geo-ready")
URL = "https://decupler.com/geo-ready/"
# Le lien de rendez-vous du simulateur lui-même (bouton « Réserver un
# échange avec Decupler ») : le même agenda, d'où qu'on arrive.
CAL_GEO = "https://calendly.com/fenina-nathan/seo-ai-systems"
PUBLIE = "2026-09-23"
DATE_FR = "23 septembre 2026"

PAPER = "https://arxiv.org/abs/2311.09735"
GOOGLE = "https://developers.google.com/search/docs/appearance/ai-features?hl=fr"
FRANCENUM = ("https://www.francenum.gouv.fr/guides-et-conseils/communication-et-"
             "publicite/referencement/optimisation-pour-les-moteurs")


A_GOOGLE_DOC = "documentation sur les fonctionnalités d'IA"
A_GOOGLE_SRC = "« Fonctionnalités d'IA et votre site Web »"
A_FN_SRC = "guide de l'optimisation pour les moteurs génératifs"


def ext(url, ancre):
    return f'<a class="lnk" href="{url}" target="_blank" rel="noopener">{ancre}</a>'


def lien(chemin, ancre):
    return f'<a class="lnk" href="https://decupler.com/{chemin}/">{ancre}</a>'


# ── Le référentiel v0.2 : blocs, règles, points ─────────────────────────────
BLOCS = [
    ("A", "Extractibilité", "Une IA peut-elle extraire un passage qui répond ?", [
        ("A1", "Réponse directe sous le H1", 8, True),
        ("A2", "H2 en questions ou intentions", 5, False),
        ("A3", "Passage citable sous chaque H2", 8, False),
        ("A4", "Format adapté à la nature de l'info", 4, False),
        ("A5", "Section « En résumé »", 3, False),
        ("A6", "Phrases courtes", 2, False)]),
    ("B", "Faits & fraîcheur", "Les faits sont-ils sourcés, datés, récents ?", [
        ("B1", "Chiffres sourcés et datés", 6, False),
        ("B2", "Au moins 2 sources externes autoritaires", 4, False),
        ("B3", "Dates visibles et cohérentes", 4, True),
        ("B4", "Donnée propriétaire", 4, False),
        ("B5", "Zéro superlatif non prouvé", 2, False)]),
    ("C", "Entité & autorité", "L'IA sait-elle qui parle ?", [
        ("C1", "Auteur identifié", 5, False),
        ("C2", "Organization complète", 5, False),
        ("C3", "Cohérence de l'entité avec le registre", 3, False),
        ("C4", "Marque et expertise nommées dans le corps", 4, False),
        ("C5", "Signaux d'expérience", 3, False)]),
    ("D", "Données structurées", "Le balisage dit-il la même chose que le texte ?", [
        ("D1", "Schema du type de page", 4, False),
        ("D2", "FAQPage", 4, False),
        ("D3", "HowTo ou Speakable", 2, False)]),
    ("E", "Accès IA", "Les robots des moteurs IA peuvent-ils lire la page ?", [
        ("E1", "robots.txt ouvert aux bots IA", 4, True),
        ("E2", "llms.txt", 2, False),
        ("E3", "Contenu dans le HTML serveur", 3, True),
        ("E4", "Page indexable", 1, True)]),
    ("F", "Couverture", "La page répond-elle aux sous-questions ?", [
        ("F1", "Couverture du fan-out", 5, False),
        ("F2", "Vocabulaire complet", 3, False),
        ("F3", "Maillage interne contextuel", 2, False)]),
]
assert sum(p for _, _, _, rs in BLOCS for _, _, p, _ in rs) == 100
assert sum(len(rs) for *_, rs in BLOCS) == 26

STATUTS = [
    ("Non citable", "Au moins un bloquant, quel que soit le score"),
    ("Fragile", "Moins de 60 sur 100"),
    ("En progrès", "De 60 à 79"),
    ("GEO Ready", "80 et plus, sans bloquant"),
    ("Référence", "90 et plus, avec une donnée propriétaire"),
]

ETAPES = [
    ("Ouvrir l'accès aux moteurs IA.",
     "Vérifiez que robots.txt n'exclut ni GPTBot, ni ClaudeBot, ni "
     "PerplexityBot, ni Google-Extended. Le texte doit être dans le HTML "
     "servi, pas injecté en JavaScript. La page doit rester indexable."),
    ("Répondre dès la première ligne.",
     "Sous le H1, 40 à 60 mots qui répondent à la question principale, sujet "
     "nommé. Formulez les H2 comme les questions qu'on pose à une IA, et "
     "ouvrez chacun par un paragraphe autonome."),
    ("Sourcer et dater chaque chiffre.",
     "Chaque chiffre porte sa source et son année. Ajoutez au moins deux "
     "sources externes solides, et une donnée qui n'existe que chez vous."),
    ("Dire qui parle.",
     "Un auteur nommé, avec un schema Person relié à un profil public. Une "
     "Organization complète, dont le nom, la ville et le dirigeant "
     "concordent avec le registre des entreprises."),
    ("Couvrir les sous-questions, puis re-tester.",
     "Listez les questions qu'une IA se pose autour du sujet et répondez à "
     "chacune. Ajoutez une FAQ balisée et un résumé. Repassez la page au "
     "simulateur pour mesurer l'écart."),
]

FAQ = [
    ("Le simulateur GEO Ready est-il gratuit ?",
     "Oui. Vous collez l'URL d'une page publiée et vos coordonnées, sans carte "
     "bancaire. Le score sur 100, les trois corrections prioritaires et le "
     "rapport complet arrivent en une à deux minutes. Seule la réécriture de "
     "la page est payante : c'est la mission GEO Ready."),
    ("Quelle différence entre optimisation GEO et SEO ?",
     "Le SEO vise un clic depuis une liste de résultats. L'optimisation GEO "
     "vise une citation dans une réponse générée. Les deux partagent le même "
     "socle : Google rappelle qu'une page doit être indexée et affichable "
     "avec un extrait pour apparaître dans ses Aperçus IA."),
    ("Une page GEO Ready est-elle sûre d'être citée ?",
     "Non, et personne ne peut le garantir. Google l'écrit lui-même : "
     "l'indexation et la diffusion ne sont jamais garanties. Le référentiel "
     "mesure les conditions qui rendent une citation possible, règle par "
     "règle. Il ne promet pas le choix final du moteur, qui dépend aussi "
     "des pages concurrentes."),
    ("Pourquoi certaines règles sont-elles « non vérifiées » ?",
     "Parce qu'une règle impossible à vérifier sort du calcul au lieu d'être "
     "comptée fausse. Si le registre des entreprises ne répond pas, par "
     "exemple, le contrôle de l'entité est retiré du score. Le rapport liste "
     "ces règles pour que vous sachiez ce qui n'a pas été mesuré."),
    ("GEO, AEO et référencement IA : est-ce la même chose ?",
     "Oui, à quelques nuances près. GEO, pour Generative Engine Optimization, "
     "est le terme de la recherche. AEO, pour Answer Engine Optimization, "
     "insiste sur les moteurs de réponse. « Référencement IA » est "
     "l'expression française. Les trois désignent le même travail : être "
     "repris dans les réponses des IA."),
    ("Faut-il un fichier llms.txt ?",
     "C'est utile, mais secondaire : la règle E2 vaut 2 points sur 100. Le "
     "fichier se place à la racine du site et présente l'entité et ses "
     "pages piliers. L'accès des robots, le HTML serveur et l'indexation "
     "pèsent plus, et trois d'entre eux sont bloquants."),
]


def page():
    o = []
    a = o.append
    a('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
      'family=Sora:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap">')
    a("<style>")
    a(bv.css_pour_la_page())
    # Tableau du référentiel : la colonne des points s'aligne à droite, les
    # règles bloquantes portent un repère lisible sans la couleur.
    # Les tableaux de cette page sont courts : ils tiennent à 490 px sans
    # la largeur minimale du skin, pensée pour les grands comparatifs.
    a(".dcp-v table{min-width:0}")
    a("@media (max-width:560px){.dcp-v table{font-size:.82rem}"
      ".dcp-v td,.dcp-v th{padding:9px 8px}}")
    a(".dcp-v .ref td.p{text-align:right;font-variant-numeric:tabular-nums;"
      "white-space:nowrap;font-weight:600}")
    a(".dcp-v .ref td.id{font-weight:700;white-space:nowrap}")
    a(".dcp-v .ref tr.grp td{background:#f3f1fb;font-weight:700;color:#1a1a2e}")
    a(".dcp-v .blq{display:inline-block;margin-left:6px;padding:1px 7px;"
      "border-radius:5px;background:#fdecea;color:#a3261b;font-size:.75rem;"
      "font-weight:700;letter-spacing:.02em}")
    a(".dcp-v .res{margin:14px 0 0;padding-left:1.2em;font-size:1rem;"
      "line-height:1.7;color:var(--tx2)}.dcp-v .res li{margin:0 0 6px}")
    a(".dcp-v .srcs,.dcp-v .ref+p,.dcp-v .res{max-width:44em}")
    a(".dcp-v .srcs{margin:0;padding-left:1.1em}.dcp-v .srcs li{margin:0 0 10px}")
    a(".dcp-v .dates{font-size:.8rem;color:var(--tx3);margin-top:10px}")
    a("</style>")

    a('<div class="dcp-v">')
    # ── hero ────────────────────────────────────────────────────────────────
    a('<div class="hero">')
    a('<div class="in">')
    a('<div class="hgrid">')
    a('<div class="st">')
    a('<div><span class="pill a1">GEO Ready · simulateur gratuit</span></div>')
    a('<h1 class="a2">GEO Ready : la méthode d\'<em>optimisation GEO</em> pour '
      'être cité par ChatGPT, Claude et Gemini</h1>')
    a('<p class="lead nr a2">L\'optimisation GEO rend une page citable par les '
      'moteurs génératifs. Il faut un passage autonome qui répond, des faits '
      'sourcés, une entité vérifiable et un accès ouvert aux robots IA. GEO '
      'Ready est le référentiel de Décupler qui mesure ces conditions en 26 '
      'règles. Le simulateur note votre page sur 100 en deux minutes.</p>')
    a(f'<div class="row a3"><a class="btn" href="{SIM}">Tester ma page '
      'gratuitement</a><a class="btn-o" href="#les-26-regles">Voir les 26 '
      'règles</a></div>')
    a('<p class="sub a3">Gratuit, sans carte bancaire. Résultat en une à deux '
      'minutes.</p>')
    a(f'<p class="dates a3">Par <a class="lnk" href="{bv.LI}">Nathan '
      f'Fenina</a>, fondateur de Décupler · publié le <time datetime="'
      f'{PUBLIE}">{DATE_FR}</time> · mis à jour le <time datetime="{PUBLIE}">'
      f'{DATE_FR}</time></p>')
    a("</div>")
    a('<div class="cards a3">')
    for k, v in [("Référentiel", "26 règles · 6 blocs · version 0.2"),
                 ("Résultat", "Un score sur 100 et vos 3 corrections prioritaires"),
                 ("Durée", "1 à 2 minutes, pour une page publiée")]:
        a(f'<div class="card"><div class="k">{k}</div><div class="v">{v}</div></div>')
    a("</div>")
    a("</div>")
    a('<div class="trust">')
    for n, l in [("26", "règles, chacune avec sa source de vérité"),
                 ("6", "blocs, de l'accès des robots à la couverture"),
                 ("5", "règles bloquantes, qui annulent le score"),
                 ("100", "points, ramenés aux règles vérifiables")]:
        a(f'<div><div class="n">{n}</div><div class="l">{l}</div></div>')
    a("</div>")
    a("</div>")
    a("</div>")

    # ── 1. définition ──────────────────────────────────────────────────────
    a('<div class="bl">')
    a('<div class="in st-s">')
    a("<h2>Qu'est-ce que l'optimisation GEO ?</h2>")
    a('<p class="lead nr">L\'optimisation GEO, pour <i>Generative Engine '
      'Optimization</i>, travaille la visibilité d\'un contenu dans les '
      'réponses des moteurs génératifs : ChatGPT, Claude, Gemini, Perplexity '
      'et les Aperçus IA de Google. Le but n\'est plus seulement d\'être '
      'classé. Le but est d\'être repris, cité et lié dans la réponse. En '
      'français, on parle aussi de référencement IA.</p>')
    a(f'<p class="lead nr">Le terme vient d\'une étude de Princeton, publiée '
      f'en 2023 et acceptée à la conférence KDD 2024 : '
      f'{ext(PAPER, "« GEO: Generative Engine Optimization »")}. Ses auteurs '
      f'montrent que des modifications de contenu peuvent augmenter la '
      f'visibilité dans une réponse générée jusqu\'à 40 %.</p>')
    a('<p class="lead nr">Trois méthodes sortent en tête : citer ses sources, '
      'ajouter des citations crédibles et ajouter des statistiques. Elles '
      'gagnent de 30 à 40 % sur la mesure principale de l\'étude. À '
      'l\'inverse, le bourrage de mots-clés, réflexe du vieux SEO, ne '
      'fonctionne pas.</p>')
    a(f'<p class="lead nr">Le sujet a quitté les laboratoires : l\'État '
      f'consacre désormais un {ext(FRANCENUM, "guide France Num")} au '
      f'référencement sur les moteurs d\'IA, publié en février 2026 et mis à '
      f'jour en avril 2026.</p>')
    a("</div>")
    a("</div>")

    # ── 2. GEO vs SEO ──────────────────────────────────────────────────────
    a('<div class="bl bl-lav">')
    a('<div class="in st-s">')
    a("<h2>GEO et SEO : quelle différence ?</h2>")
    a('<p class="lead nr">Le GEO et le SEO partagent le même socle, mais pas '
      'le même objectif. Le SEO cherche une position et un clic. Le GEO '
      'cherche une mention dans une réponse. Une page peut gagner la seconde '
      'sans jamais générer de visite.</p>')
    a('<div class="tw"><table>')
    a("<thead><tr><th></th><th>SEO</th><th>Optimisation GEO</th></tr></thead>")
    a("<tbody>")
    for l in [("Objectif", "Un clic depuis une liste de liens",
               "Une citation dans une réponse générée"),
              ("Unité jugée", "La page entière", "Le passage qui répond"),
              ("Ce qui pèse", "Pertinence, liens, expérience de page",
               "Faits sourcés, entité claire, passage autonome"),
              ("Mesure", "Positions, impressions, clics",
               "Taux de citation, part de voix face aux concurrents"),
              ("Prérequis commun", "Page indexée et lisible",
               "Page indexée et lisible")]:
        a(f"<tr><td><b>{l[0]}</b></td><td>{l[1]}</td><td>{l[2]}</td></tr>")
    a("</tbody></table></div>")
    a(f'<p class="lead nr" style="margin-top:18px">Google le dit sans détour '
      f'dans sa {ext(GOOGLE, A_GOOGLE_DOC)} : '
      f'pour apparaître comme lien dans les Aperçus IA, une page doit être '
      f'indexée et affichable avec un extrait. « Il n\'y a aucune exigence '
      f'technique supplémentaire. » Le SEO reste la porte d\'entrée du GEO, '
      f'pas son concurrent : c\'est tout le sens de l\'expression « GEO '
      f'SEO ».</p>')
    a("</div>")
    a("</div>")

    # ── 3. page GEO Ready ──────────────────────────────────────────────────
    a('<div class="bl">')
    a('<div class="in st-s">')
    a("<h2>Qu'est-ce qu'une page GEO Ready ?</h2>")
    a('<p class="lead nr">Une page est GEO Ready quand un moteur génératif '
      'peut faire quatre choses avec elle. Il peut accéder au contenu. Il '
      'peut en extraire un bloc autonome qui répond. Il peut faire confiance '
      'à l\'entité qui l\'a écrit. Et il trouve ce bloc plus précis et plus '
      'frais que ceux des concurrents.</p>')
    a('<p class="lead nr">Le principe tient en une phrase : une IA cite un '
      'passage, pas une page. Chez Décupler, nous avons traduit ces quatre '
      'mécanismes en 26 règles mesurables. Le score qui en sort donne un '
      'statut à la page.</p>')
    a('<div class="tw"><table>')
    a("<thead><tr><th>Statut</th><th>Condition</th></tr></thead><tbody>")
    for s, c in STATUTS:
        a(f"<tr><td><b>{s}</b></td><td>{c}</td></tr>")
    a("</tbody></table></div>")
    a("</div>")
    a("</div>")

    # ── 4. les 26 règles ───────────────────────────────────────────────────
    a('<div class="bl bl-lav" id="les-26-regles">')
    a('<div class="in st-s">')
    a("<h2>Quelles sont les 26 règles du référentiel GEO Ready ?</h2>")
    a('<p class="lead nr">Les 26 règles se répartissent en six blocs, pour '
      'un total de 100 points. L\'extractibilité pèse le plus lourd, avec 30 '
      'points : c\'est elle qui décide si un passage peut être repris tel '
      'quel. Cinq règles sont bloquantes : tant qu\'elles échouent, la page '
      'est « non citable », quel que soit son score.</p>')
    a('<div class="tw"><table class="ref">')
    a("<thead><tr><th>Règle</th><th>Ce qu'on vérifie</th><th>Points</th></tr>"
      "</thead><tbody>")
    for lettre, nom, question, regles in BLOCS:
        total = sum(p for _, _, p, _ in regles)
        a(f'<tr class="grp"><td>{lettre}</td><td>{nom} — {question}</td>'
          f'<td class="p">{total}</td></tr>')
        for rid, lib, pts, blq in regles:
            marque = '<span class="blq">bloquant</span>' if blq else ""
            a(f'<tr><td class="id">{rid}</td><td>{lib}{marque}</td>'
              f'<td class="p">{pts}</td></tr>')
    a("</tbody></table></div>")
    a('<p class="sub" style="margin-top:14px">Référentiel GEO Ready, version '
      '0.2. La règle B3 ne bloque qu\'au-delà de 24 mois sans revue ; E1, dès '
      'qu\'un robot d\'un moteur ciblé est exclu.</p>')
    a("</div>")
    a("</div>")

    # ── 5. comment le simulateur note ──────────────────────────────────────
    a('<div class="bl">')
    a('<div class="in st-s">')
    a("<h2>Comment le simulateur GEO Ready note-t-il une page ?</h2>")
    a('<p class="lead nr">Chez Décupler, chaque règle du simulateur a une '
      'source de vérité, et une seule. '
      'Le code mesure ce qui est reproductible : structure, dates, données '
      'structurées, liens, accès des robots. Claude juge ce qui demande une '
      'lecture : réponse directe, passages citables, preuves, sous-questions '
      'couvertes. Le registre officiel vérifie l\'entité.</p>')
    a('<div class="num2">')
    for i, (t, d) in enumerate([
            ("La mesure du code",
             "Reproductible : deux passages sur la même page donnent le même "
             "résultat. Elle couvre les H2, les phrases, les dates, le "
             "balisage, robots.txt, llms.txt et l'indexation."),
            ("Le jugement de Claude",
             "Qualitatif : la réponse sous le H1 répond-elle vraiment ? Les "
             "chiffres sont-ils sourcés ? Quelles sous-questions restent sans "
             "réponse ?"),
            ("Le registre officiel",
             "Nom, ville, année de création et dirigeant sont comparés au "
             "Registre national des entreprises, puis à Wikidata et LinkedIn "
             "quand c'est possible.")], 1):
        a(f'<div><div class="b">{i}</div><h3>{t}</h3><div class="d">{d}</div></div>')
    a("</div>")
    a('<p class="lead nr" style="margin-top:22px">Une règle impossible à '
      'vérifier sort du calcul au lieu d\'être comptée fausse. Le score est '
      'ensuite ramené sur 100. Le poids de certaines règles change selon le '
      'type de page : la preuve de marque compte plus sur une page service, '
      'le format sur un comparatif, la FAQ sur une page de questions.</p>')
    a("</div>")
    a("</div>")

    # ── 6. le rapport ──────────────────────────────────────────────────────
    a('<div class="bl bl-lav">')
    a('<div class="in st-s">')
    a("<h2>Que contient le rapport du simulateur ?</h2>")
    a('<p class="lead nr">Le rapport donne un score sur 100 et un statut. '
      'Il classe vos trois corrections prioritaires par points gagnés : '
      'd\'abord ce qui lève un bloquant, puis les règles qui pèsent le plus '
      'pour votre type de page. Il estime aussi le score potentiel une fois '
      'ces corrections faites.</p>')
    a('<div class="grid2">')
    for t, d in [
            ("Les 26 règles, une par une",
             "Le constat, sa source et les points gagnés par chaque "
             "correction."),
            ("Votre entité, vue par une IA",
             "Ce qu'un moteur trouve sur vous, sur le site, au registre et "
             "sur vos profils publics."),
            ("Les sous-questions",
             "Pour répondre, une IA décompose la question. Chaque "
             "sous-question sans réponse est une citation laissée à un "
             "concurrent."),
            ("Les règles non vérifiées",
             "Listées à part, pour savoir exactement ce qui n'a pas été "
             "mesuré.")]:
        a(f'<div><h3>{t}</h3><div class="d">{d}</div></div>')
    a("</div>")
    a(f'<div class="row" style="margin-top:26px"><a class="btn" href="{SIM}">'
      'Lancer le simulateur</a></div>')
    a("</div>")
    a("</div>")

    # ── 7. HowTo ───────────────────────────────────────────────────────────
    a('<div class="bl">')
    a('<div class="in">')
    a('<div class="split">')
    a('<div class="st-s">')
    a("<h2>Comment rendre une page GEO Ready en cinq étapes ?</h2>")
    a('<p class="lead nr">Rendre une page GEO Ready se fait en cinq étapes, '
      'dans un ordre précis. Commencez par ce qui bloque, finissez par ce qui '
      'départage. Cet ordre suit le poids des règles du référentiel : inutile '
      'de soigner une FAQ si les robots IA ne peuvent pas lire la page.</p>')
    a(f'<p class="lead nr">Pour la partie propre à ChatGPT, notre guide du '
      f'{lien("referencement-chatgpt", "référencement ChatGPT")} détaille '
      f'comment le modèle choisit ses sources.</p>')
    a("</div>")
    a('<div class="steps">')
    for i, (t, d) in enumerate(ETAPES, 1):
        a(f'<div><div class="b">{i}</div><div class="t"><b>{t}</b> {d}</div></div>')
    a("</div>")
    a("</div>")
    a("</div>")
    a("</div>")

    # ── 8. erreurs ─────────────────────────────────────────────────────────
    a('<div class="bl bl-lav">')
    a('<div class="in st-s">')
    a("<h2>Quelles erreurs rendent une page non citable ?</h2>")
    a('<p class="lead nr">Une page devient non citable dès qu\'un des cinq '
      'bloquants du référentiel échoue. Ce sont les erreurs les plus '
      'coûteuses, parce qu\'elles annulent tout le reste du score. Viennent '
      'ensuite des défauts plus discrets, qui font perdre des points sans que '
      'personne ne les remarque.</p>')
    a('<div class="duo">')
    a('<div class="col non"><div class="ct"><div class="s">\u2715</div>'
      '<div>Ce qui bloque</div></div><ul>'
      '<li><b>Une introduction d\'ambiance</b> au lieu d\'une réponse sous le '
      'H1.</li>'
      '<li><b>Un robot IA exclu</b> dans robots.txt, souvent par un réglage '
      'oublié.</li>'
      '<li><b>Un contenu chargé en JavaScript</b>, absent du HTML servi.</li>'
      '<li><b>Une balise noindex</b> restée après une mise en ligne.</li>'
      '<li><b>Une page jamais revue</b> depuis plus de deux ans.</li>'
      '</ul></div>')
    a('<div class="col non"><div class="ct"><div class="s">!</div>'
      '<div>Ce qui coûte des points</div></div><ul>'
      '<li><b>Des chiffres animés</b> qui affichent « 0 » sans JavaScript : '
      'c\'est ce que lit une IA.</li>'
      '<li><b>Un article signé « L\'équipe »</b> : une IA cherche une '
      'personne.</li>'
      '<li><b>« Leader », « le meilleur »</b> sans aucune preuve.</li>'
      '<li><b>Des chiffres sans source ni année.</b></li>'
      '<li><b>Des mots-clés répétés</b> : l\'étude de Princeton les classe '
      'parmi les méthodes qui ne marchent pas.</li>'
      '</ul></div>')
    a("</div>")
    a("</div>")
    a("</div>")

    # ── 9. parti pris ──────────────────────────────────────────────────────
    parti = {
        "parti_pill": "Mon parti pris",
        "h2_parti": "Pourquoi un score qui refuse de compter ce qu'il ne sait pas",
        "parti_role": "Fondateur de Décupler · Nice",
        "parti_pris": [
            "La plupart des scores « IA » donnent un chiffre à tout prix. "
            "Quand une donnée manque, ils la comptent fausse, ou pire, ils "
            "l'inventent. Le résultat impressionne sur une capture d'écran. "
            "Mais il ne dit ni quoi corriger, ni dans quel ordre, ni ce que "
            "la correction rapportera.",
            "<strong>J'ai construit GEO Ready à l'inverse.</strong> Chaque "
            "règle dit d'où vient son verdict : le code, Claude ou le "
            "registre. Une règle qu'on ne peut pas vérifier sort du calcul, "
            "et le rapport le dit.",
            "Un score honnête est parfois moins flatteur. Mais c'est le seul "
            "sur lequel on peut <strong>bâtir un plan de corrections</strong> "
            "et mesurer, ensuite, ce qu'il a changé.",
        ],
    }
    for x in bv.parti_pris(parti, bv.PHOTO_NATHAN):
        a(x)

    # ── 10. après le test ──────────────────────────────────────────────────
    a('<div class="bl">')
    a('<div class="in st-s">')
    a("<h2>Et si votre page ne passe pas le test ?</h2>")
    a('<p class="lead nr">Si votre page ne passe pas, le simulateur vous dit '
      'quoi corriger et combien chaque correction rapporte. Il ne réécrit pas '
      'la page : la réécriture complète, c\'est la mission GEO Ready. Chez '
      'Décupler, vingt minutes d\'échange suffisent pour choisir les pages à '
      'transformer en premier, sans engagement.</p>')
    a(f'<div class="row"><a class="btn" href="{CAL_GEO}">Réserver 20 minutes '
      'avec Nathan</a></div>')
    a(f'<p class="lead nr" style="margin-top:22px">Pour un diagnostic de tout '
      f'le site plutôt que d\'une page, voyez notre {lien("audit-geo", "audit GEO")}. Pour un '
      f'accompagnement dans la durée, notre '
      f'{lien("agence-geo", "agence GEO")} suit votre visibilité dans les '
      f'quatre grands moteurs IA. Et pour dérouler la méthode vous-même, '
      f'notre {lien("playbook-geo", "playbook GEO")} détaille chaque '
      f'chantier.</p>')
    a("</div>")
    a("</div>")

    # ── 11. en résumé ──────────────────────────────────────────────────────
    a('<div class="bl bl-lav">')
    a('<div class="in st-s">')
    a("<h2>En résumé</h2>")
    a('<ul class="res">'
      '<li>L\'optimisation GEO vise une citation, pas un clic.</li>'
      '<li>Une IA cite un passage autonome, pas une page entière.</li>'
      '<li>GEO Ready mesure 26 règles, dont 5 bloquantes.</li>'
      '<li>Chaque verdict a sa source : code, Claude ou registre.</li>'
      '<li>Le simulateur est gratuit et répond en deux minutes.</li>'
      '</ul>')
    a("</div>")
    a("</div>")

    # ── FAQ ────────────────────────────────────────────────────────────────
    a('<div class="bl">')
    a('<div class="in st-s">')
    a("<h2>Questions fréquentes sur l'optimisation GEO</h2>")
    a('<div class="faq">')
    for q, r in FAQ:
        a('<div class="decupler-faq-item">')
        a(f'<h3 class="decupler-faq-question">{q}</h3>')
        a('<div class="decupler-faq-answer"><div class="decupler-faq-answer-inner">'
          f'{r}</div></div>')
        a("</div>")
    a("</div>")
    a("</div>")
    a("</div>")

    # ── sources ────────────────────────────────────────────────────────────
    a('<div class="bl bl-lav">')
    a('<div class="in st-s">')
    a("<h2>Sur quelles sources s'appuie cette page ?</h2>")
    a('<p class="lead nr">Cette page s\'appuie sur trois sources externes et '
      'sur le référentiel de Décupler. Chaque chiffre cité renvoie à l\'une '
      'd\'elles, avec sa date. C\'est la règle B1 du référentiel, appliquée à '
      'la page qui le présente. Si une source évolue, la page est mise à jour '
      'et sa date aussi.</p>')
    a('<ol class="srcs">')
    a(f'<li>Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan et Deshpande, '
      f'{ext(PAPER, "« GEO: Generative Engine Optimization »")}, Princeton, '
      f'2023, acceptée à KDD 2024.</li>')
    a(f'<li>Google Search Central, '
      f'{ext(GOOGLE, A_GOOGLE_SRC)}, mise à '
      f'jour du 31 décembre 2025.</li>')
    a(f'<li>France Num, {ext(FRANCENUM, A_FN_SRC)}, publié le 9 février '
      '2026, mis à jour le 24 avril 2026.</li>')
    a('<li>Décupler, référentiel GEO Ready, version 0.2.</li>')
    a("</ol>")
    a("</div>")
    a("</div>")

    # ── auteur ─────────────────────────────────────────────────────────────
    a('<div class="bl">')
    a('<div class="in">')
    a('<div class="aut" data-dcp="chrome">')
    a(f'<div class="ph"><img src="{bv.PHOTO_NATHAN_LARGE}" alt="Nathan '
      'Fenina, auteur de GEO Ready, le référentiel d\'optimisation GEO de '
      'Décupler" '
      'width="1000" height="1332" loading="lazy"></div>')
    a('<div class="tx">')
    a('<div><span class="pill">Qui a construit le référentiel</span></div>')
    a('<div class="nm">Nathan Fenina</div>')
    a('<div class="rl">Fondateur de Décupler · auteur du référentiel GEO Ready</div>')
    a('<p class="lead nr">Huit ans de référencement naturel, plus de 70 '
      'entreprises accompagnées. Nathan dirige Décupler depuis Nice et a '
      'conçu le référentiel GEO Ready pour auditer les pages de ses clients, '
      'avant de l\'ouvrir à tous en simulateur.</p>')
    a(f'<div class="row"><a class="btn-o" href="{bv.LI}">Profil LinkedIn</a>'
      f'<a class="btn" href="{SIM}">Tester ma page</a></div>')
    a("</div>")
    a("</div>")
    a("</div>")
    a("</div>")

    # ── final ──────────────────────────────────────────────────────────────
    a('<div class="bl final" data-dcp="chrome">')
    a('<div class="in st-s">')
    a("<h2>Deux minutes pour savoir si votre page est citable</h2>")
    a('<p class="lead nr">Collez l\'URL d\'une page publiée : article, page '
      'service, comparatif, FAQ ou page d\'accueil. Vous recevez son score GEO '
      'Ready, son statut et les trois corrections qui rapportent le plus de '
      'points. Le test est gratuit et sans carte bancaire.</p>')
    a(f'<div class="row"><a class="btn" href="{SIM}">Tester ma page '
      'gratuitement</a></div>')
    a("</div>")
    a("</div>")

    # ── JSON-LD : un seul graphe, sur une ligne (wpautop) ──────────────────
    org = {"@type": "Organization", "@id": "https://decupler.com/#organization",
           "name": "Décupler", "url": "https://decupler.com/",
           "logo": "https://decupler.com/wp-content/uploads/2024/04/cropped-LOGO1.png",
           "description": "Agence SEO et GEO basée à Nice.",
           "founder": {"@id": "https://decupler.com/#nathan-fenina"},
           "address": {"@type": "PostalAddress",
                       "streetAddress": "10 avenue Lympia privée",
                       "postalCode": "06300", "addressLocality": "Nice",
                       "addressCountry": "FR"},
           "sameAs": ["https://decupler.substack.com"]}
    person = {"@type": "Person", "@id": "https://decupler.com/#nathan-fenina",
              "name": "Nathan Fenina", "jobTitle": "Fondateur de Décupler",
              "url": bv.LI, "sameAs": [bv.LI], "image": bv.PHOTO_NATHAN,
              "worksFor": {"@id": "https://decupler.com/#organization"}}
    graphe = [
        {"@type": "WebPage", "@id": URL + "#page", "url": URL,
         "name": "GEO Ready : rendez vos pages citables par les IA",
         "inLanguage": "fr-FR", "datePublished": PUBLIE, "dateModified": PUBLIE,
         "isPartOf": {"@id": "https://decupler.com/#website"},
         "breadcrumb": {"@id": URL + "#fil"}},
        {"@type": "Article", "@id": URL + "#article",
         "headline": "GEO Ready : la méthode d'optimisation GEO pour être cité "
                     "par ChatGPT, Claude et Gemini",
         "datePublished": PUBLIE, "dateModified": PUBLIE,
         "author": {"@id": "https://decupler.com/#nathan-fenina"},
         "publisher": {"@id": "https://decupler.com/#organization"},
         "mainEntityOfPage": {"@id": URL + "#page"},
         "about": ["Generative Engine Optimization", "Référencement IA"],
         "citation": [PAPER, GOOGLE, FRANCENUM]},
        org, person,
        {"@type": "BreadcrumbList", "@id": URL + "#fil", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil",
             "item": "https://decupler.com/"},
            {"@type": "ListItem", "position": 2, "name": "GEO Ready", "item": URL}]},
        {"@type": "HowTo", "name": "Rendre une page GEO Ready en cinq étapes",
         "step": [{"@type": "HowToStep", "position": i, "name": t.rstrip("."),
                   "text": d} for i, (t, d) in enumerate(ETAPES, 1)]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": bv.txt(r)}}
            for q, r in FAQ]},
    ]
    a('<div class="ldjson"><script type="application/ld+json">'
      + json.dumps({"@context": "https://schema.org", "@graph": graphe},
                   ensure_ascii=False) + "</script></div>")
    a('<div class="ldjson">')
    a("<script>" + bv.REVEAL + "</script>")
    a("</div>")
    a("</div>")

    brut = "\n".join(o)
    tete, _, queue = brut.partition("</style>")
    queue = "\n".join(l for l in queue.split("\n") if l.strip())
    return tete + "</style>\n" + bv.typo_fr(queue)


if __name__ == "__main__":
    sortie = os.path.join(ICI, "geo-ready.html")
    open(sortie, "w", encoding="utf-8").write(page())
    print(f"✅ {sortie} ({os.path.getsize(sortie)} octets)")
