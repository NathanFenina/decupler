# -*- coding: utf-8 -*-
"""CTA « Cartographie » Décupler — composant autonome, déployable sur tout skin.

Markup wpautop-safe : dans chaque conteneur, les enfants sont soit tous inline,
soit tous block. Sinon WordPress injecte des </p> orphelins.
"""

CALENDLY = "https://calendly.com/fenina-nathan/consultationstrategique"

CSS = """<style>
.dcta{--dv:#6366f1;--dv2:#8b5cf6;--dg:#10b981;--dink:#0f172a;--dmut:#475569;--dline:rgba(99,102,241,.16);
 position:relative;margin:0;padding:64px 0;background:linear-gradient(165deg,#f7f7fd 0%,#eef0fb 100%);
 border-top:1px solid var(--dline);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Ubuntu,sans-serif}
.dcta *{box-sizing:border-box}
.dcta .dcta-w{max-width:940px;margin:0 auto;padding:0 24px}
.dcta .dcta-eye{display:inline-block;font-family:'JetBrains Mono',ui-monospace,monospace;font-size:.68rem;font-weight:700;
 letter-spacing:.1em;text-transform:uppercase;color:var(--dv);background:rgba(99,102,241,.09);
 border:1px solid rgba(99,102,241,.22);border-radius:20px;padding:6px 14px;margin:0 0 18px}
.dcta h2{font-family:'Syne',var(--font-display,sans-serif);font-size:clamp(1.6rem,3.4vw,2.35rem);font-weight:800;
 line-height:1.14;letter-spacing:-.02em;color:var(--dink);margin:0 0 16px}
.dcta h2 em{font-style:normal;background:linear-gradient(120deg,var(--dv),var(--dv2));-webkit-background-clip:text;
 background-clip:text;-webkit-text-fill-color:transparent}
.dcta .dcta-lead{font-size:1.03rem;line-height:1.62;color:var(--dmut);margin:0 0 30px;max-width:730px}
.dcta .dcta-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:0 0 26px}
.dcta .dcta-c{background:#fff;border:1px solid var(--dline);border-radius:14px;padding:20px 20px 22px;
 transition:transform .25s,box-shadow .25s,border-color .25s}
.dcta .dcta-c:hover{transform:translateY(-3px);border-color:var(--dv);box-shadow:0 18px 36px -18px rgba(99,102,241,.42)}
.dcta .dcta-n{width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;
 font-family:'JetBrains Mono',ui-monospace,monospace;font-size:.74rem;font-weight:800;color:#fff;
 background:linear-gradient(135deg,var(--dv),var(--dv2));margin:0 0 12px}
.dcta .dcta-c h3{font-family:'Syne',sans-serif;font-size:1rem;font-weight:800;color:var(--dink);margin:0 0 7px;line-height:1.25}
.dcta .dcta-c p{font-size:.88rem;line-height:1.5;color:var(--dmut);margin:0}
.dcta .dcta-rdv{background:#fff;border:1px solid var(--dline);border-left:3px solid var(--dg);border-radius:12px;
 padding:18px 20px;margin:0 0 28px}
.dcta .dcta-rdv .dcta-lbl{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:.64rem;font-weight:700;
 letter-spacing:.07em;text-transform:uppercase;color:var(--dg);margin:0 0 6px}
.dcta .dcta-rdv p{font-size:.94rem;line-height:1.58;color:var(--dmut);margin:0}
.dcta .dcta-rdv strong{color:var(--dink)}
.dcta .dcta-act{display:flex;flex-wrap:wrap;align-items:center;gap:16px}
.dcta .dcta-btn{display:inline-flex;align-items:center;gap:9px;background:linear-gradient(135deg,var(--dv),var(--dv2));
 color:#fff!important;text-decoration:none!important;font-weight:700;font-size:1rem;padding:15px 30px;border-radius:11px;
 box-shadow:0 12px 26px -10px rgba(99,102,241,.6);transition:transform .22s,box-shadow .22s}
.dcta .dcta-btn:hover{transform:translateY(-2px);box-shadow:0 18px 34px -12px rgba(99,102,241,.7);color:#fff!important}
.dcta .dcta-btn::after{content:'\\2192';font-size:1.05em}
.dcta .dcta-sec{display:inline-flex;align-items:center;gap:7px;color:var(--dv)!important;text-decoration:none!important;
 font-size:.92rem;font-weight:600;border-bottom:1px solid rgba(99,102,241,.3);padding-bottom:2px;transition:border-color .2s}
.dcta .dcta-sec:hover{border-bottom-color:var(--dv)}
.dcta .dcta-note{font-size:.85rem;color:var(--dmut);margin:0;line-height:1.5}
.dcta .dcta-note strong{color:var(--dink)}
@media(max-width:820px){.dcta .dcta-grid{grid-template-columns:1fr}.dcta{padding:48px 0}}
</style>"""

