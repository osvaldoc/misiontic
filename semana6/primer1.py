# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 08:26:03 2021

@author: Osvaldo
"""
import os
import numpy as np
import pandas as pd

#os me permite instruccines sistema operativo, gecwd, donde estos
#os.getcwd()

#Ruta donde esta el excel, miren que \ sino /
RUTA_EXCEL="C:/sources/misiontic/semana6/" # <-Recuerde un / al final

#RUTA_EXCEL="C:/tmp/"
#RUTA_EXCEL="C:\\tmp\\"

#Es la instruccion que permite leer el excel pd.read_excel
#Se amacena en una variable cualquien nombre, pero los tutotiales
#df ->  dataframe, matriz
df=pd.read_excel(RUTA_EXCEL + "DatosRiesgoCredito.xlsx")

#columas de datraframe
df.columns

#Imprime el tipo de datos de cada columna, entero, decimal
df.dtypes

#Imprime el tipo de datos de cada columna, entero, decimal
df.info()


#Promedio de la edad de esos registros, las 2 inst hacen lo mismo
df.Edad.mean()
df['Edad'].mean()

# .describe() si un numero,entrega estadistica
df['Edad'].describe()


#el metodo .mean -> el promedio
df['Ingresos (U$)'].describe()

# Esta instruccion me mustra mas columnas, en este caso genero, edad 
df[['Genero','Edad']]

# .groupby("Genero") -> agrupe por genero y saca el promedio
df[['Genero','Edad']].groupby("Genero").mean()

#.count() cuenta resgistros
df[['Genero','Edad']].groupby("Genero").count()


#.short organiza by (por)
df[['Genero','Edad']].sort_values(by="Edad")

#La palabra NaN - Nulo, vacio, nada


