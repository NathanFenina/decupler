# -*- coding: utf-8 -*-
"""Formulaire conditionnel « Offre de rentrée » — decupler.com/rentree.

Un seul formulaire, 1 question de routage (Q0) puis 3 branches (local / PME /
freelance-agence SEO). Scoring simple calculé en JS à la soumission, écrit
directement dans Supabase (projet « LinkedIn App », table `candidatures`,
policy INSERT publique / aucune lecture anonyme — voir la migration
`create_candidatures_rentree`).

Compte à rebours et compteur de places : constantes ci-dessous, à remonter
à la main (pas de logique serveur pour l'instant — cohérent avec le reste
du site, qui est du HTML statique poussé dans WordPress).

⚠️ Deux points laissés ouverts par le brief d'origine, à trancher avec Nathan :
  - le lead magnet exact envoyé aux « orange/rouge » des branches local & PME
    (placeholder RESSOURCE_ATTENTE ci-dessous) ;
  - les dates d'ouverture/clôture (par défaut : 31 août → 6 septembre 2026,
    proposition du brief, non confirmée).
"""

SUPABASE_URL = "https://bhgsnoybkxldkzkwkbku.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable_IhHhliR-DLLuakQ2yYpZ-A_kOKRb4_m"
CALENDLY = "https://calendly.com/fenina-nathan/consultationstrategique"

# Places restantes par branche (statique, à remonter à la main).
PLACES = {"local": 10, "pme": 25, "seo": 15}
CLOTURE = "dimanche 6 septembre"
RESSOURCE_ATTENTE = "une ressource utile pour avancer sans nous"  # placeholder, à préciser

CSS = """<style>
.rf{--rv:#7B5CFA;--rv2:#9d86ff;--rg:#00E5A0;--rink:#0f1120;--rmut:#5b6072;--rline:rgba(123,92,250,.18);
 position:relative;margin:0;padding:56px 0 72px;font-family:'DM Sans',system-ui,sans-serif}
.rf *{box-sizing:border-box}
.rf .rf-w{max-width:760px;margin:0 auto;padding:0 22px}
.rf .rf-card{background:#fff;border:1px solid var(--rline);border-radius:18px;padding:32px;box-shadow:0 24px 60px -30px rgba(15,17,32,.28)}
.rf .rf-places{display:inline-flex;align-items:center;gap:8px;font-family:'JetBrains Mono',ui-monospace,monospace;
 font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--rv);
 background:rgba(123,92,250,.09);border:1px solid rgba(123,92,250,.22);border-radius:20px;padding:6px 14px;margin:0 0 18px}
.rf .rf-step{display:none}
.rf .rf-step.active{display:block}
.rf h3.rf-q{font-family:'Syne',sans-serif;font-size:1.28rem;font-weight:800;color:var(--rink);margin:0 0 18px;line-height:1.28}
.rf .rf-choices{display:grid;gap:10px;margin:0 0 8px}
.rf .rf-choice{display:block;text-align:left;background:#f7f7fd;border:1.5px solid var(--rline);border-radius:12px;
 padding:16px 18px;font-size:.98rem;font-weight:700;color:var(--rink);cursor:pointer;transition:border-color .18s,background .18s}
.rf .rf-choice:hover{border-color:var(--rv);background:#f0eefe}
.rf .rf-choice.sel{border-color:var(--rv);background:#f0eefe;box-shadow:0 0 0 3px rgba(123,92,250,.14)}
.rf .rf-choice span{display:block;font-weight:500;font-size:.85rem;color:var(--rmut);margin-top:4px}
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
.rf .rf-nav{display:flex;justify-content:space-between;align-items:center;margin-top:24px;gap:12px}
.rf .rf-next,.rf .rf-submit{background:linear-gradient(135deg,var(--rv),var(--rv2));color:#fff;border:none;
 font-weight:700;font-size:.96rem;padding:13px 26px;border-radius:10px;cursor:pointer;transition:transform .18s,box-shadow .18s}
.rf .rf-next:hover,.rf .rf-submit:hover{transform:translateY(-1px);box-shadow:0 14px 26px -12px rgba(123,92,250,.55)}
.rf .rf-back{background:none;border:none;color:var(--rmut);font-weight:600;font-size:.88rem;cursor:pointer;padding:8px}
.rf .rf-back:hover{color:var(--rink)}
.rf .rf-err{display:none;color:#c0392b;font-size:.82rem;margin-top:10px}
.rf .rf-err.show{display:block}
.rf .rf-outcome{display:none;text-align:center;padding:12px 4px}
.rf .rf-outcome.active{display:block}
.rf .rf-outcome .ic{font-size:2.2rem;margin:0 0 12px}
.rf .rf-outcome h3{font-family:'Syne',sans-serif;font-size:1.4rem;font-weight:800;color:var(--rink);margin:0 0 12px}
.rf .rf-outcome p{font-size:.98rem;line-height:1.6;color:var(--rmut);margin:0 0 22px}
.rf .rf-cal{display:inline-flex;align-items:center;gap:9px;background:linear-gradient(135deg,var(--rv),var(--rv2));
 color:#fff!important;text-decoration:none!important;font-weight:700;font-size:1rem;padding:15px 30px;border-radius:11px;
 box-shadow:0 12px 26px -10px rgba(123,92,250,.6)}
@media(max-width:640px){.rf .rf-row{grid-template-columns:1fr}.rf .rf-card{padding:24px 20px}}
</style>"""

