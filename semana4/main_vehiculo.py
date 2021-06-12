# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 18:38:29 2021

@author: Osvaldo
"""
#De este archivo (from) importeme o traigame clase Vehiculo
from vehiculo import Vehiculo

#La creacion de un objeto
veh = Vehiculo("Audi", "#FF0045", 4, 150)
veh2 = Vehiculo("BMW", "Azul", 4, 85)

print(veh.es_veloz())
print(veh2.es_veloz())


#print(veh.marca,veh.color,veh.numero_puertas )
#print(veh2.marca,veh2.color,veh2.numero_puertas )
