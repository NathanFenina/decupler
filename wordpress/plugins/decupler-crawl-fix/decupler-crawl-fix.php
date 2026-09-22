<?php
/**
 * Plugin Name:       Décupler — Budget de crawl
 * Description:       Trois correctifs mesurés le 22/09/2026 sur decupler.com : un robots.txt propre, une page « disparue » légère au lieu de 151 Ko, et un 404 sur la pagination hors limites. Objectif : arrêter de faire télécharger 1,5 Go à Googlebot pour lui apprendre que 12 000 pages n'existent plus.
 * Version:           1.0.0
 * Author:            Décupler
 * License:           GPL-2.0-or-later
 * Requires at least: 6.0
 * Requires PHP:      7.4
 *
 * CONTEXTE — pourquoi ce plugin existe
 *
 * Relevé du 22/09/2026 sur le site :
 *   - Search Console compte 12 787 URL non indexées, dont 10 210 « explorée,
 *     actuellement non indexée » : des URL héritées du piratage, que Google doit
 *     re-explorer pour les lâcher.
 *   - Chaque URL morte renvoie un 410 dont le corps pèse ~151 Ko, parce que le
 *     thème rend une page complète. 12 787 × 151 Ko ≈ 1,9 Go par passage.
 *   - /page/9999/ renvoie 200 au lieu de 404 : espace d'URL infini.
 *   - /?s=<n'importe quoi> renvoie 200 (155 Ko), en noindex mais exploré.
 *   - robots.txt ne contient aucune règle d'exploration.
 *
 * Correction du 22/09 : j'avais d'abord ecrit que le sitemap declare etait
 * mort, parce que mes requetes se faisaient couper. Search Console dit le
 * contraire — /sitemap.xml et /sitemap_index.xml sont tous deux « sains »,
 * 142 URL web, telecharges les 19 et 21/09. Le sitemap de Yoast fonctionne :
 * ce plugin n'y touche pas et se contente de le declarer.
 *
 * Ce plugin corrige les trois premiers points côté PHP, sans accès FTP, et le
 * quatrième via le filtre robots_txt de WordPress.
 *
 * ATTENTION — le filtre robots_txt n'agit que sur le robots.txt VIRTUEL de
 * WordPress. Si un fichier robots.txt physique existe à la racine, le serveur
 * le sert et ce plugin n'a aucun effet sur lui. L'écran Réglages du plugin le
 * signale.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

const DCP_CRAWL_VERSION = '1.0.0';

/* -------------------------------------------------------------------------
 * 1. robots.txt
 * ---------------------------------------------------------------------- */

/**
 * Renvoie le robots.txt voulu.
 *
 * « Disallow » empêche l'exploration, pas l'indexation : ne jamais y mettre une
 * URL qu'on veut désindexer, sinon Google ne peut plus lire son noindex ni son
 * 410 et elle reste gelée dans l'index. Les règles ci-dessous ne visent que des
 * URL déjà non indexées (recherche interne en noindex) ou canonicalisées
 * (paramètres de suivi).
 */
function dcp_crawl_robots_voulu() {
	$lignes = array(
		// Marqueur demande par Nathan : permet de savoir d'un coup d'oeil, en
		// ouvrant decupler.com/robots.txt, QUELLE source a servi le fichier.
		// Si ces trois lignes sont absentes, c'est qu'un robots.txt physique
		// existe a la racine et que le serveur le sert a la place du plugin.
		'# ====================================================================',
		'# robots.txt servi par le plugin « Décupler — Budget de crawl » v'
			. DCP_CRAWL_VERSION . '.',
		'# Si vous lisez cette ligne, c\'est CE fichier qui est actif — pas un',
		'# fichier physique a la racine, ni l\'editeur de Yoast.',
		'# Yoast gere le sitemap ; ce plugin gere les regles d\'exploration.',
		'# ====================================================================',
		'',
		'User-agent: *',
		'',
		'# Recherche interne : espace d\'URL infini, aucune valeur pour Google.',
		'Disallow: /*?s=',
		'Disallow: /*&s=',
		'',
		'# Paramètres de suivi et d\'attachement : duplicats de pages existantes.',
		'Disallow: /*?utm_',
		'Disallow: /*&utm_',
		'Disallow: /*?attachment_id=',
		'Disallow: /*?replytocom=',
		'',
		'# Administration, hors l\'endpoint ajax dont le front a besoin.',
		'Disallow: /wp-admin/',
		'Allow: /wp-admin/admin-ajax.php',
		'',
		'# Pas de « Disallow: /page/ » : la pagination du blog est légitime. La',
		'# pagination hors limites est traitée en 404 par ce plugin.',
		'',
		'Sitemap: ' . home_url( '/sitemap_index.xml' ),
	);

	return implode( "\n", $lignes ) . "\n";
}

