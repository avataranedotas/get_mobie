#!/bin/bash

AGORA=`date +"%Y%m%dT%H%M%S"`

echo Hoje  : $AGORA

#renomear lastest para previous
rm PREVIOUS.json
mv LASTEST.json PREVIOUS.json

#ir buscar o ficheiro
wget -O LASTEST.json "https://ocpi.mobinteli.com/2.2/locations"

