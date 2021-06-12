# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 08:14:43 2021

@author: Osvaldo
"""

salir = "N"
#Declaracion de un array vacio
#Inicialice el arrar con 10 posiciones
#n = int(input(“Entre tamaño del vector ”))
#V = [0] * (n + 1)

v_personas=[0]*5
#contador
i = 0
#mientras salir sea igual N quedese en ciclo
while salir == "N" or salir == "n":
    nombre_persona=input("Digite su nombre: ")
    print("Usted se llama ",nombre_persona)
    ''' asigne el nombre persona a v en posicion i'''
    v_personas[i] = nombre_persona
    #incremento +1
    # if i == len(v_personas): no puedes digitar mas info llenaron 
    i = i + 1
    ''' salir si digitan S '''
    salir=input("Desea salir del sistema S/N ")
    #si salir es otra letra, imprima un mensaje que solo admite 
    #N o S
print(v_personas)

#Cuando sale errores en editor, se le dicen que son errores 
#de sintaxis o compilacion., editor ayuda pero hay  
#errores que no detectados, estos son llamados errores 
#de ejecucion, un ejemplo de error de ejecucion es el siguiente
#IndexError: list assignment index out of range
#Se adiciono la linea 11
    
#Que hace la palabra reservada None, que palabra reservada
    
    