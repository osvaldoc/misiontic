# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:27:40 2021

@author: Osvaldo
"""
#pilas con slash al leer archivos (\) mejor el backslash /
#Se coloca toda ruta? si es el caso, pero genera un proyecto ponerlo en la misma ruta
#r - read: solo lectura
#w - write: solo escribir
#a - append: abrir y adicionar lineas
#si aparece problemas de tildes uno debe verficar en encoding - utf8 o iso8859-1
#open = abrir, extension, txt, csv, xxx, que se abra desde block de notas
#"no abre" jpg, pdf, png, los mismos son binarios, ahora pueden probar leyendo excel, word
archivo=open("C:/sources/misiontic/semana7/bichos.csv","r", encoding="utf8")

#lea linea por linea hasta final del archivo
#como saber cantidad de lineas?  piensen hasta 7:20pm, en mi caso 476
contador = 0
for linea in archivo.readlines():
    contador = contador + 1
    print(linea)
print("El numero de lineas de mi archivo es:", contador)
#cerrar el archivo, "OBLIGATORIO" cerrar, probar "write"
archivo.close() 


    