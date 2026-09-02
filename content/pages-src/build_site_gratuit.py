# -*- coding: utf-8 -*-
"""Construit la page « Site gratuit » (WordPress ID 20649).

    python3 content/pages-src/build_site_gratuit.py

Sort content/articles/site-gratuit-local.html, prêt pour wp_publish.py.

Trois décisions de structure, écrites ici pour qu'on ne les défasse pas par
inadvertance :

1. **L'offre est un socle + des modules, pas un escalier.** Le site (0 €) et
   sa mise en ligne (97 €) forment une seule décision : un site qu'on ne
   publie pas ne sert à rien. Les trois modules — agents, SEO/GEO, ads — sont
   parallèles et facultatifs, et deux d'entre eux sont au même prix. Cinq
   cartes égales mentiraient sur la forme réelle de l'offre.

2. **« Pourquoi c'est gratuit » est en position 2, pas dans la FAQ.** C'est
   LA seule objection qui compte. Une page qui l'enterre en bas se fait poser
   la question au téléphone de toute façon, mais avec de la méfiance en plus.

3. **La condition est dite en clair.** Le site est à vous après le rendez-vous,
   il n'est pas publié tant que l'hébergement n'est pas pris. Le cacher pour
   faire joli, c'est le découvrir au moment de signer — et perdre l'affaire là.

La page est tournée en Loom : chaque section porte un `id` stable pour
pouvoir sauter d'un plan à l'autre pendant l'enregistrement.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
for d in ('content/data', 'content/components', 'scripts/lib'):
    sys.path.insert(0, str(RACINE / d))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import wpcss                                              # noqa: E402
import icones as I                                        # noqa: E402
import pied_technique as PT                               # noqa: E402

SKIN = open(RACINE / 'content/skins/dcp.css', encoding='utf-8').read()
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Syne:wght@700;800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700'
         '&family=JetBrains+Mono:wght@400;700&display=swap">')

CIBLES = "artisans, professions de santé, professions libérales, métiers du bien-être"

# ── Le socle : deux colonnes, une seule décision ──────────────────────────
SOCLE = [
    ("0", "€", "Le site",
     "Conçu, écrit, illustré, testé sur mobile. Vous le voyez terminé avant "
     "de décider quoi que ce soit.",
     ["Design sur mesure, pas un thème acheté",
      "Textes rédigés, pas du faux latin",
      "Rapide sur mobile",
      "Structuré pour Google et pour les IA"]),
    ("97", "€/mois", "La mise en ligne",
     "Ce que coûte un site qui reste debout. C'est la seule ligne obligatoire, "
     "et elle ne bouge pas.",
     ["Hébergement et nom de domaine",
      "Certificat SSL et sauvegardes",
      "Mises à jour et sécurité",
      "Vos modifications de contenu"]),
]

# ── Les modules : parallèles, facultatifs, ajoutables quand on veut ───────
MODULES = [
    ("dès 297 €", "par mois",
     "Les agents IA",
     "Ils travaillent pendant que vous êtes sur le terrain : ils rattrapent "
     "les appels manqués, relancent les devis en attente et récoltent les avis.",
     ["Récolte d'avis Google", "Réponse aux avis", "Posts sur la fiche Google",
      "SMS après appel manqué", "SMS après formulaire", "Chatbot IA sur le site",
      "Chatbot WhatsApp", "Agent vocal qui décroche"]),
    ("dès 397 €", "par mois",
     "Le SEO et le GEO",
     "Être trouvé sur Google, et être cité par ChatGPT, Perplexity et les "
     "réponses IA de Google — là où une partie de vos clients cherche déjà.",
     ["Fiche Google optimisée", "Pages et articles rédigés",
      "Contenu en plusieurs formats", "Citations locales et backlinks",
      "Corrections techniques"]),
    ("dès 397 €", "par mois, budget média en sus",
     "La publicité",
     "Pour aller chercher des appels tout de suite, pendant que le référencement "
     "met ses trois à six mois à produire.",
     ["Google Ads local", "Local Services Ads (badge Google)",
      "Publicités Meta géolocalisées", "Retargeting",
      "Pages d'atterrissage dédiées", "Suivi des appels"]),
]

POURQUOI = [
    ("Le site nous coûte peu à produire",
     "On en fait beaucoup, on est outillés pour ça. Ce qui prenait trois "
     "semaines il y a deux ans nous prend deux jours."),
    ("On se rémunère sur la suite",
     "Pas sur la création. Un site qui ne vous rapporte rien ne nous rapporte "
     "rien non plus — c'est ce qui nous oblige à le faire bien."),
    ("Si vous ne prenez rien de plus, tant pis pour nous",
     "On aura passé deux heures et vous aurez gagné un site. C'est le risque "
     "qu'on prend, et on le prend en connaissance de cause."),
]

# ── Les agents, rangés par l'endroit où l'argent fuit ─────────────────────
FUITES = [
    ("capte", "L'appel que vous n'avez pas pris",
     "Vous êtes sous un évier, en soin, en consultation. Le téléphone sonne "
     "dans le vide et le client appelle le suivant.",
     [("sms-appel-manque", "SMS après appel manqué",
       "Un message part dans les secondes qui suivent : vous rappelez quand vous pouvez."),
      ("agent-vocal", "Agent vocal",
       "Une voix décroche, comprend la demande et pose le rendez-vous."),
      ("chatbot", "Chatbot sur le site et WhatsApp",
       "Il répond la nuit, le week-end, et pendant que vous travaillez.")]),
    ("transforme", "Le devis parti sans réponse",
     "C'est le trou le plus cher, et c'est celui que personne ne bouche : "
     "le devis est envoyé, puis plus rien, et on n'ose pas relancer.",
     [("relance-devis", "Relance de devis",
       "Deux relances écrites, envoyées au bon moment, sans que vous y pensiez."),
      ("rappel-rdv", "Rappel de rendez-vous",
       "Le créneau non honoré est une heure payée pour rien."),
      ("sms-formulaire", "SMS après formulaire",
       "Le premier qui répond emporte l'affaire. Vous répondez en premier.")]),
    ("capitalise", "L'avis que le client content n'a jamais laissé",
     "Vos meilleurs clients ne pensent jamais à écrire. Vos pires y pensent "
     "toujours. C'est ce déséquilibre qui fait votre note.",
     [("demande-avis", "Récolte d'avis Google",
       "La demande part au bon moment, quand le client est encore satisfait."),
      ("reponse-avis", "Réponse aux avis",
       "Chaque avis reçoit une réponse — Google le regarde, vos clients aussi."),
      ("posts-google", "Posts sur la fiche Google",
       "Une fiche qui vit se montre plus qu'une fiche à l'abandon.")]),
]

ETAPES = [
    ("On construit le site", "Sans rien vous demander. On part de votre fiche "
     "Google, de vos photos et de ce que vous faites déjà. Deux jours."),
    ("Vous le voyez en visio", "Vingt minutes, partage d'écran. Vous dites ce "
     "qui ne va pas, on le corrige devant vous."),
    ("Vous décidez", "Vous prenez la mise en ligne, ou vous ne la prenez pas. "
     "Dans les deux cas le site est à vous et personne ne vous rappelle."),
]

FAQ = [
    ("Le site m'appartient vraiment ?",
     "Oui. À partir du moment où on vous l'a présenté en rendez-vous, il est à "
     "vous : les fichiers, les textes, les images. Ce qui n'est pas compris, "
     "c'est la mise en ligne — tant que l'hébergement n'est pas pris, le site "
     "existe mais il n'est pas publié."),
    ("Il y a un engagement de durée ?",
     "Pas sur les 97 €. Sur les agents, on demande trois mois : un agent ne "
     "montre rien en trente jours, et on préfère vous le dire plutôt que de "
     "vous faire payer un mois pour rien."),
    ("Et si je veux partir avec le site ?",
     "Vous partez avec. On vous transfère les fichiers et le nom de domaine. "
     "On ne prend pas votre site en otage — ce serait le meilleur moyen de ne "
     "plus jamais être recommandés."),
    ("Pourquoi moi ?",
     "Parce que vous avez un métier local, des clients qui vous cherchent sur "
     "leur téléphone, et un site qui date ou qui n'existe pas. C'est là que "
     "l'écart entre ce que vous valez et ce qu'on voit de vous est le plus grand."),
    ("Vous faites ça pour tout le monde ?",
     "Non. On prend quelques dossiers par mois, parce qu'on construit vraiment "
     "les sites. Quand c'est plein, c'est plein."),
    ("C'est quoi le piège ?",
     "Il n'y en a pas, mais la question est saine. Le site est gratuit et le "
     "reste. Ce qui est payant est écrit plus haut, au centime près, et rien "
     "n'est facturé avant que vous ayez vu le site."),
]


RECU = [
    ("Création du site", "0 €", False),
    ("Mise en ligne et maintenance", "97 €/mois", False),
    (None, None, None),
    ("Agents IA", "dès 297 €/mois", True),
    ("SEO et GEO", "dès 397 €/mois", True),
    ("Publicité", "dès 397 €/mois", True),
]


# Trois sites réellement construits, capturés depuis les maquettes livrées.
# Le domaine affiché dans la barre du navigateur est celui de la maquette :
# ne pas inventer de domaine en ligne pour un site qui n'est pas publié.
SITES = [
    ("zimmer.jpg", "zimmer-elagage.fr", "Zimmer Élagage — élagueur à Rezé",
     "Photo pleine page, devis en un écran, numéro cliquable partout. "
     "Serif chaleureux, vert forêt et écorce.",
     "Page d'accueil du site Zimmer Élagage, élagueur à Rezé"),
    ("lm-paysage.jpg", "lm-paysage.fr", "LM Paysage — paysagiste",
     "Un carnet de pépinière : papier, mousse, étiquettes de plants.",
     "Page d'accueil du site LM Paysage, entreprise de paysagisme"),
    ("vdar.jpg", "vdar-couverture.fr", "VDAR — couvreur à Nantes",
     "Anthracite et rouge brique, sombre par défaut. Rien à voir avec les deux autres.",
     "Page d'accueil du site VDAR Couverture de l'habitat, couvreur à Nantes"),
]
MEDIA = "https://decupler.com/wp-content/uploads/2026/09/"


def shot(fichier, domaine, titre, note, alt, retard='', large=False):
    """Une maquette dans un cadre de navigateur.

    `width`/`height` sont posés en dur : sans eux la page saute quand les
    trois images arrivent, et le saut se voit d'autant plus que la section
    est la première chose sous le pli.
    """
    d = f' {retard}' if retard else ''
    w, h = (2016, 1288) if large else (2016, 1288)
    return (f'<figure class="shot rise{d}">'
            f'<div class="shot-bar"><i></i><i></i><i></i><b>{domaine}</b></div>'
            f'<img src="{MEDIA}{fichier}" alt="{alt}" width="{w}" height="{h}" '
            f'loading="lazy" decoding="async">'
            f'<figcaption class="shot-cap"><h3>{titre}</h3><p>{note}</p></figcaption>'
            f'</figure>')


def vitrine_html():
    lead = shot(*SITES[0][:5], retard='d1')
    duo = ''.join(shot(*s[:5], retard=r) for s, r in zip(SITES[1:], ('d2', 'd3')))
    return (f'<div class="vit"><div class="vit-l">{lead}</div>'
            f'<div class="vit-duo">{duo}</div></div>')


def recu_html():
    """L'offre en devis. Les trois dernières lignes sont grisées : elles sont
    facultatives, et un devis dit ça mieux qu'un paragraphe."""
    lignes = ''
    for libelle, montant, option in RECU:
        if libelle is None:
            lignes += '<div class="sep"></div>'
            continue
        cl = ' class="opt"' if option else ''
        lignes += f'<div{cl}><dt>{libelle}</dt><dd>{montant}</dd></div>'
    return (f'<div class="recu rise"><p class="recu-t">Ce que ça coûte</p>'
            f'<dl>{lignes}<div class="sep"></div>'
            f'<div class="tot"><dt>À payer aujourd\'hui</dt><dd>0 €</dd></div></dl>'
            f'<p class="recu-p">Les trois dernières lignes sont facultatives. '
            f'On les ajoute quand vous le demandez, on les retire pareil.</p></div>')


