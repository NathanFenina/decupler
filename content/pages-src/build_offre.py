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
import agents_locaux as A
import cta_prompts as CTA
import wpcss

SKIN = open(RACINE / 'content/skins/dcp.css', encoding='utf-8').read()
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Syne:wght@700;800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700'
         '&family=JetBrains+Mono:wght@400;700&display=swap">')

# ── Un visuel animé par groupe, construit en CSS ───────────────────────────
VIZ = {
"trouve": """<div class="viz rise">
  <div class="viz-h"><strong>Dupont Paysage</strong><span class="tag">16/16</span></div>
  <div class="viz-row"><span class="viz-dot"></span>Catégories et services</div>
  <div class="viz-row"><span class="viz-dot"></span>Zones desservies</div>
  <div class="viz-row"><span class="viz-dot"></span>Photos et description</div>
  <div class="viz-row"><span class="viz-dot"></span>Horaires et coordonnées</div>
  <div class="viz-bar"><i></i></div>
</div>""",

"capte": """<div class="viz rise">
  <div class="viz-h"><strong>06 12 •• •• 41</strong><span class="tag">rattrapé</span></div>
  <div class="chat">
    <div class="bub them">Appel manqué à 14:32<span class="t">Vous étiez sur un chantier</span></div>
    <div class="bub you">Bonjour, ici Dupont Paysage. Je suis en intervention, je vous rappelle très vite.<span class="t">Envoyé automatiquement · 14:32</span></div>
    <div class="bub them">Parfait merci, c'est pour une haie à tailler<span class="t">14:38</span></div>
  </div>
</div>""",

"transforme": """<div class="viz rise">
  <div class="viz-h"><strong>Devis n° 2418 · 3 240 €</strong><span class="tag">signé</span></div>
  <div class="dev-line"><span class="dev-when">J+0</span><span class="dev-what">Devis envoyé</span><span class="dev-st wait">Sans réponse</span></div>
  <div class="dev-line"><span class="dev-when">J+3</span><span class="dev-what">Première relance</span><span class="dev-st sent">Automatique</span></div>
  <div class="dev-line"><span class="dev-when">J+7</span><span class="dev-what">Seconde relance</span><span class="dev-st sent">Automatique</span></div>
  <div class="dev-line"><span class="dev-when">J+8</span><span class="dev-what">Le client rappelle</span><span class="dev-st won">Chantier signé</span></div>
</div>""",

"capitalise": """<div class="viz rise">
  <div class="viz-h"><strong>Avis Google</strong><span class="tag">+4 ce mois-ci</span></div>
  <div class="rev"><span class="rev-st">★★★★★</span><span class="rev-tx">Travail soigné, délais tenus.</span><span class="rev-ok">Répondu</span></div>
  <div class="rev"><span class="rev-st">★★★★★</span><span class="rev-tx">Très bon contact, je recommande.</span><span class="rev-ok">Répondu</span></div>
  <div class="rev"><span class="rev-st">★★★★☆</span><span class="rev-tx">Bon travail, un peu de retard.</span><span class="rev-ok">Répondu</span></div>
  <div class="viz-bar"><i></i></div>
</div>""",

"pilote": """<div class="viz rise">
  <div class="viz-h"><strong>Votre mois</strong><span class="tag">rapport auto</span></div>
  <div class="rep-l"><span>Appels rattrapés</span><b>19</b></div>
  <div class="rep-l"><span>Devis relancés</span><b>12</b></div>
  <div class="rep-l"><span>Nouveaux avis</span><b>7</b></div>
  <div class="rep-l"><span>Rendez-vous pris</span><b>4</b></div>
</div>"""}

def agents_html():
    out = ''
    for i, (cle, titre, chapo) in enumerate(A.ETAPES, 1):
        cards = ''.join(
            f'<div class="ag2"><div class="pill">{nom.split()[0]}</div><h4>{nom}</h4>'
            f'<p>{promesse}</p></div>'
            for slug, nom, _, promesse, meca, preuve in A.par_etape(cle))
        flip = ' flip' if i % 2 == 0 else ''
        alt = ' alt' if i % 2 == 1 else ''
        out += f"""
<section class="dcp-sec{alt}"><div class="in">
  <div class="step-lab rise"><div class="n">{i:02d}</div><h3>{titre}</h3></div>
  <p class="step-chapo rise">{chapo}</p>
  <div class="duo{flip}">{VIZ[cle]}<div class="rise">{cards}</div></div>
</div></section>"""
    return out

def cibles_html():
    return '<div class="cib">' + ''.join(
        f'<div class="cib-c rise"><p class="cib-ic">{ic}</p><h4>{nom}</h4><p>{txt}</p></div>'
        for nom, ic, txt in A.CIBLES) + '</div>'

