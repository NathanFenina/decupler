# -*- coding: utf-8 -*-
"""Visuels animes, construits en CSS, partages par toutes les pages.

Cinq scenes de produit : la fiche Google qui se coche, le fil de
conversation, le devis relance jusqu'a la signature, les avis repondus, le
rapport mensuel chiffre. Aucune photo de stock : on montre la mecanique.
"""

VIZ = {
"trouve": """<div class="viz rise">
  <div class="viz-h"><strong>Dupont Paysage</strong><span class="tag">16/16</span></div>
  <div class="viz-row"><span class="viz-dot"></span>Catégories et services</div>
  <div class="viz-row"><span class="viz-dot"></span>Zones desservies</div>
  <div class="viz-row"><span class="viz-dot"></span>Photos et description</div>
  <div class="viz-row"><span class="viz-dot"></span>Horaires et coordonnées</div>
  <div class="viz-bar"><i></i></div>
</div>""",

"capte": """<div class="viz rise">
  <div class="viz-h"><strong>06 12 •• •• 41</strong><span class="tag">rattrapé</span></div>
  <div class="chat">
    <div class="bub them">Appel manqué à 14:32<span class="t">Vous étiez sur un chantier</span></div>
    <div class="bub you">Bonjour, ici Dupont Paysage. Je suis en intervention, je vous rappelle très vite.<span class="t">Envoyé automatiquement · 14:32</span></div>
    <div class="bub them">Parfait merci, c'est pour une haie à tailler<span class="t">14:38</span></div>
  </div>
</div>""",

"transforme": """<div class="viz rise">
  <div class="viz-h"><strong>Devis n° 2418 · 3 240 €</strong><span class="tag">signé</span></div>
  <div class="dev-line"><span class="dev-when">J+0</span><span class="dev-what">Devis envoyé</span><span class="dev-st wait">Sans réponse</span></div>
  <div class="dev-line"><span class="dev-when">J+3</span><span class="dev-what">Première relance</span><span class="dev-st sent">Automatique</span></div>
  <div class="dev-line"><span class="dev-when">J+7</span><span class="dev-what">Seconde relance</span><span class="dev-st sent">Automatique</span></div>
  <div class="dev-line"><span class="dev-when">J+8</span><span class="dev-what">Le client rappelle</span><span class="dev-st won">Chantier signé</span></div>
</div>""",

"capitalise": """<div class="viz rise">
  <div class="viz-h"><strong>Avis Google</strong><span class="tag">+4 ce mois-ci</span></div>
  <div class="rev"><span class="rev-st">★★★★★</span><span class="rev-tx">Travail soigné, délais tenus.</span><span class="rev-ok">Répondu</span></div>
  <div class="rev"><span class="rev-st">★★★★★</span><span class="rev-tx">Très bon contact, je recommande.</span><span class="rev-ok">Répondu</span></div>
  <div class="rev"><span class="rev-st">★★★★☆</span><span class="rev-tx">Bon travail, un peu de retard.</span><span class="rev-ok">Répondu</span></div>
  <div class="viz-bar"><i></i></div>
</div>""",

"pilote": """<div class="viz rise">
  <div class="viz-h"><strong>Votre mois</strong><span class="tag">rapport auto</span></div>
  <div class="rep-l"><span>Appels rattrapés</span><b>19</b></div>
  <div class="rep-l"><span>Devis relancés</span><b>12</b></div>
  <div class="rep-l"><span>Nouveaux avis</span><b>7</b></div>
  <div class="rep-l"><span>Rendez-vous pris</span><b>4</b></div>
</div>"""}

# Le module publicite n'avait pas de visuel : les cinq maquettes existantes
# couvrent les agents et le SEO, pas l'annonce locale. Celle-ci montre ce
# qu'un client voit quand il cherche — c'est le seul endroit ou le badge
# « Garanti par Google » des Local Services Ads se comprend sans explication.
VIZ['annonce'] = """
<div class="viz rise">
  <div class="viz-h"><strong>plombier à Nice</strong><span class="tag">annonce locale</span></div>
  <div class="lsa">
    <div class="lsa-l vous"><div class="lsa-t"><b>Votre entreprise</b><span class="lsa-g">Garanti par Google</span></div><span class="lsa-n">★ 4,9 · ouvert · rappelle sous 10 min</span></div>
    <div class="lsa-l"><div class="lsa-t"><b>Un concurrent</b></div><span class="lsa-n">★ 4,6 · ferme à 18 h</span></div>
    <div class="lsa-l"><div class="lsa-t"><b>Un autre</b></div><span class="lsa-n">★ 4,4 · fermé</span></div>
  </div>
</div>
"""


