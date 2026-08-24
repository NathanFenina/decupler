# -*- coding: utf-8 -*-
"""Formulaire de candidature — page « Cartographie GEO gratuite » pour PME
(entreprises qui vendent en ligne ou visent plusieurs villes). Même mécanique
que form_local.py : assistant pas-à-pas en popup, tous les champs obligatoires,
pas de Calendly (on rappelle directement).

Écrit dans Supabase (projet « LinkedIn App », table `candidatures_pme`,
policy INSERT publique / aucune lecture anonyme).

⚠️ Ne jamais utiliser `&&` dans le JS de ce fichier : WordPress convertit
tout '&' isolé en '&#038;' à l'enregistrement, y compris dans un <script>,
ce qui casse le parsing. Utiliser des ternaires (A?B:false) à la place.
Voir scripts/lib/wpcss.py::audit(), qui bloque ce motif automatiquement.
"""

SUPABASE_URL = "https://bhgsnoybkxldkzkwkbku.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable_IhHhliR-DLLuakQ2yYpZ-A_kOKRb4_m"

PLACES = 25
CLOTURE = "dimanche 6 septembre"
N_STEPS = 9

CSS = """<style>
.rf{--rv:#7B5CFA;--rv2:#9d86ff;--rg:#00E5A0;--rink:#0f1120;--rmut:#5b6072;--rline:rgba(123,92,250,.18);
 position:relative;margin:0;padding:0;font-family:'DM Sans',system-ui,sans-serif}
.rf *{box-sizing:border-box}
.rf.rf-overlay{display:none;position:fixed;inset:0;z-index:99999;background:rgba(15,17,32,.55);
 align-items:flex-start;justify-content:center;padding:5vh 16px;overflow-y:auto}
.rf.rf-overlay.active{display:flex}
.rf .rf-w{max-width:640px;width:100%;margin:0;padding:0}
.rf .rf-card{position:relative;background:#fff;border:1px solid var(--rline);border-radius:18px;padding:36px;box-shadow:0 30px 80px -20px rgba(0,0,0,.5);min-height:360px;display:flex;flex-direction:column}
.rf .rf-x{position:absolute;top:14px;right:14px;width:32px;height:32px;border-radius:9px;border:none;
 background:#f7f7fd;color:var(--rmut);font-size:1.3rem;line-height:1;cursor:pointer;display:flex;align-items:center;justify-content:center}
.rf .rf-x:hover{background:#f0eefe;color:var(--rink)}
.rf .rf-top{display:flex;align-items:center;justify-content:space-between;gap:14px;margin:0 36px 20px 0}
.rf .rf-places{display:inline-flex;align-items:center;gap:8px;font-family:'JetBrains Mono',ui-monospace,monospace;
 font-size:.7rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--rv);
 background:rgba(123,92,250,.09);border:1px solid rgba(123,92,250,.22);border-radius:20px;padding:5px 12px;white-space:nowrap}
.rf .rf-count{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:.7rem;color:var(--rmut);white-space:nowrap}
.rf .rf-bar{height:4px;border-radius:4px;background:var(--rline);overflow:hidden;margin:0 0 26px}
.rf .rf-bar-fill{height:100%;background:linear-gradient(90deg,var(--rv),var(--rg));border-radius:4px;transition:width .3s ease}
.rf .rf-step{display:none;flex:1;flex-direction:column}
.rf .rf-step.active{display:flex}
.rf h3.rf-q{font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:800;color:var(--rink);margin:0 0 6px;line-height:1.28}
.rf .rf-sub{font-size:.86rem;color:var(--rmut);margin:0 0 20px}
.rf label.rf-lbl{display:block;font-size:.86rem;font-weight:700;color:var(--rink);margin:14px 0 6px}
.rf label.rf-lbl:first-child{margin-top:0}
.rf input[type=text],.rf input[type=email],.rf input[type=tel],.rf input[type=url],.rf textarea{
 width:100%;font:inherit;font-size:1.02rem;padding:13px 15px;border:1.5px solid var(--rline);border-radius:10px;
 background:#fbfbfe;color:var(--rink)}
.rf input:focus,.rf textarea:focus,.rf select:focus{outline:none;border-color:var(--rv)}
.rf textarea{min-height:90px;resize:vertical}
.rf select{width:100%;font:inherit;font-size:1.02rem;padding:13px 15px;border:1.5px solid var(--rline);border-radius:10px;
 background:#fbfbfe;color:var(--rink)}
.rf .rf-check-grid{display:grid;gap:8px;margin:0 0 6px}
.rf .rf-check{display:flex;align-items:center;gap:10px;background:#f7f7fd;border:1.5px solid var(--rline);border-radius:10px;
 padding:12px 14px;cursor:pointer;transition:border-color .18s,background .18s}
.rf .rf-check:hover{border-color:var(--rv)}
.rf .rf-check.sel{border-color:var(--rv);background:#f0eefe}
.rf .rf-check input{width:16px;height:16px;accent-color:var(--rv);flex:0 0 auto}
.rf .rf-check span{font-size:.95rem;font-weight:600;color:var(--rink)}
.rf .rf-eng{display:flex;align-items:flex-start;gap:10px;background:#f7f7fd;border:1px solid var(--rline);
 border-radius:12px;padding:14px 16px;margin:18px 0 4px}
.rf .rf-eng.bad{border-color:#c0392b}
.rf .rf-eng input{margin-top:3px}
.rf .rf-eng p{margin:0;font-size:.88rem;line-height:1.5;color:var(--rmut)}
.rf .rf-nav{display:flex;justify-content:space-between;align-items:center;margin-top:auto;padding-top:24px;gap:12px}
.rf .rf-next,.rf .rf-submit{background:linear-gradient(135deg,var(--rv),var(--rv2));color:#fff;border:none;
 font-weight:700;font-size:.96rem;padding:13px 26px;border-radius:10px;cursor:pointer;transition:transform .18s,box-shadow .18s}
.rf .rf-next:hover,.rf .rf-submit:hover{transform:translateY(-1px);box-shadow:0 14px 26px -12px rgba(123,92,250,.55)}
.rf .rf-back{background:none;border:none;color:var(--rmut);font-weight:600;font-size:.88rem;cursor:pointer;padding:8px}
.rf .rf-back:hover{color:var(--rink)}
.rf .rf-back-hide{visibility:hidden}
.rf .rf-spacer{flex:1}
.rf .rf-err{display:none;color:#c0392b;font-size:.82rem;margin-top:10px}
.rf .rf-err.show{display:block}
.rf .rf-outcome{display:none;text-align:center;padding:12px 4px;flex:1;flex-direction:column;justify-content:center}
.rf .rf-outcome.active{display:flex}
.rf .rf-outcome .ic{font-size:2.2rem;margin:0 0 12px}
.rf .rf-outcome h3{font-family:'Syne',sans-serif;font-size:1.4rem;font-weight:800;color:var(--rink);margin:0 0 12px}
.rf .rf-outcome p{font-size:.98rem;line-height:1.6;color:var(--rmut);margin:0 0 22px}
@media(max-width:640px){.rf .rf-card{padding:26px 20px}}
</style>"""

