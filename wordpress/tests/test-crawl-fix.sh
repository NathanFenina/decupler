#!/usr/bin/env bash
# Teste le plugin « Décupler — Budget de crawl » dans un vrai WordPress.
#
# Pourquoi ce script existe : la version 1.0.0 a été livrée sur la foi de
# `php -l` et d'une relecture. Vérifiée en ligne, deux de ses trois
# correctifs ne marchaient pas (le robots.txt physique masquait le filtre, la
# page d'accueil statique court-circuitait la pagination). La 1.2.0 a été
# testée ici avant livraison, et ce banc a trouvé deux défauts de plus : le
# bloc robots.txt de Yoast ajouté en doublon, et les apostrophes publiées en
# entités HTML dans llms.txt.
#
# Le banc reproduit les conditions de decupler.com : permaliens propres, page
# d'accueil STATIQUE, Yoast actif, et un robots.txt PHYSIQUE servi avant
# WordPress (le routeur imite Apache).
#
#   wordpress/tests/test-crawl-fix.sh            # installe puis teste
#   DOSSIER=/tmp/banc wordpress/tests/test-crawl-fix.sh
set -u
ICI="$(cd "$(dirname "$0")" && pwd)"
PLUGIN="$ICI/../plugins/decupler-crawl-fix"
D="${DOSSIER:-$(mktemp -d)}"
PORT="${PORT:-8123}"
B="http://127.0.0.1:$PORT"
OK=0; KO=0
vert(){ printf '  \033[32m✓\033[0m %s\n' "$1"; OK=$((OK+1)); }
rouge(){ printf '  \033[31m✗\033[0m %s — %s\n' "$1" "$2"; KO=$((KO+1)); }
attend(){ # attend <libelle> <obtenu> <attendu>
  if [ "$2" = "$3" ]; then vert "$1"; else rouge "$1" "obtenu « $2 », attendu « $3 »"; fi; }

echo "== Installation dans $D"
mkdir -p "$D" && cd "$D" || exit 1
if [ ! -d wordpress ]; then
  curl -sSL https://wordpress.org/latest.tar.gz | tar xz
  (cd wordpress/wp-content/plugins \
    && curl -sSL -o s.zip https://downloads.wordpress.org/plugin/sqlite-database-integration.zip \
    && curl -sSL -o y.zip https://downloads.wordpress.org/plugin/wordpress-seo.zip \
    && unzip -q s.zip && unzip -q y.zip && rm -f s.zip y.zip)
  cp wordpress/wp-content/plugins/sqlite-database-integration/db.copy wordpress/wp-content/db.php
  sed -i "s#{SQLITE_IMPLEMENTATION_FOLDER_PATH}#$D/wordpress/wp-content/plugins/sqlite-database-integration#; s#{SQLITE_PLUGIN}#sqlite-database-integration/load.php#" wordpress/wp-content/db.php
  curl -sSL -o wp-cli.phar https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
  cp wordpress/wp-config-sample.php wordpress/wp-config.php
  sed -i "s#/\* That's all, stop editing! Happy publishing. \*/#define('WP_HOME','$B'); define('WP_SITEURL','$B');#" wordpress/wp-config.php
fi
rm -rf wordpress/wp-content/plugins/decupler-crawl-fix
cp -r "$PLUGIN" wordpress/wp-content/plugins/
WP="php $D/wp-cli.phar --allow-root --path=$D/wordpress"
if ! $WP core is-installed 2>/dev/null; then
  $WP core install --url="$B" --title=decupler --admin_user=admin \
      --admin_password=admin --admin_email=a@b.co --skip-email >/dev/null 2>&1
  $WP plugin activate wordpress-seo decupler-crawl-fix >/dev/null 2>&1
  $WP rewrite structure '/%postname%/' --hard >/dev/null 2>&1
  ACC=$($WP post create --post_type=page --post_title=Accueil --post_status=publish --porcelain 2>/dev/null)
  BLOG=$($WP post create --post_type=page --post_title=Blog --post_name=blog --post_status=publish --porcelain 2>/dev/null)
  $WP option update show_on_front page >/dev/null 2>&1
  $WP option update page_on_front "$ACC" >/dev/null 2>&1
  $WP option update page_for_posts "$BLOG" >/dev/null 2>&1
  $WP option update posts_per_page 3 >/dev/null 2>&1
  for i in 1 2 3 4 5 6 7; do $WP post create --post_title="Article $i" --post_status=publish >/dev/null 2>&1; done
  for s in panier commander mon-compte boutique confirmation-de-rdv webinaire-mars26 \
           agence-seo-ia agence-aeo agence-geo agence-seo politique-de-conditionnalite; do
    $WP post create --post_type=page --post_title="$s" --post_name="$s" --post_status=publish >/dev/null 2>&1
  done
  $WP post create --post_type=page --post_title="L’agence « GEO »" --post_name=guide \
      --post_content='Partie 1<!--nextpage-->Partie 2<!--nextpage-->Partie 3' --post_status=publish >/dev/null 2>&1
