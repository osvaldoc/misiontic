# -*- coding: utf-8 -*-
"""
Created on Sat May 29 08:12:37 2021

@author: Osvaldo
"""

#1. Realizar un algoritmo que dada la edad de una persona defina 
#si puede "votar", en caso contrario mostrar "no puede votar"

#Tecnicamente califica Osvaldo: 5.0 - Docente radical: 0

edad=int(input("Por favor digite su edad: "))
#cuando se habla de condicion SIEMPRE debe dar 
#FALSO - VERDADERO
if edad >= 18:
    print("Puede votar")
else:
    print("No puede votar, ya que es menor de edad")
    
# 1. Realizar el mismo algoritmo con validaciones necesarias y 
# limitando la edad # a 110años suponiendo que digitaron bien numeros 
#y enteros

# 2. Mas adelante-> try - except -> que significa Exception en python, 
# cuando digitan cadena "diez", o un decimal (flotante, float) 4.874

