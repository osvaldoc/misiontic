# -*- coding: utf-8 -*-
"""
Created on Sat May 29 08:19:30 2021

@author: Osvaldo
"""

#2. Realizar un algoritmo que dado un numero 
#me muestre si es par o impar
numero=int(input("Por favor digite un numero: "))

#Definicion de numero par: 
#Los números pares son aquellos que se pueden dividir 
#entre 2 y obteniendo como resultado un número exacto.
#numero exacto: su residuo es 0

residuo = numero % 2

if numero%2==0:
    print("Es un numero par")
    print("junito")
    print("pepita")
    print("Numero", "numero")
    print("Numero", numero)
else:
    print("Es un impar")    
    