# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 20:19:24 2021

@author: Osvaldo
https://docs.python.org/3/library/csv.html
"""
#libreria para trabajar csv
import csv
#abre el archivo con open, variable y cierra-"close automaticamente", 
#los CSV , es como un excel filas - columnas son separadas por , o ;
#por defecto el toma coma (,) 
with open("bichos.csv", "r", encoding="utf8") as csvfile:
    #convierte un archivo a csv para procesar, 
    #pilas como esta separado si es ; delimiter = ';'
    reader = csv.reader(csvfile, delimiter=';')
    #linea por linea
    contador = 0
    for row in reader:
        #esto es igual a decir contador = contador + 1
        contador += 1
        #row es  "list" row[0] - row[4] - row[9]
        #en este caso posicion nombre bicho
        print(row[9])
    
    