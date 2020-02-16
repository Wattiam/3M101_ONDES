#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:57:16 2020

@author: yanisbelhadji
"""
# Solutions particulières simples :  "mode simple"

from scipy.integrate import odeint
import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

# --> Représentation graphique pour l'équation des ondes de D'Alembert (1)

time = np.linspace(0,1,200)
position = np.linspace(0,np.pi,200)
nb_mode = [5,10,20,300]
plot = 1

plt.figure(1)
plt.clf()

for j in nb_mode:
    mode = np.arange(0,j)
    
    for i in mode:
        
        soluce = np.sin(i*time) * np.sin(i*position)
        plt.plot(time,soluce)
        plt.subplot(2,2,plot)
        
    plot = plot+1


plt.show()
