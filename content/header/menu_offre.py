# -*- coding: utf-8 -*-
"""Genere l'entree « Site offert » du menu, desktop et mobile, a partir du
catalogue d'agents. Le menu et la page pilier decrivent la meme chose : les
ecrire a la main deux fois, c'est garantir qu'ils divergeront."""
import sys
sys.path.insert(0, 'content/data')
import agents_locaux as A

LIENS = dict(A.LIENS)
PAR_SLUG = {s: (n, p) for s, n, _, p, _, _ in A.AGENTS}

# Libelles courts pour la colonne de gauche du second niveau : « Ne rater
# aucun appel » ne tient pas dans 160 px.
COURT = {'trouve': 'Être trouvé', 'capte': 'Capter', 'transforme': 'Transformer',
         'capitalise': 'Capitaliser', 'pilote': 'Piloter'}

# Descriptions courtes propres au menu. Tronquer la promesse du catalogue
# coupait au milieu d'un mot : « sur tous les critere… ».
DESC = {
 'fiche-google':       "Tous les champs que Google regarde",
 'posts-google':       "Une photo par SMS, le post part",
 'citations-locales':  "Vos coordonnées alignées partout",
 'seo-local':          "Sortir sur votre métier, dans votre ville",
 'mots-cles-locaux':   "Viser ce que vos clients tapent",
 'sms-appel-manque':   "Rattraper l'appel que vous ratez",
 'sms-formulaire':     "Le nom et le numéro, dans la minute",
 'chatbot':            "Le site répond à 21 h",
 'messagerie-google':  "La boîte que personne ne relève",
 'estimation-en-ligne': "Ne rappeler que des gens qui savent",
 'agent-vocal':        "Une voix décroche à votre place",
 'relance-devis':      "Le trou le plus cher, bouché",
 'rappel-rdv':         "Ne plus se déplacer pour rien",
 'relance-facture':    "Sans jouer le créancier",
 'reactivation':       "Le client que vous avez déjà",
 'demande-avis':       "Demander à tous, sans filtrer",
 'reponse-avis':       "Une réponse à chaque avis",
 'parrainage':         "Le canal qu'on oublie de demander",
 'satisfaction':       "Savoir avant que ce soit écrit",
 'rapport-mensuel':    "Ce qui a été rattrapé, compté",
}

METIERS = [
    ("Dentistes et cabinets", "/creation-site-internet-dentiste/", "Le site et les agents pour un cabinet dentaire"),
    ("Plombiers et dépannage", "/creation-site-internet-plombier/", "Ne plus rater un appel d'urgence"),
    ("Électriciens", "/creation-site-internet-electricien/", "Devis, relances et avis, automatisés"),
    ("Instituts et spas", "/creation-site-internet-institut-de-beaute/", "Agenda rempli, rendez-vous honorés"),
]

GUIDES = [
    ("Supprimer un avis Google", "/supprimer-un-avis-google/", "Les motifs que Google accepte, et le recours"),
    ("Standard téléphonique IA", "/standard-telephonique-ia/", "Le comparatif : IA, SVI, IPBX, permanence"),
    ("Chatbot WordPress", "/chatbot-wordpress/", "Les 5 façons de l'installer, comparées"),
    ("Répondre aux avis Google", "/repondre-aux-avis-google/", "La méthode en 4 temps et 6 exemples"),
    ("Obtenir des avis Google", "/obtenir-des-avis-google/", "Les messages qui marchent, et les interdits"),
]


def item(titre, href, desc=''):
    d = f'<span class="d-desc">{desc}</span>' if desc else ''
    return (f'\n                    <a href="{href}" class="d-item">'
            f'<div class="d-txt"><span class="d-title">{titre}</span>{d}</div></a>')