add_filter(
	'robots_txt',
	function ( $sortie, $public ) {
		// Site en « decourager les moteurs » : on laisse WordPress faire, sinon
		// on ouvrirait un site que l'administrateur a volontairement fermé.
		if ( ! $public ) {
			return $sortie;
		}

		return dcp_crawl_robots_voulu();
	},
	20,
	2
);

/* -------------------------------------------------------------------------
 * 2. Page « disparue » légère
 * ---------------------------------------------------------------------- */

/**
 * Sert un corps minimal sur les 404 et les 410, au lieu des ~151 Ko du thème.
 *
 * Même page pour tout le monde — robots comme visiteurs. Servir un corps
 * différent selon le user-agent serait du cloaking, et ce n'est pas nécessaire :
 * une page « cette adresse n'existe plus » de 2 Ko est de toute façon meilleure
 * pour un humain que 151 Ko de thème.
 *
 * Le code de statut n'est pas modifié : si un autre plugin a déjà posé 410, on
 * le conserve.
 */
add_action(
	'template_redirect',
	function () {
		if ( is_admin() || wp_doing_ajax() || wp_doing_cron() ) {
			return;
		}
		if ( ! is_404() ) {
			return;
		}
		/**
		 * Permet de désactiver le corps léger sans désinstaller le plugin.
		 * add_filter( 'dcp_crawl_page_legere', '__return_false' );
		 */
		if ( ! apply_filters( 'dcp_crawl_page_legere', true ) ) {
			return;
		}

		// On conserve le statut déjà en place (410 posé par un autre plugin),
		// et on retombe sur 404 s'il n'y a rien d'explicite.
		$code = http_response_code();
		if ( ! in_array( $code, array( 404, 410 ), true ) ) {
			$code = 404;
		}

		$accueil = esc_url( home_url( '/' ) );
		$nom     = esc_html( get_bloginfo( 'name' ) );
		$titre   = ( 410 === $code )
			? 'Cette page n\'existe plus'
			: 'Page introuvable';
		$phrase  = ( 410 === $code )
			? 'Cette adresse a été supprimée définitivement. Elle ne reviendra pas.'
			: 'Cette adresse n\'existe pas ou plus sur ce site.';

		status_header( $code );
		nocache_headers();
		header( 'Content-Type: text/html; charset=utf-8' );
		header( 'X-Robots-Tag: noindex' );

		// Corps volontairement minimal et autonome : aucune requête
		// supplémentaire, aucune feuille de style externe, aucune police.
		echo '<!doctype html><html lang="fr"><head><meta charset="utf-8">';
		echo '<meta name="viewport" content="width=device-width,initial-scale=1">';
		echo '<meta name="robots" content="noindex">';
		echo '<title>' . esc_html( $titre ) . ' — ' . $nom . '</title>';
		echo '<style>body{margin:0;min-height:100vh;display:flex;align-items:center;'
			. 'justify-content:center;background:#fff;color:#4a4a6a;'
			. 'font:16px/1.6 system-ui,-apple-system,sans-serif;padding:24px}'
			. 'main{max-width:34rem}h1{margin:0 0 .5rem;font-size:1.4rem;color:#1a1a2e}'
			. 'p{margin:0 0 1.25rem}a{color:#512990}</style></head><body><main>';
		echo '<h1>' . esc_html( $titre ) . '</h1>';
		echo '<p>' . esc_html( $phrase ) . '</p>';
		echo '<p><a href="' . $accueil . '">Retour à l\'accueil de ' . $nom . '</a></p>';
		echo '</main></body></html>';
		exit;
	},
	1
);