def socle_html():
    out = ''
    for i, (nb, unite, quoi, txt, items) in enumerate(SOCLE):
        if i:
            out += '<div class="socle-plus" aria-hidden="true">+</div>'
        li = ''.join(f'<li>{x}</li>' for x in items)
        out += (f'<div class="socle-c"><span class="p-nb prix">{nb}'
                f'<span class="u">{unite}</span></span>'
                f'<div class="p-quoi">{quoi}</div><p class="p-txt">{txt}</p>'
                f'<ul>{li}</ul></div>')
    return f'<div class="socle rise">{out}</div>'


def modules_html():
    out = ''
    for prix, cadence, titre, chapo, items in MODULES:
        li = ''.join(f'<li>{x}</li>' for x in items)
        out += (f'<div class="mod"><div class="mod-p prix">{prix}'
                f'<small>{cadence}</small></div>'
                f'<div><h3>{titre}</h3><p>{chapo}</p>'
                f'<ul class="mod-l">{li}</ul></div></div>')
    return f'<div class="mods rise">{out}</div>'


def fuites_html():
    out = ''
    for i, (cle, titre, chapo, agents) in enumerate(FUITES, 1):
        cards = ''
        for slug, nom, txt in agents:
            cards += (f'<div class="ag2">{I.bloc(slug, "ag2-ic")}'
                      f'<div class="ag2-tx"><h4>{nom}</h4><p>{txt}</p></div></div>')
        alt = ' alt' if i % 2 == 1 else ''
        out += (f'<section class="dcp-sec{alt}"><div class="in">'
                f'<div class="step-lab rise">{I.bloc(cle, "si")}'
                f'<h3>{titre}</h3></div>'
                f'<p class="step-chapo rise">{chapo}</p>'
                f'<div class="rise">{cards}</div></div></section>')
    return out


