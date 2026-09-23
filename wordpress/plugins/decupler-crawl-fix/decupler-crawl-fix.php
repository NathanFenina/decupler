<?php
/**
 * Plugin Name:       Décupler — Budget de crawl
 * Description:       Trois correctifs mesurés le 22/09/2026 sur decupler.com : un robots.txt propre, une page « disparue » légère au lieu de 151 Ko, et un 404 sur la pagination hors limites. Objectif : arrêter de faire télécharger 1,5 Go à Googlebot pour lui apprendre que 12 000 pages n'existent plus.
 * Version:           1.3.2
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
 *
 * ---------------------------------------------------------------------------
 * 1.1.0 — 22/09/2026, après vérification en ligne des trois correctifs.
 *
 * Deux des trois ne marchaient pas, et une mesure valait mieux que la
 * confiance :
 *
 *   - robots.txt : le fichier servi fait 66 octets, sans les lignes de
 *     marquage du plugin, avec un « Allow: / » et un last-modified au
 *     12/06/2026 et AUCUN en-tête x-powered-by. C'est donc un fichier
 *     PHYSIQUE à la racine (probablement posé lors de la réparation après
 *     piratage), servi par Apache avant que PHP ne s'exécute. Le filtre
 *     robots_txt ne pouvait rien y faire. Comme Nathan n'a pas d'accès FTP,
 *     la 1.1.0 ajoute un bouton qui renomme ce fichier — réversible, et
 *     sans quitter l'administration.
 *
 *   - pagination : /page/9999/ renvoyait toujours 200 avec 347 Ko. La cause
 *     est que la page d'accueil est une page statique : WordPress résout
 *     /page/9999/ en pagination de CETTE page, donc is_singular() est vrai
 *     et le garde-fou de la 1.0.0 sortait immédiatement. Corrigé en traitant
 *     explicitement le cas d'un contenu singulier paginé.
 *
 *   - page « disparue » légère : celle-là fonctionne. Un 404 pèse désormais
 *     708 octets contre ~151 Ko, et porte bien x-robots-tag: noindex.
 *
 * La 1.1.0 ajoute aussi /llms.txt, absent du site (404) — ce qui est gênant
 * pour une agence qui vend du GEO.
 *
 * ---------------------------------------------------------------------------
 * 1.2.0 — 23/09/2026. Exécution de la carte topique, validée par Nathan.
 *
 *   - Pages fonctionnelles en noindex et hors sitemap. Vérification du
 *     23/09 : les 143 URL du sitemap répondent toutes 200, indexables, avec
 *     une canonique sur elles-mêmes — techniquement propres. Mais parmi elles
 *     figurent le panier, la validation de commande, le compte client, une
 *     boutique WooCommerce SANS AUCUN PRODUIT et la confirmation de
 *     rendez-vous. Toutes indexables. Google choisissait de ne pas les
 *     indexer ; il n'avait pas à faire ce tri à notre place.
 *
 *   - Webinaires passés (mars 26, avril 26, Warsaw) : même traitement.
 *
 *   - Redirections 301 de la grappe « agence + discipline IA ». Six pages
 *     dont trois n'ont JAMAIS été montrées par Google en douze mois, toutes à
 *     zéro clic, qui visent la même intention que /agence-geo/. Seules les
 *     redirections dont la cible couvre DÉJÀ l'intention sont actives ici.
 *     Les grappes « ChatGPT » et « avis Google » attendent que leur page
 *     cible ait été réécrite pour absorber le sujet : rediriger « obtenir des
 *     avis » vers un article sur la suppression d'avis serait pire que ne
 *     rien faire.
 *
 *   - Cache d'éléments Elementor. Une écriture de _elementor_data par l'API
 *     REST est bien enregistrée mais reste INVISIBLE en ligne, parce
 *     qu'Elementor continue de servir le rendu mis en cache et ne le purge
 *     que lors d'un enregistrement depuis son éditeur. Mesuré le 23/09 sur
 *     deux pages. Le plugin purge désormais ce cache à chaque écriture, et
 *     une fois à l'activation de la 1.2.0.
 *
 * 1.2.1 — 23/09/2026. Deux 301 de plus, sur de vrais doublons d'intention :
 *   /seo-chatgpt/ → /seo-pour-chatgpt/, et /consultant-geo-optimisation-
 *   moteurs-ia/ → /consultant-geo/. Les autres articles des grappes ChatGPT
 *   et avis Google restent en ligne : relus un par un, chacun porte une
 *   intention distincte. Ils sont désormais reliés à leur guide pilier.
 *
 * 1.3.0 — 23/09/2026. Les 144 URL du piratage répondaient bien 404, mais
 *   l'inspection d'URL du jour montre que Google garde les 34 déclarées dans
 *   Search Console en index : son dernier passage date de juin, il n'est pas
 *   revenu constater la suppression. Deux leviers :
 *   - 410 (« supprimée définitivement ») au lieu de 404 sur cette liste
 *     FERMÉE (urls-piratage.php), que Google traite plus vite ;
 *   - /sitemap-urls-supprimees.xml, un sitemap temporaire à soumettre dans
 *     Search Console : il invite Google à repasser sur ces URL et à lire le
 *     410. À retirer de Search Console une fois le compteur à zéro.
 *
 * 1.3.1 — 23/09/2026. Texte de l'écran de réglages seulement : il conseillait
 *   « Valider la correction » sur le groupe 404 de Search Console. C'est
 *   inutile ici, et même contre-productif : ce bouton sert quand on a RÉPARÉ
 *   des 404, pas quand on veut qu'elles le restent.
 *
 * 1.3.2 — 23/09/2026. Mesuré en ligne après installation : une fois le
 *   fichier physique rangé, /robots.txt répond 404 — une page d'erreur
 *   d'Apache, sans PHP. L'hébergeur ne transmet pas cette adresse à
 *   WordPress (llms.txt, lui, passe). Le robots.txt virtuel ne peut donc
 *   pas exister sur ce serveur. Le plugin sait désormais ÉCRIRE son
 *   robots.txt dans un vrai fichier, le réécrit à chaque nouvelle version,
 *   et l'écran de réglages vérifie ce que le serveur sert réellement.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

const DCP_CRAWL_VERSION = '1.3.2';

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
function dcp_crawl_robots_voulu( $fichier = false ) {
	$entete = $fichier
		? array(
			'# ====================================================================',
			'# robots.txt ÉCRIT par le plugin « Décupler — Budget de crawl » v'
				. DCP_CRAWL_VERSION . ', le ' . gmdate( 'Y-m-d' ) . '.',
			'# Fichier physique : cet hébergeur ne transmet pas /robots.txt à',
			'# WordPress. Le plugin le réécrit à chaque nouvelle version.',
			'# ====================================================================',
		)
		: array();
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
	if ( $fichier ) {
		// Les six lignes du marqueur « servi par le plugin » sont remplacées
		// par l'en-tête du fichier écrit.
		$lignes = array_merge( $entete, array_slice( $lignes, 6 ) );
	}

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
	// Priorité maximale, et c'est indispensable. Test du 23/09 sur un
	// WordPress local avec Yoast : à la priorité 20, Yoast ajoutait APRÈS
	// nous son propre bloc — un second groupe « User-agent: * » avec un
	// « Disallow: » vide et une seconde ligne Sitemap. Google fusionne les
	// groupes identiques, mais un robot qui ne retient que le dernier groupe
	// aurait ignoré toutes les règles ci-dessus. On passe donc en dernier, et
	// ce fichier est le seul à écrire le robots.txt.
	PHP_INT_MAX,
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
 * 2 bis. URL du piratage : 410 et sitemap de re-exploration
 * ---------------------------------------------------------------------- */

