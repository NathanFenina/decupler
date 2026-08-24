# -*- coding: utf-8 -*-
"""Genere l'onglet « Site offert » du menu Expertises, desktop et mobile.

L'entree vit dans le mega menu « Expertises », en sixieme colonne. Le
contenu est genere depuis content/data/agents_locaux.py plutot qu'ecrit a
la main : le menu et la page pilier decrivent la meme offre, et deux
sources qu'on tient a la main finissent toujours par diverger.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RACINE / 'content/data'))
import agents_locaux as A   # noqa: E402

PILIER = ("Site internet offert", "/site-internet-offert/",
          "Le site à 0 €, vous payez ce qui vous rapporte des clients")

METIERS = [
    ("Dentistes et cabinets", "/creation-site-internet-dentiste/",
     "Le site et les agents pour un cabinet dentaire"),
    ("Plombiers et dépannage", "/creation-site-internet-plombier/",
     "Ne plus rater un appel d'urgence"),
    ("Électriciens", "/creation-site-internet-electricien/",
     "Devis, relances et avis, automatisés"),
    ("Instituts et spas", "/creation-site-internet-institut-de-beaute/",
     "Agenda rempli, rendez-vous honorés"),
]

# Les deux pages du cluster qui ont du volume de recherche. Un lien depuis le
# menu leur donne un lien interne sur tout le site : c'est la seule raison de
# les faire figurer ici plutot que de les laisser au maillage du pilier.
GUIDES = [
    ("Supprimer un avis Google", "/supprimer-un-avis-google/",
     "Les motifs que Google accepte, et le recours"),
    ("Agent vocal IA", "/agent-vocal-ia/",
     "Une voix décroche quand vous ne pouvez pas"),
]

TOUT = [PILIER] + METIERS + GUIDES


def item(titre, href, desc='', indent=16):
    b = ' ' * indent
    d = f'<span class="d-desc">{desc}</span>' if desc else ''
    return (f'\n{b}<a href="{href}" class="d-item">'
            f'<div class="d-txt"><span class="d-title">{titre}</span>{d}</div></a>')


def colonne_desktop():
    """La sixieme entree de la colonne de gauche du mega menu Expertises."""
    return '''              <div class="d-side-item" data-target="tab-offre">
                <div class="d-side-item-inner">
                  <div class="d-icon"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/><circle cx="6.5" cy="6.5" r=".6"/></svg></div>
                  Site offert
                </div>
              </div>
'''


def onglet_desktop():
    return ('''              <!-- SITE OFFERT -->
              <div class="d-tab-content" id="tab-offre">'''
            + ''.join(item(t, h, d) for t, h, d in TOUT)
            + '\n              </div>\n')


def bloc_mobile():
    liens = ''.join(f'\n                <li><a href="{h}">{t}</a></li>' for t, h, _ in TOUT)
    return f'''            <li class="d-mobile-has-sub2">
              <div class="d-mobile-link2">Site offert <span class="d-mobile-arrow2">⌵</span></div>
              <ul class="d-mobile-sub2">{liens}
              </ul>
            </li>
'''


if __name__ == '__main__':
    for nom, contenu in (('colonne', colonne_desktop()), ('onglet', onglet_desktop()),
                         ('mobile', bloc_mobile())):
        Path(f'/tmp/menu_{nom}.html').write_text(contenu, encoding='utf-8')
        print(f'{nom:<8} {len(contenu):>5} octets')
