# -*- coding: utf-8 -*-
"""Formulaire de candidature fusionné — page « Cartographie / mini-analyse
GEO gratuite » qui sert à la fois les PME/ETI et les freelances/agences SEO
(fusion demandée des 2 pages séparées, gardant l'URL mini-analyse-geo-seo).

Q0 route vers 3 branches, chacune avec ses propres écrans et sa propre
table Supabase :
  - 'seo'   -> candidatures_seo   (déjà utilisée par l'ancienne page SEO)
  - 'pme'   -> candidatures_pme   (déjà utilisée par l'ancienne page PME),
               colonne profil_type='pme-eti'
  - 'autre' -> candidatures_pme, profil_type='autre', profil libre stocké
               dans la colonne `secteur`

Tous les champs de chaque branche vivent dans le même DOM en même temps
(pas d'injection dynamique) : leurs ids sont donc préfixés par branche
(rf-seo-*, rf-pme-*, rf-autre-*) pour ne jamais entrer en collision.

⚠️ Ne jamais utiliser `&&` dans le JS de ce fichier : WordPress convertit
tout '&' isolé en '&#038;' à l'enregistrement, y compris dans un <script>,
ce qui casse le parsing. Utiliser des ternaires (A?B:false) ou des if
imbriqués à la place. Voir scripts/lib/wpcss.py::audit(), qui bloque ce
motif automatiquement.
"""

SUPABASE_URL = "https://bhgsnoybkxldkzkwkbku.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable_IhHhliR-DLLuakQ2yYpZ-A_kOKRb4_m"

CLOTURE = "dimanche 6 septembre"
PLACES = {"seo": 20, "pme": 25, "autre": 15}
TABLE = {"seo": "candidatures_seo", "pme": "candidatures_pme", "autre": "candidatures_pme"}

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
.rf .rf-choices{display:grid;gap:10px;margin:0 0 8px}
.rf .rf-choice{display:block;text-align:left;background:#f7f7fd;border:1.5px solid var(--rline);border-radius:12px;
 padding:16px 18px;font-size:.98rem;font-weight:700;color:var(--rink);cursor:pointer;transition:border-color .18s,background .18s}
