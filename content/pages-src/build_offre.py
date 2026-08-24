# -*- coding: utf-8 -*-
"""Construit la page « Votre site, offert » (WordPress ID 20478).

    python3 content/pages-src/build_offre.py

Sort content/articles/offre-site-offert.html, prêt pour wp_publish.py.
Les audits wpcss sont des assertions : le script refuse d'écrire une page
que wpautop casserait.
"""
import sys, re, json
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
for d in ('content/data', 'content/components', 'scripts/lib'):
    sys.path.insert(0, str(RACINE / d))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import agents_locaux as A
import metiers_locaux as ML
import cta_prompts as CTA
import wpcss
import icones as I

SKIN = open(RACINE / 'content/skins/dcp.css', encoding='utf-8').read()
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Syne:wght@700;800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700'
         '&family=JetBrains+Mono:wght@400;700&display=swap">')

# ── Un visuel animé par groupe, construit en CSS ───────────────────────────
from visuels import VIZ


def agents_html():
    out = ''
    for i, (cle, titre_etape, chapo) in enumerate(A.ETAPES, 1):
        cards = ''
        for slug, nom, _, promesse, meca, preuve in A.par_etape(cle):
            # Variable distincte de titre_etape : les deux coexistaient sous le
            # meme nom, et le <h3> de la section affichait en ligne le nom du
            # dernier agent de la grille au lieu du titre de l'etape.
            titre_carte = f'<a href="{A.LIENS[slug]}">{nom}</a>' if slug in A.LIENS else nom
            cards += (f'<div class="ag2">{I.bloc(slug, "ag2-ic")}'
                      f'<div class="ag2-tx"><h4>{titre_carte}</h4><p>{promesse}</p></div></div>')
        flip = ' flip' if i % 2 == 0 else ''
        alt = ' alt' if i % 2 == 1 else ''
        out += f"""
<section class="dcp-sec{alt}"><div class="in">
  <div class="step-lab rise">{I.bloc(cle, "si")}<div class="n">{i:02d}</div><h3>{titre_etape}</h3></div>
  <p class="step-chapo rise">{chapo}</p>
  <div class="duo{flip}">{VIZ[cle]}<div class="rise">{cards}</div></div>
</div></section>"""
    return out

# L'emoji du catalogue sert de cle de lecture ; le rendu, lui, passe par le
# trait, qui ne depend pas de la police emoji du systeme.
# Les pages metier du cluster. Tant qu'elles sont en brouillon, les cartes ne
# pointent nulle part : un lien vers un brouillon est un 404 pour un visiteur.
# Basculer a True le jour ou elles passent en ligne.
CLUSTER_EN_LIGNE = True
CIBLE_LIEN = {
    'Dentistes et cabinets': 'creation-site-internet-dentiste',
    'Spas et instituts': 'creation-site-internet-institut-de-beaute',
}

NOM_PAGE = {'dentiste': 'dentiste', 'plombier': 'plombier',
            'electricien': 'électricien', 'institut-de-beaute': 'institut de beauté'}

CIBLE_IC = {'Paysagistes': 'paysagiste', 'Artisans du batiment': 'artisan',
            'Artisans du bâtiment': 'artisan', 'Dentistes et cabinets': 'dentiste',
            'Spas et instituts': 'spa', 'Agences immobilières': 'immobilier',
            "Maisons d'hôtes": 'maison-hote'}


def cibles_html():
    manquants = [n for n, _, _ in A.CIBLES if n not in CIBLE_IC]
    assert not manquants, f'metier sans icone : {manquants}'
    cartes = []
    for nom, ic, txt in A.CIBLES:
        titre = nom
        if CLUSTER_EN_LIGNE and nom in CIBLE_LIEN:
            titre = f'<a href="https://decupler.com/{CIBLE_LIEN[nom]}/">{nom}</a>'
        cartes.append(f'<div class="cib-c rise">{I.bloc(CIBLE_IC[nom], "cib-ic")}'
                      f'<h3>{titre}</h3><p>{txt}</p></div>')
    grille = '<div class="cib">' + ''.join(cartes) + '</div>'
    if not CLUSTER_EN_LIGNE or not ML.METIERS:
        return grille
    liens = ', '.join(
        f'<a href="https://decupler.com/creation-site-internet-{slug}/">{NOM_PAGE[slug]}</a>'
        for slug in ML.METIERS if slug in NOM_PAGE)
    return (grille + '<p class="cib-plus rise">On détaille la mécanique métier par métier&nbsp;: '
            + liens + '.</p>')


