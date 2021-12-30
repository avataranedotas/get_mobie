#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import collections

# Opening JSON file
with open('./LATEST.json') as json_file:
    datalatest = json.load(json_file)
 
    # debug mostrar o registo n
    # print(data[0])
    
    # for printing the key-value pair of
    # nested dictionary for loop can be used
    #print("\nLista completa de id's\n")
    #for i in datalatest:
    #    print(i["id"])

#teste        
#print(datalatest[0]["id"])

#with open('./PREVIOUS.json') as json_file2:
with open('./teste.json') as json_file2:
    dataprevious = json.load(json_file2)

latestlist=list()    
previouslist=list()

n=0
for i in datalatest:
    latestlist.append(i["id"])
    n=n+1
latestcount=n
print ("Pontos actuais: ",latestcount,"\n")    
#print (latestlist[0])
#print (latestlist[1])

n=0
for i in dataprevious:
    previouslist.append(i["id"])
    n=n+1
previouscount=n
print ("Pontos anteriores: ",previouscount,"\n")
#print (previouslist[0])
#print (previouslist[1])

#if diference found then log to file the changes

if (latestcount != previouscount):
    print ("Encontradas diferenças")
else:
    print ("Sem alterações")

    