STEPS = [
    ("Pour commencer, vos coordonnées", "On vous appelle si votre candidature est retenue.",
     """<label class="rf-lbl">Prénom &amp; nom</label><input type="text" id="rf-nom" placeholder="Votre nom">
<label class="rf-lbl">Téléphone</label><input type="tel" id="rf-tel" placeholder="C'est nous qui vous appelons">""",
     ["rf-nom", "rf-tel"]),
    ("Comment vous joindre par écrit", "",
     """<label class="rf-lbl">Email</label><input type="email" id="rf-email" placeholder="vous@exemple.fr">
<label class="rf-lbl">Secteur d'activité</label><input type="text" id="rf-secteur" placeholder="ex. e-commerce, services B2B…">""",
     ["rf-email", "rf-secteur"]),
    ("Votre entreprise", "",
     """<label class="rf-lbl">Nom de l'entreprise</label><input type="text" id="rf-entreprise">
<label class="rf-lbl">Site web actuel</label><input type="url" id="rf-site" placeholder="https://…">""",
     ["rf-entreprise", "rf-site"]),
    ("Ville / zone d'activité", "",
     """<input type="text" id="rf-ville" placeholder="ex. Lyon, ou national">""",
     ["rf-ville"]),
    ("Combien de leads ou clients générez-vous par mois, aujourd'hui&nbsp;?", "",
     """<select id="rf-clients"><option value="0-5">0 à 5</option><option value="6-20">6 à 20</option><option value="21-50">21 à 50</option><option value="50+">Plus de 50</option></select>""",
     []),
    ("Budget marketing mensuel actuel, environ", "Ça reste entre nous — ça nous aide juste à prioriser.",
     """<select id="rf-budget"><option value="ne-sait-pas">Je préfère ne pas dire</option><option value="-500">Moins de 500&nbsp;€</option><option value="500-1500">500 à 1&nbsp;500&nbsp;€</option><option value="1500-3000">1&nbsp;500 à 3&nbsp;000&nbsp;€</option><option value="3000+">Plus de 3&nbsp;000&nbsp;€</option></select>
<label class="rf-lbl">Une fois la cartographie en main, votre priorité&nbsp;?</label>
<select id="rf-priorite"><option value="ne-sait-pas">Je ne sais pas encore</option><option value="seo">SEO classique</option><option value="geo">Visibilité dans les réponses IA (GEO)</option><option value="les-deux">Les deux</option></select>""",
     []),
    ("La cartographie est gratuite.", "Une fois que vous l'aurez vue, seriez-vous prêt à payer un service ensuite&nbsp;? Combien&nbsp;?",
     """<label class="rf-lbl">Quel(s) service(s)&nbsp;?</label><input type="text" id="rf-service" placeholder="ex. contenu GEO, refonte SEO, suivi mensuel…">
<label class="rf-lbl">À quel prix par mois, environ&nbsp;?</label><input type="text" id="rf-prix" placeholder="ex. 1500€, ou une fourchette">""",
     ["rf-service", "rf-prix"]),
    ("Délai souhaité pour démarrer", "",
     """<select id="rf-delai"><option value="pas-presse">Je ne suis pas pressé</option><option value="ce-mois">Ce mois-ci</option><option value="cette-semaine">Cette semaine</option></select>""",
     []),
    ("Dernière chose", "Pourquoi vous, plutôt qu'un autre&nbsp;?",
     """<textarea id="rf-pourquoi" placeholder="Un mot sur votre situation, ce qui vous bloque aujourd'hui, pourquoi maintenant…"></textarea>
<div class="rf-eng"><input type="checkbox" id="rf-engagement"><p>Ok pour qu'on vous appelle et pour donner un accès Search Console / Analytics sous 7 jours si votre candidature est retenue&nbsp;? (clôture {cloture})</p></div>""".format(cloture=CLOTURE),
     ["rf-pourquoi"]),
]


