#!/usr/bin/env bash
# Teste le plugin « Décupler — Entité » dans un vrai WordPress + Yoast.
#
# S'appuie sur le banc du plugin de crawl :
#   DOSSIER=/tmp/banc wordpress/tests/test-crawl-fix.sh   # installe le banc
#   DOSSIER=/tmp/banc wordpress/tests/test-entite.sh
set -u
ICI="$(cd "$(dirname "$0")" && pwd)"
PLUGIN="$ICI/../plugins/decupler-entite"
D="${DOSSIER:?DOSSIER doit pointer vers un banc installé par test-crawl-fix.sh}"
PORT="${PORT:-8123}"
B="http://127.0.0.1:$PORT"
OK=0; KO=0
vert(){ printf '  \033[32m✓\033[0m %s\n' "$1"; OK=$((OK+1)); }
rouge(){ printf '  \033[31m✗\033[0m %s — %s\n' "$1" "$2"; KO=$((KO+1)); }
attend(){ if [ "$2" = "$3" ]; then vert "$1"; else rouge "$1" "obtenu « $2 », attendu « $3 »"; fi; }

cd "$D" || exit 1
[ -d wordpress ] || { echo "banc absent : lancer d'abord test-crawl-fix.sh"; exit 1; }
WP="php $D/wp-cli.phar --allow-root --path=$D/wordpress"
$WP option update home "$B" >/dev/null 2>&1; $WP option update siteurl "$B" >/dev/null 2>&1
sed -i "s#define('WP_HOME','[^']*'); define('WP_SITEURL','[^']*');#define('WP_HOME','$B'); define('WP_SITEURL','$B');#" wordpress/wp-config.php
rm -rf wordpress/wp-content/plugins/decupler-entite
cp -r "$PLUGIN" wordpress/wp-content/plugins/
$WP plugin activate decupler-entite >/dev/null 2>&1
# Yoast : le site représente une organisation, l'auteur s'appelle Nathan Fenina
# Sans logo, Yoast ne publie pas d'Organisation : le plugin doit la créer.
$WP eval 'WPSEO_Options::set("company_or_person","company"); WPSEO_Options::set("company_name","Décupler");' >/dev/null 2>&1
$WP user update 1 --display_name="Nathan Fenina" >/dev/null 2>&1
ART=$($WP post list --post_type=post --name=article-entite --field=ID 2>/dev/null)
[ -n "$ART" ] || ART=$($WP post create --post_type=post --post_title="Article entité" --post_name=article-entite --post_status=publish --post_author=1 --porcelain 2>/dev/null)

php -S "127.0.0.1:$PORT" -t wordpress routeur.php > serveur-entite.log 2>&1 &
SERVEUR=$!
trap 'kill $SERVEUR 2>/dev/null' EXIT
sleep 2

# Extrait le graphe Yoast d'une page et répond à une question en PHP
graphe(){ curl -sS "$B$1" | php -r '
  $h=stream_get_contents(STDIN);
  preg_match_all("#<script type=\"application/ld\+json\" class=\"yoast-schema-graph\">(.*?)</script>#s",$h,$m);
  $g=json_decode($m[1][0]??"null",true)["@graph"]??[];
  $q=$argv[1]; $par=[]; foreach($g as $n){ if(isset($n["@id"])) $par[$n["@id"]]=$n; }
  $org=null; foreach($par as $id=>$n){ if(substr($id,-13)==="#organization") $org=$n; }
  $pers=array_values(array_filter($g,function($n){ $t=(array)($n["@type"]??[]); return in_array("Person",$t,true); }));
  switch($q){
    case "legal": echo $org["legalName"]??""; break;
    case "siren": echo $org["identifier"]["value"]??""; break;
    case "fondateur": echo substr($org["founder"]["@id"]??"",-14); break;
    case "sameas_org": echo in_array("https://annuaire-entreprises.data.gouv.fr/entreprise/927480319",(array)($org["sameAs"]??[]),true)?"ok":"ko"; break;
    case "nb_personnes": echo count($pers); break;
    case "id_personne": echo substr($pers[0]["@id"]??"",-14); break;
    case "url_personne": echo substr($pers[0]["url"]??"",-14); break;
    case "linkedin": echo in_array("https://www.linkedin.com/in/nathan-fenina/",(array)($pers[0]["sameAs"]??[]),true)?"ok":"ko"; break;
    case "auteur": foreach($g as $n){ if(isset($n["author"])){ $a=$n["author"]; echo substr(is_array($a)&&isset($a["@id"])?$a["@id"]:json_encode($a),-14); break; } } break;
    case "orphelins": $ids=[]; array_walk_recursive($g,function($v,$k)use(&$ids){ if($k==="@id") $ids[]=$v; }); echo count(array_filter($ids,function($i){ return strpos($i,"#/schema/person/")!==false; })); break;
  }' "$2"; }

echo "== 1. Organisation (accueil)"
attend "raison sociale" "$(graphe / legal)" "DECUPLER"
attend "SIREN" "$(graphe / siren)" "927480319"
attend "fondateur → #nathan-fenina" "$(graphe / fondateur)" "#nathan-fenina"
attend "fiche du registre dans sameAs" "$(graphe / sameas_org)" "ok"
echo "== 2. Personne"
attend "une seule personne sur l'accueil" "$(graphe / nb_personnes)" "1"
attend "identifiant unique" "$(graphe / id_personne)" "#nathan-fenina"
attend "LinkedIn dans sameAs" "$(graphe / linkedin)" "ok"
attend "url → page d'entité" "$(graphe / url_personne)" "nathan-fenina/"
echo "== 3. Article : auteur fusionné"
attend "une seule personne dans l'article" "$(graphe /article-entite/ nb_personnes)" "1"
attend "auteur → #nathan-fenina" "$(graphe /article-entite/ auteur)" "#nathan-fenina"
attend "url de l'auteur = page d'entité (pas l'archive auteur)" "$(graphe /article-entite/ url_personne)" "nathan-fenina/"
attend "aucune référence à l'ancien identifiant Yoast" "$(graphe /article-entite/ orphelins)" "0"
echo "== 4. Organisation déjà publiée par Yoast (cas du site en ligne)"
R=$($WP eval '
  $b=trailingslashit(home_url());
  $g=[["@type"=>"Organization","@id"=>$b."#organization","name"=>"Décupler","sameAs"=>["https://decupler.substack.com"]],
      ["@type"=>"Article","@id"=>$b."a/#article","author"=>["@id"=>$b."#/schema/person/abc"]],
      ["@type"=>"Person","@id"=>$b."#/schema/person/abc","name"=>"Nathan Fenina"]];
  $r=dcp_entite_graphe($g);
  $orgs=array_filter($r,function($n){return ($n["@type"]??"")==="Organization";});
  $o=array_values($orgs)[0];
  echo count($orgs)."|".count($o["sameAs"])."|".$o["legalName"]."|".$r[1]["author"]["@id"];' 2>/dev/null)
attend "une seule Organisation" "$(echo "$R" | cut -d'|' -f1)" "1"
attend "sameAs fusionnés sans doublon" "$(echo "$R" | cut -d'|' -f2)" "2"
attend "données officielles ajoutées" "$(echo "$R" | cut -d'|' -f3)" "DECUPLER"
attend "auteur repointé" "$(echo "$R" | cut -d'|' -f4 | grep -o '#nathan-fenina')" "#nathan-fenina"

echo "== 5. Hygiène"
attend "aucune alerte PHP" "$(grep -ciE 'warning|notice|fatal' serveur-entite.log)" "0"

echo; echo "$OK réussis, $KO en échec."
[ "$KO" -eq 0 ]
