<?php
/**
 * Plugin Name:       Décupler — Pop-up
 * Description:       Une invitation (webinaire, workshop, offre) affichée une fois par visiteur, après un délai, sur tout le site. Fenêtre au centre sur ordinateur, bandeau en bas sur mobile. S'efface toute seule à la date de fin, et ne double jamais la pop-up des pages lead magnet.
 * Version:           1.0.0
 * Author:            Décupler
 * License:           GPL-2.0-or-later
 * Requires at least: 6.0
 * Requires PHP:      7.4
 *
 * POURQUOI CES CHOIX
 *
 * - Rien dans le HTML de la page : la configuration part dans un bloc JSON,
 *   et la fenêtre n'est construite qu'au moment de l'afficher. Le texte de
 *   l'invitation ne se répète donc pas sur les 160 pages du site aux yeux de
 *   Google, et la page ne pèse que ~3 Ko de plus.
 * - Sur mobile, un bandeau en bas plutôt qu'une fenêtre qui masque la page :
 *   Google déclasse les interstitiels intrusifs sur mobile.
 * - Une fois par visiteur : fermée, elle ne revient pas avant 7 jours ;
 *   cliquée, elle ne revient plus pour cette campagne.
 * - Les pages lead magnet ont déjà leur pop-up (#ai-content-gate) : si elle
 *   est présente, celle-ci ne s'affiche pas.
 * - La date de fin coupe tout, côté serveur ET côté navigateur (une page mise
 *   en cache avant la date ne l'affiche pas après).
 * - Tout se règle dans Réglages → Pop-up Décupler, ou par l'API REST
 *   (/wp/v2/settings, clé dcp_popup) : changer de campagne ne demande pas de
 *   nouvelle version du plugin.
 *
 * Tester : ajouter ?dcp_popup=1 à une URL (affichage après 0,5 s, même si
 * déjà fermée). ?dcp_popup=0 la bloque sur la page.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

const DCP_POPUP_VERSION = '1.0.0';

/** Réglages par défaut : le workshop live du 8 octobre 2026. */
function dcp_popup_defauts() {
	return array(
		'actif'         => true,
		'campagne'      => 'workshop-2026-10-08',
		'surtitre'      => '',
		'titre'         => '10× plus de contenu SEO, zéro abonnement en plus, le tout avec Claude Code',
		'texte'         => 'Audit GEO, monitoring de prompts IA, création de contenu, intégrations et mon système de prospection LinkedIn : je te montre tout en direct. Du concret à rejouer le lendemain, questions bienvenues.',
		'mention'       => 'Gratuit · pas de replay · 100 places maximum',
		'bouton'        => 'Je réserve ma place',
		'lien'          => 'https://www.linkedin.com/events/7508143909210910720',
		'image'         => 'https://decupler.com/wp-content/uploads/2026/09/workshop-claude-code-machine-seo-8-octobre.jpg',
		'mobile_titre'  => 'Workshop Claude Code, 8 oct. à 12 h 30',
		'mobile_bouton' => 'Réserver',
		'fin'           => '2026-10-08T12:30:00+02:00',
		'delai'         => 15,
		'exclusions'    => array(
			'geo-ready', 'newsletter', 'mentions-legales', 'politique-de-confidentialite',
			'cgv', 'panier', 'commander', 'mon-compte',
		),
	);
}

/** Réglages effectifs : l'option enregistrée, complétée par les défauts. */
function dcp_popup_reglages() {
	$r = get_option( 'dcp_popup', array() );
	return wp_parse_args( is_array( $r ) ? $r : array(), dcp_popup_defauts() );
}