/**
 * Liste FERMÉE des chemins créés par le piratage (décodés, sans barres).
 * Filtrable, mais jamais par motif : un 410 sur une vraie page la retire de
 * Google.
 */
function dcp_crawl_urls_piratage() {
	static $liste = null;
	if ( null === $liste ) {
		$liste = include __DIR__ . '/urls-piratage.php';
		$liste = is_array( $liste ) ? $liste : array();
	}
	return apply_filters( 'dcp_crawl_urls_piratage', $liste );
}

/** Date de relevé de la liste, servie en lastmod du sitemap temporaire. */
const DCP_CRAWL_DATE_PIRATAGE = '2026-09-23';

// Le statut est posé AVANT la page légère (priorité 1), qui le reprend.
add_action(
	'template_redirect',
	function () {
		if ( ! is_404() ) {
			return;
		}
		$chemin = rawurldecode( dcp_crawl_chemin_courant() );
		if ( in_array( $chemin, dcp_crawl_urls_piratage(), true ) ) {
			status_header( 410 );
		}
	},
	0
);

add_action(
	'init',
	function () {
		$chemin = wp_parse_url( $_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH );
		if ( '/sitemap-urls-supprimees.xml' !== $chemin ) {
			return;
		}
		status_header( 200 );
		header( 'Content-Type: application/xml; charset=utf-8' );
		header( 'X-Robots-Tag: noindex' );
		echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
		echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
		foreach ( dcp_crawl_urls_piratage() as $c ) {
			$u = home_url( '/' . implode( '/', array_map( 'rawurlencode', explode( '/', $c ) ) ) . '/' );
			echo '<url><loc>' . esc_url( $u ) . '</loc><lastmod>'
				. DCP_CRAWL_DATE_PIRATAGE . '</lastmod></url>' . "\n";
		}
		echo '</urlset>';
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
		global $wp_query, $post;

		if ( is_admin() ) {
			return;
		}
		if ( is_404() ) {
			return; // Déjà traité, et servi léger par le correctif 2.
		}

		// Deux variables distinctes, et c'est tout le sujet du correctif :
		//   'paged' = pagination d'une LISTE (blog, archive, page d'accueil
		//             en mode liste) ;
		//   'page'  = pagination D'UN CONTENU, découpé par <!--nextpage-->.
		// Sur decupler.com la page d'accueil est une page statique, donc
		// /page/9999/ alimente l'une ou l'autre selon la configuration — et
		// dans les deux cas is_singular() est vrai. La version 1.0.0 sortait
		// sur is_singular() et ne voyait donc jamais le problème : mesure du
		// 22/09, /page/9999/ renvoyait 200 avec 347 Ko.
		$demandee = max(
			(int) get_query_var( 'paged' ),
			(int) get_query_var( 'page' )
		);
		if ( $demandee < 2 ) {
			return;
		}

		if ( is_singular() || is_front_page() ) {
			// Nombre réel de pages du contenu : compter les <!--nextpage-->.
			$dispo = 1;
			if ( $post instanceof WP_Post ) {
				$dispo = 1 + (int) preg_match_all(
					'/<!--nextpage-->/',
					(string) $post->post_content
				);
			}
			// Une page statique en mode liste peut aussi être légitimement
			// paginée (blog posé sur une page) : on respecte max_num_pages
			// quand il existe.
			$max_liste = isset( $wp_query->max_num_pages )
				? (int) $wp_query->max_num_pages : 0;
			if ( $demandee <= $dispo || ( $max_liste > 1 && $demandee <= $max_liste ) ) {
				return;
			}
		} else {
			$max = isset( $wp_query->max_num_pages ) ? (int) $wp_query->max_num_pages : 0;
			if ( $max > 0 && $demandee <= $max ) {
				return;
			}
		}

		$wp_query->set_404();
		status_header( 404 );
		nocache_headers();
	},
	0
);