def _step_html(i, titre, sous, contenu, is_last):
    sub_html = f'<p class="rf-sub">{sous}</p>' if sous else ''
    back_cls = 'rf-back rf-back-hide' if i == 0 else 'rf-back'
    nav = (
        f'<button type="button" class="{back_cls}" data-back>&larr; Retour</button>'
        '<div class="rf-spacer"></div>'
        + (f'<button type="button" class="rf-submit" id="rf-submit">Envoyer ma candidature</button>' if is_last
           else f'<button type="button" class="rf-next" data-next>Suivant &rarr;</button>')
    )
    return f"""<div class="rf-step{' active' if i == 0 else ''}" data-step="{i}">
  <h3 class="rf-q">{titre}</h3>
  {sub_html}
  {contenu}
  <p class="rf-err" id="rf-err-{i}">Merci de remplir ce champ avant de continuer.</p>
  <div class="rf-nav">{nav}</div>
</div>"""


def render(photo_url=None, photo_alt=""):
    photo_html = (f'<div class="rf-photo"><img src="{photo_url}" alt="{photo_alt}" loading="lazy" decoding="async"></div>'
                  if photo_url else '')
    steps_html = "".join(
        _step_html(i, titre, sous, contenu, i == len(STEPS) - 1)
        for i, (titre, sous, contenu, _req) in enumerate(STEPS))
    required_json = "[" + ",".join(
        "[" + ",".join(f"'{r}'" for r in req) + "]" for (_t, _s, _c, req) in STEPS
    ) + "]"

    markup = f"""<div class="rf rf-overlay" id="candidature-form"><div class="rf-w"><div class="rf-card">
<button type="button" class="rf-x" data-close-form aria-label="Fermer">&times;</button>
<div class="rf-top">
  <div class="rf-places">🎯 {PLACES} places · clôture {CLOTURE}</div>
  <div class="rf-count" id="rf-count">Étape 1 sur {N_STEPS}</div>
</div>
<div class="rf-bar"><div class="rf-bar-fill" id="rf-bar-fill" style="width:{round(100/N_STEPS)}%"></div></div>
{photo_html}
{steps_html}

<div class="rf-outcome" data-outcome="vert">
  <div class="ic">🟢</div>
  <h3>Votre profil correspond à ce qu'on cherche.</h3>
  <p>On vous appelle sous 48&nbsp;h au numéro que vous avez laissé.</p>
</div>
<div class="rf-outcome" data-outcome="orange">
  <div class="ic">🟠</div>
  <h3>Candidature reçue.</h3>
  <p>On la relit et on vous appelle avant la clôture ({CLOTURE}) si elle est retenue.</p>
</div>
<div class="rf-outcome" data-outcome="rouge">
  <div class="ic">📩</div>
  <h3>Candidature reçue.</h3>
  <p>Cette édition est calibrée pour un petit nombre de profils&nbsp;: on garde la vôtre de côté et on vous recontacte si une place se libère.</p>
</div>

</div></div></div>"""

    js = f"""<div class="dcp-js"><script>
document.addEventListener('DOMContentLoaded',function(){{
var SUPA_URL='{SUPABASE_URL}',SUPA_KEY='{SUPABASE_ANON_KEY}';
var root=document.getElementById('candidature-form');
if(!root)return;
function openForm(e){{if(e)e.preventDefault();root.classList.add('active');document.body.style.overflow='hidden'}}
function closeForm(){{root.classList.remove('active');document.body.style.overflow=''}}
document.querySelectorAll('[data-open-form]').forEach(function(t){{t.addEventListener('click',openForm)}});
root.querySelectorAll('[data-close-form]').forEach(function(t){{t.addEventListener('click',closeForm)}});
root.addEventListener('click',function(e){{if(e.target===root)closeForm()}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape')closeForm()}});
var N={N_STEPS},cur=0;
var REQUIRED={required_json};
function steps(){{return root.querySelectorAll('.rf-step')}}
root.querySelectorAll('input,select,textarea').forEach(function(e){{
  e.addEventListener('input',function(){{e.style.borderColor=''}});
}});
function val(id){{var e=root.querySelector('#'+id);return e?e.value.trim():''}}
function checked(id){{var e=root.querySelector('#'+id);return e?!!e.checked:false}}
function goTo(i){{
  cur=i;
  steps().forEach(function(s){{s.classList.toggle('active',+s.getAttribute('data-step')===i)}});
  root.querySelector('#rf-count').textContent='Étape '+(i+1)+' sur '+N;
  root.querySelector('#rf-bar-fill').style.width=Math.round(((i+1)/N)*100)+'%';
}}
var engCb=root.querySelector('#rf-engagement');
if(engCb){{
  engCb.addEventListener('change',function(){{
    var engBox=root.querySelector('.rf-eng');
    if(engBox)engBox.classList.remove('bad');
  }});
}}
function markInvalid(id,bad){{var e=root.querySelector('#'+id);if(e)e.style.borderColor=bad?'#c0392b':''}}
root.querySelectorAll('[data-next]').forEach(function(btn){{
  btn.addEventListener('click',function(){{
    var req=REQUIRED[cur]||[],err=root.querySelector('#rf-err-'+cur),ok=true,firstBad=null;
    for(var k=0;k<req.length;k++){{
      var emailBad=(req[k]==='rf-email')?(val(req[k]).indexOf('@')===-1):false;
      var bad=!val(req[k])||emailBad;
      markInvalid(req[k],bad);
      if(bad){{ok=false;if(!firstBad)firstBad=req[k]}}
    }}
    if(!ok){{
      if(err)err.classList.add('show');
      var badEl=firstBad?root.querySelector('#'+firstBad):null;
      if(badEl)badEl.scrollIntoView({{block:'center',behavior:'smooth'}});
      return;
    }}
    if(err)err.classList.remove('show');
    if(cur<N-1)goTo(cur+1);
  }});
}});
root.querySelectorAll('[data-back]').forEach(function(btn){{
  btn.addEventListener('click',function(){{if(cur>0)goTo(cur-1)}});
}});
var DELAI={{'pas-presse':0,'ce-mois':1,'cette-semaine':2}};
var CLIENTS={{'0-5':0,'6-20':1,'21-50':2,'50+':3}};
var BUDGET={{'ne-sait-pas':0,'-500':0,'500-1500':1,'1500-3000':2,'3000+':3}};
function score(){{
  var s=0;
  s+=DELAI[val('rf-delai')]||0;
  s+=CLIENTS[val('rf-clients')]||0;
  s+=BUDGET[val('rf-budget')]||0;
  s+=checked('rf-engagement')?2:0;
  s+=(val('rf-service').length>1||val('rf-prix').length>1)?1:0;
  return s;
}}
function statut(s){{if(s>=6)return'vert';if(s>=3)return'orange';return'rouge'}}
var btn=root.querySelector('#rf-submit');
btn.addEventListener('click',function(){{
  var nom=val('rf-nom'),tel=val('rf-tel'),email=val('rf-email'),secteur=val('rf-secteur'),pourquoi=val('rf-pourquoi');
  var err=root.querySelector('#rf-err-'+(N-1));
  var emailBad=email.indexOf('@')===-1;
  var engBad=!checked('rf-engagement');
  var engBox=root.querySelector('.rf-eng');
  markInvalid('rf-pourquoi',!pourquoi);
  if(engBox)engBox.classList.toggle('bad',engBad);
  if(!nom||!tel||!email||!secteur||!pourquoi||emailBad||engBad){{if(err)err.classList.add('show');return}}
  if(err)err.classList.remove('show');
  var s=score(),st=statut(s);
  var payload={{
    statut:st,score:s,nom:nom,secteur:secteur,
    entreprise:val('rf-entreprise'),site_web:val('rf-site'),ville:val('rf-ville'),
    email:email,telephone:tel,
    clients_mois:val('rf-clients'),budget_marketing:val('rf-budget'),priorite:val('rf-priorite'),
    service_souhaite:val('rf-service'),prix_mensuel:val('rf-prix'),
    delai:val('rf-delai'),engagement_call:checked('rf-engagement'),
    pourquoi_toi:pourquoi,
    source_canal:(new URLSearchParams(location.search)).get('utm_source')||'',
    source_url:location.href,user_agent:navigator.userAgent
  }};
  btn.disabled=true;btn.textContent='Envoi…';
  fetch(SUPA_URL+'/rest/v1/candidatures_pme',{{method:'POST',headers:{{
    'apikey':SUPA_KEY,'Authorization':'Bearer '+SUPA_KEY,
    'Content-Type':'application/json','Prefer':'return=minimal'
  }},body:JSON.stringify(payload)}}).then(function(r){{
    if(!r.ok)throw new Error('http '+r.status);
    steps().forEach(function(s){{s.classList.remove('active')}});
    root.querySelectorAll('.rf-outcome').forEach(function(o){{
      o.classList.toggle('active',o.getAttribute('data-outcome')===st)
    }});
  }}).catch(function(){{
    btn.disabled=false;btn.textContent='Envoyer ma candidature';
    if(err){{err.textContent='Un problème est survenu, réessayez.';err.classList.add('show')}}
  }});
}});
}});
</script></div>"""

    return CSS + "\n" + markup + "\n" + js
