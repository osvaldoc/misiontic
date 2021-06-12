# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 08:09:12 2021

@author: Osvaldo
"""

class Triqui:
    ''' m es el numero de filas, n el numero columnas'''
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.mat = [] * (m + 1)
        for i in range(m + 1):
            a = [0] * (n + 1)
            self.mat.append(a)
            
    def imprimeMatrizPorFilas(self, mensaje="Matriz sin nombre "):
        print("\n", mensaje)
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                '''\t es un tabulador \n enter '''
                print(self.mat[i][j], "\t", end="")
            print()
    
    def jugar(self, fila, columna, ficha):
        #Si es cero deje jugar, sino saque error mensaje no puede jugar
        if self.mat[fila][columna] == 0:
            self.mat[fila][columna] = ficha
        else:
            print("Casilla ocupada")
       
    def evaluar_triqui_filas(self,ficha):
        if self.mat[1][1] == ficha and self.mat[1][2] == ficha and self.mat[1][3] == ficha:
            print("triqui en " + ficha)
        if self.mat[2][1] == ficha and self.mat[2][2] == ficha and self.mat[2][3] == ficha:
            print("triqui en " + ficha)
        if self.mat[3][1] == ficha and self.mat[3][2] == ficha and self.mat[3][3] == ficha:
            print("triqui en " + ficha)
        else:
           pass

    def evaluar_triqui_columnas(self,ficha):
        if self.mat[1][1] == ficha and self.mat[2][1] == ficha and self.mat[3][1] == ficha:
            print("triqui en " + ficha)
        if self.mat[1][2] == ficha and self.mat[2][2] == ficha and self.mat[3][2] == ficha:
            print("triqui en " + ficha)
        if self.mat[1][3] == ficha and self.mat[2][3] == ficha and self.mat[3][3] == ficha:
            print("triqui en " + ficha)
        else:
            pass


    def evaluar_triqui_diagonales(self,ficha):
        if self.mat[1][1] == ficha and self.mat[2][2] == ficha and self.mat[3][3] == ficha:
            print("triqui en " + ficha)
        if self.mat[1][3] == ficha and self.mat[2][2] == ficha and self.mat[3][1] == ficha:
            print("triqui en " + ficha)
        else:
            pass
        
    def evaluar_todo(self, ficha):
        self.evaluar_triqui_filas(ficha)
        self.evaluar_triqui_columnas(ficha)
        self.evaluar_triqui_diagonales(ficha)
        
        