# ── Les trois visuels de données ─────────────────────────────────────────
# Les chiffres sont ILLUSTRATIFS et la page le dit : l'étiquette « exemple »
# est dans l'en-tête de chaque maquette, pas en astérisque. Une courbe de
# trafic sur la page d'une agence se lit comme un résultat obtenu ; sans le
# marquage, c'est une affirmation commerciale qu'on ne peut pas prouver.

VIZ['seo-courbe'] = """
<div class="viz rise">
  <div class="viz-h"><strong>Clics depuis Google</strong><span class="tag">exemple</span></div>
  <svg viewBox="0 0 320 118" class="cx" role="img" aria-label="Courbe d'exemple : les clics depuis Google passent de 40 à 380 par mois entre le premier et le sixième mois."><defs><linearGradient id="cxg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7B5CFA" stop-opacity=".26"/><stop offset="1" stop-color="#7B5CFA" stop-opacity="0"/></linearGradient></defs><line x1="10.0" y1="92.0" x2="310.0" y2="92.0" class="cx-b"/><path d="M 10.0 84.1 C 20.0 83.3 50.0 81.5 70.0 79.7 C 90.0 77.9 110.0 76.4 130.0 73.1 C 150.0 69.9 170.0 65.2 190.0 60.2 C 210.0 55.3 230.0 50.6 250.0 43.3 C 270.0 36.1 300.0 21.0 310.0 16.5 L 310.0 92.0 L 10.0 92.0 Z" fill="url(#cxg)"/><path d="M 10.0 84.1 C 20.0 83.3 50.0 81.5 70.0 79.7 C 90.0 77.9 110.0 76.4 130.0 73.1 C 150.0 69.9 170.0 65.2 190.0 60.2 C 210.0 55.3 230.0 50.6 250.0 43.3 C 270.0 36.1 300.0 21.0 310.0 16.5" class="cx-l"/><circle cx="310.0" cy="16.5" r="4.5" class="cx-p"/><text x="304.0" y="6.5" class="cx-v" text-anchor="end">380 clics</text><text x="10.0" y="116" class="cx-m">M1</text><text x="70.0" y="116" class="cx-m">M2</text><text x="130.0" y="116" class="cx-m">M3</text><text x="190.0" y="116" class="cx-m">M4</text><text x="250.0" y="116" class="cx-m">M5</text><text x="310.0" y="116" class="cx-m">M6</text></svg>
  <div class="viz-note">Six premiers mois. Le rapport arrive chaque mois, sans que vous le demandiez.</div>
</div>
"""

VIZ['agents-flow'] = """
<div class="viz rise">
  <div class="viz-h"><strong>Agent · appel manqué</strong><span class="tag">en continu</span></div>
  <ol class="flw">
    <li class="flw-e"><b>Appel manqué</b><span>14:32 · vous êtes en intervention</span></li>
    <li class="flw-a"><b>L'agent lit le numéro</b><span>Client connu ? Devis en cours ? Heure ouvrée ?</span></li>
    <li class="flw-a"><b>Il rédige et envoie le SMS</b><span>8 secondes après la sonnerie</span></li>
    <li class="flw-s"><b>Le client répond</b><span>Le rendez-vous part dans votre agenda</span></li>
  </ol>
</div>
"""

VIZ['ads-board'] = """
<div class="viz rise">
  <div class="viz-h"><strong>Vos annonces ce mois</strong><span class="tag">exemple</span></div>
  <div class="kpi">
    <div class="kpi-c"><span class="kpi-l">Leads</span><b class="kpi-v">34</b></div>
    <div class="kpi-c"><span class="kpi-l">Coût par lead</span><b class="kpi-v">18 €</b></div>
    <div class="kpi-c"><span class="kpi-l">Clics</span><b class="kpi-v">512</b></div>
    <div class="kpi-c"><span class="kpi-l">CPC moyen</span><b class="kpi-v">1,20 €</b></div>
  </div>
  <div class="lsa">
    <div class="lsa-l vous"><div class="lsa-t"><b>Votre entreprise</b><span class="lsa-g">Garanti par Google</span></div><span class="lsa-n">★ 4,9 · ouvert · rappelle sous 10 min</span></div>
    <div class="lsa-l"><div class="lsa-t"><b>Un concurrent</b></div><span class="lsa-n">★ 4,6 · ferme à 18 h</span></div>
  </div>
</div>
"""
