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
