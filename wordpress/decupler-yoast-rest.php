<?php
/**
 * Plugin Name: Décupler — Yoast SEO via REST
 * Description: Expose les métadonnées Yoast SEO à l'API REST pour permettre leur
 *              lecture ET écriture par l'atelier de contenu Décupler (serveur MCP
 *              yoast_seo.py). Sans ce plugin, WordPress protège les métas Yoast
 *              (préfixe « _ ») et ignore silencieusement les écritures REST.
 * Author:      Décupler
 * Version:     1.0.0
 *
 * INSTALLATION (au choix) :
 *  - Déposer ce fichier dans wp-content/mu-plugins/  (chargé automatiquement), OU
 *  - Le mettre dans wp-content/plugins/decupler-yoast-rest/ et l'activer.
 *
 * SÉCURITÉ : chaque champ n'est modifiable via REST que par un utilisateur ayant
 * le droit d'éditer les contenus (edit_posts). L'API REST exige déjà une
 * authentification (mot de passe d'application). Aucune donnée n'est exposée
 * publiquement au-delà de ce que Yoast publie déjà dans <head>.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

add_action( 'init', function () {
    $keys = array(
        '_yoast_wpseo_title',
        '_yoast_wpseo_metadesc',
        '_yoast_wpseo_focuskw',
        '_yoast_wpseo_canonical',
        '_yoast_wpseo_meta-robots-noindex',
        '_yoast_wpseo_meta-robots-nofollow',
        '_yoast_wpseo_opengraph-title',
        '_yoast_wpseo_opengraph-description',
        '_yoast_wpseo_opengraph-image',
        '_yoast_wpseo_twitter-title',
        '_yoast_wpseo_twitter-description',
    );

    $post_types = array( 'post', 'page' );

    foreach ( $post_types as $post_type ) {
        foreach ( $keys as $key ) {
            register_post_meta( $post_type, $key, array(
                'type'          => 'string',
                'single'        => true,
                'show_in_rest'  => true,
                'auth_callback' => function ( $allowed, $meta_key, $post_id ) {
                    return current_user_can( 'edit_post', $post_id );
                },
            ) );
        }
    }
} );
