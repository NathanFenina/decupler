#!/usr/bin/env bash
# Teste le plugin « Décupler — Pop-up » dans un vrai WordPress, navigateur compris.
#
# S'appuie sur le banc du plugin de crawl (même WordPress + SQLite + Yoast) :
#   DOSSIER=/tmp/banc wordpress/tests/test-crawl-fix.sh   # installe le banc
#   DOSSIER=/tmp/banc wordpress/tests/test-popup.sh
#
# Le comportement (délai, doublon avec la pop-up lead magnet, bandeau mobile)
# est vérifié dans Chromium : --virtual-time-budget fait avancer les minuteries
# sans attendre 15 vraies secondes.
set -u
ICI="$(cd "$(dirname "$0")" && pwd)"
PLUGIN="$ICI/../plugins/decupler-popup"
D="${DOSSIER:?DOSSIER doit pointer vers un banc installé par test-crawl-fix.sh}"
PORT="${PORT:-8123}"
B="http://127.0.0.1:$PORT"
CHROME="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"
OK=0; KO=0
vert(){ printf '  \033[32m✓\033[0m %s\n' "$1"; OK=$((OK+1)); }
rouge(){ printf '  \033[31m✗\033[0m %s — %s\n' "$1" "$2"; KO=$((KO+1)); }
attend(){ if [ "$2" = "$3" ]; then vert "$1"; else rouge "$1" "obtenu « $2 », attendu « $3 »"; fi; }

cd "$D" || exit 1
[ -d wordpress ] || { echo "banc absent : lancer d'abord test-crawl-fix.sh"; exit 1; }
WP="php $D/wp-cli.phar --allow-root --path=$D/wordpress"
# Le banc a été installé pour un autre port : on le suit.
$WP option update home "$B" >/dev/null 2>&1; $WP option update siteurl "$B" >/dev/null 2>&1
sed -i "s#define('WP_HOME','[^']*'); define('WP_SITEURL','[^']*');#define('WP_HOME','$B'); define('WP_SITEURL','$B');#" wordpress/wp-config.php
rm -rf wordpress/wp-content/plugins/decupler-popup
cp -r "$PLUGIN" wordpress/wp-content/plugins/
$WP plugin activate decupler-popup >/dev/null 2>&1
$WP option delete dcp_popup >/dev/null 2>&1
for s in geo-ready guide-lm; do
  [ -n "$($WP post list --post_type=page --name=$s --field=ID 2>/dev/null)" ] || \
    $WP post create --post_type=page --post_title="$s" --post_name=$s --post_status=publish >/dev/null 2>&1
done
LM=$($WP post list --post_type=page --name=guide-lm --field=ID 2>/dev/null)
$WP post update "$LM" --post_content='<div id="ai-content-gate" class="ai-popup-overlay"></div><p>Guide</p>' >/dev/null 2>&1

php -S "127.0.0.1:$PORT" -t wordpress routeur.php > serveur-popup.log 2>&1 &
SERVEUR=$!
trap 'kill $SERVEUR 2>/dev/null' EXIT
sleep 2
page(){ curl -sS "$B$1"; }
dom(){ # dom <chemin> <largeur> <budget ms>
  # Hors ligne sauf le banc : une ressource externe (emoji, polices) qui ne
  # répond pas bloquerait le temps virtuel indéfiniment.
  timeout 60 "$CHROME" --headless=new --no-sandbox --disable-gpu --window-size="$2",900 \
    --host-resolver-rules="MAP * ~NOTFOUND, EXCLUDE 127.0.0.1" \
    --virtual-time-budget="$3" --dump-dom "$B$1" 2>/dev/null; }

echo "== 1. Rendu serveur"
H=$(page /)
attend "configuration présente sur l'accueil" "$(echo "$H" | grep -c 'id="dcp-popup-cfg"')" "1"
CFG=$(echo "$H" | sed -n 's#.*<script type="application/json" id="dcp-popup-cfg">\(.*\)</script>.*#\1#p' | head -1)
attend "JSON valide, bon lien" "$(echo "$CFG" | php -r '$c=json_decode(stream_get_contents(STDIN),true); echo $c["lien"]??"ko";')" "https://www.linkedin.com/events/7508143909210910720"
attend "accents intacts dans le JSON" "$(echo "$CFG" | grep -c 'création de contenu')" "1"
attend "aucun texte de l'invitation dans le HTML visible" "$(echo "$H" | grep -c 'class="dcp-t"')" "0"
attend "présente sur une page intérieure" "$(page /agence-geo/ | grep -c 'dcp-popup-cfg')" "1"
attend "absente d'une page exclue (/geo-ready/)" "$(page /geo-ready/ | grep -c 'dcp-popup-cfg')" "0"
attend "absente d'une page 404" "$(page /nexiste-pas-du-tout/ | grep -c 'dcp-popup-cfg')" "0"

