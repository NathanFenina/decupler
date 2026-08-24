# -*- coding: utf-8 -*-
"""Formulaire de candidature — page « Site gratuit » pour entreprises locales
(artisans, libéraux, médical). Un seul public, pas de routage — voir
form_rentree.py pour l'ancienne version multi-branches (conservée pour PME
et SEO, à venir).

Écrit dans Supabase (projet « LinkedIn App », table `candidatures_local`,
policy INSERT publique / aucune lecture anonyme).

Choix : le téléphone est obligatoire (canal principal de relance pour cette
audience — on les appelle, on ne compte pas sur eux pour réserver un
Calendly). Calendly reste proposé en bonus aux profils "verts" seulement.

⚠️ Brackets CA / enveloppe "payant après" posés à vue de nez — à corriger
avec Nathan une fois les premières vraies réponses en main.
"""

SUPABASE_URL = "https://bhgsnoybkxldkzkwkbku.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable_IhHhliR-DLLuakQ2yYpZ-A_kOKRb4_m"
CALENDLY = "https://calendly.com/fenina-nathan/consultationstrategique"

PLACES = 10
CLOTURE = "dimanche 6 septembre"

CSS = """<style>
.rf{--rv:#7B5CFA;--rv2:#9d86ff;--rg:#00E5A0;--rink:#0f1120;--rmut:#5b6072;--rline:rgba(123,92,250,.18);
 position:relative;margin:0;padding:0;font-family:'DM Sans',system-ui,sans-serif}
.rf *{box-sizing:border-box}
.rf .rf-w{max-width:760px;margin:0 auto;padding:0 22px}
.rf .rf-card{background:#fff;border:1px solid var(--rline);border-radius:18px;padding:32px;box-shadow:0 24px 60px -30px rgba(15,17,32,.28)}
.rf .rf-places{display:inline-flex;align-items:center;gap:8px;font-family:'JetBrains Mono',ui-monospace,monospace;
 font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--rv);
 background:rgba(123,92,250,.09);border:1px solid rgba(123,92,250,.22);border-radius:20px;padding:6px 14px;margin:0 0 18px}
.rf .rf-photo{margin:0 0 22px;border-radius:14px;overflow:hidden;border:1px solid var(--rline)}
.rf .rf-photo img{display:block;width:100%;height:auto}
.rf .rf-step{display:none}
.rf .rf-step.active{display:block}
.rf h3.rf-q{font-family:'Syne',sans-serif;font-size:1.28rem;font-weight:800;color:var(--rink);margin:0 0 18px;line-height:1.28}
.rf label.rf-lbl{display:block;font-size:.86rem;font-weight:700;color:var(--rink);margin:16px 0 6px}
.rf label.rf-lbl:first-child{margin-top:0}
.rf input[type=text],.rf input[type=email],.rf input[type=tel],.rf textarea{
 width:100%;font:inherit;font-size:.96rem;padding:12px 14px;border:1.5px solid var(--rline);border-radius:10px;
 background:#fbfbfe;color:var(--rink)}
.rf input:focus,.rf textarea:focus,.rf select:focus{outline:none;border-color:var(--rv)}
.rf textarea{min-height:76px;resize:vertical}
.rf select{width:100%;font:inherit;font-size:.96rem;padding:12px 14px;border:1.5px solid var(--rline);border-radius:10px;
 background:#fbfbfe;color:var(--rink)}
.rf .rf-row{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.rf .rf-eng{display:flex;align-items:flex-start;gap:10px;background:#f7f7fd;border:1px solid var(--rline);
 border-radius:12px;padding:14px 16px;margin:18px 0 4px}
.rf .rf-eng input{margin-top:3px}
.rf .rf-eng p{margin:0;font-size:.88rem;line-height:1.5;color:var(--rmut)}
.rf .rf-nav{display:flex;justify-content:flex-end;align-items:center;margin-top:24px;gap:12px}
.rf .rf-submit{background:linear-gradient(135deg,var(--rv),var(--rv2));color:#fff;border:none;
 font-weight:700;font-size:.96rem;padding:13px 26px;border-radius:10px;cursor:pointer;transition:transform .18s,box-shadow .18s}
.rf .rf-submit:hover{transform:translateY(-1px);box-shadow:0 14px 26px -12px rgba(123,92,250,.55)}
.rf .rf-err{display:none;color:#c0392b;font-size:.82rem;margin-top:10px}
.rf .rf-err.show{display:block}
.rf .rf-outcome{display:none;text-align:center;padding:12px 4px}
.rf .rf-outcome.active{display:block}
.rf .rf-outcome .ic{font-size:2.2rem;margin:0 0 12px}
.rf .rf-outcome h3{font-family:'Syne',sans-serif;font-size:1.4rem;font-weight:800;color:var(--rink);margin:0 0 12px}
.rf .rf-outcome p{font-size:.98rem;line-height:1.6;color:var(--rmut);margin:0 0 22px}
.rf .rf-cal-wrap{margin:0}
.rf .rf-cal{display:inline-flex;align-items:center;gap:9px;background:linear-gradient(135deg,var(--rv),var(--rv2));
 color:#fff!important;text-decoration:none!important;font-weight:700;font-size:1rem;padding:15px 30px;border-radius:11px;
 box-shadow:0 12px 26px -10px rgba(123,92,250,.6)}
@media(max-width:640px){.rf .rf-row{grid-template-columns:1fr}.rf .rf-card{padding:24px 20px}}
</style>"""