fi
printf 'User-agent: *\nAllow: /\n\nSitemap: https://decupler.com/sitemap.xml\n' > wordpress/robots.txt
$WP option update dcp_crawl_version 0 >/dev/null 2>&1

cat > routeur.php <<'PHP'
<?php
// Comme Apache + mod_rewrite : un fichier physique est servi AVANT WordPress.
$c = parse_url( $_SERVER['REQUEST_URI'], PHP_URL_PATH );
$f = __DIR__ . '/wordpress' . $c;
if ( $c !== '/' && is_file( $f ) && substr( $f, -4 ) !== '.php' ) { return false; }
chdir( __DIR__ . '/wordpress' ); $_SERVER['SCRIPT_NAME'] = '/index.php';
require __DIR__ . '/wordpress/index.php';
PHP
php -S "127.0.0.1:$PORT" -t wordpress routeur.php > serveur.log 2>&1 &
SERVEUR=$!
trap 'kill $SERVEUR 2>/dev/null' EXIT
sleep 2
code(){ curl -sS -o /dev/null -w '%{http_code}' "$B$1"; }

echo "== 1. robots.txt"
# Sauvegardes laissees par un passage precedent du banc : on les compte
# pour ne mesurer que celle que CE passage doit creer.
AVANT=$(ls wordpress/robots.txt.desactive-* 2>/dev/null | wc -l | tr -d ' ')
attend "le fichier physique masque le plugin (état de la production)" \
  "$(curl -sS "$B/robots.txt" | grep -c 'Budget de crawl')" "0"
$WP eval 'wp_set_current_user(1); $_POST["dcp_action"]="desactiver";
  $_REQUEST["_wpnonce"]=wp_create_nonce("dcp_crawl_robots");
  add_filter("wp_redirect",function(){throw new Exception();});
  try{dcp_crawl_bascule_robots();}catch(Exception $e){}' >/dev/null 2>&1
attend "le bouton range le fichier physique" "$([ -f wordpress/robots.txt ] && echo present || echo range)" "range"
attend "une sauvegarde datée est conservée" "$(( $(ls wordpress/robots.txt.desactive-* 2>/dev/null | wc -l | tr -d ' ') - AVANT ))" "1"
R=$(curl -sS "$B/robots.txt")
attend "le plugin sert le robots.txt" "$(echo "$R" | grep -c 'Budget de crawl')" "1"
attend "un seul groupe User-agent (pas de doublon Yoast)" "$(echo "$R" | grep -c '^User-agent')" "1"
attend "une seule ligne Sitemap" "$(echo "$R" | grep -c '^Sitemap')" "1"

echo "== 2. Pagination (page d'accueil statique)"
attend "/page/9999/ → 404" "$(code /page/9999/)" "404"
attend "/page/2/ → 404" "$(code /page/2/)" "404"
attend "/blog/page/2/ reste 200 (pagination légitime)" "$(code /blog/page/2/)" "200"
attend "/blog/page/99/ → 404" "$(code /blog/page/99/)" "404"
attend "/guide/3/ reste 200 (<!--nextpage--> réel)" "$(code /guide/3/)" "200"
attend "/guide/9/ → 404" "$(code /guide/9/)" "404"
attend "l'accueil reste 200" "$(code /)" "200"

echo "== 3. Page disparue légère"
T=$(curl -sS -o /dev/null -w '%{size_download}' "$B/n-existe-pas/")
attend "404 de moins de 2 Ko" "$([ "$T" -lt 2048 ] && echo oui || echo "non ($T o)")" "oui"

echo "== 4. Noindex et sitemap"
for s in panier commander mon-compte boutique confirmation-de-rdv webinaire-mars26; do
  attend "/$s/ en noindex" "$(curl -sS "$B/$s/" | grep -c 'content=.noindex')" "1"
