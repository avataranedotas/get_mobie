#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import collections

from datetime import datetime

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
with open('./teste.json',encoding="utf-8-sig") as json_file2:
    #json_file2.encoding='utf-8-sig'
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

def Diff1(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1]
    return li_dif

def Diff2(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li2]
    return li_dif

#get current time
now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("date and time:",date_time)

#added stations
adicionados=Diff2(latestlist,previouslist)
print ("Adicionados:",adicionados)

#removed stations
removidos=Diff1(latestlist,previouslist)
print ("Removidos:",removidos)

if (adicionados or removidos):
    print ("Houve alterações")
    fich = open("changes.txt", "a")
    fich.write("\n")
    fich.write(date_time)
    fich.write("\n")
    fich.write("Adicionados:")
    fich.write(str(adicionados))
    fich.write("\n")    
    fich.write("Removidos:")
    fich.write(str(removidos))
    fich.write("\n")
    fich.close()
else:
    print ("Sem alterações")
   
#check number of stations
#if (latestcount != previouscount):
#    print ("Encontradas diferenças")
#else:
#    print ("Sem alterações")

#comparação ponto a ponto

def findDiff(d1, d2, path=""):
    for k in d1:
        if k in d2:
            if type(d1[k]) is dict:
                findDiff(d1[k],d2[k], "%s -> %s" % (path, k) if path else k)
            if d1[k] != d2[k]:
                result = [ "%s: " % path, " - %s : %s" % (k, d1[k]) , " + %s : %s" % (k, d2[k])]
                print("\n".join(result))
        else:
            print ("%s%s as key not in d2\n" % ("%s: " % path if path else "", k))
            
def findDiffE(d1, d2, path=""):
    for k in d1:
        if k in d2:
            if type(d1[k]) is dict:
                findDiffE(d1[k],d2[k], "%s -> %s" % (path, k) if path else k)
            #esta comparação tenta evitar as situações em que só o updated mudou    
            if (d1[k] != d2[k]) and (d1[k].find("updated") != -1):
                result = [ "%s: " % path, " - %s : %s" % (k, d1[k]) , " + %s : %s" % (k, d2[k])]
                print("\n".join(result))
        else:
            print ("%s%s as key not in d2\n" % ("%s: " % path if path else "", k))

#encontrar ponto com o mesmo id


for x in range(5):
    m=0
    #obter id latest
    id1=datalatest[x]["id"]
    #procurar o mesmo id no previous
    for j in dataprevious:
        if ( id1 == dataprevious[m]["id"] ):
            print ("Encontrado no previous, comparando:",id1)
            findDiffE(datalatest[x],dataprevious[m])
        m=m+1

#teste

#d1= {'a':{'b':{'cs':10},'d':{'cs':20}}}
#d2= {'a':{'b':{'cs':30} ,'d':{'cs':20}},'newa':{'q':{'cs':50}}}



#print("comparing latest to previous:")

#print("comparing d2 to d1:")
#findDiff(d2,d1)
