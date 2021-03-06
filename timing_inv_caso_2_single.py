from scipy import matrix, rand, linalg
from time import perf_counter
from random import randint
from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
memoria = [[],[],[],[],[],[],[],[],[],[]]
nm = [2, 5, 10,12, 15, 20,30, 40, 45, 50, 55,60, 75, 100,125, 160, 200,250, 350, 500,600, 800, 1000,2000, 5000, 10000]
 #dimension de matrices

for i in range(0,10):
    for N in nm:
        A = np.single(matrix(rand(N,N)))

        C= np.linalg.inv(A)


        mem = 3*(N**2)*8
        memoria[i].append(mem)


#grafica memoria
plt.plot(nm,memoria[0],nm,memoria[1],nm,memoria[2],nm,memoria[3],nm,memoria[4],nm,memoria[5],nm,memoria[6],nm,memoria[7],nm,memoria[8],nm,memoria[9])
#etiqueta ejes
plt.xlabel("Dimension matriz N")
plt.ylabel("Memoria utilizada")
#Titulo
plt.title("Rendimiento Single(A)")
#malla
plt.grid(True)
#mostrar grafico
plt.show()
