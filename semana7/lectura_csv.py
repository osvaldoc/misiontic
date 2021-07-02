# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:45:11 2021

@author: Osvaldo
"""

"""
https://www.datos.gov.co/Mapas-Nacionales/Departamentos-y-municipios-de-Colombia/xdk5-pm3f/data
https://docs.python.org/3/library/csv.html
"""

import csv
# probar y adicionar en el open, encoding="utf-8"
with open('C:/sources/misiontic/semana7/Departamentos_y_municipios_de_Colombia.csv', newline='',encoding="utf-8") as File:
  reader = csv.reader(File)
  for row in reader:
     print(row)