---Informacion Pc

Dell inspiron 7559 año 2018


---Prosesador:

Procesador Intel® Core™ i5-6300HQ.

numero nucleos: 4, con 4 suprocesos cada uno.

Processor 2.3GHz (6M Cache, up to 3.20GHz).

Extensiones de conjunto de instrucciones: 
Intel® SSE4.1, Intel® SSE4.2, Intel® AVX2

 ---Tamano de cache del pordcesador:
	
 L1 256 kB
	
 L2 1.0 MB
	
 L3 6.0 MB


---Memoria RAM

8GB 1 DIMM (1x8GB) DDR3L 

1600Mhz

Form Factor: SODIMM.


---Memoria interna

1. Marca: SanDisk  Modelo: Z400s M.2 2280.

 SSD M2  256 GB (5400rpm)  sin particion .

2. Marca: WDC, Modelo : Wd5000BPVT.

 HDD SATA 512 GB(5400rpm) sin particion.


---Graficos:

-1. Intel(R) HD Grafics 530

Frecuencia base	350 MHz

Memoria máxima	64 GB

2. NVIDIA GeForce 960M

Frecuencia base	1097 MHz

Memoria:	4 GB GDDR5 a 5 GHz


---Tarjeta Wi-0fi

Intel Dual Band Wireless-AC 3165


---Proveedor de internet:

GTD Mnaquehue, Fibra Optica

---IP Router 192.168.1.235


Desempeño MATMUL

El grafico no logre ingrsarlo aqui por lo que se adjunta en el github

1. Se puede observar que el rendimiento en tiempo es similar sino un tanto mayor al del profesor, Esto se puede deber a que la presencia de mayor RAM. El prosesador presenta capacidades similares.

2. Esto puede deberse a la cantidad de memoria almacenada en phyton crece cuadraticamente, mientras 
que la cantidad de calculos y operaciones crece de manera cubica, mediente aumenta el tamano de la matriz cuadrada.

3.  Pyhton 3.6 (spyder 4.16) Se utiliza el sobre programa Anaconda.

Fue utilizado un solo prodesador durante la operacion solicitada 



** Matrices dispersas y complejidad computacional**

Codigo de emsablaje y resolucion

```
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
```

Se puede o
