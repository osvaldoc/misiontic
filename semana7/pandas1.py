# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 07:32:42 2021

@author: Osvaldo
"""

import pandas as pd
#https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr/data
#no se sube porque es pesado, hay que descargarlo y ponerlo en su carpeta respectiva
archivo="C:/tmp/Casos_positivos_de_COVID-19_en_Colombia.csv"
#Leer archivo covid
df=pd.read_csv(archivo)
#filtro solo los fallecidos
df_fallecidos=df[df['Estado']=='Fallecido']
seguir_ciclo=True
while  seguir_ciclo:
    codigo_municipio=input("Digite el municipio a consultar:")
    df_fallecidos_mun=df_fallecidos[df_fallecidos['Código DIVIPOLA municipio']==int(codigo_municipio)]
    print("En su municipio murieron", len(df_fallecidos_mun))
    salir = input("Desea seguir consultado el municipio S/N ")
    if salir == "S" or salir == "s":
        seguir_ciclo = True
    elif salir == "N" or salir == "n":
        seguir_ciclo = False
    else:
        print("Tontuelo dije S/N no otra letra")
        seguir_ciclo = False
#Nos vemos a las 10:10am, preparen retos que sus compañeros van a ayudar