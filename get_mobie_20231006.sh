#!/bin/bash

AGORA=`date +"%Y%m%dT%H%M%S"`

echo Hoje  : $AGORA

#renomear lastest para previous
rm PREVIOUS.json
mv LATEST.json PREVIOUS.json

#ir buscar o ficheiro API 2023

Body=$(curl https://www.mobie.pt/pt/redemobie/encontrar-posto)

Json_config=null
Locations_key=null
Locations_pass=null
Locations_user=null

if [[ $Body =~ portletInstance\:\ JSON\.parse\(\'([^\']*)\'\) ]]; then
  Json_config=${BASH_REMATCH[1]}
else
  echo "Config not found"
  exit 1
fi

if [[ $Json_config =~ mobiApiLocationsPass\"\:\"([^\"]*)\".*mobiApiLocationsKey\"\:\"([^\"]*)\".*mobiApiLocationsUser\"\:\"([^\"]*)\" ]]; then
  Locations_pass=${BASH_REMATCH[1]}
  Locations_key=${BASH_REMATCH[2]}
  Locations_user=${BASH_REMATCH[3]}
fi

if [ -z "$Locations_pass" ]; then
  echo "[ERROR] mobiApiLocationsPass not found"
fi

if [ -z "$Locations_key" ]; then
  echo "[ERROR] mobiApiLocationsKey not found"
fi

if [ -z "$Locations_user" ]; then
  echo "[ERROR] mobiApiLocationsUser not found"
fi

authorization() {
  echo $Locations_user:$Locations_pass | base64
}

fetch_locations() {
  curl --location 'https://pgm.mobie.pt/integration/locations' \
    --header "API-Key: $Locations_key" \
    --header "Authorization: Basic $(authorization)" \
    --header 'Origin: https://www.mobie.pt' \
    --header 'Referer: https://www.mobie.pt/'
}

echo $(fetch_locations) > LATEST.json



