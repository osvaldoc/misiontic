# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:25:34 2021

@author: Osvaldo
"""
from a import A

class B(A):
    def __init__(self):
        pass
    
    '''
    esta forma de remplazar un metodo que viene heredado se le llama 
    SOBRECARGA DE METODOS
    
    def mostrar_mensaje(self):
        return "Estoy mostrando el mensaje de B"
    
    '''
    
    ''' a este se le llama polimorfismo, significa que un metodo 
    DEL MISMO NOMBRE puede  tener diferentes funcionalidades, SOLO CAMBIANDO LOS PARAMETROS
    '''
    def mostrar_mensaje(self, 
                    mensaje="Estoy mostrando el mensaje de B"):
        return mensaje
