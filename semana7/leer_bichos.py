# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:27:40 2021

@author: Osvaldo
"""
#pilas con slash al leer archivos (\) mejor el backslash/
#Se coloca toda ruta? si en caso,
# pero genera un proyecto ponerlo en la misma ruta
#r - read: solo lectura
#w - write: solo escribir
#a - append: abrir y adicionar lineas a "igual" w
#Cual los archivo y apare problemas de tildes
#uno debe verficar en encoding - utf8 o iso8859-1
#open = abrir
#extension, txt, csv, xxx, block de nota
archivo=open("bichos_mintic.csv","r", encoding="utf8")

#lea linea por linea hasta final del archivo
for linea in archivo.readlines():
    print(linea)

archivo.close()    
    