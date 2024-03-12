#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import collections
import csv

from datetime import datetime

now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Ler ficheiro latest

with open('./latest.csv', newline='') as busy_file:
    reader = csv.reader(busy_file, delimiter=';')
    datalatest = list (reader)

#print (type(datalatest))
#print (type(datalatest[1][1]))
#print (datalatest[1][1])
#leitor = csv.reader (datalatest[2][0])

#print (leitor)


#lista= dict (leitor)
#print (lista)


#ler pontos a vigiar
with open('./watchbusy.txt', newline='') as busy_file:
    reader = csv.reader(busy_file)
    watchbusy = list (reader)

escreverfich=0


for x in datalatest:
    #procurar em cada um dos elementos
    #print (x[0],"§",x[15])
    if "uso" in x[15]:
        #print ("Found",x[0])
        #verificar se está na watchlist
        for y in watchbusy:
            if str(y[0]) in str(x[0]):
                #print (y[0])
                print ("Está na watchlist",str(y[0]))
                if (escreverfich==0) :                
                    escreverfich=1
                    fich = open("charging.txt", "a") 
                    fich.write("\n")
                    fich.write(date_time)
                    fich.write("\n")    
                result = [ "%s " %x[0] ]
                print("".join(result)) 
                fich.write("".join(result))
                fich.write("\n") 





if escreverfich == 1:
    fich.close()