/** Nettoie ce qui arrive du formulaire ou de l'API. */
function dcp_popup_nettoie( $in ) {
	$d   = dcp_popup_defauts();
	$in  = is_array( $in ) ? $in : array();
	$out = dcp_popup_reglages();
	foreach ( array( 'surtitre', 'titre', 'mention', 'bouton', 'mobile_titre', 'mobile_bouton' ) as $k ) {
		if ( isset( $in[ $k ] ) ) {
			$out[ $k ] = sanitize_text_field( $in[ $k ] );
		}
	}
	if ( isset( $in['texte'] ) ) {
		$out['texte'] = wp_kses( $in['texte'], array( 'strong' => array(), 'em' => array(), 'br' => array() ) );
	}
	if ( isset( $in['campagne'] ) ) {
		$out['campagne'] = sanitize_key( $in['campagne'] ) ?: $d['campagne'];
	}
	foreach ( array( 'lien', 'image' ) as $k ) {
		if ( isset( $in[ $k ] ) ) {
			$out[ $k ] = esc_url_raw( trim( $in[ $k ] ) );
		}
	}
	if ( isset( $in['fin'] ) ) {
		$t          = strtotime( $in['fin'] );
		$out['fin'] = $t ? wp_date( 'c', $t ) : '';
	}
	if ( isset( $in['delai'] ) ) {
		$out['delai'] = min( 120, max( 3, absint( $in['delai'] ) ) );
	}
	if ( isset( $in['exclusions'] ) ) {
		$liste = is_array( $in['exclusions'] ) ? $in['exclusions'] : preg_split( '/[\s,]+/', (string) $in['exclusions'] );
		$out['exclusions'] = array_values( array_filter( array_map(
			function ( $s ) {
				return trim( sanitize_text_field( $s ), '/ ' );
			},
			$liste
		) ) );
	}
	if ( array_key_exists( 'actif', $in ) ) {
		$out['actif'] = (bool) $in['actif'];
	}
	return $out;
}

add_action(
	'init',
	function () {
		$chaine = array( 'type' => 'string' );
		register_setting(
			'dcp_popup',
			'dcp_popup',
			array(
				'type'              => 'object',
				'default'           => dcp_popup_defauts(),
				'sanitize_callback' => 'dcp_popup_nettoie',
				'show_in_rest'      => array(
					'schema' => array(
						'type'       => 'object',
						'properties' => array(
							'actif'         => array( 'type' => 'boolean' ),
							'campagne'      => $chaine,
							'surtitre'      => $chaine,
							'titre'         => $chaine,
							'texte'         => $chaine,
							'mention'       => $chaine,
							'bouton'        => $chaine,
							'lien'          => $chaine,
							'image'         => $chaine,
							'mobile_titre'  => $chaine,
							'mobile_bouton' => $chaine,
							'fin'           => $chaine,
							'delai'         => array( 'type' => 'integer' ),
							'exclusions'    => array(
								'type'  => 'array',
								'items' => $chaine,
							),
						),
					),
				),
			)
		);
	}
);

/** La pop-up doit-elle être proposée sur la page courante ? */
function dcp_popup_eligible() {
	if ( is_admin() || wp_doing_ajax() || is_feed() || is_embed() || is_404() || is_customize_preview() ) {
		return false;
	}
	$r = dcp_popup_reglages();
	if ( empty( $r['actif'] ) || empty( $r['lien'] ) ) {
		return false;
	}
	if ( ! empty( $r['fin'] ) && strtotime( $r['fin'] ) <= time() ) {
		return false;
	}
	$chemin = trim( (string) wp_parse_url( $_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH ), '/' );
	return ! in_array( rawurldecode( $chemin ), (array) $r['exclusions'], true );
}

add_action(
	'wp_footer',
	function () {
		if ( ! dcp_popup_eligible() ) {
			return;
		}
		$r   = dcp_popup_reglages();
		$cfg = array(
			'campagne'     => $r['campagne'],
			'surtitre'     => $r['surtitre'],
			'titre'        => $r['titre'],
			'texte'        => $r['texte'],
			'mention'      => $r['mention'],
			'bouton'       => $r['bouton'],
			'lien'         => $r['lien'],
			'image'        => $r['image'],
			'mobileTitre'  => $r['mobile_titre'],
			'mobileBouton' => $r['mobile_bouton'],
			'fin'          => $r['fin'],
			'delai'        => (int) $r['delai'],
		);
		echo "\n<script type=\"application/json\" id=\"dcp-popup-cfg\">"
			. wp_json_encode( $cfg, JSON_HEX_TAG | JSON_HEX_AMP | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES )
			. "</script>\n<script id=\"dcp-popup-js\">" . dcp_popup_js() . "</script>\n";
	},
	50
);

