# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 20:12:40 2021

@author: Osvaldo
"""
#a append 
#w -> me remplaza el archivo
#a -> no remplaza el archivo, sino que adiciona a la ultima linea
archivo=open("archivo_sencillo_1.txt", "a", encoding="utf8")
archivo.write("hola amiguitos\n")
archivo.write("hola mintic\n")
archivo.write("NOS VEMOS A LAS 8:00PM CON LA SOLUCION\n")
#que pasa si no pongo close()???????
archivo.close()
