# -*- coding: utf-8 -*-
"""Le verrou email : le lien du dépôt ne s'ouvre qu'après l'adresse.

Trois décisions qui tiennent le dispositif :

1. **La clé est `lmg_sub`**, celle du reste du site. Quelqu'un qui s'est
   abonné sur une autre page n'est pas redemandé — sinon le verrou punit
   les gens déjà acquis.
2. **Sans JavaScript, les boutons restent de vrais liens.** Le `href` pointe
   vers GitHub et c'est le script qui l'intercepte. Un visiteur non capturé
   vaut mieux qu'un visiteur devant une porte que rien ne peut ouvrir.
3. **Le succès ouvre le dépôt dans la foulée.** On ne fait pas remplir un
   formulaire pour ensuite demander de recliquer.

Limite connue et non corrigée ici : le formulaire poste dans une iframe et
aucune réponse n'est lue. Un refus de Substack passe donc pour un succès.
C'est le dispositif déjà en place partout sur le site ; le changer sur une
seule page créerait deux comportements pour la même action.
"""

CLE = 'lmg_sub'


def modale(depot, titre, chapo, bouton="Ouvrir"):
    html = f"""<div class="vrl" id="vrl" role="dialog" aria-modal="true" aria-labelledby="vrl-t" hidden>
  <div class="vrl-c">
    <button class="vrl-x" type="button" id="vrl-x" aria-label="Fermer">✕</button>
    <p class="vrl-i">Accès au dépôt</p>
    <h2 id="vrl-t">{titre}</h2>
    <p>{chapo}</p>
    <form class="vrl-f" id="vrl-f" action="https://decupler.substack.com/api/v1/free" method="post" target="vrl_cible">
      <label for="vrl-e" class="vrl-lbl">Votre adresse email</label>
      <input id="vrl-e" type="email" name="email" placeholder="vous@exemple.fr" required autocomplete="email">
      <input type="hidden" name="first_url" value="https://decupler.substack.com">
      <input type="hidden" name="first_referrer" value="https://decupler.com">
      <button type="submit">{bouton}</button>
    </form>
    <p class="vrl-fine">Une fois par semaine. Désabonnement en un clic. Votre adresse ne sert qu'à ça.</p>
    <div class="vrl-ok">
      <p class="vrl-i">C'est ouvert</p>
      <h2>Merci — le dépôt est à vous.</h2>
      <p>Il s'ouvre dans un nouvel onglet. Si le navigateur l'a bloqué, le bouton est juste là.</p>
      <a class="dcp-cta vert" id="vrl-lien" href="{depot}" target="_blank" rel="noopener">Ouvrir le dépôt</a>
    </div>
    <iframe name="vrl_cible" id="vrl-cible" title="Inscription" class="vrl-cadre"></iframe>
  </div>
</div>"""
    return html + '<div class="dcp-js"><script>' + JS.replace('__CLE__', CLE) + '</script></div>'


JS = """
(function(){
  var CLE='__CLE__';
  function abonne(){
    try{ if(localStorage.getItem(CLE)==='true') return true; }catch(e){}
    try{ return document.cookie.indexOf(CLE+'=true')!==-1; }catch(e){ return false; }
  }
  function marquer(){
    try{ localStorage.setItem(CLE,'true'); }catch(e){}
    try{ document.cookie=CLE+'=true;path=/;max-age=31536000;samesite=lax'; }catch(e){}
  }
  var m=document.getElementById('vrl'), f=document.getElementById('vrl-f'),
      cadre=document.getElementById('vrl-cible'), rendu=null, envoye=false;
  if(!m||!f) return;
  function ouvrir(depuis){
    rendu=depuis; m.hidden=false; m.classList.add('on');
    document.documentElement.style.overflow='hidden';
    var e=document.getElementById('vrl-e'); if(e) e.focus();
  }
  function fermer(){
    m.classList.remove('on'); m.hidden=true;
    document.documentElement.style.overflow='';
    if(rendu&&rendu.focus) rendu.focus();
  }
  document.getElementById('vrl-x').addEventListener('click',fermer);
  m.addEventListener('click',function(ev){ if(ev.target===m) fermer(); });
  document.addEventListener('keydown',function(ev){
    if(ev.key==='Escape'&&m.classList.contains('on')) fermer();
    if(ev.key==='Tab'&&m.classList.contains('on')){
      var f2=m.querySelectorAll('button,input,a[href]'), l=f2.length; if(!l) return;
      var p=f2[0], d=f2[l-1];
      if(ev.shiftKey&&document.activeElement===p){ ev.preventDefault(); d.focus(); }
      else if(!ev.shiftKey&&document.activeElement===d){ ev.preventDefault(); p.focus(); }
    }
  });
  var b=document.querySelectorAll('[data-depot]');
  for(var i=0;i<b.length;i++){
    (function(a){
      a.addEventListener('click',function(ev){
        if(abonne()) return;
        ev.preventDefault(); ouvrir(a);
      });
    })(b[i]);
  }
  f.addEventListener('submit',function(){
    envoye=true;
    var s=f.querySelector('button[type=submit]');
    s.disabled=true; s.textContent='Un instant…';
  });
  if(cadre) cadre.onload=function(){
    if(!envoye) return;
    marquer(); m.classList.add('done');
    var l=document.getElementById('vrl-lien');
    if(l){ l.focus(); try{ window.open(l.href,'_blank','noopener'); }catch(e){} }
  };
})();
"""
