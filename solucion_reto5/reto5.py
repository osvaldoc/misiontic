# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 10:23:17 2021

@author: Osvaldo
"""
import csv
ruta_archivo_csv="analisis_archivo.csv"
encabezado = "Fecha\tConcepto\n"

with open('TSLA.csv', 
          newline='',
          encoding="utf-8") as csvtesla:
     reader = csv.DictReader(csvtesla)
     analisis_csv=open(ruta_archivo_csv,"w",encoding="utf-8")
     analisis_csv.write(encabezado)
     fecha_bajo=None
     fecha_alto=None
     precio_bajo=float('inf') #infinito
     precio_alto=0
     for row in reader:
        precio = float(row['Close'])
        fecha = row['Date']
        if precio<200:
            concepto="MUY BAJO"
        elif precio>=200 and precio <300:
            concepto="BAJO"
        elif precio >=300 and precio < 500:
            concepto="MEDIO"
        elif precio >= 500 and precio < 600:
            concepto="ALTO"
        elif  precio >= 600:
            concepto="MUY ALTO"
         
        #analizar el alto
        precio_a = float(row['High'])
        if precio_a > precio_alto:
            precio_alto = precio_a
            fecha_alto = fecha
            
        precio_b = float(row['Low'])
        if precio_b < precio_bajo:
            precio_bajo = precio_b
            fecha_bajo = fecha
            
        analisis_csv.write(row['Date']+"\t"+concepto+"\n")
     analisis_csv.close()
     
#print(precio_alto, fecha_alto)
print(precio_bajo, fecha_bajo)
    
    