RDV = 'https://calendly.com/fenina-nathan/consultationstrategique'
# Date de derniere revision du contenu. A remonter a la main quand la page
# change vraiment : une date qui bouge toute seule ne prouve rien.
MAJ = '21 août 2026'


def mini_cta(phrase, libelle='Voir mon site avant de décider'):
    """Relance courte au fil de la page, pour ne pas renvoyer tout le monde au pied."""
    return (f'<div class="dcp-mini rise"><p class="dcp-mini-t">{phrase}</p>'
            f'<p class="dcp-mini-a"><a class="dcp-cta" href="{RDV}" rel="noopener">{libelle}</a></p></div>')

FAQ = [
 ("C'est vraiment gratuit&nbsp;? Où est le piège&nbsp;?",
  "Il n'y en a pas. La création du site ne vous coûte rien et vous ne payez rien tant que vous ne l'avez pas vu. "
  "On se rémunère sur l'abonnement mensuel, qui couvre l'hébergement et les agents. Si le site ne vous plaît pas, "
  "vous nous le dites et on en reste là."),
 ("En quoi c'est différent d'une agence qui facture la création du site&nbsp;?",
  "Une agence classique est payée à la livraison&nbsp;: son travail s'arrête le jour où le site est en ligne. "
  "Ici, on n'est payé qu'ensuite, sur l'abonnement&nbsp;— donc on n'a aucun intérêt à livrer un site qui ne ramène "
  "personne. C'est le même métier que notre <a href=\"https://decupler.com/agence-seo/\">agence SEO</a>, "
  "avec un modèle économique inversé."),
 ("Pourquoi feriez-vous un site gratuitement&nbsp;?",
  "Parce qu'un site seul ne vaut plus grand-chose&nbsp;: n'importe qui peut en générer un aujourd'hui. "
  "Ce qui a de la valeur, c'est ce qui tourne derrière et qui vous ramène des clients. C'est là-dessus qu'on est payés, "
  "et c'est pour ça qu'on a intérêt à ce que ça marche."),
 ("Je n'ai pas le temps de m'occuper de tout ça.",
  "C'est exactement le point. Les agents tournent sans vous. Le seul geste qu'on vous demande, c'est d'envoyer "
  "de temps en temps une photo de chantier par SMS&nbsp;— et encore, c'est optionnel."),
 ("L'agent vocal va-t-il remplacer mon accueil&nbsp;?",
  "Non. Il ne se déclenche que si personne ne décroche. Si vous répondez, il ne se passe rien. "
  "Il prend le relais uniquement quand l'appel serait tombé dans le vide."),
 ("Vous filtrez les mauvais avis&nbsp;?",
  "Non, et méfiez-vous de ceux qui vous le proposent. Depuis 2026, Google interdit explicitement de trier les clients "
  "selon leur note avant de les envoyer sur la fiche "
  "(<a href=\"https://support.google.com/business/answer/7091\" rel=\"nofollow noopener\" target=\"_blank\">règles de Google sur les avis</a>), "
  "et sanctionne jusqu'à la suspension complète du profil. "
  "On demande l'avis à tous vos clients. En revanche, un SMS de satisfaction envoyé en fin d'intervention vous permet "
  "de rattraper un mécontent avant qu'il n'écrive&nbsp;— ça, c'est du service, et c'est parfaitement conforme."),
 ("Combien de temps avant d'avoir le site en ligne&nbsp;?",
  "Vous le voyez en visio avant toute décision. Une fois que vous dites oui, la mise en ligne et le branchement "
  "des agents se font dans la foulée."),
]
faq_html = ''.join(f'<details class="rise"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
faq_ld = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
 {"@type":"Question","name":re.sub(r'&nbsp;|<[^>]+>',' ',q).strip(),
  "acceptedAnswer":{"@type":"Answer","text":re.sub(r'&nbsp;|<[^>]+>',' ',a).strip()}} for q,a in FAQ]}, ensure_ascii=False)