def page():
    pq = ''.join(f'<div><span class="r"></span><h3>{t}</h3><p>{d}</p></div>'
                 for t, d in POURQUOI)
    et = ''.join(f'<div class="et-l rise"><div class="num"></div>'
                 f'<div><h3>{t}</h3><p>{d}</p></div></div>'
                 for t, d in ETAPES)
    faq = ''.join(f'<details class="rise"><summary>{q}</summary><p>{r}</p></details>'
                  for q, r in FAQ)

    return f"""{FONTS}
{SKIN}
<div class="dcp">

<section class="dcp-hero" id="offre"><div class="in dcp-grid">
  <div>
    <h1>On vous construit le site.<br><em>Vous ne payez pas la construction.</em></h1>
    <p class="lead">Pour les {CIBLES}. On conçoit le site, on vous le montre
    terminé, et vous décidez ensuite. Rien n'est facturé avant que vous l'ayez vu.</p>
    <p><a class="dcp-cta" href="#rdv">Voir mon site avant de décider</a></p>
    <p class="dcp-under">Vingt minutes en visio  ·  Aucune carte bancaire</p>
  </div>
  {recu_html()}
</div></section>

<section class="dcp-band" id="sites"><div class="in plein">
  <h2>Voilà ce qu'on livre</h2>
  <p class="band-p">Trois artisans, trois sites, trois identités. On ne décline
  pas un modèle en changeant le logo et la couleur — c'est justement ce que
  vous avez déjà refusé ailleurs.</p>
  {vitrine_html()}
</div></section>

<section class="dcp-sec" id="prix"><div class="in">
  <h2>Ce que vous payez, au centime près</h2>
  <p class="lead">Deux lignes forment une seule décision : un site qu'on ne
  publie pas ne sert à rien. Tout le reste s'ajoute quand vous le voulez,
  et se retire pareil.</p>
  {socle_html()}
  <p class="lead mods-intro">À ajouter quand vous voulez, dans
  l'ordre que vous voulez.</p>
  {modules_html()}
  <div class="cond rise"><b>La seule condition, dite en clair</b>
  <p>Le site est à vous dès qu'on vous l'a présenté en rendez-vous. Il n'est
  pas mis en ligne tant que l'hébergement n'est pas pris — l'héberger à nos
  frais pour quelqu'un qui n'en veut pas, on ne sait pas le faire.</p></div>
</div></section>

<section class="dcp-band" id="pourquoi"><div class="in plein">
  <h2>Pourquoi c'est gratuit</h2>
  <p class="band-p">
  C'est la première question qu'on nous pose, alors on y répond ici plutôt
  qu'en bas de page.</p>
  <div class="pq">{pq}</div>
</div></section>

{fuites_html()}

<section class="dcp-sec" id="comment"><div class="in">
  <h2>Comment ça se passe</h2>
  <div class="etapes">{et}</div>
</div></section>

<section class="dcp-sec alt" id="questions"><div class="in">
  <h2>Les questions qu'on nous pose</h2>
  <div class="rise">{faq}</div>
</div></section>

<section class="dcp-band centre" id="rdv"><div class="in plein">
  <h2>Votre site existe déjà.<br>Il ne manque que vingt minutes.</h2>
  <p class="band-p">
  On vous le montre en visio, vous dites ce qui ne va pas, on le corrige
  devant vous. Ensuite vous décidez, et pas avant.</p>
  <p class="band-act"><a class="dcp-cta vert" href="/contact/">Prendre les vingt minutes</a></p>
</div></section>

{PT.rendu(FAQ)}
</div>"""


if __name__ == '__main__':
    html = wpcss.harden(page())
    wpcss.audit(html) if hasattr(wpcss, 'audit') else None
    dst = RACINE / 'content/articles/site-gratuit-local.html'
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(html, encoding='utf-8')
    print(f"{dst}  —  {len(html):,} octets".replace(',', ' '))

# Contrôles passés avant publication, aux deux largeurs qui comptent :
#     node scripts/rendu/controle.mjs content/articles/site-gratuit-local.html 1440
#     node scripts/rendu/controle.mjs content/articles/site-gratuit-local.html 390
# Débordement horizontal nul, aucun contraste sous le seuil, hiérarchie de
# titres continue. Les 5 signalements du détecteur d'anti-patterns Impeccable
# ont été vérifiés contre le rendu réel : tous faux positifs (icônes côte à
# côte et non empilées, texte inséré de 32px par `.in`, « €/mois » à 26px et
# non 6,7px — l'`em` était résolu sur la racine au lieu du parent clampé).