/* -------------------------------------------------------------------------
 * 3 bis. Reprendre la main sur un robots.txt physique
 * ---------------------------------------------------------------------- */

/**
 * Chemin du robots.txt physique, s'il existe.
 *
 * Mesure du 22/09/2026 : decupler.com sert un robots.txt de 66 octets, daté
 * du 12/06/2026, sans en-tête x-powered-by — donc un fichier sur disque,
 * servi par Apache avant que WordPress ne s'exécute. Tant qu'il est là, le
 * filtre robots_txt de ce plugin est inopérant, quoi qu'affiche son écran.
 */
function dcp_crawl_robots_physique() {
	$chemin = ABSPATH . 'robots.txt';

	return file_exists( $chemin ) ? $chemin : '';
}

/**
 * Renomme le robots.txt physique, ou le remet en place.
 *
 * Renommer plutôt que supprimer : le fichier d'origine reste récupérable
 * d'un clic, et on ne détruit rien qu'on ne sait pas reconstruire. Le nom de
 * sauvegarde est daté pour qu'un second passage n'écrase pas le premier.
 *
 * Aucune écriture n'est tentée sans vérifier que le répertoire est
 * inscriptible : sur un hébergement durci, la racine ne l'est pas, et il
 * vaut mieux le dire que d'échouer silencieusement.
 */
function dcp_crawl_bascule_robots() {
	if ( ! current_user_can( 'manage_options' ) ) {
		wp_die( 'Droits insuffisants.' );
	}
	check_admin_referer( 'dcp_crawl_robots' );

	$action  = isset( $_POST['dcp_action'] ) ? sanitize_key( $_POST['dcp_action'] ) : '';
	$vivant  = ABSPATH . 'robots.txt';
	$message = '';

	if ( 'desactiver' === $action ) {
		if ( ! file_exists( $vivant ) ) {
			$message = 'rien';
		} elseif ( ! is_writable( ABSPATH ) ) {
			$message = 'lecture-seule';
		} else {
			$sauve = ABSPATH . 'robots.txt.desactive-' . gmdate( 'Ymd-His' );
			$message = rename( $vivant, $sauve ) ? 'desactive' : 'echec';
		}
	} elseif ( 'ecrire' === $action ) {
		if ( ! is_writable( ABSPATH ) ) {
			$message = 'lecture-seule';
		} else {
			// Un fichier étranger est d'abord mis de côté, jamais écrasé.
			if ( file_exists( $vivant ) && ! dcp_crawl_robots_est_le_notre( $vivant ) ) {
				rename( $vivant, ABSPATH . 'robots.txt.desactive-' . gmdate( 'Ymd-His' ) );
			}
			$message = dcp_crawl_ecrit_robots() ? 'ecrit' : 'echec';
		}
	} elseif ( 'restaurer' === $action ) {
		$sauves = glob( ABSPATH . 'robots.txt.desactive-*' );
		if ( empty( $sauves ) ) {
			$message = 'rien-a-restaurer';
		} elseif ( file_exists( $vivant ) && ! dcp_crawl_robots_est_le_notre( $vivant ) ) {
			$message = 'deja-la';
		} else {
			// Le plus récent : c'est celui que l'utilisateur vient de ranger.
			sort( $sauves );
			// Le fichier écrit par le plugin cède la place à l'ancien.
			if ( file_exists( $vivant ) ) {
				unlink( $vivant );
			}
			$message = rename( end( $sauves ), $vivant ) ? 'restaure' : 'echec';
		}
	}

	wp_safe_redirect(
		add_query_arg(
			array( 'page' => 'dcp-crawl-fix', 'dcp_msg' => $message ),
			admin_url( 'options-general.php' )
		)
	);
	exit;
}
add_action( 'admin_post_dcp_crawl_robots', 'dcp_crawl_bascule_robots' );

/** Le robots.txt physique a-t-il été écrit par ce plugin ? */
function dcp_crawl_robots_est_le_notre( $chemin ) {
	return false !== strpos( (string) @file_get_contents( $chemin ), 'Décupler — Budget de crawl' );
}

/** Écrit le robots.txt du plugin sur disque. */
function dcp_crawl_ecrit_robots() {
	return false !== @file_put_contents( ABSPATH . 'robots.txt', dcp_crawl_robots_voulu( true ) );
}

// À chaque nouvelle version, un robots.txt écrit par le plugin est réécrit :
// sans cela, ses règles resteraient figées à la version qui l'a posé. Un
// fichier qui n'est pas le nôtre n'est jamais touché.
add_action(
	'init',
	function () {
		if ( get_option( 'dcp_crawl_robots_version' ) === DCP_CRAWL_VERSION ) {
			return;
		}
		$chemin = ABSPATH . 'robots.txt';
		if ( file_exists( $chemin ) && dcp_crawl_robots_est_le_notre( $chemin ) ) {
			dcp_crawl_ecrit_robots();
		}
		update_option( 'dcp_crawl_robots_version', DCP_CRAWL_VERSION, false );
	}
);