/** Le script : construit la fenêtre au moment de l'afficher, pas avant. */
function dcp_popup_js() {
	return <<<'JS'
(function(){
var el=document.getElementById('dcp-popup-cfg');if(!el)return;
var c;try{c=JSON.parse(el.textContent)}catch(e){return}
var q=location.search,force=/[?&]dcp_popup=1\b/.test(q);
if(/[?&]dcp_popup=0\b/.test(q))return;
if(c.fin&&Date.now()>=Date.parse(c.fin))return;
var K='dcp_popup_'+c.campagne;
function lire(){try{return JSON.parse(localStorage.getItem(K)||'null')}catch(e){return null}}
function ecrire(v){try{localStorage.setItem(K,JSON.stringify(v))}catch(e){}}
var s=lire();
if(!force&&s&&(s.clic||(s.ferme&&Date.now()-s.ferme<7*864e5)))return;
var CSS='#dcp-pop,#dcp-pop *{box-sizing:border-box}'
+'#dcp-pop{position:fixed;inset:0;z-index:2147483000;display:flex;align-items:center;justify-content:center;padding:16px;background:rgba(15,14,40,.55);font-family:"DM Sans",system-ui,-apple-system,"Segoe UI",sans-serif;animation:dcpIn .22s ease-out}'
+'#dcp-pop .dcp-c{position:relative;width:100%;max-width:520px;max-height:calc(100vh - 32px);overflow:auto;background:#fff;color:#1a1a2e;border-radius:18px;box-shadow:0 24px 64px rgba(20,16,70,.35)}'
+'#dcp-pop .dcp-img{display:block;width:100%;height:auto;border-radius:18px 18px 0 0}'
+'#dcp-pop .dcp-b{padding:26px 28px 24px}'
+'#dcp-pop .dcp-sur{display:inline-block;margin:0 0 12px;padding:5px 11px;border-radius:999px;background:#ece9f8;color:#4c47c9;font-size:12.5px;font-weight:700;letter-spacing:.02em}'
+'#dcp-pop .dcp-t{margin:0 0 10px;font-size:22px;line-height:1.25;font-weight:800;color:#1a1a2e;text-wrap:balance}'
+'#dcp-pop .dcp-x{margin:0 0 12px;font-size:15px;line-height:1.55;color:#4a4a6a}'
+'#dcp-pop .dcp-m{margin:0 0 18px;font-size:13px;font-weight:600;color:#666687}'
+'#dcp-pop .dcp-go{box-sizing:border-box;display:flex;align-items:center;justify-content:center;width:100%;padding:13px 20px;border-radius:12px;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff!important;font-size:16px;font-weight:700;text-decoration:none!important;transition:transform .15s,box-shadow .15s}'
+'#dcp-pop .dcp-go:hover{transform:translateY(-1px);box-shadow:0 8px 22px rgba(79,70,229,.35)}'
+'#dcp-pop .dcp-no{display:block;margin:12px auto 0;padding:4px 6px;background:none;border:0;color:#666687;font:inherit;font-size:13px;text-decoration:underline;cursor:pointer}'
+'#dcp-pop button{margin:0;min-width:0;min-height:0;text-transform:none;letter-spacing:normal;box-shadow:none}'
+'#dcp-pop .dcp-close{position:absolute;top:10px;right:10px;display:flex;align-items:center;justify-content:center;width:36px;height:36px;padding:0;border:0;border-radius:50%;background:rgba(255,255,255,.92);color:#1a1a2e;font-size:22px;line-height:1;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,.12)}'
+'#dcp-pop .dcp-go:focus-visible,#dcp-pop .dcp-close:focus-visible,#dcp-pop .dcp-no:focus-visible{outline:3px solid #7c3aed;outline-offset:2px}'
+'#dcp-pop.dcp-mob{inset:auto 0 0 0;padding:0 10px 10px;background:none;align-items:flex-end}'
+'#dcp-pop.dcp-mob .dcp-c{max-width:none;border-radius:16px;display:flex;align-items:center;gap:12px;padding:14px 46px 14px 16px}'
+'#dcp-pop.dcp-mob .dcp-mt{flex:1;margin:0;font-size:14.5px;line-height:1.35;font-weight:700}'
+'#dcp-pop.dcp-mob .dcp-go{width:auto;flex:none;padding:10px 14px;font-size:14px;border-radius:10px}'
+'#dcp-pop.dcp-mob .dcp-close{top:50%;right:6px;transform:translateY(-50%);width:32px;height:32px;font-size:20px;box-shadow:none;background:transparent}'
+'@media (max-height:780px){#dcp-pop .dcp-img{max-height:30vh;object-fit:contain;background:#0e0f14}#dcp-pop .dcp-b{padding:20px 26px 18px}#dcp-pop .dcp-t{font-size:20px}}'
+'@keyframes dcpIn{from{opacity:0}to{opacity:1}}'
+'@media (prefers-reduced-motion:reduce){#dcp-pop{animation:none}#dcp-pop .dcp-go{transition:none}}';
function n(t,cl,txt){var e=document.createElement(t);if(cl)e.className=cl;if(txt!=null)e.textContent=txt;return e}
function montrer(){
if(document.getElementById('dcp-pop'))return;
// Les pages lead magnet ont deja leur pop-up : pas de doublon.
if(!force&&document.getElementById('ai-content-gate'))return;
var mob=window.matchMedia('(max-width:700px)').matches;
var st=n('style');st.textContent=CSS;document.head.appendChild(st);
var w=n('div',mob?'dcp-mob':'');w.id='dcp-pop';
var card=n('div','dcp-c');card.tabIndex=-1;card.style.outline='none';card.setAttribute('role','dialog');card.setAttribute('aria-labelledby','dcp-pop-t');
if(!mob)card.setAttribute('aria-modal','true');
var avant=document.activeElement;
function fermer(){w.remove();st.remove();document.removeEventListener('keydown',clav);if(!force)ecrire({ferme:Date.now()});if(avant&&avant.focus)avant.focus()}
function clav(e){if(e.key==='Escape')fermer()}
var go=n('a','dcp-go',mob?c.mobileBouton:c.bouton);go.href=c.lien;go.target='_blank';go.rel='noopener';
go.addEventListener('click',function(){ecrire({clic:Date.now()});setTimeout(function(){w.remove();st.remove()},50)});
var x=n('button','dcp-close','×');x.type='button';x.setAttribute('aria-label','Fermer');x.addEventListener('click',fermer);
if(mob){var mt=n('p','dcp-mt',c.mobileTitre);mt.id='dcp-pop-t';card.appendChild(mt);card.appendChild(go);card.appendChild(x)}
else{
if(c.image){var il=n('a');il.href=c.lien;il.target='_blank';il.rel='noopener';il.tabIndex=-1;il.setAttribute('aria-hidden','true');il.addEventListener('click',function(){ecrire({clic:Date.now()})});var im=n('img','dcp-img');im.src=c.image;im.alt='';im.width=1280;im.height=720;il.appendChild(im);card.appendChild(il)}
var b=n('div','dcp-b');
if(c.surtitre)b.appendChild(n('p','dcp-sur',c.surtitre));
var t=n('h2','dcp-t',c.titre);t.id='dcp-pop-t';b.appendChild(t);
if(c.texte){var tx=n('p','dcp-x');tx.innerHTML=c.texte;b.appendChild(tx)}
if(c.mention)b.appendChild(n('p','dcp-m',c.mention));
b.appendChild(go);
var no=n('button','dcp-no','Non merci');no.type='button';no.addEventListener('click',fermer);b.appendChild(no);
card.appendChild(b);card.appendChild(x);
w.addEventListener('click',function(e){if(e.target===w)fermer()});
}
w.appendChild(card);document.body.appendChild(w);
document.addEventListener('keydown',clav);
if(!mob)card.focus({preventScroll:true});
}
setTimeout(montrer,force?500:Math.max(3,c.delai|0)*1000);
})();
JS;
}