# ── Champs communs (posés après le routage, avant la branche) ──────────────
IDENTITE = """
<div class="rf-row">
  <div><label class="rf-lbl">Prénom &amp; nom</label><input type="text" id="rf-nom" required></div>
  <div><label class="rf-lbl">Entreprise / activité</label><input type="text" id="rf-entreprise"></div>
</div>
<div class="rf-row">
  <div><label class="rf-lbl">Email</label><input type="email" id="rf-email" required></div>
  <div><label class="rf-lbl">Téléphone</label><input type="tel" id="rf-tel"></div>
</div>"""

# ── Contenu par branche : (label bouton Q0, sous-texte, champs HTML, options select) ──
BRANCHES = {
 "local": dict(
   label="Une entreprise locale",
   sous="Artisan, cabinet, institut, commerce physique.",
   champs=IDENTITE + """
<label class="rf-lbl">Métier &amp; ville</label>
<div class="rf-row">
  <input type="text" id="rf-metier" placeholder="ex. plombier, dentiste, institut de beauté">
  <input type="text" id="rf-ville" placeholder="ex. Lyon">
</div>
<label class="rf-lbl">Vous avez déjà un site ?</label>
<select id="rf-site"><option value="non">Non</option><option value="oui-a-refaire">Oui, mais à refaire</option><option value="oui-ok">Oui, il me convient</option></select>
<label class="rf-lbl">Combien de nouveaux clients par mois, aujourd'hui ?</label>
<select id="rf-clients"><option value="0-2">0 à 2</option><option value="3-5">3 à 5</option><option value="6-10">6 à 10</option><option value="10+">Plus de 10</option></select>
<label class="rf-lbl">Une fois le site en ligne, sur quoi voudriez-vous qu'on aille ensuite ?</label>
<select id="rf-ensuite"><option value="ne-sait-pas">Je ne sais pas encore</option><option value="ads">Publicité (Ads)</option><option value="agent-ia">Agents IA (SMS, appels manqués)</option><option value="seo-local">SEO local</option><option value="geo">Visibilité dans les réponses IA (GEO)</option></select>
<label class="rf-lbl">Si le résultat vous plaît, quelle enveloppe mensuelle ça représenterait pour vous ?</label>
<select id="rf-enveloppe"><option value="ne-sait-pas">Je ne sais pas encore</option><option value="-150">Moins de 150&nbsp;€</option><option value="150-300">150 à 300&nbsp;€</option><option value="300-600">300 à 600&nbsp;€</option><option value="600+">Plus de 600&nbsp;€</option></select>
<label class="rf-lbl">Délai souhaité de mise en ligne</label>
<select id="rf-delai"><option value="pas-presse">Je ne suis pas pressé</option><option value="ce-mois">Ce mois-ci</option><option value="cette-semaine">Cette semaine</option></select>"""),
 "pme": dict(
   label="Une PME",
   sous="Vous vendez en ligne ou visez plusieurs villes.",
   champs=IDENTITE + """
<label class="rf-lbl">Secteur &amp; site web actuel</label>
<div class="rf-row">
  <input type="text" id="rf-metier" placeholder="ex. e-commerce, B2B services…">
  <input type="text" id="rf-ville" placeholder="URL du site actuel">
</div>
<label class="rf-lbl">Combien de leads/clients générez-vous par mois aujourd'hui ?</label>
<select id="rf-clients"><option value="0-2">0 à 5</option><option value="3-5">6 à 20</option><option value="6-10">21 à 50</option><option value="10+">Plus de 50</option></select>
<label class="rf-lbl">Priorité, une fois la cartographie en main</label>
<select id="rf-ensuite"><option value="ne-sait-pas">Je ne sais pas encore</option><option value="seo-local">SEO classique</option><option value="geo">Visibilité dans les réponses IA (GEO)</option><option value="ads">Les deux</option></select>
<label class="rf-lbl">Si le résultat vous plaît, quelle enveloppe mensuelle ça représenterait pour vous ?</label>
<select id="rf-enveloppe"><option value="ne-sait-pas">Je ne sais pas encore</option><option value="-150">Moins de 500&nbsp;€</option><option value="150-300">500 à 1&nbsp;500&nbsp;€</option><option value="300-600">1&nbsp;500 à 3&nbsp;000&nbsp;€</option><option value="600+">Plus de 3&nbsp;000&nbsp;€</option></select>
<label class="rf-lbl">Délai souhaité</label>
<select id="rf-delai"><option value="pas-presse">Je ne suis pas pressé</option><option value="ce-mois">Ce mois-ci</option><option value="cette-semaine">Cette semaine</option></select>"""),
 "seo": dict(
   label="Freelance ou agence SEO",
   sous="Vous gérez des clients, pas seulement votre propre site.",
   champs=IDENTITE + """
<label class="rf-lbl">Combien de clients gérez-vous actuellement ?</label>
<select id="rf-clients"><option value="0-2">1 à 3</option><option value="3-5">4 à 10</option><option value="6-10">11 à 25</option><option value="10+">Plus de 25</option></select>
<label class="rf-lbl">Ce qui vous intéresse le plus</label>
<select id="rf-ensuite"><option value="ne-sait-pas">La mini-analyse gratuite, pour voir</option><option value="marque-blanche">Revendre en marque blanche (vous facturez, on livre)</option><option value="abonnement">Internaliser via un abonnement à notre stack Claude Code SEO</option><option value="ads">Les deux</option></select>
<label class="rf-lbl">À quel prix mensuel trouveriez-vous ça juste ?</label>
<select id="rf-enveloppe"><option value="ne-sait-pas">Je ne sais pas encore</option><option value="-150">Moins de 80&nbsp;€</option><option value="150-300">80 à 150&nbsp;€</option><option value="300-600">150 à 300&nbsp;€</option><option value="600+">Plus de 300&nbsp;€</option></select>
<label class="rf-lbl">Qu'avez-vous déjà payé ces 12 derniers mois pour des outils/formations SEO ?</label>
<textarea id="rf-paye" placeholder="ex. Semrush, une formation, un freelance sous-traitant…"></textarea>
<label class="rf-lbl">Délai souhaité pour démarrer</label>
<select id="rf-delai"><option value="pas-presse">Je ne suis pas pressé</option><option value="ce-mois">Ce mois-ci</option><option value="cette-semaine">Cette semaine</option></select>"""),
}

