# -*- coding: utf-8 -*-
"""Construit une page fille du cluster « site internet pour <métier> ».

    python3 content/pages-src/build_metier.py dentiste

Sort content/articles/metier-<slug>.html, prêt pour wp_publish.py.
Le skin, les icônes et le catalogue d'agents sont ceux de la page pilier :
une page métier n'invente rien, elle sélectionne et elle contextualise.
Les audits wpcss sont des assertions.
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

PAR_SLUG = {slug: (nom, promesse) for slug, nom, _, promesse, _, _ in A.AGENTS}


def phone(evts):
    """Le téléphone du hero, rejouant la scène du métier."""
    lignes = ''
    for e in evts:
        tag = f'<span class="evt-tag">{e[3]}</span>' if len(e) > 3 else ''
        lignes += f'<div class="evt evt-{e[0]}"><b>{e[1]}</b><span>{e[2]}</span>{tag}</div>'
    return ('<div class="phone"><div class="phone-scr">'
            '<div class="phone-top"><div class="phone-notch"></div></div>'
            f'<div class="phone-body">{lignes}</div></div></div>')


def agents_html(slugs):
    manquants = [s for s in slugs if s not in PAR_SLUG]
    assert not manquants, f'agent inconnu : {manquants}'
    cartes = ''
    for s in slugs:
        nom, promesse = PAR_SLUG[s]
        cartes += (f'<div class="ag2 rise">{I.bloc(s, "ag2-ic")}'
                   f'<div class="ag2-tx"><h3>{nom}</h3><p>{promesse}</p></div></div>')
    return f'<div class="ag-grille">{cartes}</div>'


def deonto_html(m):
    if not m.get('deonto'):
        return ''
    blocs = ''.join(
        f'<div class="ag2 non rise">{I.bloc(ic, "ag2-ic")}'
        f'<div class="ag2-tx"><h3>{t}</h3><p>{p}</p></div></div>' for ic, t, p in m['deonto'])
    d1, u1, d2, u2 = m['deonto_source']
    return f"""
<section class="dcp-sec alt" id="deonto"><div class="in">
  <div class="eyebrow rise">Ce qu'on refuse de vendre</div>
  <h2 class="rise">{m['deonto_titre']}</h2>
  <p class="lead rise">Une agence qui vous vend tout ce qu'elle sait faire vous met en risque. Voici les trois choses
  qu'on ne branchera pas chez vous, même si elles se vendent très bien ailleurs.</p>
  <div class="ag-grille">{blocs}</div>
  <div class="dcp-tip rise"><div class="ic">⚖️</div><p>{m['remplace']}</p></div>
  <p class="dcp-src rise">Sources&nbsp;: <a href="{u1}" rel="nofollow noopener" target="_blank">{d1}</a>
  et les <a href="{u2}" rel="nofollow noopener" target="_blank">{d2}</a>.</p>
</div></section>"""


def construis(slug):
    m = ML.METIERS[slug]
    faq_html = ''.join(f'<details class="rise"><summary>{q}</summary><p>{a}</p></details>' for q, a in m['faq'])
    faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": re.sub(r'&nbsp;|<[^>]+>', ' ', q).strip(),
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'&nbsp;|<[^>]+>', ' ', a).strip()}}
        for q, a in m['faq']]}, ensure_ascii=False)
    img, alt = m['image']
    # Le titre de la section prix est ecrit a la main par metier : une
    # substitution automatique produit « pour dentiste » au lieu de
    # « d'un cabinet dentaire ».
    titre_prix = m['titre_prix']
    lost_t, lost_c, won_t, won_c = m['bande']

    body = f"""{FONTS}
{SKIN}
<div class="dcp">

<section class="dcp-hero"><div class="in dcp-grid">
  <div>
    <h1><span class="k">{m['kicker']}</span>{m['h1']}</h1>
    <p class="lead">{m['lead']}</p>
    <p class="lead">{m['lead2']}</p>
    <div class="dcp-act"><a class="dcp-cta" href="{ML.RDV}" rel="noopener">Voir mon site avant de décider</a></div>
    <p class="dcp-under">Site 0&nbsp;€ · puis dès 199&nbsp;€/mois</p>
  </div>
  <div class="hero-visuel">
    <div class="photo"><img src="{img}" alt="{alt}" width="1536" height="1024" loading="eager" decoding="async"></div>
    {phone(m['phone'])}
  </div>
</div></section>

<section class="dcp-band"><div class="in">
  <div class="cnt lost">{I.bloc("sms-appel-manque", "cnt-ic")}<p class="lbl">Sans le système</p><p class="num">{lost_t}</p><p class="cap">{lost_c}</p></div>
  <div class="arrow">→</div>
  <div class="cnt won">{I.bloc("sms-formulaire", "cnt-ic")}<p class="lbl">Avec</p><p class="num">{won_t}</p><p class="cap">{won_c}</p></div>
</div></section>

<section class="dcp-sec"><div class="in">
  <div class="eyebrow rise">Le vrai problème</div>
  <h2 class="rise">{m['probleme_titre']}</h2>
  <p class="lead rise">{m['probleme']}</p>
  <div class="photo rise"><img src="{img}" alt="{alt}" width="1536" height="1024" loading="lazy" decoding="async"></div>
  <p class="photo-cap rise">{m['legende']}</p>
  <p class="lead rise">{m['probleme2']}</p>
  <div class="dcp-tip rise"><div class="ic">💡</div><p>Un joli site ne bouche aucun de ces trous. C'est pour ça qu'on vous l'offre&nbsp;:
  <strong>la valeur est dans ce qui tourne derrière</strong>. Le travail difficile, c'est le
  <a href="https://decupler.com/seo-local/">SEO local</a> et ce qui se passe après le clic.</p></div>
