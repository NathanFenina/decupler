<?php
/**
 * Plugin Name: Décupler — SEO meta via API REST
 * Description: Expose les champs SEO (Rank Math, et Yoast si un jour) à l'API REST
 *              de WordPress, pour pouvoir écrire le titre SEO et la méta description
 *              depuis un script (scripts/wp_publish.py) au lieu de l'admin.
 * Author: Décupler
 * Version: 1.0
 *
 * INSTALLATION
 *   Déposer ce fichier dans :  wp-content/mu-plugins/decupler-seo-rest.php
 *   (créer le dossier mu-plugins s'il n'existe pas — les « must-use plugins »
 *    s'activent tout seuls, rien à cliquer dans l'admin).
 *
 * POURQUOI
 *   Rank Math et Yoast stockent la méta dans des champs personnalisés (post meta).
 *   WordPress n'expose PAS ces champs à l'API REST par défaut : sans ça, un POST
 *   sur /wp-json/wp/v2/pages/<id> avec {"meta":{...}} est silencieusement ignoré.
 *   register_post_meta(show_in_rest) corrige ça, en réservant l'écriture aux
 *   utilisateurs qui ont le droit d'éditer la page.
 *
 * SÉCURITÉ
 *   auth_callback vérifie edit_posts : seul un compte authentifié avec les droits
 *   d'édition peut écrire. Aucune donnée n'est exposée publiquement en écriture.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action( 'init', function () {

	$seo_meta_keys = array(
		// Rank Math (le plugin actuellement installé)
		'rank_math_title',
		'rank_math_description',
		'rank_math_focus_keyword',
		'rank_math_robots',
		'rank_math_canonical_url',

		// Yoast — inoffensif si Yoast n'est pas installé, utile en cas de migration
		'_yoast_wpseo_title',
		'_yoast_wpseo_metadesc',
		'_yoast_wpseo_focuskw',
		'_yoast_wpseo_canonical',
	);

	$post_types = array( 'post', 'page' );

	foreach ( $post_types as $post_type ) {
		foreach ( $seo_meta_keys as $meta_key ) {
			register_post_meta(
				$post_type,
				$meta_key,
				array(
					'show_in_rest'  => true,
					'single'        => true,
					// rank_math_robots est un tableau, le reste des chaînes.
					'type'          => ( 'rank_math_robots' === $meta_key ) ? 'array' : 'string',
					'auth_callback' => function () {
						return current_user_can( 'edit_posts' );
					},
					'show_in_rest'  => ( 'rank_math_robots' === $meta_key )
						? array(
							'schema' => array(
								'type'  => 'array',
								'items' => array( 'type' => 'string' ),
							),
						)
						: true,
				)
			);
		}
	}
} );