def desktop():
    # Onglet « Les agents » : cinq sous-onglets, un par etape du parcours,
    # exactement ceux de la page pilier.
    sous_nav, sous_tabs = '', ''
    for i, (cle, _, _) in enumerate(A.ETAPES):
        act = ' active' if i == 0 else ''
        sous_nav += (f'\n                    <div class="d-sub-item{act}" data-subtarget="sub-{cle}">'
                     f'<div class="d-sub-label">{COURT[cle]}</div>'
                     f'<span style="font-size:10px;opacity:0.4;">›</span></div>')
        liens = ''
        for slug, nom, _, promesse, _, _ in A.par_etape(cle):
            url = LIENS.get(slug)
            if not url:
                continue
            liens += item(nom, url, DESC.get(slug, ''))
        sous_tabs += (f'\n                  <div class="d-sub-tab{" d-active" if i == 0 else ""}" id="sub-{cle}">'
                      f'{liens}\n                  </div>')

    offre = item("Site internet offert", "/site-internet-offert/",
                 "Le site à 0 €, vous payez ce qui vous rapporte des clients")
    offre += ''.join(item(t, h, d) for t, h, d in METIERS)
    guides = ''.join(item(t, h, d) for t, h, d in GUIDES)

    return f'''        <!-- SITE OFFERT -->
        <li class="d-has-mega">
          <a href="/site-internet-offert/">Site offert <span class="d-arrow">⌵</span></a>
          <div class="d-mega-box d-senek-style">
            <div class="d-side-nav">
              <div class="d-side-item active" data-target="tab-offre">
                <div class="d-side-item-inner">
                  <div class="d-icon"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/><circle cx="6.5" cy="6.5" r=".6"/></svg></div>
                  L'offre
                </div>
              </div>
              <div class="d-side-item" data-target="tab-agents">
                <div class="d-side-item-inner">
                  <div class="d-icon"><svg viewBox="0 0 24 24"><rect x="4" y="7" width="16" height="12" rx="3"/><path d="M12 7V4"/><circle cx="12" cy="3" r="1"/><path d="M9 12v1.5M15 12v1.5"/></svg></div>
                  Les agents
                </div>
                <span class="d-side-chevron">›</span>
              </div>
              <div class="d-side-item" data-target="tab-guides">
                <div class="d-side-item-inner">
                  <div class="d-icon"><svg viewBox="0 0 24 24"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H19v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M8 7.5h7M8 11h5"/></svg></div>
                  Les guides
                </div>
              </div>
            </div>
            <div class="d-side-content">
              <!-- L'OFFRE -->
              <div class="d-tab-content d-active" id="tab-offre">{offre}
              </div>
              <!-- LES AGENTS -->
              <div class="d-tab-content d-tab-2n" id="tab-agents">
                <div class="d-sub-nav d-sub-nav-large">{sous_nav}
                </div>
                <div class="d-sub-content">{sous_tabs}
                </div>
              </div>
              <!-- LES GUIDES -->
              <div class="d-tab-content" id="tab-guides">{guides}
              </div>
            </div>
          </div>
        </li>
'''


def mobile():
    blocs = ''
    for cle, titre, _ in A.ETAPES:
        liens = ''.join(
            f'\n                <li><a href="{LIENS[s]}">{n}</a></li>'
            for s, n, _, _, _, _ in A.par_etape(cle) if s in LIENS)
        blocs += f'''            <li class="d-mobile-has-sub2">
              <div class="d-mobile-link2">{titre} <span class="d-mobile-arrow2">⌵</span></div>
              <ul class="d-mobile-sub2">{liens}
              </ul>
            </li>
'''
    metiers = ''.join(f'\n                <li><a href="{h}">{t}</a></li>' for t, h, _ in METIERS)
    guides = ''.join(f'\n                <li><a href="{h}">{t}</a></li>' for t, h, _ in GUIDES)
    return f'''        <li class="d-mobile-has-sub">
          <div class="d-mobile-link">Site offert <span class="d-mobile-arrow">⌵</span></div>
          <ul class="d-mobile-sub">
            <li><a href="/site-internet-offert/"><strong>L'offre site offert</strong></a></li>
            <li class="d-mobile-has-sub2">
              <div class="d-mobile-link2">Par métier <span class="d-mobile-arrow2">⌵</span></div>
              <ul class="d-mobile-sub2">{metiers}
              </ul>
            </li>
{blocs}            <li class="d-mobile-has-sub2">
              <div class="d-mobile-link2">Les guides <span class="d-mobile-arrow2">⌵</span></div>
              <ul class="d-mobile-sub2">{guides}
              </ul>
            </li>
          </ul>
        </li>
'''


if __name__ == '__main__':
    open('/tmp/menu_desktop.html', 'w', encoding='utf-8').write(desktop())
    open('/tmp/menu_mobile.html', 'w', encoding='utf-8').write(mobile())
    print('desktop', len(desktop()), 'octets · mobile', len(mobile()), 'octets')