/**
 * Ce que le serveur sert VRAIMENT sur /robots.txt, vu de l'extérieur.
 * Mesure au lieu de supposition : c'est elle qui a trouvé le 404 d'Apache.
 */
function dcp_crawl_robots_en_ligne() {
	$r = wp_remote_get( home_url( '/robots.txt' ), array( 'timeout' => 8, 'sslverify' => false ) );
	if ( is_wp_error( $r ) ) {
		return array( 'code' => 0, 'corps' => $r->get_error_message() );
	}
	return array( 'code' => (int) wp_remote_retrieve_response_code( $r ),
		'corps' => (string) wp_remote_retrieve_body( $r ) );
}

/* -------------------------------------------------------------------------
 * 4. /llms.txt
 * ---------------------------------------------------------------------- */

/**
 * Sert un /llms.txt construit depuis le contenu réellement publié.
 *
 * Le site renvoyait 404 sur cette adresse (mesure du 22/09), ce qui est
 * gênant pour une agence qui vend de la visibilité dans les moteurs
 * génératifs. Le fichier liste les pages et les articles publiés, avec leur
 * titre et leur description — c'est un sommaire lisible par une machine, pas
 * une directive : aucun moteur n'est obligé de le lire.
 *
 * Généré depuis la base et mis en cache 12 heures : pas de fichier à
 * maintenir à la main, et pas une requête par visite de robot.
 */
function dcp_crawl_llms_txt() {
	$cache = get_transient( 'dcp_crawl_llms' );
	if ( is_string( $cache ) && '' !== $cache ) {
		return $cache;
	}

	// Format de llmstxt.org : un H1, un résumé en citation, puis des sections
	// H2 de liens « - [titre](url): description ». Le résumé est la phrase
	// que les moteurs génératifs liront en premier sur l'entreprise : il est
	// écrit, pas emprunté au slogan du thème.
	$resume = apply_filters(
		'dcp_crawl_llms_resume',
		'Décupler est une agence de référencement naturel (SEO) et de '
		. 'référencement dans les moteurs génératifs (GEO) basée à Nice, fondée '
		. 'et dirigée par Nathan Fenina. Elle rend les entreprises visibles sur '
		. 'Google et citables par ChatGPT, Claude, Gemini et Perplexity.'
	);

	$out = array( '# ' . dcp_crawl_texte( get_bloginfo( 'name' ) ), '', '> ' . $resume, '' );
	$out[] = 'Site : ' . home_url( '/' );
	$out[] = 'Sitemap : ' . home_url( '/sitemap_index.xml' );
	$out[] = '';

	// Les pages piliers d'abord : un modèle qui lit ce fichier doit trouver
	// l'offre avant les 104 autres pages rangées par ordre alphabétique.
	$piliers = apply_filters(
		'dcp_crawl_llms_piliers',
		array( 'agence-seo', 'agence-geo', 'accompagnement-seo', 'audit-geo',
			'seo-local', 'agence-seo-nice', 'cas-clients', 'machine-de-guerre-seo' )
	);
	$deja = array();
	$lignes_piliers = array();
	foreach ( $piliers as $chemin ) {
		$p = get_page_by_path( $chemin, OBJECT, array( 'page', 'post' ) );
		if ( $p && 'publish' === $p->post_status && dcp_crawl_llms_publiable( $p ) ) {
			$lignes_piliers[] = dcp_crawl_llms_ligne( $p );
			$deja[]           = (int) $p->ID;
		}
	}
	if ( $lignes_piliers ) {
		$out[] = '## Offre';
		$out[] = '';
		$out   = array_merge( $out, $lignes_piliers, array( '' ) );
	}

	foreach ( array( 'page' => 'Pages', 'post' => 'Articles' ) as $type => $titre ) {
		$q = new WP_Query(
			array(
				'post_type'           => $type,
				'post_status'         => 'publish',
				'posts_per_page'      => ( 'page' === $type ) ? 150 : 250,
				'orderby'             => ( 'page' === $type ) ? 'title' : 'date',
				'order'               => ( 'page' === $type ) ? 'ASC' : 'DESC',
				'ignore_sticky_posts' => true,
				'no_found_rows'       => true,
				'post__not_in'        => $deja,
			)
		);
		$lignes = array();
		foreach ( $q->posts as $p ) {
			if ( dcp_crawl_llms_publiable( $p ) ) {
				$lignes[] = dcp_crawl_llms_ligne( $p );
			}
		}
		if ( $lignes ) {
			$out[] = '## ' . $titre;
			$out[] = '';
			$out   = array_merge( $out, $lignes, array( '' ) );
		}
	}

	$txt = implode( "\n", $out ) . "\n";
	set_transient( 'dcp_crawl_llms', $txt, 12 * HOUR_IN_SECONDS );

	return $txt;
}

/**
 * Texte brut, entités décodées.
 *
 * WordPress rend les titres et les extraits avec des entités HTML : une
 * apostrophe devient « &#8217; ». Test du 23/09 : le premier jet publiait
 * donc « It&#8217;s » en clair dans un fichier texte — sur un site en
 * français, c'est une entité toutes les trois lignes.
 */
function dcp_crawl_texte( $s ) {
	$s = html_entity_decode( wp_strip_all_tags( (string) $s ), ENT_QUOTES | ENT_HTML5, 'UTF-8' );

	return trim( preg_replace( '/\s+/u', ' ', $s ) );
}

/**
 * Un contenu a-t-il sa place dans llms.txt ? Ni ce qui est en noindex, ni ce
 * qu'on sort de l'index, ni ce qui redirige : on ne recommande pas à un
 * moteur une page qu'on a soi-même écartée.
 */
