# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:59:51 2021

@author: Osvaldo
"""

import csv

#Taller: Solicitar el codigo del municipio e imprimir el nombre municipio, 
#el departamento y la region, sino existe el codigo, sacar advertencia
with open('Departamentos_y_municipios_de_Colombia.csv', 
          newline='',
          encoding="utf-8") as File:
  reader = csv.reader(File)
  contador = 0
  codigo_municipio=input("Digite el municipio a buscar: ")
  encontre_municipio=False
  for row in reader:
      contador +=1
      if row[3] == codigo_municipio:
          print("Municipio:",row[4],"\nDepartamento:",row[2],"\nRegion:",row[0])
          encontre_municipio = True
  
  #si es falso
  if not encontre_municipio:      
      print("no existe el municipio con ese codigo ",codigo_municipio )
      
  #-1 es porque encabezado
  #print("Total municipios", contador-1)
      
#probar con su municipio, para saber el codigo de su
#municipio abrir el archivo en excel o buscarlo en el print de python
