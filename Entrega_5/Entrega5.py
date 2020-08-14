from scipy import matrix, rand, linalg
from time import perf_counter
from random import randint
from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
def Matriz_Laplaciana(M):
    fila = []
    MatrizA = []
    for i in range(1,M+1):
        for j in range(1,M+1):
            if j==(i-1):
                fila.append(-1)

            elif j==(i):
                fila.append(2)

            elif j==(i+1):
                fila.append(-1)

            else:
                fila.append(0)


        MatrizA.append(fila)
        fila=[]
    return(np.array(MatrizA))
def Vectorb(J):
    vector=[1 for i in range(0,J)]
    return (np.array(vector).reshape(J,1))
tiempo1 = [[],[],[],[],[],[],[],[],[],[]]#en cada lista(10) dentro de esta lista se agregan los tiempos en correr matrices de distintas dimensiones
tiempo2 = [[],[],[],[],[],[],[],[],[],[]]
tf = [[],[]]
contador=0
nm = [1,4,10,11,13,15,20,30,40,45,50,55,60,75,80,100,200,500,1000,5000] #dimension de matrices
#INVERSA
for i in range(0,10):
    for N in nm:
        A = Matriz_Laplaciana(N)
        b = Vectorb(N)

        t1 = perf_counter()
        x = (np.linalg.inv(A))@b
        t2 = perf_counter()

        dt = t2 - t1
        tiempo1[i].append(dt)
for j in range(0,len(tiempo1[0])):
    for i in tiempo1:
        contador = contador + i[j]
    contador=(contador/10)
    tf[0].append(contador)
    contador=0
#NUMPY
for i in range(0,10):
    for N in nm:
        A = Matriz_Laplaciana(N)
        b = Vectorb(N)

        t1 = perf_counter()
        x = np.linalg.solve(A,b)
        t2 = perf_counter()

        dt = t2 - t1
        tiempo2[i].append(dt)
for j in range(0,len(tiempo2[0])):
    for i in tiempo2:
        contador = contador + i[j]
    contador=(contador/10)
    tf[1].append(contador)
    contador=0
file= open("datos3.txt","w")
file.write("Datos inversa\n")
for i in tf[0]:
    file.write('i=%s'%i)
file.write("Datos np.solve\n")
for i in tf[1]:
    file.write('i=%s'%i)
file.close()
tf.append(contador)
#grafica
plt.plot(nm,tf[0],label="INVERSA de A")
plt.plot(nm,tf[1],label="np.Solve")
#etiqueta ejes
plt.xlabel("Dimension matriz N")
plt.ylabel("Tiempo transcurrido (s)")
#Titulo
plt.title("Rendimiento A*b (A)")
#malla
plt.grid(True)

plt.legend(loc=1)
#mostrar grafico
plt.show()
