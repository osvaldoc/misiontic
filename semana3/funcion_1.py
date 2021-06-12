# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 18:31:20 2021

@author: Osvaldo
"""

#Cuando creo una funcion, subproceso, procedimiento???
#cuando observo un conjunto de instrucciones que se repiten o las 
#llamo continuamente, esa agrupacion se llama funcion
#lo que hay entre parentesis son parametros 1 o  muchos parametros
def suma_dos_numeros(num1, num2):
    return num1 + num2 #retorna la suma


#suma los numeros como una funcion y retorna los valor
suma_1 = suma_dos_numeros(5,6)
suma_2 = suma_dos_numeros(9,9)
suma_3 = suma_dos_numeros(-54,6)
suma_4 = suma_dos_numeros(8,-14)


print(suma_1)
print(suma_2)
print(suma_3)
print(suma_4)