.rf .rf-choice:hover{border-color:var(--rv);background:#f0eefe}
.rf .rf-choice.sel{border-color:var(--rv);background:#f0eefe;box-shadow:0 0 0 3px rgba(123,92,250,.14)}
.rf .rf-choice span{display:block;font-weight:500;font-size:.85rem;color:var(--rmut);margin-top:4px}
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

# ---------------------------------------------------------------------------
# Branche SEO (freelances / agences)
INTERET_APRES = [
    ("acc", "Un accompagnement SEO / GEO"),
    ("infra", "Créer une infra Claude Code (MCP, skills)"),
    ("formation", "Une formation"),
    ("rien", "Rien pour l'instant"),
]
_interet_html = "".join(
    f'<label class="rf-check" data-check><input type="checkbox" id="rf-seo-interet-{k}"><span>{lbl}</span></label>'
    for k, lbl in INTERET_APRES)

SEO_STEPS = [
    ("Pour commencer, vos coordonnées", "On vous appelle si votre candidature est retenue.",
     """<label class="rf-lbl">Prénom &amp; nom</label><input type="text" id="rf-seo-nom" placeholder="Votre nom">
<label class="rf-lbl">Téléphone</label><input type="tel" id="rf-seo-tel" placeholder="C'est nous qui vous appelons">""",
     ["rf-seo-nom", "rf-seo-tel"]),
    ("Comment vous joindre par écrit", "",
     """<label class="rf-lbl">Email</label><input type="email" id="rf-seo-email" placeholder="vous@exemple.fr">
<label class="rf-lbl">Votre structure</label><input type="text" id="rf-seo-entreprise" placeholder="Freelance, ou nom de l'agence">""",
     ["rf-seo-email", "rf-seo-entreprise"]),
    ("Combien de clients gérez-vous actuellement&nbsp;?", "",
     """<select id="rf-seo-clients"><option value="1-3">1 à 3</option><option value="4-10">4 à 10</option><option value="11-25">11 à 25</option><option value="25+">Plus de 25</option></select>""",
     []),
    ("Pour quel client voulez-vous la mini-analyse GEO&nbsp;?", "Le domaine du client à qui elle est destinée — l'analyse sera à votre marque, prête à envoyer.",
     """<input type="url" id="rf-seo-client-domaine" placeholder="https://client-exemple.fr">""",
     ["rf-seo-client-domaine"]),
    ("Une fois la mini-analyse livrée, seriez-vous intéressé par…", "Cochez tout ce qui vous parle.",
     f"""<div class="rf-check-grid">{_interet_html}</div>
<label class="rf-lbl">Autre chose&nbsp;?</label><input type="text" id="rf-seo-interet-autre" placeholder="Précisez si besoin">""",
     []),
    ("Sous quel format, et à quel prix mensuel trouveriez-vous ça juste&nbsp;?", "",
     """<label class="rf-lbl">Format souhaité</label><input type="text" id="rf-seo-format" placeholder="ex. autonome, accompagné, clé en main…">
<label class="rf-lbl">Prix mensuel, environ</label><input type="text" id="rf-seo-prix" placeholder="ex. 100€, ou une fourchette">""",
     ["rf-seo-format", "rf-seo-prix"]),
    ("Qu'avez-vous déjà payé ces 12 derniers mois pour des outils ou formations SEO&nbsp;?", "C'est la question la plus utile de tout le formulaire — soyez précis.",
     """<textarea id="rf-seo-deja-paye" placeholder="ex. Semrush, une formation, un freelance sous-traitant…"></textarea>""",
     ["rf-seo-deja-paye"]),
    ("Délai souhaité pour démarrer", "",
     """<select id="rf-seo-delai"><option value="pas-presse">Je ne suis pas pressé</option><option value="ce-mois">Ce mois-ci</option><option value="cette-semaine">Cette semaine</option></select>""",
     []),
    ("Dernière chose", "Pourquoi vous, plutôt qu'un autre&nbsp;?",
     """<textarea id="rf-seo-pourquoi" placeholder="Un mot sur votre situation, ce qui vous bloque aujourd'hui, pourquoi maintenant…"></textarea>
<div class="rf-eng"><input type="checkbox" id="rf-seo-engagement"><p>Ok pour un call de 20&nbsp;minutes si votre candidature est retenue&nbsp;? (clôture {cloture})</p></div>""".format(cloture=CLOTURE),
     ["rf-seo-pourquoi"]),
]

# ---------------------------------------------------------------------------
# Branche PME / ETI
PME_STEPS = [
    ("Pour commencer, vos coordonnées", "On vous appelle si votre candidature est retenue.",
     """<label class="rf-lbl">Prénom &amp; nom</label><input type="text" id="rf-pme-nom" placeholder="Votre nom">
<label class="rf-lbl">Téléphone</label><input type="tel" id="rf-pme-tel" placeholder="C'est nous qui vous appelons">""",
     ["rf-pme-nom", "rf-pme-tel"]),
    ("Comment vous joindre par écrit", "",
     """<label class="rf-lbl">Email</label><input type="email" id="rf-pme-email" placeholder="vous@exemple.fr">
<label class="rf-lbl">Secteur d'activité</label><input type="text" id="rf-pme-secteur" placeholder="ex. e-commerce, services B2B…">""",
     ["rf-pme-email", "rf-pme-secteur"]),
    ("Votre entreprise", "",
     """<label class="rf-lbl">Nom de l'entreprise</label><input type="text" id="rf-pme-entreprise">
<label class="rf-lbl">Site web actuel</label><input type="url" id="rf-pme-site" placeholder="https://…">""",
     ["rf-pme-entreprise", "rf-pme-site"]),
    ("Ville / zone d'activité", "",
     """<input type="text" id="rf-pme-ville" placeholder="ex. Lyon, ou national">""",
     ["rf-pme-ville"]),
    ("Combien de leads ou clients générez-vous par mois, aujourd'hui&nbsp;?", "",
     """<select id="rf-pme-clients"><option value="0-5">0 à 5</option><option value="6-20">6 à 20</option><option value="21-50">21 à 50</option><option value="50+">Plus de 50</option></select>""",
     []),
    ("Budget marketing mensuel actuel, environ", "Ça reste entre nous — ça nous aide juste à prioriser.",
     """<select id="rf-pme-budget"><option value="ne-sait-pas">Je préfère ne pas dire</option><option value="-500">Moins de 500&nbsp;€</option><option value="500-1500">500 à 1&nbsp;500&nbsp;€</option><option value="1500-3000">1&nbsp;500 à 3&nbsp;000&nbsp;€</option><option value="3000+">Plus de 3&nbsp;000&nbsp;€</option></select>
<label class="rf-lbl">Une fois la cartographie en main, votre priorité&nbsp;?</label>
<select id="rf-pme-priorite"><option value="ne-sait-pas">Je ne sais pas encore</option><option value="seo">SEO classique</option><option value="geo">Visibilité dans les réponses IA (GEO)</option><option value="les-deux">Les deux</option></select>""",
     []),
    ("La cartographie est gratuite.", "Une fois que vous l'aurez vue, seriez-vous prêt à payer un service ensuite&nbsp;? Combien&nbsp;?",
     """<label class="rf-lbl">Quel(s) service(s)&nbsp;?</label><input type="text" id="rf-pme-service" placeholder="ex. contenu GEO, refonte SEO, suivi mensuel…">
<label class="rf-lbl">À quel prix par mois, environ&nbsp;?</label><input type="text" id="rf-pme-prix" placeholder="ex. 1500€, ou une fourchette">""",
     ["rf-pme-service", "rf-pme-prix"]),
    ("Délai souhaité pour démarrer", "",
     """<select id="rf-pme-delai"><option value="pas-presse">Je ne suis pas pressé</option><option value="ce-mois">Ce mois-ci</option><option value="cette-semaine">Cette semaine</option></select>""",
     []),
    ("Dernière chose", "Pourquoi vous, plutôt qu'un autre&nbsp;?",
     """<textarea id="rf-pme-pourquoi" placeholder="Un mot sur votre situation, ce qui vous bloque aujourd'hui, pourquoi maintenant…"></textarea>
<div class="rf-eng"><input type="checkbox" id="rf-pme-engagement"><p>Ok pour qu'on vous appelle et pour donner un accès Search Console / Analytics sous 7 jours si votre candidature est retenue&nbsp;? (clôture {cloture})</p></div>""".format(cloture=CLOTURE),
     ["rf-pme-pourquoi"]),
]

# ---------------------------------------------------------------------------
# Branche Autre (profil hors SEO / PME)
AUTRE_STEPS = [
    ("Pour commencer, vos coordonnées", "On vous appelle si votre candidature est retenue.",
     """<label class="rf-lbl">Prénom &amp; nom</label><input type="text" id="rf-autre-nom" placeholder="Votre nom">
<label class="rf-lbl">Téléphone</label><input type="tel" id="rf-autre-tel" placeholder="C'est nous qui vous appelons">""",
     ["rf-autre-nom", "rf-autre-tel"]),
    ("Comment vous joindre par écrit, et qui êtes-vous&nbsp;?", "",
     """<label class="rf-lbl">Email</label><input type="email" id="rf-autre-email" placeholder="vous@exemple.fr">
<label class="rf-lbl">Décrivez votre activité</label><input type="text" id="rf-autre-profil" placeholder="ex. association, indépendant, startup…">""",
     ["rf-autre-email", "rf-autre-profil"]),
    ("Délai souhaité pour démarrer", "",
     """<select id="rf-autre-delai"><option value="pas-presse">Je ne suis pas pressé</option><option value="ce-mois">Ce mois-ci</option><option value="cette-semaine">Cette semaine</option></select>""",
     []),
    ("Dernière chose", "Pourquoi vous, plutôt qu'un autre&nbsp;?",
     """<textarea id="rf-autre-pourquoi" placeholder="Un mot sur votre situation, ce qui vous bloque aujourd'hui, pourquoi maintenant…"></textarea>
<div class="rf-eng"><input type="checkbox" id="rf-autre-engagement"><p>Ok pour qu'on vous appelle si votre candidature est retenue&nbsp;? (clôture {cloture})</p></div>""".format(cloture=CLOTURE),
     ["rf-autre-pourquoi"]),
]

BRANCHES = {
    "seo": dict(label="Agence ou freelance SEO", sous="Vous gérez des clients, pas seulement votre propre site.", steps=SEO_STEPS),
    "pme": dict(label="PME / ETI", sous="Vous vendez en ligne ou visez plusieurs villes.", steps=PME_STEPS),
    "autre": dict(label="Autre", sous="Précisez votre situation.", steps=AUTRE_STEPS),
}


def _step_html(branch, i, titre, sous, contenu, is_last):
    sub_html = f'<p class="rf-sub">{sous}</p>' if sous else ''
    nav = (
        '<button type="button" class="rf-back" data-back>&larr; Retour</button>'
        '<div class="rf-spacer"></div>'
        + (f'<button type="button" class="rf-submit" data-submit="{branch}">Envoyer ma candidature</button>' if is_last
           else '<button type="button" class="rf-next" data-next>Suivant &rarr;</button>')
    )
    return f"""<div class="rf-step" data-branch="{branch}" data-idx="{i}">
  <h3 class="rf-q">{titre}</h3>
  {sub_html}
  {contenu}
  <p class="rf-err" id="rf-err-{branch}-{i}">Merci de remplir ce champ avant de continuer.</p>
  <div class="rf-nav">{nav}</div>
</div>"""


def render():
    choix = "".join(
        f'<button type="button" class="rf-choice" data-route="{cle}">{b["label"]}<span>{b["sous"]}</span></button>'
        for cle, b in BRANCHES.items())

    steps_html = "".join(
        "".join(_step_html(branche, i, titre, sous, contenu, i == len(b["steps"]) - 1)
                for i, (titre, sous, contenu, _req) in enumerate(b["steps"]))
        for branche, b in BRANCHES.items()
    )

    required_json = "{" + ",".join(
        f"'{branche}':[" + ",".join(
            "[" + ",".join(f"'{r}'" for r in req) + "]" for (_t, _s, _c, req) in b["steps"]
        ) + "]"
        for branche, b in BRANCHES.items()
    ) + "}"

    places_json = "{" + ",".join(f"'{k}':{v}" for k, v in PLACES.items()) + "}"
    table_json = "{" + ",".join(f"'{k}':'{v}'" for k, v in TABLE.items()) + "}"

    markup = f"""<div class="rf rf-overlay" id="candidature-form"><div class="rf-w"><div class="rf-card">
<button type="button" class="rf-x" data-close-form aria-label="Fermer">&times;</button>
<div class="rf-top">
  <div class="rf-places" id="rf-places">🎯 Candidatures ouvertes · clôture {CLOTURE}</div>
  <div class="rf-count" id="rf-count"></div>
</div>
<div class="rf-bar"><div class="rf-bar-fill" id="rf-bar-fill" style="width:8%"></div></div>

<div class="rf-step active" data-step="q0">
  <h3 class="rf-q">Pour commencer, vous êtes plutôt…</h3>
  <div class="rf-choices">{choix}</div>
</div>

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
var PLACES={places_json};
var TABLES={table_json};
var REQUIRED={required_json};
var branch=null,cur=0;
function openForm(e){{if(e)e.preventDefault();root.classList.add('active');document.body.style.overflow='hidden'}}
function closeForm(){{root.classList.remove('active');document.body.style.overflow=''}}
document.querySelectorAll('[data-open-form]').forEach(function(t){{t.addEventListener('click',openForm)}});
root.querySelectorAll('[data-close-form]').forEach(function(t){{t.addEventListener('click',closeForm)}});
root.addEventListener('click',function(e){{if(e.target===root)closeForm()}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape')closeForm()}});
function val(id){{var e=root.querySelector('#'+id);return e?e.value.trim():''}}
function checked(id){{var e=root.querySelector('#'+id);return e?!!e.checked:false}}
function markInvalid(id,bad){{var e=root.querySelector('#'+id);if(e)e.style.borderColor=bad?'#c0392b':''}}
root.querySelectorAll('input,select,textarea').forEach(function(e){{
  e.addEventListener('input',function(){{e.style.borderColor=''}});
}});
root.querySelectorAll('[data-check]').forEach(function(lbl){{
  var cb=lbl.querySelector('input');
  cb.addEventListener('change',function(){{lbl.classList.toggle('sel',cb.checked)}});
}});
function branchSteps(){{return root.querySelectorAll('.rf-step[data-branch="'+branch+'"]')}}
function updateBar(){{
  var steps=branchSteps(),N=steps.length+1;
  root.querySelector('#rf-count').textContent='Étape '+(cur+2)+' sur '+N;
  root.querySelector('#rf-bar-fill').style.width=Math.round(((cur+2)/N)*100)+'%';
}}
function showStep(i){{
  cur=i;
  var steps=branchSteps();
  steps.forEach(function(s,k){{s.classList.toggle('active',k===i)}});
  updateBar();
  root.scrollTop=0;
}}
root.querySelectorAll('[data-route]').forEach(function(btn){{
  btn.addEventListener('click',function(){{
    branch=btn.getAttribute('data-route');
    var pl=PLACES[branch];
    root.querySelector('#rf-places').textContent='🎯 '+pl+' places · clôture {CLOTURE}';
    root.querySelector('[data-step="q0"]').classList.remove('active');
    showStep(0);
  }});
}});
root.querySelectorAll('[data-back]').forEach(function(btn){{
  btn.addEventListener('click',function(){{
    if(cur>0){{showStep(cur-1);return}}
    branchSteps().forEach(function(s){{s.classList.remove('active')}});
    root.querySelector('[data-step="q0"]').classList.add('active');
    branch=null;
    root.scrollTop=0;
  }});
}});
var INTERET_KEYS=['acc','infra','formation','rien'];
root.querySelectorAll('[data-next]').forEach(function(btn){{
  btn.addEventListener('click',function(){{
    var req=REQUIRED[branch][cur]||[];
    var err=root.querySelector('#rf-err-'+branch+'-'+cur),ok=true,firstBad=null;
    for(var k=0;k<req.length;k++){{
      var isEmail=req[k].indexOf('email')!==-1;
      var emailBad=isEmail?(val(req[k]).indexOf('@')===-1):false;
      var bad=!val(req[k])||emailBad;
      markInvalid(req[k],bad);
      if(bad){{ok=false;if(!firstBad)firstBad=req[k]}}
    }}
    if(branch==='seo'){{
      if(cur===4){{
        var nChecked=0;
        INTERET_KEYS.forEach(function(kk){{if(checked('rf-seo-interet-'+kk))nChecked++}});
        var interetBad=(nChecked===0)?(!val('rf-seo-interet-autre')):false;
        if(interetBad){{ok=false;if(!firstBad)firstBad='rf-seo-interet-autre'}}
      }}
    }}
    if(!ok){{
      if(err)err.classList.add('show');
      var badEl=firstBad?root.querySelector('#'+firstBad):null;
      if(badEl)badEl.scrollIntoView({{block:'center',behavior:'smooth'}});
      return;
    }}
    if(err)err.classList.remove('show');
    var steps=branchSteps();
    if(cur<steps.length-1)showStep(cur+1);
  }});
}});
var DELAI={{'pas-presse':0,'ce-mois':1,'cette-semaine':2}};
function interetList(){{
  var out=[];
  INTERET_KEYS.forEach(function(k){{if(checked('rf-seo-interet-'+k))out.push(k)}});
  var autre=val('rf-seo-interet-autre');if(autre)out.push('autre: '+autre);
  return out.join(', ');
}}
function submitPayload(){{
  if(branch==='seo'){{
    return {{
      statut:'nouveau',nom:val('rf-seo-nom'),entreprise:val('rf-seo-entreprise'),
      email:val('rf-seo-email'),telephone:val('rf-seo-tel'),
      client_domaine:val('rf-seo-client-domaine'),nb_clients:val('rf-seo-clients'),
      interet:interetList(),format_souhaite:val('rf-seo-format'),prix_mensuel:val('rf-seo-prix'),
      deja_paye:val('rf-seo-deja-paye'),delai:val('rf-seo-delai'),
      engagement_call:checked('rf-seo-engagement'),pourquoi_toi:val('rf-seo-pourquoi'),
      score:(DELAI[val('rf-seo-delai')]||0)+({{'1-3':0,'4-10':1,'11-25':2,'25+':3}}[val('rf-seo-clients')]||0)+(checked('rf-seo-engagement')?2:0)+(val('rf-seo-deja-paye').length>4?1:0)
    }};
  }}
  if(branch==='pme'){{
    return {{
      statut:'nouveau',profil_type:'pme-eti',nom:val('rf-pme-nom'),secteur:val('rf-pme-secteur'),
      entreprise:val('rf-pme-entreprise'),site_web:val('rf-pme-site'),ville:val('rf-pme-ville'),
      email:val('rf-pme-email'),telephone:val('rf-pme-tel'),
      clients_mois:val('rf-pme-clients'),budget_marketing:val('rf-pme-budget'),priorite:val('rf-pme-priorite'),
      service_souhaite:val('rf-pme-service'),prix_mensuel:val('rf-pme-prix'),
      delai:val('rf-pme-delai'),engagement_call:checked('rf-pme-engagement'),pourquoi_toi:val('rf-pme-pourquoi'),
      score:(DELAI[val('rf-pme-delai')]||0)+({{'0-5':0,'6-20':1,'21-50':2,'50+':3}}[val('rf-pme-clients')]||0)+({{'ne-sait-pas':0,'-500':0,'500-1500':1,'1500-3000':2,'3000+':3}}[val('rf-pme-budget')]||0)+(checked('rf-pme-engagement')?2:0)+((val('rf-pme-service').length>1?1:val('rf-pme-prix').length>1?1:0))
    }};
  }}
  return {{
    statut:'nouveau',profil_type:'autre',nom:val('rf-autre-nom'),secteur:'Autre : '+val('rf-autre-profil'),
    email:val('rf-autre-email'),telephone:val('rf-autre-tel'),
    delai:val('rf-autre-delai'),engagement_call:checked('rf-autre-engagement'),pourquoi_toi:val('rf-autre-pourquoi'),
    score:(DELAI[val('rf-autre-delai')]||0)+(checked('rf-autre-engagement')?2:0)
  }};
}}
function statut(s){{if(s>=5)return'vert';if(s>=2)return'orange';return'rouge'}}
root.querySelectorAll('[data-submit]').forEach(function(btn){{
  btn.addEventListener('click',function(){{
    var b=btn.getAttribute('data-submit');
    var nom=val('rf-'+b+'-nom'),tel=val('rf-'+b+'-tel'),email=val('rf-'+b+'-email'),pourquoi=val('rf-'+b+'-pourquoi');
    var err=root.querySelector('#rf-err-'+b+'-'+cur);
    var emailBad=email.indexOf('@')===-1;
    var engBad=!checked('rf-'+b+'-engagement');
    var engBox=root.querySelector('.rf-step[data-branch="'+b+'"].active .rf-eng');
    markInvalid('rf-'+b+'-pourquoi',!pourquoi);
    if(engBox)engBox.classList.toggle('bad',engBad);
    if(!nom||!tel||!email||!pourquoi||emailBad||engBad){{if(err)err.classList.add('show');return}}
    if(err)err.classList.remove('show');
    var payload=submitPayload();
    payload.statut=statut(payload.score);
    payload.source_canal=(new URLSearchParams(location.search)).get('utm_source')||'';
    payload.source_url=location.href;
    payload.user_agent=navigator.userAgent;
    var st=payload.statut;
    btn.disabled=true;btn.textContent='Envoi…';
    fetch(SUPA_URL+'/rest/v1/'+TABLES[b],{{method:'POST',headers:{{
      'apikey':SUPA_KEY,'Authorization':'Bearer '+SUPA_KEY,
      'Content-Type':'application/json','Prefer':'return=minimal'
    }},body:JSON.stringify(payload)}}).then(function(r){{
      if(!r.ok)throw new Error('http '+r.status);
      branchSteps().forEach(function(s){{s.classList.remove('active')}});
      root.querySelectorAll('.rf-outcome').forEach(function(o){{
        o.classList.toggle('active',o.getAttribute('data-outcome')===st)
      }});
    }}).catch(function(){{
      btn.disabled=false;btn.textContent='Envoyer ma candidature';
      if(err){{err.textContent='Un problème est survenu, réessayez.';err.classList.add('show')}}
    }});
  }});
}});
}});
</script></div>"""

    return CSS + "\n" + markup + "\n" + js
