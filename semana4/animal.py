# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 18:54:46 2021

@author: Osvaldo
"""
#numero patas, familia (hervivoro, mamifero, carnivoro), peligrosidad, nombre_cientifico, 

class Animal:
    def __init__(self, nombre_comun, familia, numero_patas, peligrosidad):
        self.familia = familia
        self.numero_patas=numero_patas
        self.nombre_comun = nombre_comun
        self.peligrosidad=peligrosidad
        
    def es_ave(self):
        pass
        
        
        
        
        