/* -------------------------------------------------------------------------
 * 3. Pagination hors limites
 * ---------------------------------------------------------------------- */

/**
 * /page/9999/ renvoyait 200 avec la page d'accueil complète (347 Ko) et une
 * balise canonique vers /. Un espace d'URL infini, exploré pour rien. Au-dela
 * de la derniere page reelle, on renvoie un 404 — que le correctif ci-dessus
 * sert ensuite en version legere.
 */
add_action(
	'template_redirect',
	function () {
		global $wp_query;

		if ( is_admin() || is_404() || is_singular() ) {
			return;
		}

		$page = (int) get_query_var( 'paged' );
		if ( $page < 2 ) {
			return;
		}

		$max = isset( $wp_query->max_num_pages ) ? (int) $wp_query->max_num_pages : 0;
		if ( $max > 0 && $page <= $max ) {
			return;
		}

		$wp_query->set_404();
		status_header( 404 );
		nocache_headers();
	},
	0
);

/* -------------------------------------------------------------------------
 * 4. Écran de contrôle
 * ---------------------------------------------------------------------- */

add_action(
	'admin_menu',
	function () {
		add_options_page(
			'Décupler — Budget de crawl',
			'Budget de crawl',
			'manage_options',
			'dcp-crawl-fix',
			'dcp_crawl_ecran'
		);
	}
);

function dcp_crawl_ecran() {
	if ( ! current_user_can( 'manage_options' ) ) {
		return;
	}

	$physique = file_exists( ABSPATH . 'robots.txt' );

	echo '<div class="wrap"><h1>Décupler — Budget de crawl</h1>';

	echo '<h2>1. robots.txt</h2>';
	if ( $physique ) {
		echo '<div class="notice notice-error inline"><p><strong>Un fichier '
			. 'robots.txt physique existe à la racine.</strong> Le serveur le sert '
			. 'en priorité : les règles de ce plugin ne s\'appliquent pas. '
			. 'Supprimez ou renommez <code>' . esc_html( ABSPATH ) . 'robots.txt</code>'
			. ' pour que WordPress reprenne la main.</p></div>';
	} else {
		echo '<p>Aucun fichier physique : WordPress sert le robots.txt virtuel, '
			. 'et ce plugin le remplit. Vérifiez-le sur <a href="'
			. esc_url( home_url( '/robots.txt' ) ) . '" target="_blank">'
			. esc_html( home_url( '/robots.txt' ) ) . '</a>.</p>';
	}
	echo '<pre style="background:#fff;border:1px solid #c3c4c7;padding:14px;'
		. 'overflow:auto">' . esc_html( dcp_crawl_robots_voulu() ) . '</pre>';

	echo '<h2>2. Page « disparue » légère</h2>';
	echo '<p>Les réponses 404 et 410 servent désormais un corps d\'environ 2 Ko '
		. 'au lieu des ~151 Ko du thème. Le code de statut n\'est pas modifié : '
		. 'un 410 posé ailleurs reste un 410. Test : <a href="'
		. esc_url( home_url( '/test-url-inexistante-dcp/' ) ) . '" target="_blank">'
		. 'ouvrir une URL qui n\'existe pas</a>.</p>';

	echo '<h2>3. Pagination hors limites</h2>';
	echo '<p>Au-delà de la dernière page réelle, la pagination renvoie 404 au '
		. 'lieu de 200. Test : <a href="'
		. esc_url( home_url( '/page/9999/' ) ) . '" target="_blank">/page/9999/</a>.</p>';

	echo '<h2>Après activation</h2>';
	echo '<ol><li>Vérifier les trois tests ci-dessus.</li>'
		. '<li>Dans Search Console → Indexation → Pages, ouvrir le motif '
		. '« Introuvable (404) » et cliquer <strong>Valider le correctif</strong> : '
		. 'c\'est ce qui demande à Google de re-explorer le groupe en priorité.</li>'
		. '<li>Ne pas ajouter de règle « Disallow » sur une URL qu\'on veut '
		. 'désindexer : Google ne pourrait plus lire son 410.</li></ol>';

	echo '</div>';
}