ENGAGEMENT = ("Ok pour un call de 20&nbsp;minutes et pour fournir accès / contenus "
              f"sous 7 jours si votre candidature est retenue&nbsp;? (clôture {CLOTURE})")

FOOTER = """
<label class="rf-lbl">Pourquoi vous&nbsp;?</label>
<textarea id="rf-pourquoi" placeholder="Un mot sur votre situation, ce qui vous bloque, pourquoi maintenant…"></textarea>
<div class="rf-eng"><input type="checkbox" id="rf-engagement"><p>{eng}</p></div>"""


def _step_branche(cle):
    b = BRANCHES[cle]
    return f"""<div class="rf-step" data-step="branche-{cle}">
<h3 class="rf-q">Quelques précisions</h3>
{b['champs']}
{FOOTER.format(eng=ENGAGEMENT)}
<p class="rf-err" id="rf-err-{cle}">Merci de remplir au moins votre nom et votre email.</p>
<div class="rf-nav"><button type="button" class="rf-back" data-back>&larr; Retour</button>
<button type="button" class="rf-submit" data-submit="{cle}">Envoyer ma candidature</button></div>
</div>"""


def render():
    places_local, places_pme, places_seo = PLACES["local"], PLACES["pme"], PLACES["seo"]
    choix = "".join(
        f'<button type="button" class="rf-choice" data-route="{cle}">{b["label"]}<span>{b["sous"]}</span></button>'
        for cle, b in BRANCHES.items())
    steps = "".join(_step_branche(cle) for cle in BRANCHES)

    markup = f"""<section class="rf" id="rentree-form"><div class="rf-w"><div class="rf-card">
<div class="rf-places" id="rf-places">🎯 Candidatures ouvertes · clôture {CLOTURE}</div>

<div class="rf-step active" data-step="q0">
  <h3 class="rf-q">Pour commencer, vous êtes plutôt…</h3>
  <div class="rf-choices">{choix}</div>
</div>

{steps}

<div class="rf-outcome" data-outcome="vert">
  <div class="ic">🟢</div>
  <h3>Votre profil correspond à ce qu'on cherche.</h3>
  <p>Réservez directement 20&nbsp;minutes en visio&nbsp;: on regarde ensemble si on part sur cette édition.</p>
  <div class="rf-cal-wrap"><a class="rf-cal" href="{CALENDLY}" rel="noopener">Réserver mon créneau</a></div>
</div>
<div class="rf-outcome" data-outcome="orange">
  <div class="ic">🟠</div>
  <h3>Candidature reçue.</h3>
  <p>On la relit et on revient vers vous avant la clôture ({CLOTURE}). En attendant, on vous envoie {RESSOURCE_ATTENTE} par email.</p>
</div>
<div class="rf-outcome" data-outcome="rouge">
  <div class="ic">📩</div>
  <h3>Candidature reçue.</h3>
  <p>Cette édition est calibrée pour un petit nombre de profils&nbsp;: on garde la vôtre de côté et on vous recontacte si une place se libère. Vous recevez {RESSOURCE_ATTENTE} par email dans tous les cas.</p>
</div>

</div></div></section>"""

    js = f"""<div class="dcp-js"><script>
(function(){{
var SUPA_URL='{SUPABASE_URL}',SUPA_KEY='{SUPABASE_ANON_KEY}';
var root=document.getElementById('rentree-form');
if(!root)return;
var state={{branche:null}};
function steps(){{return root.querySelectorAll('.rf-step')}}
function show(sel){{steps().forEach(function(s){{s.classList.toggle('active',s===sel)}})}}
function byStep(name){{return root.querySelector('.rf-step[data-step="'+name+'"]')}}
root.querySelectorAll('[data-route]').forEach(function(btn){{
  btn.addEventListener('click',function(){{
    root.querySelectorAll('[data-route]').forEach(function(b){{b.classList.remove('sel')}});
    btn.classList.add('sel');
    state.branche=btn.getAttribute('data-route');
    setTimeout(function(){{show(byStep('branche-'+state.branche))}},160);
  }});
}});
root.querySelectorAll('[data-back]').forEach(function(btn){{
  btn.addEventListener('click',function(){{show(byStep('q0'))}});
}});
function val(id){{var e=root.querySelector('#'+id);return e?e.value.trim():''}}
function checked(id){{var e=root.querySelector('#'+id);return !!(e&&e.checked)}}
var BRACKET={{'-150':1,'150-300':2,'300-600':3,'600+':3,'ne-sait-pas':0}};
var DELAI={{'pas-presse':0,'ce-mois':1,'cette-semaine':2}};
function score(branche){{
  var s=0;
  s+=BRACKET[val('rf-enveloppe')]||0;
  s+=DELAI[val('rf-delai')]||0;
  s+=checked('rf-engagement')?2:0;
  if(branche==='seo'){{s+=val('rf-paye').length>4?1:0}}
  else{{var c=val('rf-clients');if(c==='6-10')s+=1;if(c==='10+')s+=2}}
  return s;
}}
function statut(s){{if(s>=6)return'vert';if(s>=3)return'orange';return'rouge'}}
root.querySelectorAll('[data-submit]').forEach(function(btn){{
  btn.addEventListener('click',function(){{
    var branche=btn.getAttribute('data-submit');
    var nom=val('rf-nom'),email=val('rf-email');
    var err=root.querySelector('#rf-err-'+branche);
    if(!nom||!email||email.indexOf('@')===-1){{if(err)err.classList.add('show');return}}
    if(err)err.classList.remove('show');
    var s=score(branche),st=statut(s);
    var payload={{
      branche:branche,statut:st,score:s,nom:nom,
      entreprise:val('rf-entreprise'),email:email,telephone:val('rf-tel'),
      site_web:val('rf-site')||val('rf-ville'),ville:val('rf-ville'),metier:val('rf-metier'),
      delai:val('rf-delai'),enveloppe:val('rf-enveloppe'),
      deja_paye:val('rf-paye'),engagement_call:checked('rf-engagement'),
      pourquoi_toi:val('rf-pourquoi'),
      reponses:{{clients:val('rf-clients'),ensuite:val('rf-ensuite')}},
      source_canal:(new URLSearchParams(location.search)).get('utm_source')||'',
      source_url:location.href,user_agent:navigator.userAgent
    }};
    btn.disabled=true;btn.textContent='Envoi…';
    fetch(SUPA_URL+'/rest/v1/candidatures',{{method:'POST',headers:{{
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
}})();
</script></div>"""

    return CSS + "\n" + markup + "\n" + js
