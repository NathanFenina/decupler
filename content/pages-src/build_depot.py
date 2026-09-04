# -*- coding: utf-8 -*-
"""Construit la page « Le dépôt claude-seo » (WordPress ID 7805).

    python3 content/pages-src/build_depot.py

L'inventaire vient de content/data/depot_claude_seo.py, lui-même extrait de
la documentation du dépôt. La page ne recopie donc rien à la main : elle
annonce le nombre de skills que le dépôt contient réellement, et le jour où
il en gagne un, on régénère au lieu de corriger un chiffre à trois endroits.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
for d in ('content/data', 'content/components', 'scripts/lib'):
    sys.path.insert(0, str(RACINE / d))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import wpcss                                              # noqa: E402
import pied_technique as PT                               # noqa: E402
import depot_claude_seo as D                              # noqa: E402

SKIN = open(RACINE / 'content/skins/dcp.css', encoding='utf-8').read()
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Syne:wght@700;800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700'
         '&family=JetBrains+Mono:wght@400;700&display=swap">')

DEPOT = "https://github.com/NathanFenina/claude-seo"
N_SKILLS = sum(len(v) for _, v in D.BLOCS)

# Le tableau du README du dépôt, repris tel quel. Ce sont les mesures que le
# dépôt annonce : la page les relaie, elle ne les invente pas et ne les
# arrondit pas dans le bon sens.
AVANT_APRES = [
    ("Quick wins du mois", "~2 h", "6 min"),
    ("Brief adossé à la SERP", "~1 h 30", "4 min"),
    ("Article + visuels + publication", "~4 h", "9 min"),
    ("Mesure de visibilité IA", "~2 h", "5 min"),
    ("Rapport mensuel", "~3 h", "3 min"),
]
TOTAL = ("12 h 30", "27 min")

MCP = ["dataforseo", "ahrefs", "semrush", "ubersuggest", "search-console",
       "google-analytics", "firecrawl", "chrome-devtools", "wordpress",
       "webflow", "notion", "perplexity", "reddit"]

# Le terminal du hero. Ce qu'il montre est ce que /seo-audit fait vraiment :
# huit agents en parallèle, un score, un plan. Rien d'inventé.
TERM = """<div class="term rise"><div class="term-bar"><i></i><i></i><i></i><b>claude code — votre-site.fr</b></div><pre><span class="tp">›</span> <span class="tc">/seo-audit votre-site.fr</span>
<span class="tm">8 agents lancés en parallèle…</span>

<span class="ln l1">  <span class="st s1"><span class="run tm">⠿</span><span class="ok tok">✓</span></span> <span class="tc">seo-technique</span>     <span class="tm">14 problèmes · 9 corrigés</span></span>
<span class="ln l2">  <span class="st s2"><span class="run tm">⠿</span><span class="ok tok">✓</span></span> <span class="tc">seo-performance</span>   <span class="tm">LCP 4,1 s · causes localisées</span></span>
<span class="ln l3">  <span class="st s3"><span class="run tm">⠿</span><span class="ok tok">✓</span></span> <span class="tc">seo-crawler</span>       <span class="tm">312 URL · 6 orphelines</span></span>
<span class="ln l4">  <span class="st s4"><span class="run tm">⠿</span><span class="ok tok">✓</span></span> <span class="tc">seo-contenu</span>       <span class="tm">6 pages minces</span></span>
<span class="ln l5">  <span class="st s5"><span class="run tm">⠿</span><span class="ok tok">✓</span></span> <span class="tc">seo-schema</span>        <span class="tm">JSON-LD absent · 31 pages</span></span>
<span class="ln l6">  <span class="st s6"><span class="run tm">⠿</span><span class="ok tok">✓</span></span> <span class="tc">seo-eeat</span>          <span class="tm">score 22/40</span></span>
<span class="ln l7">  <span class="st s7"><span class="run tm">⠿</span><span class="ok tok">✓</span></span> <span class="tc">seo-geo</span>           <span class="tm">0 citation IA sur 12 requêtes</span></span>
<span class="ln l8">  <span class="st s8"><span class="run tm">⠿</span><span class="ok tok">✓</span></span> <span class="tc">seo-data</span>          <span class="tm">Search Console · 90 jours</span></span>

