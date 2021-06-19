# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 20:27:33 2021

@author: Osvaldo
"""

#Esto es el vector, pero apartir de este momento lo llamaremos 
#list o array
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
#Me cuenta cuantas manazanas hay en la lista
fruits.count('apple')

#Adiciona un elemento al lista
fruits.append('uchua')

#elementos de un array-list
len(fruits)

#Organiza ascendentemente 
fruits.sort()

#Organiza descendentemente 
fruits.sort(reverse=True)

#En que posicion se encuentra la palabra apple, la prumera que encuente
fruits.index('apple')

# LIFO (Last Input First Output),
# El ultimo en entrar sera el primero en salir
#El pop ELIMINA ELEMento, se asigno pasa saber que elim
fruits.pop()

#descolo el elemento y lo almacena en un variable 
#llamada fruta, motivo, por si lo necesito o para qu ese vea en la pantalla
#pero no es obligatorio
fruta=fruits.pop()



stack = [3, 4, 5]