FAQ = [
 ("C'est vraiment gratuit&nbsp;? Où est le piège&nbsp;?",
  "Il n'y en a pas. La création du site ne vous coûte rien et vous ne payez rien tant que vous ne l'avez pas vu. "
  "On se rémunère sur l'abonnement mensuel, qui couvre l'hébergement et les agents. Si le site ne vous plaît pas, "
  "vous nous le dites et on en reste là."),
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
  "selon leur note avant de les envoyer sur la fiche, et sanctionne jusqu'à la suspension complète du profil. "
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
    <div class="eyebrow">Entreprises locales</div>
    <h2>Votre site, <em>offert</em>.<br>Vous ne payez que ce qui vous rapporte.</h2>
    <p class="lead">On construit votre site, vous le voyez terminé, puis vous décidez. Ensuite les agents travaillent pendant que vous êtes sur le terrain&nbsp;: ils rattrapent les appels manqués, relancent les devis en attente, récoltent les avis.</p>
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
  <div class="cnt lost"><p class="lbl">Sans le système</p><p class="num">L'appel manqué ne laisse aucune trace</p><p class="cap">Le client ne laisse pas de message. Il compose le numéro suivant, et vous ne saurez jamais qu'il a appelé.</p></div>
  <div class="arrow">→</div>
  <div class="cnt won"><p class="lbl">Avec</p><p class="num">Le SMS part avant qu'il ait raccroché</p><p class="cap">À votre nom, avec le lien de votre formulaire. Vous rappelez quand vous descendez du toit.</p></div>
</div></section>

<section class="dcp-sec"><div class="in">
  <div class="eyebrow rise">Le vrai problème</div>
  <h2 class="rise">Vous ne manquez pas de clients. Vous les perdez en route.</h2>
  <p class="lead rise">Il est 18&nbsp;h&nbsp;12. Quelqu'un cherche votre métier dans votre ville et appelle le premier numéro de la liste&nbsp;: le vôtre. Vous êtes sur un chantier, en rendez-vous, en soin. Ça sonne dans le vide. <strong>Il ne laisse pas de message. Il appelle le suivant.</strong> Vous ne saurez jamais qu'il a existé.</p>
  <div class="photo rise"><img src="https://decupler.com/wp-content/uploads/2026/08/offre-probleme.jpg" alt="Un téléphone qui sonne dans un atelier vide : l'appel manqué que personne ne rattrape" width="1536" height="1024" loading="lazy" decoding="async"></div>
  <p class="photo-cap rise">Le lead le moins cher de votre année, c'est celui qui vous appelait déjà.</p>
  <p class="lead rise">Et ce n'est pas qu'une affaire d'appels. Le devis parti la semaine dernière qui n'a jamais reçu de réponse. Le rendez-vous que le client a oublié. Les deux cents clients satisfaits qui n'ont jamais laissé l'avis qui vous en aurait amené un de plus.</p>
  <div class="dcp-tip rise"><div class="ic">💡</div><p>Un joli site ne bouche aucun de ces trous. C'est pour ça qu'on vous l'offre&nbsp;: <strong>la valeur est dans ce qui tourne derrière</strong>.</p></div>
</div></section>

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">Ce qui travaille pour vous</div>
  <h2 class="rise">Les agents, rangés par endroit où l'argent fuit</h2>
  <p class="lead rise">Vous n'êtes pas obligé de tout prendre. On démarre par les trois qui rapportent le plus vite, et on ajoute au fur et à mesure&nbsp;— c'est ce qui fait varier l'abonnement.</p>
</div></section>
{agents_html()}

<section class="dcp-sec"><div class="in">
  <div class="eyebrow rise">Le prix</div>
  <h2 class="rise">Un seul abonnement, qui monte avec ce que vous branchez</h2>
  <p class="lead rise">Pas de frais d'installation, pas de facture de création, pas de surprise.</p>
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
  <h2 class="rise">Les métiers où ça change le plus</h2>
  <p class="lead rise">Le point commun&nbsp;: vous travaillez avec vos mains, vos patients ou vos clients devant vous&nbsp;— pas devant un écran à guetter les demandes.</p>
  <div class="photo rise"><img src="https://decupler.com/wp-content/uploads/2026/08/offre-metiers.jpg" alt="La gérante d'un institut de beauté consulte son téléphone à l'accueil de son établissement" width="1536" height="1024" loading="lazy" decoding="async"></div>
  {cibles_html()}
</div></section>

<section class="dcp-sec"><div class="in">
  <div class="eyebrow rise">Comment ça se passe</div>
  <h2 class="rise">Trois étapes, et vous décidez à la deuxième</h2>
  <div class="etapes">
    <div class="et-l rise"><div class="num"></div><div><h4>On construit le site</h4><p>À partir de vos photos, de vos prestations et de ce que vos clients cherchent réellement dans votre ville. C'est notre métier de départ&nbsp;: on est <a href="https://decupler.com/agence-seo/">agence SEO</a> avant d'être fournisseur de sites. Vous n'avez rien à faire et rien à payer.</p></div></div>
    <div class="et-l rise"><div class="num"></div><div><h4>On vous le montre en visio</h4><p>Quinze minutes, partage d'écran. Vous voyez le site fini. Si vous n'aimez pas, on s'arrête là et ça ne vous a rien coûté.</p></div></div>
    <div class="et-l rise"><div class="num"></div><div><h4>On branche les agents</h4><p>Mise en ligne, numéro de suivi, <a href="https://decupler.com/fiche-gmb/">fiche Google</a>, agents choisis. Ensuite, chaque mois, vous recevez le compte de ce que le système a rattrapé.</p></div></div>
  </div>
</div></section>

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">FAQ</div>
  <h2 class="rise">Les questions qu'on nous pose</h2>
  {faq_html}
</div></section>

</div>
{CTA.render('vous', href='https://calendly.com/fenina-nathan/consultationstrategique')}
<div class="dcp-js"><script type="application/ld+json">{faq_ld}</script></div>
<noscript><style>.dcp .rise{{opacity:1;transform:none}}</style></noscript>
<div class="dcp-js"><script>
(function(){{
  /* Le theme affiche son propre titre de page au-dessus du contenu : on le retire,
     comme le font deja les 15 autres pages. */
  document.querySelectorAll('.entry-header,.entry-title,.ast-single-entry-banner,.page-header')
    .forEach(function(e){{e&&e.remove&&e.remove()}});
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
