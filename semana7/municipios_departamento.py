# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 21:45:35 2021

@author: Osvaldo
"""
import pandas as pd
import csv

#Taller2: mostrar cuandos municipios tiene UN departamento
#1.Inicio
#2.Preguntar que departamento desea buscar
codigo_departamento = input("Digite el codigo del departamento:")
#3.Leer el archivo Departamentos_y_municipios_de_Colombia.csv
with open('Departamentos_y_municipios_de_Colombia.csv', 
          newline='',
          encoding="utf-8") as File:
  contador_municipios=0    
#4.Convertir el archivo csv
  reader = csv.reader(File)
#5.Hacer un recorrido
  for row in reader:
#6.preguntar SI es departamento
      if row[1] == codigo_departamento:
#7.si SI entonces contar
        contador_municipios=contador_municipios+1
#8.Imprimir la cantidad de municipios
print(contador_municipios)
#9.Fin
"""
Ejemplo: 5(Antioquia) -> Total municipios: 124
8:40am, tomar como referencia el ejemplo anterior buscar
"""