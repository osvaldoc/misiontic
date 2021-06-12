# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 18:42:29 2021

@author: Osvaldo
"""
#Funcion, dado un numero entrega el Factorial
#Reutiliza codigo
def factorial(num):
    #validacion 
    if (num >=15 ):
        print("Estas muy desocupado es hasta 14 ")
        return -1
    mult = 1
    for i in range (1, num + 1 ):
        mult = mult * i
    return mult

respuesta = factorial(5)
#print("La respuesta es: ",respuesta)


respuesta2 = factorial(7)
#print("La respuesta es: ",respuesta2)

n =int(input("Entre valor : "))
respuesta3 = factorial(n)
print("La respuesta es: ",respuesta3)
   
