# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 17:32:45 2021

@author: Osvaldo
"""

#Clase o un objeto es cualquier cosa que atributos,
#Vehiculos, Animales, Personas, Semaforo

#con palabra class definimos que es un objeto

class Vehiculo:
    ''' 
     A esto se le llama CONSTRUCTOR
     Puede ser vacio o con parametros o con los 
     atributos: marca, color, numero_puertas, velocidad o parametros
     __init__ :  siempre va con ese nombre
    '''
    def __init__(self, marca, color, numero_puertas, velocidad):
        self.marca = marca
        self.color = color
        self.numero_puertas = numero_puertas
        self.velocidad = velocidad
        
    def funcion1():
        pass
        
    def calcular_velocidad():
        pass
    
    def abrir_puerta():
        pass
    
    ''' Esto es un metodo en POO -> Programacion orientada o objetos
      son como funciones pero de un objeto '''
    def es_veloz(self):
        if self.velocidad >= 100 :
            return "Este vehiculo es muy veloz"
        else:
            return "Este vehiculo es una lenteja"
    