<span class="ln l9"><span class="tm">Score</span> <span class="tc">58/100</span><span class="tm"> · plan écrit dans</span> <span class="tc">audit.md</span></span>
<span class="ln l10"><span class="tp">›</span> <span class="tc">/seo-fix --auto</span>   <span class="tm">9 correctifs appliqués</span></span></pre></div>"""

CHIFFRES = [(N_SKILLS, "skills"), (len(D.AGENTS), "agents"),
            (len(D.COMMANDES), "commandes"), (len(MCP), "MCP branchés")]


def avant_apres_html():
    li = ''.join(f'<tr><td>{t}</td><td class="main">{a}</td>'
                 f'<td class="ici">{b}</td></tr>' for t, a, b in AVANT_APRES)
    return (f'<table class="av rise"><thead><tr><th>Tâche</th><th>À la main</th>'
            f'<th>Ici</th></tr></thead><tbody>{li}</tbody>'
            f'<tfoot><tr><td>Sur un mois</td><td class="main">{TOTAL[0]}</td>'
            f'<td class="ici">{TOTAL[1]}</td></tr></tfoot></table>')


def blocs_html():
    out = ''
    for titre, skills in D.BLOCS:
        li = ''.join(f'<li><code>{s}</code><span>{d}</span></li>' for s, d in skills)
        # La grille est en deux colonnes et le fond du conteneur fait les
        # filets de 1px : un bloc impair laisse donc une cellule grise a nu.
        # On la comble plutot que d'abandonner les filets.
        if len(skills) % 2:
            li += '<li aria-hidden="true"></li>'
        out += (f'<div class="blc rise"><div class="blc-h"><h3>{titre}</h3>'
                f'<span>{len(skills)} skills</span></div>'
                f'<ul class="blc-l">{li}</ul></div>')
    return out


def jetons(items, mono=False):
    cl = ' mcp' if mono else ''
    li = ''.join((f'<li>{i}</li>' if mono else
                  f'<li><b>{i}</b><span>{d}</span></li>')
                 for i, d in items) if not mono else \
         ''.join(f'<li>{i}</li>' for i in items)
    return f'<ul class="jet{cl} rise">{li}</ul>'


FAQ = [
    ("C'est gratuit ?",
     "Oui, licence MIT. Vous clonez, vous modifiez, vous utilisez en clientèle "
     "sans rien demander à personne."),
    ("Il faut savoir coder ?",
     "Non. Vous tapez une commande en français dans Claude Code, les agents font "
     "le reste. L'installation est un copier-coller."),
    ("Et si je n'ai pas les MCP payants ?",
     f"Les {len(MCP)} MCP sont tous optionnels, avec repli gracieux : sans Ahrefs "
     "ni Semrush, les skills qui en dépendent basculent sur ce qui est "
     "disponible et vous le disent."),
    ("Ça publie tout seul sur mon site ?",
     "Seulement si vous le demandez, et en brouillon par défaut. Un hook "
     "<code>garde-fou.sh</code> bloque les actions destructrices avant "
     "qu'elles partent."),
    ("Quelle différence avec un ChatGPT à qui je demande du SEO ?",
     "Un chatbot vous répond. Ici les agents lisent votre Search Console, "
     "crawlent vos pages, interrogent la SERP en direct, corrigent vos "
     "fichiers et publient. La réponse n'est pas le livrable — le site "
     "corrigé l'est."),
]


def page():
    ch = ''.join(f'<div class="cnt"><div class="num">{n}</div>'
                 f'<div class="lbl">{l}</div></div>' for n, l in CHIFFRES)
    faq = ''.join(f'<details class="rise"><summary>{q}</summary><p>{r}</p></details>'
                  for q, r in FAQ)
    return f"""{FONTS}
{SKIN}
<div class="dcp">

<section class="dcp-hero" id="depot"><div class="in dcp-grid">
  <div>
    <h1>Le SEO manuel,<br><em>c'est terminé.</em></h1>
    <p class="lead">{N_SKILLS} skills, {len(D.AGENTS)} agents et {len(D.COMMANDES)} commandes
    pour Claude Code. Ça audite, ça corrige, ça rédige, ça publie, ça mesure —
    en français, et en autonomie.</p>
    <p><a class="dcp-cta" href="{DEPOT}" target="_blank" rel="noopener">Ouvrir le dépôt sur GitHub</a></p>
    <p class="dcp-under">Licence MIT · installation en une commande · {len(MCP)} MCP optionnels</p>
  </div>
  {TERM}
</div></section>

<section class="dcp-band" id="chiffres"><div class="in chiffres">{ch}</div></section>

<section class="dcp-band" id="ce-que-ca-change"><div class="in plein">
  <h2>{TOTAL[0]} de SEO à la main<br>→ <em class="vert">{TOTAL[1]}</em></h2>
  <p class="band-p">Les mesures annoncées par le dépôt, tâche par tâche. Ce ne
  sont pas des gains théoriques : c'est le temps que prend la même sortie,
  faite à la main puis faite par les agents.</p>
  {avant_apres_html()}
</div></section>

<section class="dcp-sec" id="skills"><div class="in">
  <h2>Les {N_SKILLS} skills, rangés par ce qu'ils font</h2>
  <p class="lead">Un skill se déclenche tout seul quand votre demande le
  concerne. Vous n'avez pas à retenir cette liste — elle est là pour que vous
  sachiez ce qui est couvert avant d'installer.</p>
  {blocs_html()}
</div></section>

