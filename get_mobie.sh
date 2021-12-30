#!/bin/bash

AGORA=`date +"%Y%m%dT%H%M%S"`

echo Hoje  : $AGORA

#ir buscar o ficheiro
wget -O $AGORA.json "https://ocpi.mobinteli.com/2.2/locations"

