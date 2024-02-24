#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import collections
import csv

from datetime import datetime

# Opening JSON file
with open('./LATEST_static.json') as json_file:
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

with open('./PREVIOUS_static.json') as json_file2:
#with open('./teste_f.json',encoding="utf-8-sig") as json_file2:
    #json_file2.encoding='utf-8-sig'
    dataprevious = json.load(json_file2)

#ler pontos sujeitos a verificacao
##with open('./lista.txt', newline='') as lista_file:
##    reader = csv.reader(lista_file)
##    watchlista = list (reader)
#print ("Watchlista: ",watchlista)

latestlist=list()    
previouslist=list()
watchlist=list()

n=0
for i in datalatest["energyInfrastructureTable"]:
    latestlist.append(i["energyInfrastructureSite"])
    n=n+1
latestcount=n
print ("Pontos actuais: ",latestcount)    
print (latestlist[0]["name"],"§",latestlist[0]["energyInfrastructureStation"]["infrastructureStationIndex"])
#print (latestlist[0]["energyInfrastructureStation"]["infrastructureStationIndex"])
#print ("\n")
#print (latestlist[1])


n=0
for i in dataprevious["energyInfrastructureTable"]:
    previouslist.append(i["energyInfrastructureSite"])
    n=n+1
previouscount=n
print ("Pontos anteriores: ",previouscount)
print (previouslist[0]["name"],"§",previouslist[0]["energyInfrastructureStation"]["infrastructureStationIndex"])
#print (previouslist[0])
#print (previouslist[1])

##n=0
##for element in watchlista:
    #print ("Teste")
##    if (len(element)) == 1 :
        #print (str(element[0]))
##        watchlist.append(str(element[0]))
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
    #print ("    ident a procurar:",ident,"\n")
##    print (d1)
    #print ("\n\n")
    if type(d1) is dict:
        #print ("É dicionário")    
        #print (d1["energyInfrastructureSite"]["name"])
        if ( "energyInfrastructureSite" in d1 ) and ( "name" in d1["energyInfrastructureSite"] ) and (d1["energyInfrastructureSite"]["name"] == ident) :
            print ("\nDetalhes do Novo posto encontrado")
            print (d1["energyInfrastructureSite"]["energyInfrastructureStation"]["infrastructureStationIndex"],d1["energyInfrastructureSite"]["energyInfrastructureStation"]["operator"]["OrganisationSpecification"]["nationalOrganisationNumber"],d1["energyInfrastructureSite"]["siteLocation"]["pointByCoordinates"]["pointCoordinates"]["latitude"],d1["energyInfrastructureSite"]["siteLocation"]["pointByCoordinates"]["pointCoordinates"]["longitude"],d1["energyInfrastructureSite"]["address"]["detailedAddressInformation"]["city"],d1["energyInfrastructureSite"]["address"]["detailedAddressInformation"]["street"])
            #print ("\n")
            #print (d1["coordinates"])
            detalhesadic = detalhesadic + "\n" + (d1["energyInfrastructureSite"]["name"])
            detalhesadic = detalhesadic + " "+ str(d1["energyInfrastructureSite"]["energyInfrastructureStation"]["infrastructureStationIndex"])
            detalhesadic = detalhesadic+ " --> " + str(d1["energyInfrastructureSite"]["energyInfrastructureStation"]["operator"]["OrganisationSpecification"]["nationalOrganisationNumber"]) 
            detalhesadic = detalhesadic + " "+ str(d1["energyInfrastructureSite"]["siteLocation"]["pointByCoordinates"]["pointCoordinates"]["latitude"])
            detalhesadic = detalhesadic + " " + str(d1["energyInfrastructureSite"]["siteLocation"]["pointByCoordinates"]["pointCoordinates"]["longitude"])
            detalhesadic = detalhesadic + " " + str(d1["energyInfrastructureSite"]["address"]["detailedAddressInformation"]["city"])
            detalhesadic = detalhesadic + " " + str(d1["energyInfrastructureSite"]["address"]["detailedAddressInformation"]["street"]) 
            #detalhesadic = detalhesadic + str(d1) + "\n"
