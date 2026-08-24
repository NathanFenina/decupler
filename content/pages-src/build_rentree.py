# -*- coding: utf-8 -*-
"""Construit la page « Offre de rentrée » (candidatures) — decupler.com/rentree.

    python3 content/pages-src/build_rentree.py

Sort content/articles/rentree.html, prêt pour wp_publish.py. Un seul
formulaire conditionnel (voir content/components/form_rentree.py), qui
écrit dans Supabase (projet « LinkedIn App », table `candidatures`).

Points laissés ouverts par le brief d'origine — voir form_rentree.py :
lead magnet exact pour les « orange/rouge » local & PME, dates de clôture.
"""
import sys, re, json
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
for d in ('content/components', 'scripts/lib'):
    sys.path.insert(0, str(RACINE / d))
import form_rentree as FORM
import wpcss

SKIN = open(RACINE / 'content/skins/dcp.css', encoding='utf-8').read()
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Syne:wght@700;800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700'
         '&family=JetBrains+Mono:wght@400;700&display=swap">')

CALENDLY = 'https://calendly.com/fenina-nathan/consultationstrategique'
CLOTURE = FORM.CLOTURE
MAJ = '24 août 2026'

TEASER_CSS = """<style>
.rt-tri{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:26px 0 4px}
.rt-c{background:#fff;border:1px solid var(--edge);border-radius:14px;padding:22px 20px 24px;transition:transform .22s,box-shadow .22s,border-color .22s}
.rt-c:hover{transform:translateY(-3px);border-color:var(--vio);box-shadow:0 18px 36px -18px rgba(123,92,250,.35)}
.rt-c .eyebrow{margin:0 0 12px}
.rt-c h3{font-family:var(--display);font-size:1.05rem;font-weight:800;color:var(--ink);margin:0 0 8px;line-height:1.3}
.rt-c p{font-size:.88rem;line-height:1.55;color:var(--soft);margin:0}
.rt-trust{font-family:var(--mono);font-size:.78rem;letter-spacing:.04em;color:var(--faint);margin:14px 0 0}
.rt-trust b{color:var(--ink);font-weight:700}
@media(max-width:820px){.rt-tri{grid-template-columns:1fr}}
</style>"""

TEASERS = [
    ("Entreprise locale", "Votre site, offert",
     "Un site construit et mis en ligne sans rien vous facturer. Vous ne payez qu'un abonnement mensuel une fois le résultat vu — et seulement si vous dites oui."),
    ("PME", "Cartographie GEO offerte",
     "Les prompts exacts où vos concurrents sortent et vous non, vos angles morts, vos pages qui reçoivent du trafic sans jamais convertir."),
    ("Freelance / agence SEO", "Mini-analyse GEO, à votre marque",
     "Une analyse GEO prête à envoyer à l'un de vos clients, sous votre nom. Zéro effort de votre côté — et une porte d'entrée sur la revente en marque blanche."),
]
teaser_html = "".join(
    f'<div class="rt-c rise"><div class="eyebrow">{eb}</div><h3>{h}</h3><p>{p}</p></div>'
    for eb, h, p in TEASERS)

CALENDRIER = [
    ("Vous candidatez", "Un seul formulaire, trois branches selon votre situation. Cinq minutes, pas plus — on trie ensuite."),
    ("On sélectionne", f"Places limitées par audience. On regarde budget, délai et engagement — pas qui a candidaté en premier. Clôture {CLOTURE}."),
    ("On vous répond", "Retenu : un call de 20 minutes est déjà dans votre agenda. Pas retenu cette fois : vous repartez quand même avec quelque chose d'utile, par email."),
]
calendrier_html = "".join(
    f'<div class="et-l rise"><div class="num"></div><div><h3>{h}</h3><p>{p}</p></div></div>'
    for h, p in CALENDRIER)

FAQ = [
    ("C'est vraiment gratuit&nbsp;? Où est le piège&nbsp;?",
     "Il n'y en a pas, et ce n'est pas un cadeau&nbsp;: c'est un échange. On lance une nouvelle offre (infrastructure IA / GEO) et on a besoin de dix cas documentés, avec des chiffres réels, pour la vendre correctement. En échange du travail gratuit, on vous demande un retour honnête et le droit de publier les résultats."),
    ("Pourquoi un formulaire et pas juste un premier arrivé, premier servi&nbsp;?",
     "Parce que les places sont limitées et qu'on veut les donner aux profils où ça a le plus de chances de marcher&nbsp;— pas aux plus rapides à cliquer. Le formulaire sert à ça&nbsp;: candidater, pas s'inscrire."),
    ("Je ne suis retenu(e) ni maintenant ni dans cette édition&nbsp;: je repars les mains vides&nbsp;?",
     "Non. Chaque candidature reçoit une réponse et quelque chose d'utile par email, que vous soyez sélectionné ou non."),
    ("Combien de temps ça prend de répondre au formulaire&nbsp;?",
     "Environ cinq minutes. Une question de routage, puis quelques précisions selon votre situation."),
]
faq_html = ''.join(f'<details class="rise"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": re.sub(r'&nbsp;|<[^>]+>', ' ', q).strip(),
     "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'&nbsp;|<[^>]+>', ' ', a).strip()}} for q, a in FAQ
]}, ensure_ascii=False)

