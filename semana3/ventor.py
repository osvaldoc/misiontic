# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:59:53 2021

@author: Osvaldo
"""

class Vector:
    
    
    ''' Esta fincion contruye un vector y recibe como parametros
    el vector y la cantidad
    '''
    def construyeVector(V, n):
        V[0] = n
        for i in range(1, n + 1):
            V[i] = random.randint(1, 99)
    
    def esVacio(V):
        if V[0] == 0:        
            return True
        return False
    
    def intercambiar(V, i, j):
       aux = V[i]
       V[i] = V[j]
       V[j] = aux