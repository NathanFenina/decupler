#!/usr/bin/env bash
# Envoie une requête Jev (API TypeSafe) et affiche la réponse.
# Prérequis : une clé créée sur https://console.typesafe.ai/keys, exportée dans
# votre terminal (jamais collée dans un chat) :
#   export TYPESAFE_API_KEY=...
# Usage :
#   bash exemple-requete.sh requete-page.json
#   bash exemple-requete.sh requete-reponse-ia.json
set -euo pipefail
FICHIER="${1:-requete-page.json}"
: "${TYPESAFE_API_KEY:?Exportez TYPESAFE_API_KEY avant de lancer ce script}"
curl -sS -X POST https://api.typesafe.ai/v1/systemone \
  -H "Authorization: Bearer $TYPESAFE_API_KEY" \
  -H "Content-Type: application/json" \
  --data @"$FICHIER"
echo