# (titre, texte) des 3 cartes — le coeur de l'offre
CARDS_VOUS = [
 ("Les prompts où ils sortent, pas vous",
  "La liste des questions que pose votre marché, avec le nom des concurrents que ChatGPT, Perplexity et les AI&nbsp;Overviews citent à votre place."),
 ("Vos angles morts",
  "Les sujets que vos acheteurs cherchent et sur lesquels vous n'avez, aujourd'hui, strictement rien à leur montrer."),
 ("Vos fuites de leads",
  "Les pages qui reçoivent déjà des visites et n'en transforment aucune&nbsp;— là où l'argent est posé par terre."),
]
CARDS_TU = [
 ("Les prompts où ils sortent, pas toi",
  "La liste des questions que pose ton marché, avec le nom des concurrents que ChatGPT, Perplexity et les AI&nbsp;Overviews citent à ta place."),
 ("Tes angles morts",
  "Les sujets que tes acheteurs cherchent et sur lesquels tu n'as, aujourd'hui, strictement rien à leur montrer."),
 ("Tes fuites de leads",
  "Les pages qui reçoivent déjà des visites et n'en transforment aucune&nbsp;— là où l'argent est posé par terre."),
]

COPY = {
 "vous": dict(
  eye="Cartographie offerte",
  h2="Vos concurrents sont cités dans ces réponses.<br><em>Vous n'y êtes pas.</em>",
  lead="On vous envoie la cartographie de votre marché&nbsp;: les prompts exacts où vos concurrents apparaissent et vous non, les sujets sur lesquels vous êtes absent, et les pages qui vous amènent du trafic sans jamais produire un lead.",
  cards=CARDS_VOUS,
  rdv="On la parcourt ensemble en 30&nbsp;minutes. Je vous montre <strong>exactement quoi faire, et dans quel ordre</strong>&nbsp;— et sur le premier sujet prioritaire, <strong>je vous sors le contenu à publier</strong>. Pas un conseil&nbsp;: le texte.",
  btn="Recevoir ma cartographie",
  note="<strong>Gratuit, 30&nbsp;minutes, sans engagement.</strong> Vous repartez avec la cartographie même si on ne travaille pas ensemble."),
 "tu": dict(
  eye="Cartographie offerte",
  h2="Tes concurrents sont cités dans ces réponses.<br><em>Tu n'y es pas.</em>",
  lead="On t'envoie la cartographie de ton marché&nbsp;: les prompts exacts où tes concurrents apparaissent et toi non, les sujets sur lesquels tu es absent, et les pages qui t'amènent du trafic sans jamais produire un lead.",
  cards=CARDS_TU,
  rdv="On la parcourt ensemble en 30&nbsp;minutes. Je te montre <strong>exactement quoi faire, et dans quel ordre</strong>&nbsp;— et sur le premier sujet prioritaire, <strong>je te sors le contenu à publier</strong>. Pas un conseil&nbsp;: le texte.",
  btn="Recevoir ma cartographie",
  note="<strong>Gratuit, 30&nbsp;minutes, sans engagement.</strong> Tu repars avec la cartographie même si on ne travaille pas ensemble."),
}


def render(ton="vous", href=CALENDLY, with_css=True, sec=None, sec_label=None):
    c = COPY[ton]
    cards = "".join(
        f'<div class="dcta-c"><div class="dcta-n">{i}</div><h3>{t}</h3><p>{d}</p></div>'
        for i, (t, d) in enumerate(c["cards"], 1))
    secl = f'<a class="dcta-sec" href="{sec}">{sec_label}</a>' if sec else ''
    html = f"""<section class="dcta">
<div class="dcta-w">
<div class="dcta-eye">{c['eye']}</div>
<h2>{c['h2']}</h2>
<p class="dcta-lead">{c['lead']}</p>
<div class="dcta-grid">{cards}</div>
<div class="dcta-rdv"><div class="dcta-lbl">Et pendant les 30 minutes</div><p>{c['rdv']}</p></div>
<div class="dcta-act"><a class="dcta-btn" href="{href}" rel="noopener">{c['btn']}</a>{secl}<p class="dcta-note">{c['note']}</p></div>
</div>
</section>"""
    return (CSS + "\n" + html) if with_css else html