BODY = f"""{FONTS}
{SKIN}
{TEASER_CSS}
<div class="dcp">

<section class="dcp-hero"><div class="in">
  <div style="max-width:680px">
    <div class="eyebrow rise">Candidatures ouvertes · clôture {CLOTURE}</div>
    <h1 class="rise">On ouvre <em>dix, vingt-cinq et quinze</em> places gratuites — contre vos résultats, pas votre argent.</h1>
    <p class="lead rise">On lance une nouvelle offre d'infrastructure IA / GEO. Pour la vendre correctement, il nous faut des cas documentés, avec de vrais chiffres&nbsp;: un site, une cartographie ou une analyse, livrés gratuitement à un petit nombre de candidats, en échange d'un retour honnête et du droit de publier les résultats.</p>
    <p class="lead rise">Un seul formulaire ci-dessous&nbsp;: il s'adapte à votre situation. Cinq minutes pour candidater, on répond à tout le monde avant le {CLOTURE}.</p>
    <div class="dcp-act rise"><a class="dcp-cta" href="#rentree-form" rel="noopener">Voir si je corresponds</a></div>
    <p class="rt-trust rise">Déjà au travail avec <b>Apogea</b> · <b>Pluxee</b> · <b>BeTomorrow</b></p>
  </div>
</div></section>

<section class="dcp-sec"><div class="in">
  <div class="eyebrow rise">Trois portes, un seul formulaire</div>
  <h2 class="rise">Vous candidatez, on ne devine pas à votre place.</h2>
  <p class="lead rise">La première question du formulaire route automatiquement vers ce qui vous concerne&nbsp;: pas besoin de savoir où cliquer.</p>
  <div class="rt-tri">{teaser_html}</div>
</div></section>

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">Comment ça se passe</div>
  <h2 class="rise">Trois étapes, et une place n'est jamais donnée au hasard</h2>
  <div class="etapes">{calendrier_html}</div>
</div></section>

<section class="dcp-sec"><div class="in">
  {FORM.render()}
</div></section>

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">FAQ</div>
  <h2 class="rise">Les questions qu'on nous pose</h2>
  {faq_html}
  <div class="dcp-sign rise">
    <p class="dcp-sign-t">Écrit par <strong>Nathan Fenina</strong>, fondateur de <strong>Décupler</strong>, agence SEO et GEO. Voir <a href="https://decupler.com/cas-clients/">nos cas clients</a> et notre approche de la <a href="https://decupler.com/visibilite-llm/">visibilité dans les LLM</a>.</p>
    <p class="dcp-sign-d">Dernière mise à jour&nbsp;: {MAJ}</p>
  </div>
</div></section>

</div>
<div class="dcp-js"><script type="application/ld+json">{faq_ld}</script></div>
<div class="dcp-js"><noscript><style>.dcp .rise{{opacity:1;transform:none}}.dcp .ic-svg>*{{stroke-dashoffset:0}}</style></noscript></div>
<div class="dcp-js"><script>
(function(){{
  document.querySelectorAll('.entry-header,.entry-title,.ast-single-entry-banner,.page-header')
    .forEach(function(e){{e&&e.remove&&e.remove()}});
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
  setTimeout(showAll,2500);
}})();
</script></div>
"""

BODY = wpcss.harden(BODY)
probs = wpcss.audit(BODY)
assert not probs, probs
risques = wpcss.audit_markup(BODY)
assert not risques, f'{len(risques)} conteneur(s) que wpautop cassera : {risques[:3]}'
struct = wpcss.audit_structure(BODY)
assert not struct, f'{len(struct)} probleme(s) de structure : {struct[:3]}'
out = str(RACINE / 'content/articles/rentree.html')
open(out, 'w', encoding='utf-8').write(BODY)
txt = re.sub(r'<[^>]+>', ' ', re.sub(r'<style.*?</style>|<script.*?</script>', '', BODY, flags=re.S))
print('écrit :', out, len(BODY), 'octets ·', len(txt.split()), 'mots')
