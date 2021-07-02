# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:37:23 2021

@author: Osvaldo
"""

archivo = open("C:/sources/misiontic/semana7/nuevo_archivo_lectura.txt","a")

seguir_ciclo = True
print("===== Ingrese los paises ===========")
while seguir_ciclo:
    pais=input("Digite el pais: ")
    archivo.write(pais)
    pregunta_salir=input("Desea seguir ingresando paises S/N : ")
    if pregunta_salir == "S" or pregunta_salir == "s":
        seguir_ciclo = True
    elif pregunta_salir == "N" or pregunta_salir == "n":
        seguir_ciclo = False
    else:
        print("Que paso si dije que es S o N: ?")
archivo.close()
