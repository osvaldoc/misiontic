# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:29:03 2021

@author: Osvaldo
"""
#uso de librerias
import math
import sys
import misFunciones as mf

prueba=mf.esPrimo(5)
print("Estamos probando 5",prueba)

prueba=mf.esPrimo(25)
print("Estamos probando 25",prueba)


prueba=mf.esPrimo(7)
print("Estamos probando 7",prueba)

prueba=mf.esPrimo(80)
print("Estamos probando 80",prueba)

#Esta funcion ya la trae python, que tiene
#adentro???? por dentro tiene algoritmo
resultado=math.factorial(5)
print(resultado)

print(sys.api_version)
print("Correcto! grabado con exito!")