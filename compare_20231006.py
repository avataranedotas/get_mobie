#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import collections
import csv

from datetime import datetime

# Opening JSON file
with open('./LATEST.json') as json_file:
    datalatest = json.load(json_file)
 
    # debug mostrar o registo n
    
    #print (type(datalatest))
    #print (type(datalatest["data"]))
    #print (type(datalatest["data"][0]))
    #print(datalatest["data"][0])
    #print (type(datalatest["data"][0]["evses"]))
    #print(datalatest["data"][0]["evses"])

    
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

#ler pontos sujeitos a verificacao
with open('./lista.txt', newline='') as lista_file:
    reader = csv.reader(lista_file)
    watchlista = list (reader)
#print ("Watchlista: ",watchlista)

latestlist=list()    
previouslist=list()
watchlist=list()

n=0
for i in datalatest["data"]:
    latestlist.append(i["id"])
    n=n+1
latestcount=n
print ("Pontos actuais: ",latestcount)    
#print (latestlist[0])
#print (latestlist[1])


n=0
for i in dataprevious["data"]:
    previouslist.append(i["id"])
    n=n+1
previouscount=n
print ("Pontos anteriores: ",previouscount)
#print (previouslist[0])
#print (previouslist[1])

n=0
for element in watchlista:
    #print ("Teste")
    if (len(element)) == 1 :
        #print (str(element[0]))
        watchlist.append(str(element[0]))
#print (watchlist[0])
#print (watchlist[1])




#if diference found then log to file the changes


#-------------- DEFS -------


def Diff1(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1]
    return li_dif

def Diff2(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li2]
    return li_dif

def Remove(origem, aremover):
    li_dif = [i for i in origem if i not in aremover]
    return li_dif


def finddetails(ident, d1, path=""):
    global levelglobal2
    global detalhesadic
    #global escreverfich
    #global fich
    #global watchbusy
    #levelmax=0
    nomeactual=""
    if type(d1) is dict:
        #print ("            Start dict")        
        if ( "id" in d1 ) and ( "coordinates" in d1 ) and (d1["id"] == ident) :
            #print ("\nDetalhes do Novo posto encontrado")
            #print (d1)
            #print ("\n")
            #print (d1["coordinates"])
            detalhesadic = detalhesadic + "\n" + (d1["id"]) + " --> " + str(d1["party_id"]) + " "+ str(d1["coordinates"]["latitude"]) + " " + str(d1["coordinates"]["longitude"]) + " " + str(d1["city"]) + " " + str(d1["address"]) + " " + str(d1["parking_type"]) 
            #detalhesadic = detalhesadic + str(d1) + "\n"
            nomeactual=d1["id"]
            if ( "evses" in d1) :
                conta=0
                for cada in d1["evses"] :
                    detalhesadic = detalhesadic + "\n" + (str (d1["evses"][conta]["connectors"]))
                    conta=conta+1
            detalhesadic = detalhesadic + "\n"
        for k in d1:
            #print ("            Encontrar dentro dict")
            #if (k == "coordinates") :
                #print ("        Encontrada coord:")
                #print (levelglobal)
                #print (k)
                #verificar se estão na watch list
                #result = [ "%s " %nomeactual, "%s: " % path, "%s : %s" % (k, d1[k])]
                #levelmax=levelglobal
                #print("".join(result))  
                #fich.write ("".join(result))
                #fich.write("\n")


            levelglobal2=levelglobal2+1
            finddetails(ident, d1[k], "%s -> %s" % (path, k) if path else k)
            levelglobal2=levelglobal2-1

    elif type(d1) is list:
        n=0 
        for j in d1:
            #print ("            Percorrer lista")
            #print (n)
            #print (d1[n])
            #print ("            Encontrada lista, tentando entrar dentro da lista")
            #if ( (d1[n]) == ident ):
            #    print ("Encontrado")
            levelglobal2=levelglobal2+1      
            finddetails(ident,d1[n], "%s -> %s" % (path, n) if path else n)
            levelglobal2=levelglobal2-1 
            n=n+1
        
#-------------------




#get current time
now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")
#print("date and time:",date_time)

#added stations
adicionados=Diff2(latestlist,previouslist)
#print ("Adicionados:",adicionados)

#remover locais que estejam na lista de postos existentes
adicionados=Remove(adicionados,watchlist)
print ("Adicionados:",adicionados)

#new location details
levelglobal2=0
z1=0
detalhesadic=""
for z in adicionados:
	#print (adicionados[z1])
	finddetails (adicionados[z1],datalatest["data"])
	z1=z1+1
#print ("detalhes ficheiro")
print (detalhesadic)


#removed stations
removidos=Diff1(latestlist,previouslist)
#print ("Removidos:",removidos)

#remover locais que estejam na lista de postos existentes
removidos=Remove(removidos,watchlist)
print ("Removidos:",removidos)

   
#check number of stations
#if (latestcount != previouscount):
#    print ("Encontradas diferenças")
#else:
#    print ("Sem alterações")


  



#comparação ponto a ponto



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
    fich.write(str(detalhesadic))
    #fich.write("\n")
    fich.write("Removidos:")
    fich.write(str(removidos))
    fich.write("\n")
    escreverfich=1

#else:
    #print ("Sem alterações")


#encontrar ponto com o mesmo id


n=0
#for x in range(10):
for x in datalatest["data"]:
    m=0
    #obter id latest
    id1=datalatest["data"][n]["id"]
    #procurar o mesmo id no previous
    for j in dataprevious["data"]:
        if ( id1 == dataprevious["data"][m]["id"] ):
            #print ("Encontrado no previous, comparando:",id1)
            findDiffB(id1, datalatest["data"][n],dataprevious["data"][m])
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


