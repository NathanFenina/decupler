# -*- coding: utf-8 -*-
"""Genere les deux colonnes « Site offert » et « Agents IA » du footer.

Pourquoi ce fichier existe. Au 28/08/2026, l'inspection GSC des 25 pages du
cluster donne 22 « Detectee, actuellement non indexee » et 3 « Google ne
reconnait pas cette URL » — zero indexee. Le sitemap les contient toutes et a
ete resoumis. La cause est ailleurs : l'accueil, /agence-seo/, /agence-geo/ et
/visibilite-en-ligne/ ne pointent vers AUCUNE des 25 pages, et le footer
sitewide (48 liens, 8 colonnes) non plus. Le cluster est une ile : ses pages se
lient entre elles et rien d'etabli ne pointe vers elles.

Un lien depuis le footer est present sur chaque page deja exploree du site.
C'est le seul levier d'indexation reellement actionnable — le bouton
« Demander l'indexation » de la Search Console n'a pas d'API publique, et
l'Indexing API ne couvre officiellement que JobPosting et BroadcastEvent.

    python3 content/footer/colonnes_offre.py            # ecrit le HTML
    python3 content/footer/colonnes_offre.py --verifier # + controle les 200

Le HTML se colle dans le widget HTML `footer-seo-ia` du template Elementor 2788,
apres la colonne « Villes ».

Les URLs sont ecrites en clair, pas derivees de agents_locaux : la liste
AGENTS y contient des slugs internes (`demande-avis`, `chatbot`, `agent-vocal`)
qui ne sont pas les slugs publies (`obtenir-des-avis-google`,
`chatbot-wordpress`, `agent-vocal-ia`). Un footer sitewide qui pointe vers une
404 est pire que pas de footer du tout, donc on ne devine pas : on liste, et
--verifier controle.
"""
import sys
import urllib.request

OFFRE = [
    ("Site internet offert", "/site-internet-offert/"),
    ("Site pour dentiste", "/creation-site-internet-dentiste/"),
    ("Site pour plombier", "/creation-site-internet-plombier/"),
    ("Site pour électricien", "/creation-site-internet-electricien/"),
    ("Site pour institut de beauté", "/creation-site-internet-institut-de-beaute/"),
    ("Supprimer un avis Google", "/supprimer-un-avis-google/"),
    ("Répondre aux avis Google", "/repondre-aux-avis-google/"),
    ("Obtenir des avis Google", "/obtenir-des-avis-google/"),
]

AGENTS = [
    ("Agent vocal IA", "/agent-vocal-ia/"),
    ("Standard téléphonique IA", "/standard-telephonique-ia/"),
    ("Chatbot WordPress", "/chatbot-wordpress/"),
    ("Agent fiche Google", "/agent-fiche-google/"),
    ("Agent posts Google", "/agent-posts-google/"),
    ("Agent mots-clés locaux", "/agent-mots-cles-locaux/"),
    ("Agent SMS appel manqué", "/agent-sms-appel-manque/"),
    ("Agent SMS formulaire", "/agent-sms-formulaire/"),
    ("Agent relance de devis", "/agent-relance-devis/"),
    ("Agent rappel de RDV", "/agent-rappel-rdv/"),
    ("Agent de réactivation", "/agent-reactivation/"),
    ("Agent satisfaction", "/agent-satisfaction/"),
    ("Agent rapport mensuel", "/agent-rapport-mensuel/"),
    ("Agent relance de facture", "/agent-relance-facture/"),
    ("Agent messagerie Google", "/agent-messagerie-google/"),
    ("Agent parrainage", "/agent-parrainage/"),
    ("Agent estimation en ligne", "/agent-estimation-en-ligne/"),
]

BASE = "https://decupler.com"


def colonne(titre, liens):
    items = "\n".join(
        f'          <li><a href="{BASE}{href}">{nom}</a></li>'
        for nom, href in liens)
    return (f'      <div class="footer-nav-column">\n'
            f'        <h4>{titre}</h4>\n'
            f'        <ul class="footer-nav-list">\n{items}\n'
            f'        </ul>\n'
            f'      </div>')


def verifier(liens):
    """Aucun lien sitewide ne part sans que son code HTTP soit connu."""
    ko = []
    for nom, href in liens:
        req = urllib.request.Request(BASE + href, method="HEAD",
                                     headers={"User-Agent": "decupler-check"})
        try:
            code = urllib.request.urlopen(req, timeout=20).status
        except Exception as e:                       # noqa: BLE001
            code = getattr(e, "code", str(e))
        etat = "ok" if code == 200 else "ECHEC"
        print(f"  {etat:<6} {code}  {href}", file=sys.stderr)
        if code != 200:
            ko.append(href)
    if ko:
        sys.exit(f"\n{len(ko)} URL(s) ne repondent pas 200 : {', '.join(ko)}")
    print(f"\n  {len(liens)} URLs verifiees, toutes en 200.", file=sys.stderr)


if __name__ == "__main__":
    tout = OFFRE + AGENTS
    if "--verifier" in sys.argv:
        verifier(tout)
    print(colonne("Site offert", OFFRE))
    print(colonne("Agents IA", AGENTS))
    print(f"\n{len(tout)} liens ({len(OFFRE)} offre + {len(AGENTS)} agents)",
          file=sys.stderr)
