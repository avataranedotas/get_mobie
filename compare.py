#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

# Opening JSON file
with open('./teste.json') as json_file:
    data = json.load(json_file)
 
    # mostrar o registo n
    print(data[1])
     
    # for printing the key-value pair of
    # nested dictionary for loop can be used
    print("\nPrinting nested dictionary as a key-value pair\n")
    for i in data[0]:
        print("Ref:", i['id'])
        print("Operador:", i['party_id'])
        print()


