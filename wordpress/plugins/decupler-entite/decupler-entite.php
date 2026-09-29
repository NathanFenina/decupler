<?php
/**
 * Plugin Name:       Décupler — Entité
 * Description:       Complète le graphe schema.org de Yoast sur tout le site : l'Organisation Décupler avec ses données officielles (registre national) et ses profils, une seule entité Nathan Fenina, et un auteur unique pour les contenus. C'est la couche « données structurées » du trio sémantique.
 * Version:           1.0.0
 * Author:            Décupler
 * License:           GPL-2.0-or-later
 * Requires at least: 6.0
 * Requires PHP:      7.4
 *
 * POURQUOI
 *
 *   Audit du 29/09/2026 sur dix pages du site :
 *   - l'Organisation de Yoast n'a aucun sameAs : rien ne relie le site à
 *     LinkedIn, Substack ou au registre officiel ;
 *   - Nathan Fenina existe sous trois identifiants différents selon les
 *     pages (#nathan-fenina, #/schema/person/<empreinte>, et sans @id) ;
 *   - deux URL LinkedIn différentes circulent.
 *   Un moteur (Google, ChatGPT, Perplexity) qui ne peut pas relier ces
 *   morceaux voit trois inconnus au lieu d'un expert identifié.
 *
 * CE QUE FAIT LE PLUGIN (filtre wpseo_schema_graph, rien d'autre)
 *
 *   1. Organisation (#organization) : raison sociale, date de création,
 *      SIREN, TVA, adresse du siège, fondateur, domaines, profils.
 *      Source : Registre national des entreprises, relevé le 29/09/2026.
 *   2. Personne (#nathan-fenina) : ajoutée à chaque page, avec ses profils.
 *   3. Les « personnes » générées par Yoast pour l'auteur WordPress sont
 *      fusionnées dans #nathan-fenina : toutes les références (author,
 *      creator…) pointent vers le même identifiant.
 *
 * Tout est filtrable (decupler_entite_organisation, decupler_entite_personne).
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

const DCP_ENTITE_VERSION = '1.0.0';

function dcp_entite_base() {
	return trailingslashit( home_url() );
}

function dcp_entite_id_personne() {
	return dcp_entite_base() . '#nathan-fenina';
}

function dcp_entite_organisation() {
	return apply_filters(
		'decupler_entite_organisation',
		array(
			'legalName'    => 'DECUPLER',
			'foundingDate' => '2024-04-10',
			'identifier'   => array(
				'@type'      => 'PropertyValue',
				'propertyID' => 'SIREN',
				'value'      => '927480319',
			),
			'vatID'        => 'FR43927480319',
			'address'      => array(
				'@type'           => 'PostalAddress',
				'streetAddress'   => '10 avenue Lympia',
				'postalCode'      => '06300',
				'addressLocality' => 'Nice',
				'addressCountry'  => 'FR',
			),
			'areaServed'   => array( '@type' => 'Country', 'name' => 'France' ),
			'knowsAbout'   => array( 'SEO', 'Generative Engine Optimization', 'Référencement naturel', 'Référencement IA', 'SEO local' ),
			'sameAs'       => array(
				'https://annuaire-entreprises.data.gouv.fr/entreprise/927480319',
				'https://decupler.substack.com',
			),
		)
	);
}

function dcp_entite_personne() {
	return apply_filters(
		'decupler_entite_personne',
		array(
			'@type'      => 'Person',
			'@id'        => dcp_entite_id_personne(),
			'name'       => 'Nathan Fenina',
			'jobTitle'   => 'Fondateur et président de Décupler',
			'worksFor'   => array( '@id' => dcp_entite_base() . '#organization' ),
			'image'      => 'https://decupler.com/wp-content/uploads/2026/09/nathan-fenina-portrait.jpg',
			'knowsAbout' => array( 'SEO', 'Generative Engine Optimization', 'Claude Code', 'SEO local' ),
			'sameAs'     => array(
				'https://www.linkedin.com/in/nathan-fenina/',
				'https://www.youtube.com/@nathanfenina',
			),
		)
	);
}

/** Fusionne deux listes sans doublon, en gardant l'ordre. */
function dcp_entite_union( $a, $b ) {
	$a = is_array( $a ) ? $a : ( $a ? array( $a ) : array() );
	$b = is_array( $b ) ? $b : ( $b ? array( $b ) : array() );
	return array_values( array_unique( array_merge( $a, $b ), SORT_REGULAR ) );
}

