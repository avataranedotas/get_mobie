#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

# Opening JSON file
with open('./teste.json') as json_file:
    data = json.load(json_file)
 
    # mostrar o registo n
    print(data[0])
     
    # for printing the key-value pair of
    # nested dictionary for loop can be used
    print("\nPrinting nested dictionary as a key-value pair\n")
    for i in data:
        print("0:", i[0])
        print("1:", i[1])
        print()