FORM_HTML = """
<div class="rf-row">
  <div><label class="rf-lbl">Prénom &amp; nom</label><input type="text" id="rf-nom" required></div>
  <div><label class="rf-lbl">Métier</label><input type="text" id="rf-metier" placeholder="ex. plombier, dentiste, kiné, institut…" required></div>
</div>
<div class="rf-row">
  <div><label class="rf-lbl">Entreprise / cabinet</label><input type="text" id="rf-entreprise"></div>
  <div><label class="rf-lbl">Ville</label><input type="text" id="rf-ville"></div>
</div>
<div class="rf-row">
  <div><label class="rf-lbl">Téléphone</label><input type="tel" id="rf-tel" required placeholder="C'est nous qui vous appelons"></div>
  <div><label class="rf-lbl">Email</label><input type="email" id="rf-email" required></div>
</div>
<label class="rf-lbl">Site web actuel</label>
<select id="rf-site"><option value="non">Je n'en ai pas</option><option value="oui-a-refaire">J'en ai un, mais il est à refaire</option><option value="oui-ok">J'en ai un qui me convient</option></select>
<label class="rf-lbl">Chiffre d'affaires annuel, environ</label>
<select id="rf-ca"><option value="ne-sait-pas">Je préfère ne pas dire</option><option value="-30k">Moins de 30&nbsp;000&nbsp;€</option><option value="30-60k">30 000 à 60 000&nbsp;€</option><option value="60-120k">60 000 à 120 000&nbsp;€</option><option value="120k+">Plus de 120 000&nbsp;€</option></select>
<label class="rf-lbl">Une fois le site en ligne, de quoi auriez-vous le plus besoin&nbsp;?</label>
<select id="rf-besoin"><option value="ne-sait-pas">Je ne sais pas encore</option><option value="agent-sms">Rattraper les appels manqués (agent SMS)</option><option value="agent-vocal">Un agent vocal qui répond à ma place</option><option value="ads">De la publicité (Ads)</option><option value="seo-local">Être mieux classé sur Google (SEO local)</option><option value="geo">Être visible dans les réponses des IA (GEO)</option></select>
<label class="rf-lbl">Le site est gratuit. Une fois que vous l'aurez vu, seriez-vous prêt à payer un service ensuite&nbsp;? Combien&nbsp;?</label>
<select id="rf-payant"><option value="non">Non, je ne pense pas</option><option value="peut-etre">Peut-être, à voir selon le résultat</option><option value="-150">Oui, jusqu'à 150&nbsp;€/mois</option><option value="150-300">Oui, entre 150 et 300&nbsp;€/mois</option><option value="300+">Oui, plus de 300&nbsp;€/mois</option></select>
<label class="rf-lbl">Délai souhaité de mise en ligne</label>
<select id="rf-delai"><option value="pas-presse">Je ne suis pas pressé</option><option value="ce-mois">Ce mois-ci</option><option value="cette-semaine">Cette semaine</option></select>
<label class="rf-lbl">Pourquoi vous&nbsp;?</label>
<textarea id="rf-pourquoi" placeholder="Un mot sur votre situation, ce qui vous bloque aujourd'hui, pourquoi maintenant…"></textarea>
<div class="rf-eng"><input type="checkbox" id="rf-engagement"><p>Ok pour qu'on vous appelle et pour fournir quelques photos/infos sous 7 jours si votre candidature est retenue&nbsp;? (clôture {cloture})</p></div>
<p class="rf-err" id="rf-err">Merci de remplir au moins votre nom, votre métier, votre téléphone et votre email.</p>
<div class="rf-nav"><button type="button" class="rf-submit" id="rf-submit">Envoyer ma candidature</button></div>
""".format(cloture=CLOTURE)


