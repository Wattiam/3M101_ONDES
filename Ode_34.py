#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:31:10 2020

@author: yanisbelhadji
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.integrate import odeint
from F_ode import F_34


#Paramètres:

M1 = 2 #mu

#Intervalle de temps
ti = 0
tf = 300
N = 10000  #Nombre de pas
t_ode = np.linspace(ti,tf,N) 

#Conditions initiales
C0 = np.array([5,3,5,10])


#Résolution:
solu = odeint(F_34,C0,t_ode, args = (M1,))


rsolu = solu[:,[0,1]] #On récupère les deux premières colonnes (Phi,Psi)



## Représentation des solutions :

fig = plt.figure(1, figsize = [9,7], constrained_layout=True)
plt.clf()

#Mise en forme
plt.axis('off')
plt.title("Solution du système (34) \n Paramètres : ($\phi_0$,$\psi_0$,$\phi_0'$,$\psi_0'$) = ({},{},{},{})\n $\mu$ = {} , t = {} \n" .format(C0[0],C0[1],C0[2],C0[3],M1,tf))

gs = gridspec.GridSpec(3, 2)  #Mise en page pour les subplots 

#Tracé de phi en fonction de t:
ax1 = fig.add_subplot(gs[0,0])
plt.title("$\phi = f(t)$", fontsize = 9)

plt.plot(t_ode,rsolu[:,0],'b-',linewidth= 0.3) 


#Tracé de psi en fonction de t:
ax2 = fig.add_subplot(gs[0,1])
plt.title("$\psi = f(t)$", fontsize = 9)

plt.plot(t_ode,rsolu[:,1],'b-',linewidth= 0.3) 


#Tracé de psi en fonction de phi:
ax3 = fig.add_subplot(gs[1:3,:])
plt.title("\n$\psi = f(\phi)$", y=-0.1)

ax3.spines['left'].set_position('zero')      #Positionnement de axes au centre
ax3.spines['bottom'].set_position('zero')

ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')      #Suppression des axes inutiles

plt.xticks([])
plt.yticks([])  #Suppression des graduations

plt.plot(rsolu[:,0],rsolu[:,1],'b-',linewidth= 0.3) 



plt.show()