/** Remplace récursivement les références {"@id": ancien} par le nouvel identifiant. */
function dcp_entite_repointe( $noeud, array $anciens, $nouveau ) {
	if ( ! is_array( $noeud ) ) {
		return $noeud;
	}
	foreach ( $noeud as $cle => $valeur ) {
		if ( '@id' === $cle && is_string( $valeur ) && in_array( $valeur, $anciens, true ) ) {
			$noeud[ $cle ] = $nouveau;
		} elseif ( is_array( $valeur ) ) {
			$noeud[ $cle ] = dcp_entite_repointe( $valeur, $anciens, $nouveau );
		}
	}
	return $noeud;
}

function dcp_entite_est_type( $noeud, $type ) {
	$t = isset( $noeud['@type'] ) ? (array) $noeud['@type'] : array();
	return in_array( $type, $t, true );
}

function dcp_entite_graphe( $graphe ) {
	if ( ! is_array( $graphe ) ) {
		return $graphe;
	}
	$id_org      = dcp_entite_base() . '#organization';
	$id_personne = dcp_entite_id_personne();
	$personne    = dcp_entite_personne();
	$anciens     = array();

	foreach ( $graphe as $i => $noeud ) {
		if ( ! is_array( $noeud ) ) {
			continue;
		}
		// 1. Organisation
		if ( isset( $noeud['@id'] ) && $noeud['@id'] === $id_org ) {
			foreach ( dcp_entite_organisation() as $cle => $valeur ) {
				if ( 'sameAs' === $cle || 'knowsAbout' === $cle ) {
					$noeud[ $cle ] = dcp_entite_union( isset( $noeud[ $cle ] ) ? $noeud[ $cle ] : array(), $valeur );
				} elseif ( empty( $noeud[ $cle ] ) ) {
					$noeud[ $cle ] = $valeur;
				}
			}
			$noeud['founder'] = array( '@id' => $id_personne );
			$graphe[ $i ]     = $noeud;
		}
		// 3. Personnes générées par Yoast pour l'auteur : fusion dans #nathan-fenina
		if ( dcp_entite_est_type( $noeud, 'Person' ) && isset( $noeud['@id'] ) && $noeud['@id'] !== $id_personne
			&& false !== strpos( $noeud['@id'], '#/schema/person/' ) ) {
			$anciens[] = $noeud['@id'];
			foreach ( array( 'sameAs', 'knowsAbout' ) as $cle ) {
				if ( ! empty( $noeud[ $cle ] ) ) {
					$personne[ $cle ] = dcp_entite_union( $personne[ $cle ], $noeud[ $cle ] );
				}
			}
			unset( $graphe[ $i ] );
		}
		// Une personne #nathan-fenina déjà présente (autre source) : on la complète
		if ( isset( $noeud['@id'] ) && $noeud['@id'] === $id_personne ) {
			$personne = array_merge( $noeud, $personne );
			unset( $graphe[ $i ] );
		}
	}

	// Yoast ne publie l'Organisation que si nom et logo sont réglés : sans
	// elle, founder/worksFor pointeraient dans le vide. On la crée alors.
	$trouvee = false;
	foreach ( $graphe as $noeud ) {
		if ( is_array( $noeud ) && isset( $noeud['@id'] ) && $noeud['@id'] === $id_org ) {
			$trouvee = true;
		}
	}
	if ( ! $trouvee ) {
		$graphe[] = array_merge(
			array(
				'@type' => 'Organization',
				'@id'   => $id_org,
				'name'  => 'Décupler',
				'url'   => dcp_entite_base(),
			),
			dcp_entite_organisation(),
			array( 'founder' => array( '@id' => $id_personne ) )
		);
	}

	$graphe = array_values( $graphe );
	if ( $anciens ) {
		$graphe = dcp_entite_repointe( $graphe, $anciens, $id_personne );
	}
	// 2. Personne, une seule fois par page
	$graphe[] = $personne;
	return $graphe;
}
add_filter( 'wpseo_schema_graph', 'dcp_entite_graphe', 20 );
