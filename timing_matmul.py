
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter

def memory_usage_psutil():
    # return the memory usage in MB
    # obtenida del siguiente link: https://es.stackoverflow.com/questions/16392/calcular-memoria-en-python
    import psutil
    import os
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem


Tiempos=[[],[],[],[],[],[],[],[],[],[],[],[]]
Memoria=[]
valores=[2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000,5000,10000]
for i in range(len(valores)):
    serie=[]
    n=valores[i]
    A= np.random.rand(n,n)
    B= np.random.rand(n,n)
    for a in range (len(Tiempos)):
        
        t0 = perf_counter()    
        C= np.dot(A,B)    
        t1 = perf_counter()    
        Tiempos[a].append(t1-t0)
    Memoria.append(memory_usage_psutil())        

plt.figure()
plt.subplot(2, 1, 1)    
for i in range (len(Tiempos)):
    plt.plot(valores,Tiempos[i])
    
plt.title('Rendimiento  A*B')

plt.ylabel("Tiempo transcurrido (seg.)")
plt.yscale('log')
plt.xscale('log')

    
plt.subplot(2, 1, 2)

plt.plot(valores,Memoria)
plt.ylabel("Memoria utilizada (Mb)")
plt.xlabel("Tamaño matriz N")
plt.yscale('log')
plt.xscale('log')

plt.show() 

