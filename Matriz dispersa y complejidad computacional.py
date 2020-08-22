import matplotlib.pyplot as plt
from time import perf_counter
from scipy.sparse.linalg import spsolve

import numpy as np
import scipy.sparse as scsp
import scipy.linalg as sp

def matriz_laplaciana(n):
    return 2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)

def matriz_laplaciana_dispersa(n):    
    qq= 2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
    ww=np.matrix(qq)
    return scsp.csr_matrix(ww)

#valores=[2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000,5000,10000]
valores=[2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000,5000]
veces=3


tiempo_solver_matriz_llena=[]
tiempo_creacion_matriz_llena=[]
for i in valores:  
    promedio_trabajo_lleno=[]
    promedio_creacion_lleno=[]
    for j in range(veces):  
        t0=perf_counter()
        m=matriz_laplaciana(i)      
        A=np.matrix(m)
        b=np.matrix(np.ones(i)) 
        t1=perf_counter()
        x= np.matmul(A**-1,b.T)
        t2=perf_counter()   
        promedio_trabajo_lleno.append(t2-t1)
        promedio_creacion_lleno.append(t1-t0)
        
    tiempo_solver_matriz_llena.append(np.mean(promedio_trabajo_lleno))  
    tiempo_creacion_matriz_llena.append(np.mean(promedio_creacion_lleno))
    

 

tiempo_solver_matriz_dispersa=[]
tiempo_creacion_matriz_dispersa=[]
for i in valores:  
    promedio_trabajo_dispersa=[]
    promedio_creacion_dispersa=[]
    for j in range(veces):  
        t0=perf_counter()
        A=matriz_laplaciana_dispersa(i)      
        b=np.ones(i)
        t1=perf_counter()
        x=spsolve(A,b)
        t2=perf_counter()    
        promedio_trabajo_dispersa.append(t2-t1)
        promedio_creacion_dispersa.append(t1-t0)
        
    tiempo_solver_matriz_dispersa.append(np.mean(promedio_trabajo_dispersa))  
    tiempo_creacion_matriz_dispersa.append(np.mean(promedio_creacion_dispersa))
    

col="r"
lineas=['c','m','b','y']
segm='.'


 
plt.title('Rendimiento  A*x=b')

plt.suptitle("Matriz llena")
plt.subplot(2, 2, 1)
plt.plot(valores,tiempo_solver_matriz_llena,color=col)
plt.plot(valores,[max(tiempo_solver_matriz_llena)]*len(valores),color=lineas[0],label=segm)

plt.ylabel("Tiempo transcurrido (seg.)")
plt.yscale('log')
plt.xscale('log')

valores_x=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
xTicks = valores_x
xTicks_Text = valores_x

yTicks = [0.0001,0.001,0.01,0.1,1,10,60,600]
yTicks_Text = ['0.1ms','1ms','10ms','0.1s','1s','10s','1min','10min']
plt.yticks(yTicks, yTicks_Text)
plt.xticks(xTicks, xTicks_Text)  



plt.subplot(2, 2, 2)
plt.plot(valores,tiempo_creacion_matriz_llena,color=col)
plt.plot(valores,[max(tiempo_creacion_matriz_llena)]*len(valores),color=lineas[0],label=segm)

plt.yscale('log')
plt.xscale('log')

valores_x=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
xTicks = valores_x
xTicks_Text = valores_x

yTicks = [0.0001,0.001,0.01,0.1,1,10,60,600]
yTicks_Text = ['0.1ms','1ms','10ms','0.1s','1s','10s','1min','10min']
plt.yticks(yTicks, yTicks_Text)
plt.xticks(xTicks, xTicks_Text) 



plt.subplot(2, 2, 3) 
plt.plot(valores,tiempo_solver_matriz_dispersa,color=col)
plt.plot(valores,[max(tiempo_solver_matriz_dispersa)]*len(valores),color=lineas[0],label=segm)
plt.ylabel("Tiempo transcurrido (seg.)")
plt.xlabel("Tamaño matriz N")

plt.yscale('log')
plt.xscale('log')

valores_x=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
xTicks = valores_x
xTicks_Text = valores_x

yTicks = [0.0001,0.001,0.01,0.1,1,10,60,600]
yTicks_Text = ['0.1ms','1ms','10ms','0.1s','1s','10s','1min','10min']
plt.yticks(yTicks, yTicks_Text)
plt.xticks(xTicks, xTicks_Text) 



plt.subplot(2, 2, 4)
plt.plot(valores,tiempo_creacion_matriz_dispersa,color=col)
plt.plot(valores,[max(tiempo_creacion_matriz_dispersa)]*len(valores),color=lineas[0],label=segm)

plt.yscale('log')
plt.xscale('log')

valores_x=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
xTicks = valores_x
xTicks_Text = valores_x

yTicks = [0.0001,0.001,0.01,0.1,1,10,60,600]
yTicks_Text = ['0.1ms','1ms','10ms','0.1s','1s','10s','1min','10min']
plt.xlabel("Tamaño matriz N")
plt.yticks(yTicks, yTicks_Text)
plt.xticks(xTicks, xTicks_Text) 

plt.show()