##            nomeactual=d1["id"]
            if ( "refillPoint" in d1["energyInfrastructureSite"]["energyInfrastructureStation"]) :
                conta=0
                print ("Encontrado evse")
                for cada in d1["energyInfrastructureSite"]["energyInfrastructureStation"]["refillPoint"] :
                    detalhesadic = detalhesadic + "\n" + (str (d1["energyInfrastructureSite"]["energyInfrastructureStation"]["refillPoint"][conta]))
                    print (d1["energyInfrastructureSite"]["energyInfrastructureStation"]["refillPoint"][conta])
                    conta=conta+1
            detalhesadic = detalhesadic + "\n"
##        for k in d1:
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


##            levelglobal2=levelglobal2+1
##            finddetails(ident, d1[k], "%s -> %s" % (path, k) if path else k)
##            levelglobal2=levelglobal2-1

    elif type(d1) is list:
        print ("É lista")
        n=0 
        for j in d1:
            #print ("            Percorrer lista")
            #print (n)
            #print (d1[0])
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

adicionados=0
removidos=0

#added stations
adicionados=Diff2(latestlist,previouslist)
print ("Adicionados:",adicionados,"\n\n")

#remover locais que estejam na lista de postos existentes
##adicionados=Remove(adicionados,watchlist)
##print ("Adicionados:",adicionados)

#new location details
levelglobal2=0
z1=0
detalhesadic=""
print ("Begin procurar detalhes")
for z in adicionados:
    print ("Z1:",z1," Procurando:",adicionados[z1]["name"],"\n")
    #print (adicionados[z1]["name"])
    finddetails (adicionados[z1]["name"],datalatest["energyInfrastructureTable"])
    z1=z1+1
#print ("detalhes ficheiro")
print (detalhesadic)


#removed stations
removidos=Diff1(latestlist,previouslist)
#print ("Removidos:",removidos)

#remover locais que estejam na lista de postos existentes
##removidos=Remove(removidos,watchlist)
##print ("Removidos:",removidos)

   
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
    #print ("Start find Diff B ",ident)
    #print (d1)
    #print (d2)
    if type(d1) is dict:
        #print ("            Start dict")        
        for k in d1:
            if k in d2:
                #print (k)
                #print (path)
                #print ("            Encontrar dentro dict\n",d1[k],"\n",d2[k],"\n\n")
                if (d1[k] != d2[k]):
                    #print ("            Encontrada diferença dict, tentando entrar dentro do dict\n",d1[k],"\n",d2[k],"\n\n")
                    findDiffB(ident,d1[k],d2[k], "%s -> %s" % (path, k) if path else k)
                    if (reportar == 1) and (k != "energyInfrastructureStation") and (k != "connector") and (k != "electricChargingPoint") and (k != "refillPoint"):                    
                        print ("Reportar: ", k)
                        print ("\n",ident)
                        if (escreverfich == 0):
                            fich = open("changes.txt", "a") 
                            fich.write("\n")
                            fich.write(date_time)
                            fich.write("\n")
                            escreverfich=1
                        fich.write("\n")
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
            print ("            Start list")
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
    fich.write("Adicionados:\n")
    for cada1 in adicionados :
        fich.write(str(cada1["name"]))
        fich.write("\n")
    #fich.write("\n")
    #fich.write(str(adicionados))
    #fich.write("\n")
    fich.write(str(detalhesadic))
    fich.write("\n")
    fich.write("Removidos:\n")
    for cada2 in removidos :
        fich.write(str(cada2["name"]))
        fich.write("\n")
    #fich.write(str(removidos))
    #fich.write("\n")
    escreverfich=1

#else:
    #print ("Sem alterações")


#encontrar ponto com o mesmo id


#n=0
#for x in range(10):
for xa in datalatest["energyInfrastructureTable"]:
    m=0
    #obter id latest
    #print (xa["energyInfrastructureSite"]["name"])
    id7=xa["energyInfrastructureSite"]["name"]
    #procurar o mesmo id no previous
    for j in dataprevious["energyInfrastructureTable"]:
        if ( id7 == j["energyInfrastructureSite"]["name"] ):
            #print ("Encontrado no previous, comparando:",id7)
            #print ("Encontrado no previous, comparando:",id7," §§§ ",x["energyInfrastructureSite"])
            findDiffB(id7, xa["energyInfrastructureSite"],j["energyInfrastructureSite"])
            m=m+1
#    n=n+1


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