done
attend "/agence-geo/ reste indexable" "$(curl -sS "$B/agence-geo/" | grep -c 'content=.noindex')" "0"
SM=$(curl -sS "$B/page-sitemap.xml")
attend "panier hors sitemap" "$(echo "$SM" | grep -c '/panier/')" "0"
attend "page redirigée hors sitemap" "$(echo "$SM" | grep -c '/agence-seo-ia/')" "0"
attend "agence-geo dans le sitemap" "$(echo "$SM" | grep -c '/agence-geo/')" "1"

echo "== 5. Redirections"
attend "/agence-seo-ia/ → 301" "$(code /agence-seo-ia/)" "301"
attend "cible = /agence-geo/" "$(curl -sS -o /dev/null -w '%{redirect_url}' "$B/agence-seo-ia/")" "https://decupler.com/agence-geo/"
# Un ARTICLE redirigé (et non une page) : la grappe ChatGPT.
if [ -z "$($WP post list --post_type=post --name=seo-chatgpt --field=ID 2>/dev/null)" ]; then
  $WP post create --post_title="SEO ChatGPT" --post_name=seo-chatgpt --post_status=publish >/dev/null 2>&1
  $WP transient delete --all >/dev/null 2>&1
fi
attend "article /seo-chatgpt/ → 301" "$(code /seo-chatgpt/)" "301"
attend "cible = /seo-pour-chatgpt/" "$(curl -sS -o /dev/null -w '%{redirect_url}' "$B/seo-chatgpt/")" "https://decupler.com/seo-pour-chatgpt/"
attend "article redirigé hors sitemap" "$(curl -sS "$B/post-sitemap.xml" | grep -c '/seo-chatgpt/')" "0"

echo "== 6. llms.txt"
L=$(curl -sS "$B/llms.txt")
attend "/llms.txt → 200" "$(code /llms.txt)" "200"
attend "aucune entité HTML" "$(echo "$L" | grep -c '&#')" "0"
attend "apostrophe française intacte" "$(echo "$L" | grep -c 'L’agence « GEO »')" "1"
attend "nextpage remplacé par une espace" "$(echo "$L" | grep -c 'Partie 1 Partie 2')" "1"
attend "pages redirigées exclues" "$(echo "$L" | grep -c 'agence-seo-ia')" "0"
attend "pages hors index exclues" "$(echo "$L" | grep -c '/panier/')" "0"

echo "== 7. Cache Elementor"
$WP eval 'update_post_meta(1,"_elementor_element_cache","ancien");
  update_post_meta(1,"_elementor_data","[]/*".microtime(true)."*/");' >/dev/null 2>&1
attend "écrire _elementor_data purge le cache" "$($WP post meta get 1 _elementor_element_cache 2>/dev/null)" ""

echo "== 8. URL du piratage"
attend "/casino-offre/ → 410" "$(code /casino-offre/)" "410"
attend "410 servi en page légère" "$(curl -sS "$B/casino-offre/" | grep -c 'existe plus')" "1"
attend "chemin accentué encodé → 410" "$(code '/o%C3%B9-jouer-roulette-en-ligne-en-france/')" "410"
attend "adresse inconnue hors liste → 404" "$(code /une-page-qui-n-existe-pas/)" "404"
attend "vraie page intacte" "$(code /agence-geo/)" "200"
SX=$(curl -sS "$B/sitemap-urls-supprimees.xml")
attend "sitemap temporaire → 200" "$(code /sitemap-urls-supprimees.xml)" "200"
attend "144 URL dans le sitemap" "$(echo "$SX" | grep -o '<loc>' | wc -l | tr -d ' ')" "144"
attend "accents encodés dans le sitemap" "$(echo "$SX" | grep -c '/o%C3%B9-jouer-roulette-en-ligne-en-france/')" "1"
attend "XML bien formé" "$(echo "$SX" | php -r '$x=@simplexml_load_string(stream_get_contents(STDIN)); echo $x?"ok":"ko";')" "ok"

echo "== 9. Hygiène"
attend "aucune alerte PHP pendant les tests" "$(grep -ciE 'warning|notice|fatal' serveur.log)" "0"

echo; echo "$OK réussis, $KO en échec."
[ "$KO" -eq 0 ]
