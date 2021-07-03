# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:29:30 2021

@author: Osvaldo
"""
#mire es "w" PUEDEN probar con "a" y observen que sucede
archivo=open("archivo_sencillo.txt","w", encoding="utf8")
#como hacer para que quede separado linea por linea
#colocando \n -> salto de linea
archivo.write("hola amiguitos\n")
archivo.write("hola mintic\n")
archivo.write("NOS VEMOS A LAS 8:00PM CON LA SOLUCION\n")
#que pasa si no pongo close()???????
archivo.close()


