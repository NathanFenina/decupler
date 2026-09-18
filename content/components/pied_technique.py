# -*- coding: utf-8 -*-
"""Le bloc technique commun aux pages du skin « dcp ».

Trois choses que toute page `.dcp` doit embarquer, sous peine d'être cassée
en production :

1. **Le script de révélation.** `.rise` pose `opacity:0`. Sans l'observateur
   qui ajoute `.vu`, la page reste blanche — pas « moins animée » : vide.
   Constaté le 2 septembre 2026 sur une page qui avait le skin mais pas le
   script : socle tarifaire et modules invisibles au rendu.
2. **Le filet noscript**, qui force `.rise` visible sans JavaScript.
3. **La mesure de gouttière**, qui fait déborder les bandes d'un bord à
   l'autre sans utiliser `100vw` — lequel compte la barre de défilement.

Le bloc vivait en copie dans build_offre.py. Deux copies d'un correctif
finissent toujours par diverger : celle qu'on corrige, et l'autre.
"""
import json


def faq_ld(questions):
    """JSON-LD FAQPage. `questions` est une liste de (question, réponse)."""
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": r}}
                       for q, r in questions],
    }, ensure_ascii=False)


def rendu(questions=None):
    ld = (f'<div class="dcp-js"><script type="application/ld+json">'
          f'{faq_ld(questions)}</script></div>\n') if questions else ''
    return ld + """<div class="dcp-js"><noscript><style>.dcp .rise{opacity:1;transform:none}.dcp .ic-svg>*{stroke-dashoffset:0}</style></noscript></div>
<div class="dcp-js"><script>
(function(){
  document.querySelectorAll('.entry-header,.entry-title,.ast-single-entry-banner,.page-header')
    .forEach(function(e){e&&e.remove&&e.remove()});
  function bleed(){
    var d=document.querySelector('.dcp'); if(!d) return;
    var r=d.getBoundingClientRect(), w=document.documentElement.clientWidth, st=document.documentElement.style;
    st.setProperty('--dcp-bl', Math.min(400,Math.max(0,Math.round(r.left)))+'px');
    st.setProperty('--dcp-br', Math.min(400,Math.max(0,Math.round(w-r.right)))+'px');
  }
  bleed();
  var t; addEventListener('resize',function(){clearTimeout(t);t=setTimeout(bleed,120)});
  addEventListener('load',bleed);
  var els=document.querySelectorAll('.dcp .rise');
  function showAll(){for(var i=0;i<els.length;i++)els[i].classList.add('vu')}
  if(!('IntersectionObserver' in window)){showAll();return}
  var io=new IntersectionObserver(function(en){
    en.forEach(function(e){if(e.isIntersecting){e.target.classList.add('vu');io.unobserve(e.target)}})
  },{rootMargin:'0px 0px -8% 0px',threshold:.05});
  for(var i=0;i<els.length;i++)io.observe(els[i]);
  setTimeout(showAll,2500);
})();
</script></div>"""
