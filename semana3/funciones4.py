# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 20:33:49 2021

@author: Osvaldo
"""
''' Funcion buscar - "Como la de excel???" '''
#2 parametros , 1. Vector, 2. numero a buscar,
# devuelve la posicion donde lo encontro
#osea v=[15,8,9,12,6,4]
#busque 12, el me entrega 3 -> posicion
#busque 4, el me entrega 5 -> Posicion
#este hay mejorar un poco
def buscarEn(Vec_Ele, numero):
    for i in range(0, len(Vec_Ele)):
        if Vec_Ele[i] == numero:
            return i

#seria bueno comparar y verificar si son iguales las funciones?
def buscarDato (V,d):
  i = 1
  while i <= V[0] and V[i] != d:
    i = i + 1
  if i <= V[0]:
    return i
  return -1

def eliminar_elemento(Vec_Ele, numero):
    for i in range(0, len(Vec_Ele)):
        if Vec_Ele[i] == numero:
            return i

#a un Vector
#1. buscar un elemento devolver la posicion
#2. buscar un elemento devolver si la encontro o no (Falso o Verdadero)
#3. ordernar un vector de mayor a menor, solo numeros
#4. ordernar un vector de menor a mayor, solo numeros
#5. eliminar los repetidos
#6. Sumar/multiplicar/etc los elementos del vector
#7. Operaciones basicas : Insertar, Actualizar, Eliminar 
#8. El elemento mayor del vector
#9. Encontrar los repetidos y sacarlos a otro vector
#10. Sumar 2 vectores

#Como encuentro el elemento mayor de este vector??
v=[8,9,12,15,6,4]






       


    
        