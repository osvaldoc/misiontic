# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 21:26:26 2021

@author: Osvaldo
"""

#Como encuentro el elemento mayor de este vector??
v=[8,9,12,15,6,4]
v[0]>v[1] # 8>9
v[1]>v[2] # 9>12
v[2]>v[3] # 12>15

''' Encuentra el mayor dato y lo devuelve valor:15 '''
def encontrar_mayor(v):
    mayor = -1
    for i in range(0,len(v)):
      if v[i] > mayor:
          mayor = v[i]
    return mayor      

var_may= encontrar_mayor(v)
print(var_may)
''' Encuentra el mayor dato y devuelve en posicio lo encontro posicion :3'''
#mientra que la funcion de la guia, devuelve la posicion del mayor
