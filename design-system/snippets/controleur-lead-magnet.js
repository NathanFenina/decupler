/* Contrôleur des pop-ups lead magnet (decupler.com)
 *
 * Posé une fois dans l'en-tête du site (template Elementor 2762), il agit sur
 * toutes les pages dont la pop-up email suit la structure #ai-content-gate
 * (build_article.py et anciennes pages Elementor).
 *
 * - Lien de campagne (?acces=linkedin) : rien ne change, la pop-up reste
 *   obligatoire (flou, défilement bloqué, pas de fermeture).
 * - Tous les autres visiteurs (Google compris) : la pop-up n'apparaît qu'à
 *   25 s, sans flou ni blocage, avec une croix et « Continuer sans email »,
 *   une fois par session. Google pénalise sur mobile les interstitiels qui
 *   masquent le contenu d'une page ouverte depuis la recherche.
 *
 * Les pages déjà construites avec --gate-param gèrent cela elles-mêmes : le
 * contrôleur les reconnaît (croix déjà présente) et ne fait rien.
 */
(function () {
  var PARAM = 'acces', VALEUR = 'linkedin', DOUX_MS = 25000;
  function lance() {
    var p = document.getElementById('ai-content-gate');
    if (!p) return;
    // Correctifs d'affichage pour toutes les variantes, campagne comprise :
    // carte qui déborde sur mobile (box-sizing), titre blanc sur les pages sombres.
    var base = document.createElement('style');
    base.textContent = '#ai-content-gate,#ai-content-gate *{box-sizing:border-box}#ai-content-gate .ai-popup-card{max-width:min(460px,100%)}#ai-content-gate .ai-popup-title{color:#1e293b!important;-webkit-text-fill-color:#1e293b!important;background:none!important}#ai-content-gate .ai-popup-desc{color:#475569!important;-webkit-text-fill-color:#475569!important}';
    document.head.appendChild(base);
    try {
      if (new URLSearchParams(location.search).get(PARAM) === VALEUR) return;
    } catch (e) { return; }
    var debut = Date.now(), ferme = false, doux = false;
    try { ferme = !!sessionStorage.getItem('lmg_ferme'); } catch (e) {}
    function libere() {
      document.body.classList.remove('lmg-gated');
      document.body.style.overflow = '';
      document.documentElement.style.overflow = '';
    }
    function fermer() {
      p.classList.remove('active'); libere(); ferme = true;
      try { sessionStorage.setItem('lmg_ferme', '1'); } catch (e) {}
    }
    function adoucit() {
      if (doux) return; doux = true;
      var st = document.createElement('style'); st.textContent = '#ai-content-gate.ai-soft{backdrop-filter:none;-webkit-backdrop-filter:none;background:rgba(15,23,42,.45)}#ai-content-gate .ai-popup-card{position:relative}#ai-content-gate .ai-popup-close{position:absolute;top:10px;right:12px;width:36px;height:36px;margin:0;padding:0;min-width:0;border:0;border-radius:50%;background:none;box-shadow:none;color:#64748b;font-size:1.5rem;line-height:1;display:flex;align-items:center;justify-content:center;cursor:pointer}#ai-content-gate .ai-popup-close:hover{background:#f1f5f9;color:#1e293b}#ai-content-gate .ai-popup-skip{display:inline-block;margin:.9rem 0 0;padding:4px 6px;min-width:0;background:none;border:0;box-shadow:none;color:#475569;font-size:.88rem;text-decoration:underline;text-underline-offset:3px;cursor:pointer}'; document.head.appendChild(st);
      p.classList.add('ai-soft');
      var c = p.querySelector('.ai-popup-card'); if (!c) return;
      var t = c.querySelector('.ai-popup-title'), d = c.querySelector('.ai-popup-desc'), b = c.querySelector('.ai-popup-submit, button[type=submit]');
      if (t) t.textContent = 'Tu veux les prochains guides ?';
      if (d) d.textContent = 'Laisse ton email : je t’envoie les prochains playbooks dès leur sortie.';
      if (b) b.textContent = 'Je m’abonne (gratuit) →';
      var x = document.createElement('button'); x.type = 'button'; x.className = 'ai-popup-close'; x.setAttribute('aria-label', 'Fermer'); x.textContent = '×';
      var n = document.createElement('button'); n.type = 'button'; n.className = 'ai-popup-skip'; n.textContent = 'Continuer sans email';
      x.onclick = fermer; n.onclick = fermer; c.insertBefore(x, c.firstChild); c.appendChild(n);
      p.addEventListener('click', function (e) { if (e.target === p) fermer(); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && p.classList.contains('active')) fermer(); });
    }
    function surveille() {
      if (!p.classList.contains('active')) return;
      if (doux) return;                                        // déjà pris en charge
      if (p.querySelector('.ai-popup-close')) return;          // page déjà en mode campagne
      // Appelé après le script de la page : la pop-up vient d'être ouverte
      // en mode obligatoire. On la retire et on la reprogramme en mode doux.
      p.classList.remove('active'); libere();
      if (ferme) return;
      var reste = Math.max(0, DOUX_MS - (Date.now() - debut));
      setTimeout(function () { if (!ferme) { adoucit(); p.classList.add('active'); libere(); } }, reste);
    }
    new MutationObserver(surveille).observe(p, { attributes: true, attributeFilter: ['class'] });
    surveille();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', lance); else lance();
})();
