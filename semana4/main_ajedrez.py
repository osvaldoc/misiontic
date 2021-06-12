# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 09:34:25 2021

@author: Osvaldo
"""
from ajedrez import Ajedrez
tablero=Ajedrez()
tablero.llenar_matriz_numeros_aleatorios()
tablero.imprimeMatrizPorFilas(mensaje="Ajedrez")
tablero.recorrer_diagonal_secundaria1()