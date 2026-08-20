# -*- coding: utf-8 -*-
"""CTA « 10 prompts » Décupler — version courte et animée.

~35 mots contre 186 pour la version longue. Une promesse, un bouton.
Markup wpautop-safe. Animations desactivees si prefers-reduced-motion.
"""
CALENDLY = "https://calendly.com/fenina-nathan/consultationstrategique"

CSS = """<style>
.pcta{--pv:#6366f1;--pv2:#8b5cf6;--pg:#10b981;--pink:#0f172a;--pmut:#475569;
 position:relative;overflow:hidden;margin:0;padding:72px 0;
 background:radial-gradient(120% 140% at 15% 0%,#f4f4fe 0%,#eceefb 55%,#e8ebfa 100%);
 border-top:1px solid rgba(99,102,241,.14);
 font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Ubuntu,sans-serif}
.pcta *{box-sizing:border-box}
.pcta::before{content:'';position:absolute;top:-45%;left:-10%;width:60%;height:190%;
 background:radial-gradient(closest-side,rgba(99,102,241,.16),transparent 70%);
 animation:pctaDrift 17s ease-in-out infinite alternate;pointer-events:none}
.pcta::after{content:'';position:absolute;bottom:-55%;right:-8%;width:52%;height:180%;
 background:radial-gradient(closest-side,rgba(16,185,129,.13),transparent 70%);
 animation:pctaDrift 21s ease-in-out infinite alternate-reverse;pointer-events:none}
@keyframes pctaDrift{from{transform:translate3d(0,0,0) scale(1)}to{transform:translate3d(7%,5%,0) scale(1.14)}}
.pcta .pcta-w{position:relative;z-index:1;max-width:800px;margin:0 auto;padding:0 24px;text-align:center}
.pcta h2{font-family:'Syne',sans-serif;font-size:clamp(1.55rem,3.6vw,2.5rem);font-weight:800;
 line-height:1.14;letter-spacing:-.022em;color:var(--pink);margin:0 0 18px}
.pcta h2 .pcta-hl{position:relative;display:inline-block;white-space:nowrap;
 background:linear-gradient(120deg,var(--pv) 0%,var(--pv2) 50%,var(--pv) 100%);
 background-size:220% 100%;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
 animation:pctaShine 5.5s linear infinite}
@keyframes pctaShine{to{background-position:-220% 0}}
.pcta .pcta-lead{font-size:clamp(1rem,1.6vw,1.12rem);line-height:1.6;color:var(--pmut);margin:0 auto 30px;max-width:640px}
.pcta .pcta-lead b{color:var(--pink);font-weight:700;white-space:nowrap}
.pcta .pcta-btn{display:inline-flex;align-items:center;gap:10px;position:relative;
 background:linear-gradient(135deg,var(--pv),var(--pv2));color:#fff!important;text-decoration:none!important;
 font-weight:700;font-size:1.04rem;padding:17px 36px;border-radius:12px;
 box-shadow:0 14px 30px -10px rgba(99,102,241,.55);transition:transform .22s ease,box-shadow .22s ease}
.pcta .pcta-btn::after{content:'\\2192';transition:transform .22s ease}
.pcta .pcta-btn:hover{transform:translateY(-2px);box-shadow:0 20px 40px -12px rgba(99,102,241,.7);color:#fff!important}
.pcta .pcta-btn:hover::after{transform:translateX(4px)}
.pcta .pcta-btn::before{content:'';position:absolute;inset:-3px;border-radius:15px;border:1px solid rgba(99,102,241,.5);
 opacity:0;animation:pctaPulse 3.2s ease-out infinite}
@keyframes pctaPulse{0%{opacity:.7;transform:scale(.97)}70%{opacity:0;transform:scale(1.07)}100%{opacity:0}}
.pcta .pcta-note{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:.74rem;letter-spacing:.05em;
 text-transform:uppercase;color:var(--pmut);margin:16px 0 0;opacity:.8}
@media(max-width:640px){.pcta{padding:52px 0}.pcta h2 .pcta-hl{white-space:normal}}
@media(prefers-reduced-motion:reduce){
 .pcta::before,.pcta::after,.pcta h2 .pcta-hl,.pcta .pcta-btn::before{animation:none}
 .pcta h2 .pcta-hl{background-position:0 0}}
</style>"""

COPY = {
 "vous": dict(
  h2='Vos concurrents sont cités par les IA.<br><span class="pcta-hl">Vous, vous êtes absent.</span>',
  lead='Prenez 30&nbsp;minutes&nbsp;: je vous sors <b>les 10 prompts</b> où vous n\'apparaissez pas, et <b>les 3 quick wins</b> pour y entrer.',
  btn='Réserver mes 30 minutes',
  note='Gratuit · sans engagement'),
 "tu": dict(
  h2='Tes concurrents sont cités par les IA.<br><span class="pcta-hl">Toi, tu es absent.</span>',
  lead='Prends 30&nbsp;minutes&nbsp;: je te sors <b>les 10 prompts</b> où tu n\'apparais pas, et <b>les 3 quick wins</b> pour y entrer.',
  btn='Réserver mes 30 minutes',
  note='Gratuit · sans engagement'),
}


def render(ton="vous", href=CALENDLY, with_css=True):
    c = COPY[ton]
    html = f"""<section class="pcta">
<div class="pcta-w">
<h2>{c['h2']}</h2>
<p class="pcta-lead">{c['lead']}</p>
<p class="pcta-cta"><a class="pcta-btn" href="{href}" rel="noopener">{c['btn']}</a></p>
<p class="pcta-note">{c['note']}</p>
</div>
</section>"""
    return (CSS + "\n" + html) if with_css else html
