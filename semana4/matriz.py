# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:15:40 2021

@author: Osvaldo
"""
import random

class Matriz:
    ''' m es el numero de filas, n el numero columnas'''
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.mat = [] * (m + 1)
        for i in range(m + 1):
            a = [0] * (n + 1)
            self.mat.append(a)
        
    def llenar_matriz_numeros_aleatorios(self):
        for i in range(1,self.m + 1):
            for j in range (1 , self.n + 1):
                self.mat [i][j] = random.randint(0,99)

    
    def imprimeMatrizPorFilas(self, mensaje="Matriz sin nombre "):
        print("\n", mensaje)
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                '''\t es un tabulador \n enter '''
                print(self.mat[i][j], "\t", end="")
            print()