# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:59:08 2021

@author: Osvaldo
"""
from LSL import LSL
from nodoSimple import nodoSimple

a = LSL()

#No tengo idea???? lo comento
#for i in range(1, 10):

d = input("Entre un dato: ")
#y es posicion, primera vez es un 0
y = a.buscarDondeInsertar(d)

#inserta ese valor en "cajon"=nodoSimple
a.insertar(d, y)

#Segunda peticion de insertar datos
d = input("Entre más datos:")
#El 0 me saca del ciclo, pero while, pero continua
#con el ciclo de arriba for que va hasta 10
while d != "0":
   a.agregarDato(d)
   d = input("Entre más datos: ")

# QUE diferencia tiene agregarDato(d) 
#y insertar(d, y)


a.recorrerLista()
l = a.longitud()
print(l)


#A partir de estas lineas por la consola, 
#no ejecutarlo como RUN, sino linea por linea
'''       
y = nodoSimple()
x = a.buscarDato("a", y)
a.borrar(x, y)
print("despues de borrar primer vez")
a.recorrerLista()
l = a.longitud()
print(l)
x = a.primerNodo()
a.borrar(x)

print("despues de borrar segunda vez")
a.recorrerLista()
l = a.longitud()
print(l)

x = a.buscarDato("z", y)
a.borrar(x)
print("despues de borrar tercera vez")

a.recorrerLista()
l = a.longitud()
print(l)
'''