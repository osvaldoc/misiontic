# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:59:08 2021

@author: Osvaldo
"""
from LSL import LSL
from nodoSimple import nodoSimple

a = LSL()
for i in range(1, 10):
    d = input("Entre dato: ")
    y = a.buscarDondeInsertar(d)
    a.insertar(d, y)
    d = input("Entre más datos:")
    while d != "0":
       a.agregarDato(d)
       d = input("Entre más datos: ")
       
a.recorrerLista()
l = a.longitud()
print(l)
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