def render(photo_url=None, photo_alt=""):
    photo_html = (f'<div class="rf-photo"><img src="{photo_url}" alt="{photo_alt}" loading="lazy" decoding="async"></div>'
                  if photo_url else '')
    markup = f"""<section class="rf" id="candidature-form"><div class="rf-w"><div class="rf-card">
<div class="rf-places" id="rf-places">🎯 {PLACES} places · clôture {CLOTURE}</div>
{photo_html}
<div class="rf-step active" data-step="form">
  <h3 class="rf-q">Votre candidature</h3>
  {FORM_HTML}
</div>

<div class="rf-outcome" data-outcome="vert">
  <div class="ic">🟢</div>
  <h3>Votre profil correspond à ce qu'on cherche.</h3>
  <p>On vous appelle sous 48&nbsp;h. Si vous préférez choisir vous-même le créneau, c'est possible aussi&nbsp;:</p>
  <div class="rf-cal-wrap"><a class="rf-cal" href="{CALENDLY}" rel="noopener">Réserver mon créneau</a></div>
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

</div></div></section>"""

    js = f"""<div class="dcp-js"><script>
(function(){{
var SUPA_URL='{SUPABASE_URL}',SUPA_KEY='{SUPABASE_ANON_KEY}';
var root=document.getElementById('candidature-form');
if(!root)return;
function val(id){{var e=root.querySelector('#'+id);return e?e.value.trim():''}}
function checked(id){{var e=root.querySelector('#'+id);return !!(e&&e.checked)}}
var PAYANT={{'non':0,'peut-etre':1,'-150':2,'150-300':3,'300+':3}};
var DELAI={{'pas-presse':0,'ce-mois':1,'cette-semaine':2}};
var CA={{'ne-sait-pas':0,'-30k':0,'30-60k':1,'60-120k':2,'120k+':3}};
function score(){{
  var s=0;
  s+=PAYANT[val('rf-payant')]||0;
  s+=DELAI[val('rf-delai')]||0;
  s+=CA[val('rf-ca')]||0;
  s+=checked('rf-engagement')?2:0;
  return s;
}}
function statut(s){{if(s>=6)return'vert';if(s>=3)return'orange';return'rouge'}}
var btn=root.querySelector('#rf-submit');
btn.addEventListener('click',function(){{
  var nom=val('rf-nom'),metier=val('rf-metier'),tel=val('rf-tel'),email=val('rf-email');
  var err=root.querySelector('#rf-err');
  if(!nom||!metier||!tel||!email||email.indexOf('@')===-1){{if(err)err.classList.add('show');return}}
  if(err)err.classList.remove('show');
  var s=score(),st=statut(s);
  var payload={{
    statut:st,score:s,nom:nom,metier:metier,
    entreprise:val('rf-entreprise'),ville:val('rf-ville'),
    email:email,telephone:tel,site_actuel:val('rf-site'),
    ca:val('rf-ca'),besoin:val('rf-besoin'),payant_apres:val('rf-payant'),
    delai:val('rf-delai'),engagement_call:checked('rf-engagement'),
    pourquoi_toi:val('rf-pourquoi'),
    source_canal:(new URLSearchParams(location.search)).get('utm_source')||'',
    source_url:location.href,user_agent:navigator.userAgent
  }};
  btn.disabled=true;btn.textContent='Envoi…';
  fetch(SUPA_URL+'/rest/v1/candidatures_local',{{method:'POST',headers:{{
    'apikey':SUPA_KEY,'Authorization':'Bearer '+SUPA_KEY,
    'Content-Type':'application/json','Prefer':'return=minimal'
  }},body:JSON.stringify(payload)}}).then(function(r){{
    if(!r.ok)throw new Error('http '+r.status);
    root.querySelector('[data-step="form"]').classList.remove('active');
    root.querySelectorAll('.rf-outcome').forEach(function(o){{
      o.classList.toggle('active',o.getAttribute('data-outcome')===st)
    }});
  }}).catch(function(){{
    btn.disabled=false;btn.textContent='Envoyer ma candidature';
    if(err){{err.textContent='Un problème est survenu, réessayez.';err.classList.add('show')}}
  }});
}});
}})();
</script></div>"""

    return CSS + "\n" + markup + "\n" + js
