<?php
/**
 * Plugin Name: Décupler — Yoast en écriture via l'API REST
 * Description: Expose les champs Yoast (title, meta description, focus keyword) à
 *              l'API REST pour les articles ET les pages. Sans ça, WordPress
 *              renvoie 200 et jette silencieusement les valeurs sur les pages.
 * Version:     1.0
 *
 * Installation : déposer ce fichier dans wp-content/mu-plugins/
 * (créer le dossier s'il n'existe pas). Aucune activation nécessaire :
 * les mu-plugins se chargent automatiquement et ne peuvent pas être
 * désactivés par erreur depuis l'admin.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'init', function () {

	$champs = array(
		'_yoast_wpseo_title'    => 'Titre SEO Yoast',
		'_yoast_wpseo_metadesc' => 'Meta description Yoast',
		'_yoast_wpseo_focuskw'  => 'Requête cible Yoast',
	);

	// Types de contenu concernés. Ajouter ici un CPT si besoin plus tard.
	$types = array( 'post', 'page' );

	foreach ( $types as $type ) {
		foreach ( $champs as $cle => $libelle ) {
			register_post_meta( $type, $cle, array(
				'type'              => 'string',
				'description'       => $libelle,
				'single'            => true,
				'show_in_rest'      => true,
				'sanitize_callback' => 'sanitize_text_field',
				// Réservé aux comptes qui peuvent déjà éditer le contenu :
				// un mot de passe d'application hérite des droits de son compte.
				'auth_callback'     => function ( $allowed, $cle, $post_id ) {
					return current_user_can( 'edit_post', $post_id );
				},
			) );
		}
	}
} );
