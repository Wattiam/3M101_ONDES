#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:06:49 2020

@author: yanisbelhadji
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from F_ode import F_30, E30

#Paramètres:
M1 = 10

#Intervalle de temps
ti = 0
tf = 500
N = 3000    #Nombre de pas
t_ode = np.linspace(ti,tf,N) 

#Conditions initiales
C0 = np.array([5,2,4,4])

#Résolution:
solu = odeint(F_30,C0,t_ode, args = (M1,))

rsolu = solu[:,[0,1]] #On récupère les deux premières colonnes (Phi,Psi)


#Représentation des solutions dans le plan (phi,psi):
fig = plt.figure(1)
plt.clf()

#Mise en forme
ax = fig.add_subplot(1,1,1)

ax.spines['left'].set_position('zero')      #Positionnement de axes au centre
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')      #Suppression des axes inutiles

plt.xticks([])
plt.yticks([])      #Suppression des graduations


plt.plot(rsolu[:,0],rsolu[:,1],'b-',linewidth= 0.3, label = 'MF')

plt.title("Solution de l'équation (30) dans le plan ($\phi$,$\psi$) \n Paramètres:($\phi_0$,$\psi_0$,$\phi_0'$,$\psi_0'$) = ({},{},{},{})\n $\mu$ = {} , Temps = {}" .format(C0[0],C0[1],C0[2],C0[3],M1,tf))

plt.show()

Energie = E30(C0[0],C0[1],C0[2],C0[3],M1)

