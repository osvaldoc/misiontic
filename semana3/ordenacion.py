# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 08:45:19 2021

@author: Osvaldo
"""

v=[5,9,3,15,12]
#como ordeno ascendente, video de ayer tambien dice como
#Piensen 9:30am
#
'''
v=[5,9,3,15,12] #compare el valor pos:1 con los demas, en caso encontrar uno menor lo intercambio
v=[3,9,5,15,12] #compare el valor pos:2 con los demas, en caso encontrar uno menor lo intercambio
v=[3,5,9,15,12] #compare el valor pos:3 con los demas, en caso encontrar uno menor lo intercambio
v=[3,5,9,15,12] #compare el valor pos:4 con los demas, en caso encontrar uno menor lo intercambio
v=[3,5,9,12,15]
'''
#A LAS 10AM REGRESAMOS, ciclo dentro de un ciclo, 

# (1):COMPARE el valor pos:1
# con (2):LOS DEMAS, en caso encontrar 
#uno menor lo (3):INTERCAMBIO
v=[5,9,3,15,12]
print("Vector antes: ",v) 
for i in range(0,len(v)):
    #obtengo el valor a comparar
    #valor_a_comparar=v[i]
    #(2)
    for j in range(i + 1, len(v)):
        #(1)
        if v[i] > v[j]:
            aux = v[i]
            v[i] = v[j]
            v[j] = aux
print("Vector despues: ",v) 

#como seria descendentemente?

#SIN FUNCIONES DE PYTHON