BODY = f"""{FONTS}
{SKIN}
<div class="dcp">

<section class="dcp-hero"><div class="in dcp-grid">
  <div>
    <h1><span class="k">Création de site internet pour entreprise locale</span>Votre site, <em>offert</em>.<br>Vous ne payez que ce qui vous rapporte des clients.</h1>
    <p class="lead"><strong>La création de votre site internet ne vous est pas facturée&nbsp;:</strong> on le construit, vous le voyez terminé, puis vous décidez. Vous ne payez ensuite qu'un abonnement mensuel — hébergement et agents — à partir de 199&nbsp;€. Pour une entreprise locale — un artisan, un cabinet, un institut, une agence — c'est le seul modèle où le prestataire n'est payé que si le site rapporte des clients.</p>
    <p class="lead">Pendant que vous êtes sur le terrain, les agents rattrapent les appels manqués, relancent les devis en attente et récoltent les avis.</p>
    <div class="dcp-act"><a class="dcp-cta" href="https://calendly.com/fenina-nathan/consultationstrategique" rel="noopener">Voir mon site avant de décider</a></div>
    <p class="dcp-under">Site 0&nbsp;€ · puis dès 199&nbsp;€/mois</p>
  </div>
  <div class="hero-visuel">
    <div class="photo"><img src="https://decupler.com/wp-content/uploads/2026/08/offre-hero.jpg" alt="Un paysagiste en fin de journée regarde son téléphone : le SMS automatique a retenu le client qu'il n'a pas pu prendre" width="1536" height="1024" loading="eager" decoding="async"></div>
    <div class="phone"><div class="phone-scr">
      <div class="phone-top"><div class="phone-notch"></div></div>
      <div class="phone-body">
        <div class="evt evt-call"><b>06 12 •• •• 41</b><span>Appel entrant · 14:32</span></div>
        <div class="evt evt-miss"><b>Appel manqué</b><span>Vous êtes sur un chantier</span></div>
        <div class="evt evt-sms"><b>SMS envoyé</b><span>«&nbsp;Bonjour, ici Dupont Paysage. Je vous rappelle très vite.&nbsp;»</span><span class="evt-tag">Client retenu</span></div>
      </div>
    </div></div>
  </div>
</div></section>

<section class="dcp-band"><div class="in">
  <div class="cnt lost">{I.bloc("sms-appel-manque", "cnt-ic")}<p class="lbl">Sans le système</p><p class="num">L'appel manqué ne laisse aucune trace</p><p class="cap">Le client ne laisse pas de message. Il compose le numéro suivant, et vous ne saurez jamais qu'il a appelé.</p></div>
  <div class="arrow">→</div>
  <div class="cnt won">{I.bloc("sms-formulaire", "cnt-ic")}<p class="lbl">Avec</p><p class="num">Le SMS part avant qu'il ait raccroché</p><p class="cap">À votre nom, avec le lien de votre formulaire. Vous rappelez quand vous descendez du toit.</p></div>
</div></section>

<section class="dcp-sec"><div class="in">
  <div class="eyebrow rise">Le vrai problème</div>
  <h2 class="rise">Vous ne manquez pas de clients. Vous les perdez en route.</h2>
  <p class="lead rise">Il est 18&nbsp;h&nbsp;12. Quelqu'un cherche votre métier dans votre ville et appelle le premier numéro de la liste&nbsp;: le vôtre. Vous êtes sur un chantier, en rendez-vous, en soin. Ça sonne dans le vide. <strong>Il ne laisse pas de message. Il appelle le suivant.</strong> Vous ne saurez jamais qu'il a existé.</p>
  <div class="photo rise"><img src="https://decupler.com/wp-content/uploads/2026/08/offre-probleme.jpg" alt="Un téléphone qui sonne dans un atelier vide : l'appel manqué que personne ne rattrape" width="1536" height="1024" loading="lazy" decoding="async"></div>
  <p class="photo-cap rise">Le lead le moins cher de votre année, c'est celui qui vous appelait déjà.</p>
  <p class="lead rise">Et ce n'est pas qu'une affaire d'appels. Le devis parti la semaine dernière qui n'a jamais reçu de réponse. Le rendez-vous que le client a oublié. Les deux cents clients satisfaits qui n'ont jamais laissé l'avis qui vous en aurait amené un de plus.</p>
  <div class="dcp-tip rise"><div class="ic">💡</div><p>Un joli site ne bouche aucun de ces trous. C'est pour ça qu'on vous l'offre&nbsp;: <strong>la valeur est dans ce qui tourne derrière</strong>. La création d'un site internet n'est plus le travail difficile&nbsp;— le travail difficile, c'est le <a href="https://decupler.com/seo-local/">SEO local</a> et ce qui se passe après le clic.</p></div>
</div></section>

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">Ce qui travaille pour vous</div>
  <h2 class="rise">Les agents, rangés par endroit où l'argent fuit</h2>
  <p class="lead rise">Un site internet local qui ne fait qu'exister ne sert à rien. Ce sont ces agents qui le rendent rentable. Vous n'êtes pas obligé de tout prendre&nbsp;: on démarre par les trois qui rapportent le plus vite, et on ajoute au fur et à mesure&nbsp;— c'est ce qui fait varier l'abonnement.</p>
</div></section>
{agents_html()}

<section class="dcp-sec"><div class="in">
  {mini_cta('Vous voulez savoir lesquels de ces agents changeraient quelque chose chez vous&nbsp;? On regarde ensemble, en quinze minutes.', 'Prendre 15 minutes')}
</div></section>

<section class="dcp-sec"><div class="in">
  <div class="eyebrow rise">Le prix</div>
  <h2 class="rise">Combien coûte la création d'un site internet pour une entreprise locale&nbsp;?</h2>
  <p class="lead rise">Zéro. La création du site est offerte, et vous ne payez qu'un abonnement mensuel une fois le site validé. Pas de frais d'installation, pas de facture de création, pas de surprise.</p>
  <div class="prix rise">
    <div class="prix-c zero"><p class="lbl">Création du site</p><p class="val">0&nbsp;€</p><p class="sub">Vous le voyez avant de décider</p></div>
    <div class="prix-plus">+</div>
    <div class="prix-c"><p class="lbl">Hébergement et agents</p><p class="val">dès 199&nbsp;€</p><p class="sub">par mois, selon le nombre d'agents</p></div>
  </div>
  <table class="rise"><thead><tr><th>Ce que vous payez</th><th>Ce que ça couvre</th></tr></thead><tbody>
    <tr><td>La création du site</td><td>Rien. Vous le voyez terminé avant de vous engager.</td></tr>
    <tr><td>À partir de 199&nbsp;€/mois</td><td>L'hébergement, la maintenance, et le premier socle d'agents.</td></tr>
    <tr><td>Au-delà</td><td>Chaque agent supplémentaire fait monter l'abonnement. Vous choisissez lesquels.</td></tr>
  </tbody></table>
  <div class="dcp-tip rise"><div class="ic">🧮</div><p>La bonne façon de juger&nbsp;: si le système vous fait signer <strong>un seul chantier ou un seul contrat de plus dans l'année</strong>, l'abonnement est déjà remboursé. Le rapport mensuel est là pour que vous le vérifiiez vous-même, pas pour que vous nous croyiez sur parole.</p></div>
</div></section>

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">Pour qui</div>
  <h2 class="rise">Les entreprises locales où ça change le plus</h2>
  <p class="lead rise">La création d'un site internet pour une entreprise locale n'a rien à voir avec celle d'un site vitrine classique&nbsp;: ici, tout se joue sur la recherche locale et sur le téléphone. Les six métiers ci-dessous ne sont que des exemples&nbsp;— la mécanique est la même dès que vos clients vous trouvent à moins de trente kilomètres. Le point commun de ces métiers&nbsp;: vous travaillez avec vos mains, vos patients ou vos clients devant vous&nbsp;— pas devant un écran à guetter les demandes.</p>
  <div class="photo rise"><img src="https://decupler.com/wp-content/uploads/2026/08/offre-metiers.jpg" alt="La gérante d'un institut de beauté consulte son téléphone à l'accueil de son établissement" width="1536" height="1024" loading="lazy" decoding="async"></div>
  {cibles_html()}
</div></section>

<section class="dcp-sec"><div class="in">
  <div class="eyebrow rise">Comment ça se passe</div>
  <h2 class="rise">Trois étapes, et vous décidez à la deuxième</h2>
  <div class="etapes">
    <div class="et-l rise"><div class="num"></div><div><h3>On construit le site</h3><p>À partir de vos photos, de vos prestations et de ce que vos clients cherchent réellement dans votre ville. C'est notre métier de départ&nbsp;: on est <a href="https://decupler.com/agence-seo/">agence SEO</a> avant d'être fournisseur de sites. Vous n'avez rien à faire et rien à payer.</p></div></div>
    <div class="et-l rise"><div class="num"></div><div><h3>On vous le montre en visio</h3><p>Quinze minutes, partage d'écran. Vous voyez le site fini. Si vous n'aimez pas, on s'arrête là et ça ne vous a rien coûté.</p></div></div>
    <div class="et-l rise"><div class="num"></div><div><h3>On branche les agents</h3><p>Mise en ligne, numéro de suivi, <a href="https://decupler.com/fiche-gmb/">fiche Google</a>, agents choisis. Ensuite, chaque mois, vous recevez le compte de ce que le système a rattrapé.</p></div></div>
  </div>
  {mini_cta('La deuxième étape ne vous engage à rien&nbsp;: vous voyez le site fini, et vous décidez ensuite.')}
</div></section>

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">FAQ</div>
  <h2 class="rise">Les questions qu'on nous pose</h2>
  {faq_html}
  <div class="dcp-sign rise">
    <p class="dcp-sign-t">Écrit par <strong>Nathan Fenina</strong>, fondateur de <strong>Décupler</strong>, agence SEO et GEO. On construit des sites d'entreprises locales et on les fait remonter&nbsp;— d'abord sur Google, ensuite dans les réponses des IA. Voir <a href="https://decupler.com/cas-clients/">nos cas clients</a> et notre approche de la <a href="https://decupler.com/visibilite-llm/">visibilité dans les LLM</a>.</p>
    <p class="dcp-sign-d">Dernière mise à jour&nbsp;: {MAJ}</p>
  </div>
</div></section>

</div>
{CTA.render('vous', href='https://calendly.com/fenina-nathan/consultationstrategique')}
<div class="dcp-js"><script type="application/ld+json">{faq_ld}</script></div>
<div class="dcp-js"><noscript><style>.dcp .rise{{opacity:1;transform:none}}.dcp .ic-svg>*{{stroke-dashoffset:0}}</style></noscript></div>
<div class="dcp-js"><script>
(function(){{
  /* Le theme affiche son propre titre de page au-dessus du contenu : on le retire,
     comme le font deja les 15 autres pages. */
  document.querySelectorAll('.entry-header,.entry-title,.ast-single-entry-banner,.page-header')
    .forEach(function(e){{e&&e.remove&&e.remove()}});
  /* Les bandes vont d'un bord a l'autre. On mesure la vraie gouttiere plutot
     que d'utiliser 100vw, qui compte la barre de defilement et deborde. */
  function bleed(){{
    var d=document.querySelector('.dcp'); if(!d) return;
    var r=d.getBoundingClientRect(), w=document.documentElement.clientWidth, st=document.documentElement.style;
    st.setProperty('--dcp-bl', Math.min(400,Math.max(0,Math.round(r.left)))+'px');
    st.setProperty('--dcp-br', Math.min(400,Math.max(0,Math.round(w-r.right)))+'px');
  }}
  bleed();
  var t; addEventListener('resize',function(){{clearTimeout(t);t=setTimeout(bleed,120)}});
  addEventListener('load',bleed);

  var els=document.querySelectorAll('.dcp .rise');
  function showAll(){{for(var i=0;i<els.length;i++)els[i].classList.add('vu')}}
  if(!('IntersectionObserver' in window)){{showAll();return}}
  var io=new IntersectionObserver(function(en){{
    en.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('vu');io.unobserve(e.target)}}}})
  }},{{rootMargin:'0px 0px -8% 0px',threshold:.05}});
  for(var i=0;i<els.length;i++)io.observe(els[i]);
  /* filet de securite : rien ne doit rester invisible */
  setTimeout(showAll,2500);
}})();
</script></div>
"""

# wpautop insere </p><p> dans les blocs <style> des qu'il y a une ligne vide :
# on minifie chaque feuille avant publication.
BODY = wpcss.harden(BODY)
probs = wpcss.audit(BODY)
assert not probs, probs
# Un enfant inline voisin d'un enfant block : wpautop y glisse un </p> orphelin,
# le navigateur en fait un paragraphe vide, et la grille se decale.
risques = wpcss.audit_markup(BODY)
assert not risques, f'{len(risques)} conteneur(s) que wpautop cassera : {risques[:3]}'
# Une balise mal fermee laisse son conteneur ouvert : il avale la suite du
# document et lui impose ses styles. Silencieux, visible seulement au rendu.
struct = wpcss.audit_structure(BODY)
assert not struct, f'{len(struct)} probleme(s) de structure : {struct[:3]}'
out = str(RACINE / 'content/articles/offre-site-offert.html')
open(out, 'w', encoding='utf-8').write(BODY)
txt = re.sub(r'<[^>]+>', ' ', re.sub(r'<style.*?</style>|<script.*?</script>', '', BODY, flags=re.S))
print('écrit :', out, len(BODY), 'octets ·', len(txt.split()), 'mots')
