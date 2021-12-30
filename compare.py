#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

#with open("./LATEST.json", mode="r", encoding="utf-8") as f:
#    dict = json.load(f)
#    for key in dict:
#        print(dict[key])


json_filename="./LATEST.json"
print (json_filename)

try:
    json_file=open(json_filename)
    json_data=json.load(json_file)
except IOError:
    print ("Error: File does not appear to exist.")
finally:
    json_file.close()

my_dict={}

for item in json_data['result']:
    #print item['templateid'], ": ",item['name']
    my_dict.update({ item['templateid']: item['name']})

for key in sorted(my_dict.iterkeys()):
    print ("%s: %s" % (key, my_dict[key]))