function dcp_crawl_llms_publiable( $p ) {
	if ( '1' === (string) get_post_meta( $p->ID, '_yoast_wpseo_meta-robots-noindex', true ) ) {
		return false;
	}
	$slug = get_post_field( 'post_name', $p );

	return ! in_array( $slug, dcp_crawl_chemins_hors_index(), true )
		&& ! isset( dcp_crawl_redirections()[ $slug ] );
}

/**
 * Une ligne de liste : « - [titre](url): description », la description
 * coupée proprement à la fin d'un mot.
 */
function dcp_crawl_llms_ligne( $p ) {
	$desc = get_post_meta( $p->ID, '_yoast_wpseo_metadesc', true );
	if ( ! $desc ) {
		// Repli sur le contenu : sans shortcodes, et chaque commentaire HTML
		// (<!--nextpage-->, balises Gutenberg) remplacé par une espace — sinon
		// « Partie 1<!--nextpage-->Partie 2 » devient « Partie 1Partie 2 ».
		$corps = preg_replace( '/<!--.*?-->/s', ' ', strip_shortcodes( $p->post_content ) );
		$desc  = has_excerpt( $p ) ? $p->post_excerpt : wp_trim_words( $corps, 40, '' );
	}
	$desc = dcp_crawl_texte( $desc );
	if ( mb_strlen( $desc ) > 200 ) {
		$desc = mb_substr( $desc, 0, 200 );
		$desc = preg_replace( '/\s+\S*$/u', '', $desc ) . '…';
	}
	$ligne = '- [' . dcp_crawl_texte( get_the_title( $p ) ) . '](' . get_permalink( $p ) . ')';

	return $desc ? $ligne . ': ' . $desc : $ligne;
}

/**
 * Le vidage du cache à chaque publication : sinon un article neuf n'apparaît
 * dans /llms.txt qu'au bout de douze heures.
 */
add_action( 'save_post', function () { delete_transient( 'dcp_crawl_llms' ); } );

add_action(
	'init',
	function () {
		// Comparaison sur le chemin seul : /llms.txt?v=2 doit répondre aussi.
		$chemin = wp_parse_url( $_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH );
		if ( '/llms.txt' !== $chemin ) {
			return;
		}
		// Un fichier physique, s'il en existe un, garde la priorité : Apache
		// l'aura de toute façon servi avant nous.
		if ( file_exists( ABSPATH . 'llms.txt' ) ) {
			return;
		}
		status_header( 200 );
		header( 'Content-Type: text/plain; charset=utf-8' );
		header( 'Cache-Control: public, max-age=3600' );
		echo dcp_crawl_llms_txt(); // phpcs:ignore WordPress.Security.EscapeOutput
		exit;
	},
	1
);

/* -------------------------------------------------------------------------
 * 5. Pages à sortir de l'index et du sitemap
 * ---------------------------------------------------------------------- */

/**
 * Pages qui ne répondent à aucune recherche : fonctions de boutique, pages
 * de remerciement, événements passés. Identifiées par leur chemin, parce
 * qu'un identifiant change d'un environnement à l'autre et qu'un chemin se
 * relit.
 */
function dcp_crawl_chemins_hors_index() {
	return apply_filters(
		'dcp_crawl_chemins_hors_index',
		array(
			// WooCommerce : panier, commande, compte, et une boutique vide.
			'panier',
			'commander',
			'mon-compte',
			'boutique',
			// Page de remerciement après prise de rendez-vous.
			'confirmation-de-rdv',
			// Webinaires dont la date est passée.
			'webinaire-mars26',
			'webinaire-avril-26',
			'webinaire-ecommerce-warsaw',
		)
	);
}

/**
 * Redirections 301 de la carte topique.
 *
 * N'y figurent que les pages dont la cible couvre DÉJÀ l'intention. Chaque
 * ligne est un chemin sans barre initiale, vers une URL absolue.
 */
function dcp_crawl_redirections() {
	return apply_filters(
		'dcp_crawl_redirections',
		array(
			// Grappe « agence + discipline IA » → hub GEO. Douze mois de
			// Search Console : 0 clic sur les six, et trois jamais montrées.
			'agence-seo-ia'                => 'https://decupler.com/agence-geo/',
			'agence-aeo'                   => 'https://decupler.com/agence-geo/',
			'agence-referencement-ia'      => 'https://decupler.com/agence-geo/',
			'agence-visibilite-ia'         => 'https://decupler.com/agence-geo/',
			'agence-referencement-chatgpt' => 'https://decupler.com/agence-geo/',
			'agence-seo-chatgpt'           => 'https://decupler.com/agence-geo/',
			// Doublon d'intention : l'ancien article Elementor « SEO ChatGPT »
			// (non indexé) et « SEO pour ChatGPT », le socle technique. Les
			// autres articles de la grappe ChatGPT restent : chacun porte une
			// intention distincte, et le guide pilier les relie (23/09).
			'seo-chatgpt'                  => 'https://decupler.com/seo-pour-chatgpt/',
			// Meme intention que /consultant-geo/ (indexee) : l'ancienne version
			// de decembre 2025, jamais exploree par Google en neuf mois.
			'consultant-geo-optimisation-moteurs-ia' => 'https://decupler.com/consultant-geo/',
		)
	);
}

/**
 * Identifiants des contenus visés par un chemin, pour Yoast qui raisonne en
 * identifiants. Mis en cache une heure : la résolution fait une requête par
 * chemin, et le sitemap peut être demandé souvent.
 */
