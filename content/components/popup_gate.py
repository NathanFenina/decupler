# -*- coding: utf-8 -*-
"""Popup « lead magnet » Décupler — le contenu se débloque contre un email.

La CSS (.ai-popup-*, .ai-success-message, body.lmg-gated) vit déjà dans le bloc
de style de base des pages .lm-mcp : ce composant ne fournit que le markup et
le script de gating.

Mécanique : au bout de `delai` ms, l'overlay s'affiche, le contenu passe en
flou et le scroll est bloqué. L'inscription Substack part dans une iframe
cachée ; au retour, on mémorise en localStorage + cookie (1 an) et on ferme.
Ajouter ?reset=true à l'URL pour réarmer la popup pendant les tests.
"""

SUBSTACK = "https://decupler.substack.com/api/v1/free"


def render(titre, desc, bouton, icone="📊", delai=6000, unlock=None,
           succes="✅ C'est bon ! Bonne lecture.",
           footer="🔒 Pas de spam. Désabonnement en 1 clic."):
    markup = (
        '<div id="ai-content-gate" class="ai-popup-overlay">'
        '<div class="ai-popup-card">'
        f'<span class="ai-popup-icon">{icone}</span>'
        f'<h3 class="ai-popup-title">{titre}</h3>'
        f'<p class="ai-popup-desc">{desc}</p>'
        '<iframe name="hidden_iframe" id="hidden_iframe" style="display:none"></iframe>'
        f'<form id="ai-popup-form" action="{SUBSTACK}" method="post" target="hidden_iframe">'
        '<input type="email" name="email" placeholder="votre@email.com" class="ai-popup-input" required>'
        '<input type="hidden" name="first_url" value="https://decupler.substack.com">'
        '<input type="hidden" name="first_referrer" value="https://decupler.com">'
        f'<button type="submit" class="ai-popup-submit">{bouton}</button>'
        f'<p class="ai-popup-footer">{footer}</p>'
        '</form>'
        f'<div id="ai-success-msg" class="ai-success-message">{succes}</div>'
        '</div></div>')

    # deverrouillage d'une section gardee (ex. le coffre des skills)
    unl = (f"var v=document.getElementById('{unlock}');"
           "function unlock(){if(v)v.classList.remove('locked')}"
           "if(localStorage.getItem('lmg_sub')==='true'||document.cookie.indexOf('lmg_sub=true')!==-1)unlock();"
           "document.querySelectorAll('[data-open-gate]').forEach(function(el){"
           "el.addEventListener('click',function(e){e.preventDefault();"
           "p.classList.add('active');document.body.classList.add('lmg-gated');"
           "document.body.style.overflow='hidden'})});") if unlock else "function unlock(){}"

    js = (
        '<div class="dcp-js"><script>'
        "document.addEventListener('DOMContentLoaded',function(){"
        "var p=document.getElementById('ai-content-gate'),f=document.getElementById('ai-popup-form'),"
        "s=document.getElementById('ai-success-msg'),i=document.getElementById('hidden_iframe'),sub=false;"
        "if(!p)return;"
        + unl +
        "function op(){if(localStorage.getItem('lmg_sub')==='true')return;"
        "if(document.cookie.indexOf('lmg_sub=true')!==-1)return;"
        "p.classList.add('active');document.body.classList.add('lmg-gated');"
        "document.body.style.overflow='hidden'}"
        f"setTimeout(op,{delai});"
        "function cl(){p.classList.remove('active');document.body.classList.remove('lmg-gated');"
        "document.body.style.overflow='auto'}"
        "if(f)f.addEventListener('submit',function(){sub=true;"
        "var b=f.querySelector('button[type=submit]');b.textContent='Validation…';b.style.opacity='0.7'});"
        "if(i)i.onload=function(){if(sub){f.style.display='none';s.style.display='block';"
        "localStorage.setItem('lmg_sub','true');"
        "document.cookie='lmg_sub=true; max-age=31536000; path=/';unlock();setTimeout(cl,1500);sub=false}};"
        "if(location.search.indexOf('reset=true')!==-1){localStorage.removeItem('lmg_sub');"
        "document.cookie='lmg_sub=; max-age=0; path=/'}});"
        '</script></div>')

    return markup + '\n' + js
