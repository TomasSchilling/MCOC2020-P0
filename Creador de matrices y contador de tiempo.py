# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:30:59 2020

@author: Arkantos
"""

""" Multiplicador de matrices con tiempo agregado"""

import numpy as np
from time import perf_counter

n=1000
A= np.random.rand(n,n)
B= np.random.rand(n,n)

t0 = perf_counter()

C= np.dot(A,B)

t1 = perf_counter()

print (t1-t0,"seg")

print( "para n=1 000 se tardo 0.02497 seg. y para n= 10 000 se tardo 17.6334 seg.")

print("Se corroboro que efectivamente es un mutliplicador de matrices",A[0][0]*B[0][0], C[0][0])