echo "== 2. Navigateur"
attend "rien avant le délai (5 s)" "$(dom / 1440 5000 | grep -c 'id="dcp-pop"')" "0"
D1=$(dom / 1440 17000)
attend "affichée après 15 s" "$(echo "$D1" | grep -c 'id="dcp-pop"')" "1"
attend "fenêtre au centre sur ordinateur" "$(echo "$D1" | grep -c 'id="dcp-pop" class=""')" "1"
attend "titre affiché" "$(echo "$D1" | grep -c 'le tout avec Claude Code')" "1"
attend "bouton vers l'événement, nouvel onglet" "$(echo "$D1" | grep -o 'class="dcp-go" href="https://www.linkedin.com/events/7508143909210910720" target="_blank" rel="noopener"' | wc -l | tr -d ' ')" "1"
attend "bandeau en bas sur mobile" "$(dom / 400 17000 | grep -c 'id="dcp-pop" class="dcp-mob"')" "1"
attend "pas de doublon sur une page lead magnet" "$(dom /guide-lm/ 1440 17000 | grep -c 'id="dcp-pop"')" "0"
attend "aperçu ?dcp_popup=1 en 0,5 s" "$(dom '/?dcp_popup=1' 1440 1500 | grep -c 'id="dcp-pop"')" "1"
attend "?dcp_popup=0 la bloque" "$(dom '/?dcp_popup=0' 1440 17000 | grep -c 'id="dcp-pop"')" "0"

echo "== 3. Fin de campagne"
$WP eval 'update_option("dcp_popup", array_merge(dcp_popup_reglages(), array("fin"=>"2020-01-01T00:00:00+01:00")));' >/dev/null 2>&1
attend "date passée : plus rien côté serveur" "$(page / | grep -c 'dcp-popup-cfg')" "0"
$WP eval 'update_option("dcp_popup", array_merge(dcp_popup_reglages(), array("fin"=>"2099-01-01T00:00:00+01:00","actif"=>false)));' >/dev/null 2>&1
attend "désactivée : plus rien" "$(page / | grep -c 'dcp-popup-cfg')" "0"
$WP option delete dcp_popup >/dev/null 2>&1

echo "== 4. Réglages par l'API REST"
R=$($WP eval 'wp_set_current_user(1);
  $q=new WP_REST_Request("POST","/wp/v2/settings");
  $q->set_body_params(array("dcp_popup"=>array("titre"=>"Nouveau <b>titre</b>","delai"=>999,"lien"=>"javascript:alert(1)")));
  $r=rest_do_request($q); $d=$r->get_data(); $p=$d["dcp_popup"]??array();
  echo $r->get_status()."|".($p["titre"]??"")."|".($p["delai"]??"")."|".($p["lien"]??"")."|".($p["bouton"]??"");' 2>/dev/null)
attend "écriture acceptée (200)" "$(echo "$R" | cut -d'|' -f1)" "200"
attend "HTML retiré du titre" "$(echo "$R" | cut -d'|' -f2)" "Nouveau titre"
attend "délai plafonné à 120 s" "$(echo "$R" | cut -d'|' -f3)" "120"
attend "lien javascript: refusé" "$(echo "$R" | cut -d'|' -f4)" ""
attend "les autres réglages sont gardés" "$(echo "$R" | cut -d'|' -f5)" "Je réserve ma place"
attend "sans lien, plus rien d'affiché" "$(page / | grep -c 'dcp-popup-cfg')" "0"
$WP option delete dcp_popup >/dev/null 2>&1

echo "== 5. Hygiène"
attend "écran de réglages sans erreur" "$($WP eval 'wp_set_current_user(1); ob_start(); dcp_popup_ecran(); echo strpos(ob_get_clean(),"Pop-up Décupler")!==false?"ok":"ko";' 2>/dev/null)" "ok"
attend "aucune alerte PHP" "$(grep -ciE 'warning|notice|fatal' serveur-popup.log)" "0"

echo; echo "$OK réussis, $KO en échec."
[ "$KO" -eq 0 ]
