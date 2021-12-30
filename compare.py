#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

# Opening JSON file
with open('./LATEST.json') as json_file:
    datalatest = json.load(json_file)
 
    # debug mostrar o registo n
    # print(data[0])
    
    # for printing the key-value pair of
    # nested dictionary for loop can be used
    print("\nLista completa de id's\n")
    for i in datalatest:
        print(i["id"])

#teste        
print(datalatest[0]["id"])

