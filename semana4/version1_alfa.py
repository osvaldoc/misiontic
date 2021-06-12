# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 08:14:56 2021

@author: Osvaldo
"""
from triqui import Triqui
#inicializamos el triqui
triqui=Triqui(3,3)


seguir_juego = True
jugador_actual = "X"
while seguir_juego == True:
    print("Inicia el jugador "+jugador_actual)
    fila=int(input("Digite la fila:"))
    col=int(input("Digite la columna:"))
    triqui.jugar(fila, col, jugador_actual)
    opcion=input("1. salir del juego \n2. imprimir la triqui \n3.Seguir jugando")
    if opcion == "1":
        seguir_juego = False
    elif opcion == "2":
        triqui.imprimeMatrizPorFilas("Triqui")
    else:
        pass
    #Este condicionas me intercambia jugadores
    if jugador_actual == "X":
        jugador_actual = "A"
    else:
        jugador_actual = "X"