function dcp_crawl_ids_pour( array $chemins ) {
	$cle = 'dcp_crawl_ids_' . md5( implode( '|', $chemins ) );
	$ids = get_transient( $cle );
	if ( is_array( $ids ) ) {
		return $ids;
	}
	$ids = array();
	foreach ( $chemins as $chemin ) {
		foreach ( array( 'page', 'post' ) as $type ) {
			$p = get_page_by_path( $chemin, OBJECT, $type );
			if ( $p ) {
				$ids[] = (int) $p->ID;
			}
		}
	}
	set_transient( $cle, $ids, HOUR_IN_SECONDS );

	return $ids;
}

/**
 * Chemin de la requête courante, sans barres ni paramètres.
 */
function dcp_crawl_chemin_courant() {
	$chemin = wp_parse_url( $_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH );

	return trim( (string) $chemin, '/' );
}

// Noindex via Yoast, qui produit la balise robots sur ce site. On passe par
// le tableau plutôt que par la chaîne : il survit aux changements de format
// de Yoast.
add_filter(
	'wpseo_robots_array',
	function ( $robots ) {
		if ( in_array( dcp_crawl_chemin_courant(), dcp_crawl_chemins_hors_index(), true ) ) {
			$robots['index'] = 'noindex';
		}
		return $robots;
	}
);

// Et en en-tête HTTP, pour le cas où Yoast serait désactivé un jour : le
// noindex ne doit pas dépendre d'un seul plugin.
add_action(
	'template_redirect',
	function () {
		if ( in_array( dcp_crawl_chemin_courant(), dcp_crawl_chemins_hors_index(), true ) ) {
			header( 'X-Robots-Tag: noindex, follow' );
		}
	},
	5
);

// Hors sitemap : les pages hors index ET les pages redirigées. Un sitemap
// qui annonce une URL redirigée fait explorer deux URL au lieu d'une.
add_filter(
	'wpseo_exclude_from_sitemap_by_post_ids',
	function ( $ids ) {
		$sortir = array_merge(
			dcp_crawl_chemins_hors_index(),
			array_keys( dcp_crawl_redirections() )
		);

		return array_values( array_unique( array_merge(
			(array) $ids,
			dcp_crawl_ids_pour( $sortir )
		) ) );
	}
);

// Les redirections, avant tout rendu. Priorité 0 : avant le correctif de
// pagination et avant la page « disparue », pour qu'une URL redirigée ne
// soit jamais servie en 404.
add_action(
	'template_redirect',
	function () {
		$carte  = dcp_crawl_redirections();
		$chemin = dcp_crawl_chemin_courant();
		if ( isset( $carte[ $chemin ] ) ) {
			wp_redirect( $carte[ $chemin ], 301, 'Decupler carte topique' );
			exit;
		}
	},
	-1
);

/* -------------------------------------------------------------------------
 * 6. Cache d'éléments Elementor
 * ---------------------------------------------------------------------- */

/**
 * Purge le rendu mis en cache d'une page Elementor dès que ses données
 * changent, quel que soit le chemin de l'écriture.
 *
 * Elementor ne purge ce cache que lors d'un enregistrement depuis son
 * éditeur. Une écriture de _elementor_data par l'API REST est donc bien
 * stockée, mais la page continue d'afficher l'ancien rendu — sans erreur,
 * sans avertissement. Constaté le 23/09 sur /claude-skills-seo/ et
 * /installer-mcp-data-for-seo-sur-chatgpt/.
 */
function dcp_crawl_purge_elementor_post( $post_id ) {
	delete_post_meta( $post_id, '_elementor_element_cache' );
	delete_post_meta( $post_id, '_elementor_css' );
	// Le fichier CSS de la page est régénéré au prochain affichage.
	$upload = wp_upload_dir();
	$css    = trailingslashit( $upload['basedir'] ) . 'elementor/css/post-' . (int) $post_id . '.css';
	if ( file_exists( $css ) ) {
		wp_delete_file( $css );
	}
}

foreach ( array( 'updated_post_meta', 'added_post_meta' ) as $crochet ) {
	add_action(
		$crochet,
		function ( $meta_id, $post_id, $cle ) {
			if ( '_elementor_data' === $cle ) {
				dcp_crawl_purge_elementor_post( $post_id );
			}
		},
		10,
		3
	);
}

/**
 * Purge globale, une seule fois, au passage en 1.2.0 : c'est l'équivalent
 * du bouton « Effacer les fichiers et les données » d'Elementor, et c'est ce
 * qui rend visibles les écritures faites avant l'installation de ce
 * correctif.
 */
add_action(
	'init',
	function () {
		if ( get_option( 'dcp_crawl_version' ) === DCP_CRAWL_VERSION ) {
			return;
		}
		global $wpdb;
		if ( class_exists( '\Elementor\Plugin' )
			&& isset( \Elementor\Plugin::$instance->files_manager ) ) {
			\Elementor\Plugin::$instance->files_manager->clear_cache();
		}
		// Selon la version d'Elementor, la purge ci-dessus ne vide pas
		// forcément le cache d'éléments. On le vide explicitement : Elementor
		// le reconstruit au prochain affichage de chaque page.
		$wpdb->delete( $wpdb->postmeta, array( 'meta_key' => '_elementor_element_cache' ) );
		// Les identifiants résolus peuvent avoir changé avec la liste.
		$wpdb->query( "DELETE FROM {$wpdb->options} WHERE option_name LIKE '\_transient\_dcp\_crawl\_%' OR option_name LIKE '\_transient\_timeout\_dcp\_crawl\_%'" );
		update_option( 'dcp_crawl_version', DCP_CRAWL_VERSION, false );
	},
	99
);

