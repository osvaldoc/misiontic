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
    archivo_grabado = open("bichos_depurados.csv", "a", encoding="utf8")
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
        #vida real - no print-> almacenarlo en otra parte, por general
        #en una base de datos SQL
        #columnas a una variable
        #fecha = row[0],    mes	= row[1],  nombre_sitio= row[2]	,   proceso	= row[3]
        #punto	= row[4] ,  phylum	= row[5],    clase	= row[6],   orden	= row[7]
        familia	= row[8]
        morfoespecie	= row[9]
        abundancia	= row[10]
        densidad= row[11]
        #algortmos, calculos matematicos, XXX???
        #normalmente pongo DB -> mysql, oracle, postgresql, sqlserver 
        #simulamos la grabada bichos_depurados.csv
        archivo_grabado.write(morfoespecie+"\n")
        #print(familia)
    archivo_grabado.close()
    #ETL: Extraer, Transformar, Cargar(Load)
    
    