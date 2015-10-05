# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:20:20 2015

@author: giacomo
"""
#
from operator import itemgetter
import matplotlib.pyplot
import pylab

with open(r'/home/giacomo/Documents/Progetti/Python IPA game/Sounds/dictionaries/it_ITmod.dic')  as f:     
   with open(r'/home/giacomo/Documents/Progetti/Python IPA game/Sounds/dictionaries/lista4.txt', 'w') as csvfile:
       for i in f:
           csvfile.write(i.split("/")[0].replace("'","").replace("\n","")+"\n")
           
from collections import defaultdict          
          
composti={
"sce":"0",
"sci":"0",
"gli":"5",
"gn":"2",
"go":"7",
"ga":"7",
"ghe":"7",
"ghi":"7",
"che":"7",
"chi":"7",
"ci":"6",
"tt":"1",
"dd":"1",
"ll":"5",
"nn":"2",
"rr":"4",
"mm":"3",
"ss":"0",
"pp":"9",
"zz":"0",
"cc":"7",
"gg":"6",
"ff":"8"
}
lettere={
"è":"",
"é":"",
"ò":"",
"ì":"",
"à":"",
"ù":"",
"a":"",
"b":"9",
"c":"7",
"d":"1",
"e":"",
"f":"8",
"g":"6",
"h":"0",
"i":"",
"j":"5",
"k":"7",
"l":"5",
"m":"3",
"n":"2",
"o":"",
"p":"9",
"q":"7",
"r":"4",
"s":"0",
"t":"1",
"u":"",
"v":"8",
"w":"8",
"x":"0",
"y":"",
"z":"0",
#forin letters
"ç":"0",
"â":"",
"ô":"",
 
 }
 
def conver(frase):
   
   for i in composti:
     frase2=frase.lower().replace(i,composti[i])
     frase=frase2
     
   for j in lettere:
     frase3=frase.replace(j,lettere[j])
     frase=frase3 
   return frase3
   
   
def convertfile(path=r'/home/giacomo/Documents/Progetti/Python IPA game/Sounds/dictionaries/lista4.txt'):
    d = defaultdict(list) 
    with open(path, 'r') as text:
        for i in text:
                f=i.strip()
                d[conver(f)].append(f)
    return d

def printfile(path):
    d = defaultdict(list) 
    with open(r'/home/giacomo/Documents/Progetti/Python IPA game/Sounds/dictionaries/lista4.txt', 'r') as text:
        with open(r'/home/giacomo/Documents/Progetti/Python IPA game/Sounds/dictionaries/lista4mod.txt', 'w') as text2:
            for i in text:
                    f=i.strip()
                    d[conver(f)].append(f)
                    text2.write(f+"->"+conver(f)+"\n")

 
import numpy as np
import matplotlib.pyplot as plt



def plotdistribution(dictionary):
    data=[]
    x=[]
    y=[]
    for t in dictionary:
        if t !="":
            data.append([int(t),len(dictionary[t])])
    datasorted=sorted(data, key=itemgetter(0))
    for i in datasorted:
        x.append(i[0])
        y.append(i[1])
    
    #matplotlib.pyplot.scatter(x,y)
    #matplotlib.pyplot.show()
    return x,y 

def ragrupbylenght(dictio):
    grupo=defaultdict(dict) 
    for i in dictio:
        grupo[len(i)][i]=dictio[i]
    return grupo
        
dicti=convertfile()
   