/* -------------------------------------------------------------------------
 * 7. Écran de contrôle
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

	$physique = dcp_crawl_robots_physique();
	// Un fichier écrit par ce plugin n'est pas un fichier étranger à ranger.
	$le_notre = $physique && dcp_crawl_robots_est_le_notre( $physique );
	if ( $le_notre ) {
		$physique = '';
	}
	$sauves   = glob( ABSPATH . 'robots.txt.desactive-*' );

	echo '<div class="wrap"><h1>Décupler — Budget de crawl</h1>';

	// Retour de l'action de bascule.
	$msgs = array(
		'desactive'        => array( 'success', 'Le fichier physique a été rangé. '
			. 'WordPress reprend la main : rechargez /robots.txt pour voir '
			. 'apparaître les lignes de marquage.' ),
		'restaure'         => array( 'success', 'Le fichier physique est remis en '
			. 'place. Les règles de ce plugin sont de nouveau inopérantes.' ),
		'lecture-seule'    => array( 'error', 'La racine du site n\'est pas '
			. 'inscriptible par PHP : le fichier ne peut pas être renommé depuis '
			. 'ici. Il faut passer par le gestionnaire de fichiers de '
			. 'l\'hébergeur.' ),
		'echec'            => array( 'error', 'Le renommage a échoué. Droits du '
			. 'fichier ou du répertoire.' ),
		'rien'             => array( 'warning', 'Aucun fichier physique à ranger.' ),
		'rien-a-restaurer' => array( 'warning', 'Aucune sauvegarde à restaurer.' ),
		'deja-la'          => array( 'warning', 'Un robots.txt physique est déjà '
			. 'en place : rangez-le d\'abord.' ),
		'ecrit'            => array( 'success', 'Le robots.txt du plugin est écrit '
			. 'dans un fichier à la racine. Rechargez /robots.txt pour vérifier.' ),
	);
	$msg = isset( $_GET['dcp_msg'] ) ? sanitize_key( $_GET['dcp_msg'] ) : '';
	if ( isset( $msgs[ $msg ] ) ) {
		echo '<div class="notice notice-' . esc_attr( $msgs[ $msg ][0] )
			. ' is-dismissible"><p>' . esc_html( $msgs[ $msg ][1] ) . '</p></div>';
	}

	echo '<h2>1. robots.txt</h2>';
	if ( $physique ) {
		$actuel = (string) file_get_contents( $physique );
		echo '<div class="notice notice-error inline"><p><strong>Un fichier '
			. 'robots.txt physique existe à la racine et c\'est LUI qui est '
			. 'servi.</strong> Apache le rend avant que WordPress ne s\'exécute, '
			. 'donc les règles de ce plugin n\'ont aucun effet. Mesuré le '
			. '22/09/2026 : 66 octets, daté du 12/06/2026 — probablement posé '
			. 'lors de la réparation après piratage.</p>'
			. '<p>Contenu réellement servi aujourd\'hui :</p>'
			. '<pre style="background:#fff;border:1px solid #c3c4c7;padding:10px;'
			. 'max-height:160px;overflow:auto">' . esc_html( $actuel ) . '</pre>'
			. '<p>Le bouton ci-dessous le <strong>renomme</strong> (il ne le '
			. 'supprime pas) en <code>robots.txt.desactive-<em>date</em></code>. '
			. 'WordPress reprend alors la main et sert la version de ce plugin. '
			. 'C\'est réversible d\'un clic, et ça évite un passage en FTP.</p>';
		echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) )
			. '">';
		wp_nonce_field( 'dcp_crawl_robots' );
		echo '<input type="hidden" name="action" value="dcp_crawl_robots">'
			. '<input type="hidden" name="dcp_action" value="desactiver">'
			. '<p><button type="submit" class="button button-primary">Ranger le '
			. 'fichier physique et reprendre la main</button></p></form>';
		if ( ! is_writable( ABSPATH ) ) {
			echo '<p><em>Attention : la racine du site ne semble pas inscriptible '
				. 'par PHP. Le bouton vous le dira, mais il y a de fortes chances '
				. 'qu\'il faille passer par le gestionnaire de fichiers de '
				. 'l\'hébergeur.</em></p>';
		}
		echo '</div>';
	} else {
		echo $le_notre
			? '<p>Le robots.txt est un <strong>fichier écrit par ce plugin</strong>, '
				. 'réécrit à chaque nouvelle version.'
			: '<p>Aucun fichier physique : WordPress sert le robots.txt virtuel, '
			. 'et ce plugin le remplit. Vérifiez-le sur <a href="'
			. esc_url( home_url( '/robots.txt' ) ) . '" target="_blank">'
			. esc_html( home_url( '/robots.txt' ) ) . '</a>.</p>';
	}
	$enligne = dcp_crawl_robots_en_ligne();
	$bon     = 200 === $enligne['code'] && false !== strpos( $enligne['corps'], 'Budget de crawl' );
	echo '<p><strong>Vérifié à l\'instant :</strong> ' . esc_html( home_url( '/robots.txt' ) )
		. ' répond <code>' . (int) $enligne['code'] . '</code>'
		. ( $bon ? ' avec les règles de ce plugin. ✅' : '.' ) . '</p>';
	if ( ! $bon && ! $physique ) {
		echo '<div class="notice notice-warning inline"><p><strong>L\'hébergeur ne '
			. 'transmet pas /robots.txt à WordPress</strong> : le robots.txt virtuel '
			. 'ne peut pas être servi. Écrivez-le dans un vrai fichier.</p>';
		echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) ) . '">';
		wp_nonce_field( 'dcp_crawl_robots' );
		echo '<input type="hidden" name="action" value="dcp_crawl_robots">'
			. '<input type="hidden" name="dcp_action" value="ecrire">'
			. '<p><button type="submit" class="button button-primary">Écrire le '
			. 'robots.txt du plugin dans un fichier</button></p></form></div>';
	}
	echo '<p><strong>Ce que ce plugin sert (ou servirait) :</strong></p>';
	echo '<pre style="background:#fff;border:1px solid #c3c4c7;padding:14px;'
		. 'overflow:auto">' . esc_html( dcp_crawl_robots_voulu() ) . '</pre>';
	if ( ! empty( $sauves ) && ! $physique ) {
		sort( $sauves );
		echo '<p>Sauvegarde conservée : <code>'
			. esc_html( basename( (string) end( $sauves ) ) ) . '</code>.</p>';
		echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) )
			. '">';
		wp_nonce_field( 'dcp_crawl_robots' );
		echo '<input type="hidden" name="action" value="dcp_crawl_robots">'
			. '<input type="hidden" name="dcp_action" value="restaurer">'
			. '<p><button type="submit" class="button">Remettre l\'ancien fichier '
			. 'physique en place</button></p></form>';
	}

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

	echo '<h2>4. /llms.txt</h2>';
	echo '<p>Le site renvoyait 404 sur cette adresse — gênant pour une agence '
		. 'qui vend du GEO. Ce plugin la sert désormais, construite depuis les '
		. 'pages et les articles publiés (les contenus en noindex sont exclus), '
		. 'avec un cache de 12 heures vidé à chaque publication. Vérifier : '
		. '<a href="' . esc_url( home_url( '/llms.txt' ) ) . '" target="_blank">'
		. esc_html( home_url( '/llms.txt' ) ) . '</a>.</p>';
	echo '<p><em>Ce n\'est pas une directive : aucun moteur n\'est obligé de '
		. 'lire ce fichier. C\'est un sommaire lisible par une machine.</em></p>';

	echo '<h2>5. Pages sorties de l\'index et du sitemap</h2>';
	echo '<p>Noindex (balise Yoast et en-tête HTTP) et exclusion du sitemap pour '
		. 'les pages qui ne répondent à aucune recherche&nbsp;:</p><ul style="list-style:disc;padding-left:20px">';
	foreach ( dcp_crawl_chemins_hors_index() as $c ) {
		echo '<li><a href="' . esc_url( home_url( '/' . $c . '/' ) ) . '" target="_blank">/'
			. esc_html( $c ) . '/</a></li>';
	}
	echo '</ul>';

	echo '<h2>6. Redirections 301 de la carte topique</h2>';
	echo '<table class="widefat striped" style="max-width:760px"><thead><tr><th>Ancienne '
		. 'adresse</th><th>Redirigée vers</th></tr></thead><tbody>';
	foreach ( dcp_crawl_redirections() as $de => $vers ) {
		echo '<tr><td><a href="' . esc_url( home_url( '/' . $de . '/' ) ) . '" target="_blank">/'
			. esc_html( $de ) . '/</a></td><td>' . esc_html( $vers ) . '</td></tr>';
	}
	echo '</tbody></table>';
	echo '<p><em>Seuls les vrais doublons d\'intention sont redirigés. Les '
		. 'autres articles des grappes « ChatGPT » et « avis Google » restent en '
		. 'ligne, reliés à leur guide pilier : relus un par un le 23/09, chacun '
		. 'porte une intention distincte.</em></p>';

	echo '<h2>8. URL du piratage</h2>';
	echo '<p>' . count( dcp_crawl_urls_piratage() ) . ' adresses créées par le '
		. 'piratage répondent <strong>410</strong> (supprimée définitivement) au '
		. 'lieu de 404. Test : <a href="' . esc_url( home_url( '/casino-offre/' ) )
		. '" target="_blank">une adresse de la liste</a> doit afficher « Cette '
		. 'page n\'existe plus ».</p>';
	echo '<p>Sitemap de re-exploration, à soumettre <strong>une fois</strong> dans '
		. 'Search Console → Sitemaps : <code>sitemap-urls-supprimees.xml</code> '
		. '(<a href="' . esc_url( home_url( '/sitemap-urls-supprimees.xml' ) )
		. '" target="_blank">voir</a>). Search Console y signalera des erreurs '
		. '410 : c\'est le but. Le retirer quand plus aucune de ces adresses '
		. 'n\'est indexée.</p>';

	echo '<h2>7. Cache Elementor</h2>';
	echo '<p>Toute modification de <code>_elementor_data</code> — y compris par '
		. 'l\'API REST — purge désormais le rendu mis en cache de la page. Sans ce '
		. 'correctif, une modification faite hors de l\'éditeur Elementor était '
		. 'enregistrée mais restait invisible en ligne.</p>';

	echo '<h2>Après activation</h2>';
	echo '<ol><li>Vérifier les trois tests ci-dessus.</li>'
		. '<li>Dans Search Console → Sitemaps, soumettre '
		. '<code>sitemap-urls-supprimees.xml</code> (section 8). Ne pas cliquer '
		. '« Valider la correction » sur le groupe « Introuvable (404) » : ces '
		. 'adresses DOIVENT rester introuvables, la validation échouerait.</li>'
		. '<li>Ne pas ajouter de règle « Disallow » sur une URL qu\'on veut '
		. 'désindexer : Google ne pourrait plus lire son 410.</li></ol>';

	echo '</div>';
}