/* -------------------------------------------------------------------------
 * Écran de réglages
 * ---------------------------------------------------------------------- */

add_action(
	'admin_menu',
	function () {
		add_options_page( 'Pop-up Décupler', 'Pop-up Décupler', 'manage_options', 'dcp-popup', 'dcp_popup_ecran' );
	}
);

function dcp_popup_ecran() {
	if ( ! current_user_can( 'manage_options' ) ) {
		return;
	}
	$r      = dcp_popup_reglages();
	$champs = array(
		'campagne'      => array( 'Identifiant de campagne', 'Le changer fait réapparaître la pop-up chez les visiteurs qui l’avaient fermée.' ),
		'surtitre'      => array( 'Surtitre (pastille)', '' ),
		'titre'         => array( 'Titre', '' ),
		'texte'         => array( 'Texte', 'Gras et italique autorisés.' ),
		'mention'       => array( 'Mention sous le texte', '' ),
		'bouton'        => array( 'Texte du bouton', '' ),
		'lien'          => array( 'Lien du bouton', 'Ouvert dans un nouvel onglet.' ),
		'image'         => array( 'Image (URL, facultative)', 'Format conseillé 1200 × 630. Affichée sur ordinateur seulement.' ),
		'mobile_titre'  => array( 'Texte du bandeau mobile', 'Court : une ligne sur téléphone.' ),
		'mobile_bouton' => array( 'Bouton du bandeau mobile', '' ),
		'fin'           => array( 'Fin d’affichage', 'Date et heure, ex. 2026-10-08T12:30:00+02:00. Vide = pas de fin.' ),
		'delai'         => array( 'Délai avant affichage (secondes)', 'Entre 3 et 120.' ),
		'exclusions'    => array( 'Pages exclues', 'Adresses sans barres, séparées par des virgules (ex. geo-ready, newsletter).' ),
	);
	echo '<div class="wrap"><h1>Pop-up Décupler</h1>';
	echo '<p>Affichée une fois par visiteur après le délai, sur tout le site sauf les pages exclues et les pages lead magnet. '
		. 'Aperçu : ajoutez <code>?dcp_popup=1</code> à n’importe quelle adresse du site.</p>';
	if ( ! empty( $r['fin'] ) && strtotime( $r['fin'] ) <= time() ) {
		echo '<div class="notice notice-warning"><p>La date de fin est passée : la pop-up ne s’affiche plus.</p></div>';
	}
	echo '<form method="post" action="options.php">';
	settings_fields( 'dcp_popup' );
	echo '<table class="form-table" role="presentation">';
	echo '<tr><th scope="row">Active</th><td><input type="hidden" name="dcp_popup[actif]" value="0">'
		. '<label><input type="checkbox" name="dcp_popup[actif]" value="1"' . checked( ! empty( $r['actif'] ), true, false ) . '> Afficher la pop-up</label></td></tr>';
	foreach ( $champs as $k => $c ) {
		$v = 'exclusions' === $k ? implode( ', ', (array) $r[ $k ] ) : (string) $r[ $k ];
		echo '<tr><th scope="row"><label for="dcp-' . esc_attr( $k ) . '">' . esc_html( $c[0] ) . '</label></th><td>';
		if ( 'texte' === $k ) {
			echo '<textarea id="dcp-texte" name="dcp_popup[texte]" rows="4" class="large-text">' . esc_textarea( $v ) . '</textarea>';
		} else {
			$type = 'delai' === $k ? 'number' : 'text';
			echo '<input type="' . $type . '" id="dcp-' . esc_attr( $k ) . '" name="dcp_popup[' . esc_attr( $k ) . ']" value="' . esc_attr( $v ) . '" class="' . ( 'delai' === $k ? 'small-text' : 'large-text' ) . '">';
		}
		if ( $c[1] ) {
			echo '<p class="description">' . esc_html( $c[1] ) . '</p>';
		}
		echo '</td></tr>';
	}
	echo '</table>';
	submit_button();
	echo '</form></div>';
}