<section class="dcp-band" id="agents"><div class="in plein">
  <h2>Les {len(D.AGENTS)} agents</h2>
  <p class="band-p">Un skill décide, un agent exécute. Ils tournent en
  parallèle : c'est ce qui fait qu'un audit complet prend six minutes au lieu
  de deux heures.</p>
  {jetons(D.AGENTS)}
</div></section>

<section class="dcp-sec alt" id="commandes"><div class="in">
  <h2>Les {len(D.COMMANDES)} commandes</h2>
  <p class="lead">Pour quand vous savez déjà ce que vous voulez.</p>
  {jetons([('/' + c, d) for c, d in D.COMMANDES])}
</div></section>

<section class="dcp-sec" id="mcp"><div class="in">
  <h2>Les {len(MCP)} MCP préconfigurés</h2>
  <p class="lead">Le fichier <code>.mcp.json</code> les déclare tous. Chacun
  est optionnel : sans clé, le skill qui en dépend bascule sur ce qui est
  disponible et vous dit ce qui lui manque, au lieu de s'arrêter.</p>
  {jetons(MCP, mono=True)}
  <p class="lead suite">Le détail de chaque MCP, ce qu'il
  coûte et ce qu'il apporte, est sur la page
  <a href="https://decupler.com/machine-de-guerre-seo/">machine de guerre SEO
  dans Claude Code</a> — c'est le pas d'avant : brancher les outils, puis
  installer ce dépôt par-dessus.</p>
</div></section>

<section class="dcp-sec alt" id="garde-fou"><div class="in">
  <h2>Le garde-fou</h2>
  <p class="lead">C'est la partie dont personne ne parle et qui décide si vous
  pouvez laisser un agent toucher un site en production.</p>
  <div class="cond rise"><b>Deux hooks, avant chaque action</b>
  <p><code>garde-fou.sh</code> bloque les commandes destructrices avant
  qu'elles s'exécutent. <code>verifier-schema.sh</code> valide le JSON-LD
  produit avant qu'il parte en ligne. La publication est en brouillon par
  défaut : rien n'atteint le public sans que vous l'ayez relu.</p></div>
</div></section>

<section class="dcp-sec" id="installer"><div class="in">
  <h2>Installer</h2>
  <div class="etapes">
    <div class="et-l rise"><div class="num"></div><div><h3>Par le marketplace Claude Code</h3>
    <p>Le chemin recommandé : skills, agents, commandes et MCP arrivent d'un
    seul coup.</p>
    <div class="term"><div class="term-bar"><i></i><i></i><i></i><b>claude code</b></div><pre><span class="tp">›</span> <span class="tc">/plugin marketplace add NathanFenina/claude-seo</span>
<span class="tp">›</span> <span class="tc">/plugin install claude-code-seo-decupler@decupler</span></pre></div></div></div>
    <div class="et-l rise"><div class="num"></div><div><h3>Ou par le script</h3>
    <p>Si vous préférez voir ce qui s'installe.</p>
    <div class="term"><div class="term-bar"><i></i><i></i><i></i><b>terminal</b></div><pre><span class="tm"># macOS, Linux</span>
<span class="tp">$</span> <span class="tc">curl -fsSL https://raw.githubusercontent.com/NathanFenina/claude-seo/main/install.sh | bash</span>

<span class="tm"># Windows, PowerShell</span>
<span class="tp">&gt;</span> <span class="tc">irm https://raw.githubusercontent.com/NathanFenina/claude-seo/main/install.ps1 | iex</span></pre></div></div></div>
    <div class="et-l rise"><div class="num"></div><div><h3>Puis lancez la première commande</h3>
    <p><code>/seo-onboarding</code> vous accueille, diagnostique ce qui est
    branché et lance la première action utile sur votre site.</p></div></div>
  </div>
</div></section>

<section class="dcp-sec alt" id="questions"><div class="in">
  <h2>Les questions qu'on nous pose</h2>
  <div class="rise">{faq}</div>
</div></section>

<section class="dcp-band centre" id="fin"><div class="in plein">
  <h2>Le dépôt est ouvert.<br>Servez-vous.</h2>
  <p class="band-p">Licence MIT, {N_SKILLS} skills, {len(D.AGENTS)} agents.
  Et si vous voulez ce qu'on publie avant tout le monde, la newsletter est là.</p>
  <p class="band-act"><a class="dcp-cta vert" href="{DEPOT}" target="_blank" rel="noopener">Ouvrir le dépôt</a>
  &nbsp;<a class="dcp-cta" href="https://decupler.substack.com" target="_blank" rel="noopener">La newsletter</a></p>
</div></section>

{PT.rendu(FAQ)}
</div>"""


if __name__ == '__main__':
    html = wpcss.harden(page())
    dst = RACINE / 'content/articles/claude-skills-repo-github.html'
    dst.write_text(html, encoding='utf-8')
    print(f"{dst}  —  {len(html):,} octets".replace(',', ' '))
