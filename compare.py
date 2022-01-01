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
    
    #print (type(datalatest))
    #print (type(datalatest[0]))
    #print(datalatest[0])
    #print (type(datalatest[0]["evses"]))
    #print(datalatest[0]["evses"])

    
    # for printing the key-value pair of
    # nested dictionary for loop can be used
    #print("\nLista completa de id's\n")
    #for i in datalatest:
    #    print(i["id"])

#teste        
#print(datalatest[0]["id"])

with open('./PREVIOUS.json') as json_file2:
#with open('./teste_f.json',encoding="utf-8-sig") as json_file2:
    #json_file2.encoding='utf-8-sig'
    dataprevious = json.load(json_file2)

latestlist=list()    
previouslist=list()

n=0
for i in datalatest:
    latestlist.append(i["id"])
    n=n+1
latestcount=n
print ("Pontos actuais: ",latestcount)    
#print (latestlist[0])
#print (latestlist[1])

n=0
for i in dataprevious:
    previouslist.append(i["id"])
    n=n+1
previouscount=n
print ("Pontos anteriores: ",previouscount)
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
#print("date and time:",date_time)

#added stations
adicionados=Diff2(latestlist,previouslist)
print ("Adicionados:",adicionados)

#removed stations
removidos=Diff1(latestlist,previouslist)
print ("Removidos:",removidos)


   
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
            #if (d1[k] != d2[k]) and (str(d1[k]).find("updated") != -1):
            if d1[k] != d2[k]:
                result = [ "%s: " % path, " - %s : %s" % (k, d1[k]) , " + %s : %s" % (k, d2[k])]
                print("\n".join(result))
                print (type(d1[k]))
                print (str(d1[k]).find("updated"))
        else:
            print ("%s%s as key not in d2\n" % ("%s: " % path if path else "", k))



def findDiffA(d1, d2, path=""):
    for k in d1:
        if k in d2:
            if type(d1[k]) is dict:
                findDiffE(d1[k],d2[k], "%s -> %s" % (path, k) if path else k)
            if d1[k] != d2[k]:
                result = [ "%s: " % path, " - %s : %s" % (k, d1[k]) , " + %s : %s" % (k, d2[k])]
                print("\n".join(result))
                #print (type(d1[k]))
        else:
            print ("%s%s as key not in d2\n" % ("%s: " % path if path else "", k))




def findDiffB(ident, d1, d2, path=""):
    global fich
    global escreverfich
    reportar=1
    if type(d1) is dict:
        #print ("            Start dict")        
        for k in d1:
            if k in d2:
                #print (k)
                #print (path)
                #print ("            Encontrar dentro dict")
                if (d1[k] != d2[k]):
                    #print ("            Encontrada diferença dict, tentando entrar dentro do dict")
                    findDiffB(ident,d1[k],d2[k], "%s -> %s" % (path, k) if path else k)
                    if (reportar == 1) and (k != "last_updated") and (k != "evses") and (k != "connectors") and (k != "status"):                    
                        print (ident)
                        if (escreverfich == 0):
                            fich = open("changes.txt", "a") 
                            fich.write("\n")
                            fich.write(date_time)
                            fich.write("\n")
                            escreverfich=1
                        fich.write(ident)
                        fich.write("\n")
                        result = [ "%s: " % path, " NEW %s : %s" % (k, d1[k]) , " OLD %s : %s" % (k, d2[k])]
                        print("\n".join(result))
                        fich.write("\n".join(result))
                        fich.write("\n")
            else:
                print ("%s%s as key not in d2\n" % ("%s: " % path if path else "", k))    
    elif type(d1) is list:
        n=0 #falta confirmar se as listas têm o mesmo tamanho
        
        n1=0
        n2=0
        for j1 in d1:
            n1=n1+1
        for j2 in d2:
            n2=n2+1
        if (n1 == n2):
            #print ("            Start list")
            for j in d1:
                #print ("            Percorrer lista")
                #print (n)
                #print (d1[n])
                #print (d2[n])
                if d1[n] != d2[n]:
                        #print ("            Encontrada diferença list, tentando entrar dentro da lista")    
                        findDiffB(ident,d1[n],d2[n], "%s -> %s" % (path, n) if path else n)
                        #result = [ "%s: " % path, " - %s : %s" % (n, d1[n]) , " + %s : %s" % (n, d2[n])]
                        #print("\n".join(result))               
                            
                #if j in d2:
                    #print (d1)
                    #print ("Encontrar dentro list")
                    #if d1[n] != d2[n]:
                        #print ("Encontrada diferença list")    
                        #result = [ "%s: " % path, " - %s : %s" % (n, d1[n]) , " + %s : %s" % (n, d2[n])]
                        #print("\n".join(result))               
                #else:
                    #print ("Não encontrado")            
                n=n+1
        else:
            print ("Lista com numero elementos diferentes")
    #elif type(d1) is str:
        #if d1 != d2:
            #print ("            Encontrada diferença str")
            #result = [" %s / %s " %(d1,d2)]
            #print("\n".join(result))  

escreverfich=0
            
  
if (adicionados or removidos):
    fich = open("changes.txt", "a") 
    fich.write("\n")
    fich.write(date_time)
    fich.write("\n")    
    print ("Houve alterações")
    fich.write("Adicionados:")
    fich.write(str(adicionados))
    fich.write("\n")    
    fich.write("Removidos:")
    fich.write(str(removidos))
    fich.write("\n")
    escreverfich=1

#else:
    #print ("Sem alterações")


#encontrar ponto com o mesmo id


n=0
#for x in range(10):
for x in datalatest:
    m=0
    #obter id latest
    id1=datalatest[n]["id"]
    #procurar o mesmo id no previous
    for j in dataprevious:
        if ( id1 == dataprevious[m]["id"] ):
            #print ("Encontrado no previous, comparando:",id1)
            findDiffB(id1, datalatest[n],dataprevious[m])
        m=m+1
    n=n+1


if escreverfich == 1:
    fich.close()

    
#teste finddiffs misto
#print ("Start debug\n\n\n\n\n\n\n")
 
#dA=   datalatest[0]#["evses"]#[0]#["last_updated"]
#dB=   datalatest[0]["evses"]#[0]#["last_updated"]
#dB= dataprevious[0]#["evses"]#[0]#["last_updated"]
#print (type(dA))
#print (dA)
#print (type(dB))
#print (dB)



#findDiffB(dA,dB)

