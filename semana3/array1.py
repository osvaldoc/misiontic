# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 20:17:33 2021

@author: Osvaldo
"""
#Listas o vectores, son como UNA fila en excel
#ASI SE DECLARA aSI
#  0, 1,2, 3,4,5,
#Tamaño del array es 6
#comentario, para tamaño solo pongo la funcion len()
v=[15,8,9,12,6,4]
#print(v[3]) #12
#print(v[5]) #4
len(v) #entregue el tamaño, ejemplo 6
print ("El tamaño del vector es : ",len(v))

#recorrer el vector, lista, array, coleccion, collection
#para i desde 0 hasta 6
for i in range(0, len(v)):
    ''' v[i] se lee asi: V en la posicion i '''
    print("Array posicion",i," = ",v[i]) 

#los array o vectores, pueden tener dentro numero, letras, palabras
v1=["maria","juana","dario","pedro","luis"]
v2=["a","b","c","d"]
v3=["a",45,"juan",3.96,"?$"]




