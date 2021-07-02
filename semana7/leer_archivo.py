# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:27:35 2021

@author: Osvaldo
"""

#Abre un archivo  "r" = read, solo lectura, "a" - Append, "w" - Write
archivo = open("C:/sources/misiontic/semana7/palabras.txt","r")
for linea in archivo.readlines():
    print(linea)
archivo.close()
