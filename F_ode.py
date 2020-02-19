#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:02:27 2020

@author: yanisbelhadji
"""

import numpy as np


"""
Définition de la fonction qui renvoie la dérivé de phi,psi,phi prime et psi prime 
pour l'équation 30,33 et 33 modofiée (inédit), dans le format de odeint.
"""

def F_30(tab,t,M):
    phi,psi,vphi,vpsi = tab
    du = np.array([vphi, vpsi, - phi - (phi**2 + M*(psi**2))*phi , -M*psi -M*(phi**2 + M*psi**2)*psi])
    return du


def F_33(tab,t,M):
    phi,psi,vphi,vpsi = tab
    du = np.array([vphi, vpsi, - phi - (phi**2 +psi**2)*phi , -M*psi -(phi**2 +psi**2)*psi])
    return du


def F_inédit(tab,t,M):
    phi,psi,vphi,vpsi = tab
    du = np.array([vphi, vpsi, - phi - ((phi**2 +psi**2)**2) *phi , -M*psi - ((phi**2 +psi**2)**2) *psi])
    return du