</div></section>

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">Ce qui travaille pour vous</div>
  <h2 class="rise">Les agents qui comptent pour ce métier</h2>
  <p class="lead rise">La {titre_prix} ne s'arrête pas à la mise en ligne&nbsp;: c'est ce qui tourne derrière qui
  la rend rentable. Le catalogue complet compte quatorze agents&nbsp;— vous les trouverez sur la
  <a href="{ML.PILIER}">page de l'offre pour entreprises locales</a>. Voici ceux qu'on installe en priorité
  {m['dans_ce_metier']}, et dans cet ordre.</p>
  {agents_html(m['agents'])}
</div></section>
{deonto_html(m)}
<section class="dcp-sec"><div class="in">
  <div class="eyebrow rise">Le prix</div>
  <h2 class="rise">Combien coûte la {titre_prix}&nbsp;?</h2>
  <p class="lead rise">Zéro. La {titre_prix} est offerte, et vous ne payez qu'un abonnement mensuel une fois le site validé. Pas de frais d'installation, pas de facture de création.</p>
  <div class="prix rise">
    <div class="prix-c zero"><p class="lbl">Création du site</p><p class="val">0&nbsp;€</p><p class="sub">Vous le voyez avant de décider</p></div>
    <div class="prix-plus">+</div>
    <div class="prix-c"><p class="lbl">Hébergement et agents</p><p class="val">dès 199&nbsp;€</p><p class="sub">par mois, selon le nombre d'agents</p></div>
  </div>
  {mini_cta("On regarde ensemble ce que ça donnerait chez vous, en quinze minutes. Vous ne vous engagez à rien.", "Prendre 15 minutes")}
</div></section>

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">Comment ça se passe</div>
  <h2 class="rise">Trois étapes, et vous décidez à la deuxième</h2>
  <div class="etapes">
    <div class="et-l rise"><div class="num"></div><div><h3>On construit le site</h3><p>À partir de vos informations et de ce que vos futurs clients cherchent réellement dans votre ville. C'est notre métier de départ&nbsp;: on est <a href="https://decupler.com/agence-seo/">agence SEO</a> avant d'être fournisseur de sites. Vous n'avez rien à faire et rien à payer.</p></div></div>
    <div class="et-l rise"><div class="num"></div><div><h3>On vous le montre en visio</h3><p>Quinze minutes, partage d'écran. Vous voyez le site fini. Si vous n'aimez pas, on s'arrête là et ça ne vous a rien coûté.</p></div></div>
    <div class="et-l rise"><div class="num"></div><div><h3>On branche les agents</h3><p>Mise en ligne, numéro de suivi, <a href="https://decupler.com/fiche-gmb/">fiche Google</a>, agents choisis. Ensuite, chaque mois, vous recevez le compte de ce que le système a rattrapé.</p></div></div>
  </div>
</div></section>

<section class="dcp-sec"><div class="in">
  <div class="eyebrow rise">FAQ</div>
  <h2 class="rise">Les questions qu'on nous pose</h2>
  {faq_html}
  <div class="dcp-sign rise">
    <p class="dcp-sign-t">Écrit par <strong>Nathan Fenina</strong>, fondateur de <strong>Décupler</strong>, agence SEO et GEO. On construit des sites d'entreprises locales et on les fait remonter&nbsp;— d'abord sur Google, ensuite dans les réponses des IA. Voir <a href="https://decupler.com/cas-clients/">nos cas clients</a> et <a href="{ML.PILIER}">l'offre complète</a>.</p>
    <p class="dcp-sign-d">Dernière mise à jour&nbsp;: {MAJ}</p>
  </div>
</div></section>

</div>
{CTA.render('vous', href=ML.RDV)}
<div class="dcp-js"><script type="application/ld+json">{faq_ld}</script></div>
<noscript><style>.dcp .rise{{opacity:1;transform:none}}.dcp .ic-svg>*{{stroke-dashoffset:0}}</style></noscript>
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
</script></div>"""
    return wpcss.harden(body)


MAJ = '21 août 2026'


def mini_cta(phrase, libelle):
    return (f'<div class="dcp-mini rise"><p class="dcp-mini-t">{phrase}</p>'
            f'<p class="dcp-mini-a"><a class="dcp-cta" href="{ML.RDV}" rel="noopener">{libelle}</a></p></div>')


if __name__ == '__main__':
    slug = sys.argv[1] if len(sys.argv) > 1 else 'dentiste'
    if slug not in ML.METIERS:
        sys.exit(f"❌ « {slug} » n'est pas encore rédigé. Disponibles : {', '.join(ML.METIERS)}")
    body = construis(slug)
    for nom, audit in (('style', wpcss.audit), ('balisage', wpcss.audit_markup), ('structure', wpcss.audit_structure)):
        pb = audit(body)
        assert not pb, f'{nom} : ' + ' | '.join(pb[:5])
    out = RACINE / f'content/articles/metier-{slug}.html'
    out.write_text(body, encoding='utf-8')
    mots = len(re.sub(r'<[^>]+>', ' ', re.sub(r'<style>.*?</style>|<script.*?</script>', '', body, flags=re.S)).split())
    print(f'écrit : {out} · {len(body)} octets · {mots} mots')
