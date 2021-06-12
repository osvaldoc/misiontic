# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:12:57 2021

@author: Osvaldo
"""
#Clase hereda matriz
from matriz import Matriz

class Ajedrez(Matriz):
    def __init__(self):
        #Definimos que matriz es de 8,8
        Matriz.__init__(self, 8, 8)
    
    
    def recorrer_reina(self):
        pass        

    def recorrer_diagonal_principal(self):
        #Para I desde 1 hasta 9
        for i in range(1, self.m + 1):
            print("Fila columna: "+ str(i) + " Valor dentro "+ str(self.mat[i][i]))


    def recorrer_diagonal_secundaria1(self):
        ''' Abajo hasta arriba [8,1] [7,2] [6,3] [5,4] [4,5] 
        a medida que va incrementando una la otra va disminuyendo
        '''
        col = 1
        #para fila desde 8 hasta 1 decremente
        for fila in range(8, 0, -1 ):
            print("Fila: "+ str(fila) +" columna: " + str(col) + " Valor: " + 
                  str(self.mat[fila][col]))
            #incremento o contador
            col = col + 1



    def recorrer_toda_matriz(self):
        #Para I desde 1 hasta 9
        for i in range(1, self.m + 1):
            #Para J desde 1 hasta 9
            for j in range(1, self.n + 1):        
                print("fila: "+ str(i) + " col:" + str(j) +" Valor dentro "+ str(self.mat[i][j]))
    
    def recorrer_torre(self):
        pass       
    