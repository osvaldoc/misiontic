# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:59:51 2021

@author: Osvaldo
"""

import csv

#Reto: Solicitar el codigo del municipio e imprimir el nombre, el departamento y la region

# probar y adicionar en el open, encoding="utf-8"
with open('C:/sources/misiontic/semana7/Departamentos_y_municipios_de_Colombia.csv', newline='',encoding="utf-8") as File:
  reader = csv.reader(File)
  for row in reader:
      #Codificar aca utilizar comandos como input, split, print, condicional
      print(row)