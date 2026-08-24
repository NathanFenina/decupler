# -*- coding: utf-8 -*-
"""Petites icônes au trait, en SVG inline.

Un seul dessin par idée, partagé entre la page offre et les futures pages
agent. Tout est en `currentColor` : la couleur vient du CSS, jamais du SVG.

Contraintes WordPress :
  · chaque SVG tient sur UNE ligne — wpautop coupe sur les lignes vides ;
  · on l'enveloppe toujours dans un bloc (`<div>`), jamais posé nu à côté
    d'un `<h4>` : un enfant inline au milieu d'enfants block fait injecter
    un `</p>` orphelin (voir wpcss.audit_markup).
"""

_O = ('<svg class="ic-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
      'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" '
      'aria-hidden="true" focusable="false">')

_D = {
 # ── Être trouvé ──────────────────────────────────────────────────────────
 "fiche-google":     '<path d="M12 21s7-5.3 7-11a7 7 0 1 0-14 0c0 5.7 7 11 7 11Z"/><path d="m9 10 2 2 4-4"/>',
 "posts-google":     '<rect x="3" y="5" width="18" height="14" rx="2.5"/><circle cx="8.5" cy="10" r="1.6"/><path d="m4 17 4.5-4.2a2 2 0 0 1 2.7 0L20 20"/>',
 "citations-locales":  '<path d="M9 20s5-3.8 5-8a5 5 0 1 0-10 0c0 4.2 5 8 5 8Z"/><circle cx="9" cy="12" r="1.7"/><path d="M15.5 5.5h5M15.5 9h5M15.5 12.5h3"/>',
 "seo-local":         '<path d="M12 21s6.5-5 6.5-10.5a6.5 6.5 0 1 0-13 0C5.5 16 12 21 12 21Z"/><path d="M9.6 11.2h4.8M12 8.8v4.8"/>',
 "mots-cles-locaux": '<circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/><path d="M8.5 11h5"/>',
 # ── Ne rater aucun appel ─────────────────────────────────────────────────
 "sms-appel-manque": '<path d="M5 4h3l1.6 4-2 1.4a12 12 0 0 0 5.6 5.6l1.4-2 4 1.6v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 3 6.2 2 2 0 0 1 5 4Z"/><path d="M15.5 3.5 21 9"/><path d="M21 3.5 15.5 9"/>',
 "sms-formulaire":   '<rect x="4" y="3" width="13" height="18" rx="2"/><path d="M8 8h5M8 12h5M8 16h3"/><path d="M17 14h4m-2-2 2 2-2 2"/>',
 "chatbot":          '<path d="M20 15a3 3 0 0 1-3 3H9l-4 3v-3.5A3 3 0 0 1 4 15V7a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3Z"/><circle cx="9" cy="11" r=".9" fill="currentColor" stroke="none"/><circle cx="12.5" cy="11" r=".9" fill="currentColor" stroke="none"/><circle cx="16" cy="11" r=".9" fill="currentColor" stroke="none"/>',
 "agent-vocal":      '<rect x="9" y="2.5" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0"/><path d="M12 17.5V21"/><path d="M9 21h6"/>',
 # ── Transformer ──────────────────────────────────────────────────────────
 "relance-devis":    '<path d="M6 3h8l4 4v9a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2Z"/><path d="M14 3v4h4"/><path d="M8 20.5a5 5 0 0 0 8.5-2"/><path d="M6.5 17.5 8 20.5l3-1"/>',
 "rappel-rdv":       '<rect x="3" y="5" width="18" height="16" rx="2.5"/><path d="M3 10h18M8 3v4M16 3v4"/><circle cx="12" cy="15" r="3"/><path d="M12 13.6V15l1 .8"/>',
 "reactivation":     '<path d="M20 12a8 8 0 1 1-2.6-5.9"/><path d="M20 4v4h-4"/><path d="M12 8.5v4l2.5 1.6"/>',
 # ── Capitaliser ──────────────────────────────────────────────────────────
 "demande-avis":     '<path d="m12 3.5 2.6 5.4 5.9.8-4.3 4.1 1.1 5.9L12 16.9 6.7 19.7l1.1-5.9L3.5 9.7l5.9-.8Z"/>',
 "reponse-avis":     '<path d="M20 14a3 3 0 0 1-3 3H9.5L5 20v-3.2A3 3 0 0 1 4 14V7a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3Z"/><path d="m12 7.2 1.2 2.4 2.6.4-1.9 1.8.5 2.6-2.4-1.3-2.4 1.3.5-2.6-1.9-1.8 2.6-.4Z"/>',
 "satisfaction":     '<circle cx="12" cy="12" r="8.5"/><path d="M8.5 14a4.5 4.5 0 0 0 7 0"/><path d="M9 9.5h.01M15 9.5h.01"/>',
 # ── Piloter ──────────────────────────────────────────────────────────────
 "rapport-mensuel":  '<path d="M4 20V4"/><path d="M4 20h16"/><rect x="7" y="12" width="3" height="5" rx="1"/><rect x="12" y="8" width="3" height="9" rx="1"/><rect x="17" y="5" width="3" height="12" rx="1"/>',
 # ── Étapes (repris d'un agent représentatif) ─────────────────────────────
 "trouve":           '<path d="M12 21s7-5.3 7-11a7 7 0 1 0-14 0c0 5.7 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/>',
 "capte":            '<path d="M5 4h3l1.6 4-2 1.4a12 12 0 0 0 5.6 5.6l1.4-2 4 1.6v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 3 6.2 2 2 0 0 1 5 4Z"/>',
 "transforme":       '<path d="M4 17 10 11l3.5 3.5L20 8"/><path d="M15 8h5v5"/>',
 "capitalise":       '<path d="m12 3.5 2.6 5.4 5.9.8-4.3 4.1 1.1 5.9L12 16.9 6.7 19.7l1.1-5.9L3.5 9.7l5.9-.8Z"/>',
 "pilote":           '<path d="M4 20V4"/><path d="M4 20h16"/><path d="m7 15 4-4 3 3 5-6"/><path d="M15 8h4v4"/>',
 # ── Métiers ──────────────────────────────────────────────────────────────
 "paysagiste":       '<path d="M12 21v-7"/><path d="M12 14c0-4 3-7 8-7 0 5-3.5 7-8 7Z"/><path d="M12 17c0-3-2.2-5-6-5 0 3.6 2.6 5 6 5Z"/>',
 "artisan":          '<path d="M14.7 6.3a4 4 0 0 0 5.2 5.2l-8.4 8.4a2.4 2.4 0 0 1-3.4-3.4Z"/><path d="M6.5 3.5 9 6 7 8 4.5 5.5a2 2 0 0 1 2-2Z"/>',
 "dentiste":         '<path d="M7.5 3.5C5.6 3.5 4 5.2 4 7.5c0 3 .9 4.4 1.4 7.2.4 2.4.6 5.3 2.1 5.3 1.7 0 1.5-4.4 4.5-4.4s2.8 4.4 4.5 4.4c1.5 0 1.7-2.9 2.1-5.3.5-2.8 1.4-4.2 1.4-7.2 0-2.3-1.6-4-3.5-4-1.9 0-2.6 1-4.5 1s-2.6-1-4.5-1Z"/>',
 "spa":              '<path d="M12 13c0-4 2.6-7.5 6-9 .8 4.6-1.4 8.2-6 9Z"/><path d="M12 13C12 9 9.4 5.5 6 4c-.8 4.6 1.4 8.2 6 9Z"/><path d="M4.5 15.5c2.5 0 2.5 2 5 2s2.5-2 5-2 2.5 2 5 2"/>',
 "immobilier":       '<path d="m3.5 10.5 8.5-7 8.5 7"/><path d="M6 9.5V20h12V9.5"/><path d="M10 20v-5.5h4V20"/>',
 "maison-hote":      '<path d="M3 18v-4a2 2 0 0 1 2-2h11a3 3 0 0 1 3 3v3"/><path d="M3 18h18"/><path d="M3 12V7"/><circle cx="8" cy="9" r="1.8"/>',
}


def ic(cle: str) -> str:
    """Le SVG d'une clé, sur une seule ligne. Clé inconnue : chaîne vide."""
    d = _D.get(cle)
    return f'{_O}{d}</svg>' if d else ''


def bloc(cle: str, classe: str = 'ic') -> str:
    """Le SVG enveloppé dans un bloc, prêt à cohabiter avec des <h4>/<p>."""
    return f'<div class="{classe}">{ic(cle)}</div>' if _D.get(cle) else ''
