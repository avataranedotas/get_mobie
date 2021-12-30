#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

"""
explanation of json-module
json.load(file_obj) : file_obj --> dict
json.loads(json_str) : json_str --> dict
json.dumps(dict) : dict --> json_str
json.dump(dict, file_obj) : write variable-of-dict to JSON file
If json_file contains 2 or more objects, "json.load(file_obj)"　will be to an error.
As JSON-file contains multiple objects, "json.load()" cannot extract 2 or more objects from JSON file at once.
"""

with open("./LATEST.json", mode="r", encoding="utf-8") as f:
    dict = json.load(f)
    for key in dict:
        print(dict[key])
