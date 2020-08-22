# MCOC2020-PO

# Mi computador principal

* Marca/Modelo: Lenovo ideapad
* Tipo: Notebook
* Año Adquisicion: 2017
* Procesador:
  * Marca/Modelo: intel Core i7-7500U
  * capacidad base: 2,7GHz
  * Velocidad Maxima: 3,5GHz
  * Numero de nucleos: 2
  * Numero de hilos: 4
  * Arquitectura: Nehalem
  * Set de instrucciones: 64-bit
* Tamaño de las caches del procesador
  * L1: 128kb
  * L2: 512kb
  * L3: 4Mb
* Memoria
  * Total: 8192 Mb
  * Tipo Memoria: DDR3
  * Velocidad Memoria: 2133 MHz
  * Numero de (SO)DIMM: 1
* Tarjeta Grafica
  * Marca/Modelo: Intel HD Graphics 620(integrada)
  * Meoria dedicada: -
  * Resolucion: 1920 x 1080
* Disco Unico:
  * Marca: Samsung 
  * Tipo: SSD
  * Tamaño: 118 GB
  * Particiones: 3
  * Sistema de archivos: NTFS
* Dirección MAC de la tarjeta wifi: 58-00-53-F1-31-3D
* Dirección IP (Interna, del router): 192.168.100.1 
* Dirección IP (Externa, del ISP): 181.43.140.65
* Proveedor de internet: Entel

# Desempeño MATMUL

![AB_plot_performance](/Figure_1.png)

* ¿Como difiere del gráfico del profesor/ayudante?
 * El el grafico obtenido se puede notar que aumenta mucho mas el tiempo a medida que aumentan las dimensiones de la matriz
* ¿A qué se pueden deber las diferencias?
 * Esto puede deberse a las distintas caracteristicas de cada ordenador, al tener distintos procesadores y memoria se pueden obtener distintos resultados
* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
 * Esto puede deberse a que al medir memoria se esta evaluando el almacenamiento ocupado al desarrollar este ejercicio(no depenede de la operacion para obtener el resultado), mientras que el tiempo depende de la cantidad de operaciones que se deben realizar(al aumentar las dimensiones aumenta exponencialmente las operaciones a realizar).
 * ¿Qué versión de python está usando?
  *Python 3.6
 * ¿Qué versión de numpy está usando?
  * 1.14
 * Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
 
![Processor_performance](/proce.jpg)

  * Se utilizan 4 procesadores
  
# Desempeño miMATMUL 
![AB_plot_performance](/Figure_2.png)

* ¿Como difiere del gráfico del profesor/ayudante?
 * Se puede notar claramente que los tiempo aumentan de manera considerable, tan asi que luego de 5 horas no terminaba de correr el programa, es por esto que solo se realizaron hasta n=200. 
* ¿A qué se pueden deber las diferencias?
 * Esto puede deberse a que la galeria numpy utilizada en el caso anterior esta codificaca en c, lo cual es un programa de bajo nivel y mucho mas simple de correr para el procesador, numpy esta diseñada para correr de manera optima provechando al maximo los procesadores. Aumentando de esta manera la velocidad en realizar este tipo de operaciones.

 
![Processor_performance](/procesador.jpg)
# Entrega 4
* Diferencias entre scipy.linalg.inv() y numpy.linalg.inv()

![performance_INV(A)](/numpy(invA).png)

![performance_INV(A)](/scipyinv(A).png)

![performance_INV(A)](/scipyoverwriteA.png)

 * Se puede notar que scipy(sin overwrite) es inferior a numpy respecto al tiempo requerido para realizar la misma operacion, tambien se puede notar que los resultados son menos consistentes notando que hay diferencias considerables de tiempo entre las corridas.
 * Al comparar los 2 ultimos graficos se puede notar que cuando se utiliza el comando overwrite() vs scipy los tiempos disminuyen de manera considerable estabilizando tambien los resultados, logrando resultados mas consistentes al hacer 10 corridas.
![Memory_INV(A)](/Single.png)
![Memory_INV(A)](/DoubleA.png)
![Memory_INV(A)](/longdouble.png)

 * Single utiliza numeros de 8 bits y 23 de mantissa, esto hace que utilice poca memoria pero no se lograran resultados tan precisos como cuando se utilizan numeros de mayor bits, en el caso de longdouble y double se utlilizan numero de 11 bits y 52 bits de mantissa lo que nos entregara resultados mas precisos pero con una mayor demanda de memoria.
# Entrega 6
* Diferencias agregando los solvers de scipy y sus distintas opciones que apliquen al caso para resolver el sistema de A*x=b (overwrites, tipos de matriz A, etc).
 
![performance)](/Grafico_6.png)


 * Se puede notar claramente que el metodo menos eficiente es el creado por mi, es decir, invirtiendo la matriz A y luego multiplicarla con el vector b.
 * El punto anterior era esperado ya que las funciones de numpy y scipy estan optimizadas en muchos sentidos y escritas en lenguajes de bajo nivel, lo que hace que el computador encuentre mucho mas rapido las funciones utilizadas.

 * Se puede observar en el grafico que los mejores numero los obtuvieron el scipy.linalg.solve(A,b,pos) y scipy.linalg.solve(A,b,pos con ovewrite) sin notar una mayor diferencias entre estos dos metodos.
 * El programa se corrio con 4 iteraciones de cada metodo y hasta N=8000 ya que en un principio se utilizaron 10 iteraciones con Nmax=10000 y el programa lo detuve luego de 1.5 Horas por tiempo.
# Entrega 7

* COMPLEJIDAD ALGORITMICA DE MATMUL

 * Llena
 
![PERFORMANCE](/MATMUL_LLENA.png)

 * Dispersa
 
![PERFORMANCE](/MATMUL_DISPERSA.png)

* Preguntas
  * Se puede notar que en el caso de la matriz dispersa los timpos de solucion bajan considerablemente, pero los de ensamblado es similar, esto se debe    a que se utiliza la matriz llena para generar la matriz dispersa con el comando csr_matrix. 
  * La complejidad asintotica de ensamblado para la matriz llenay dispersa predominaria N^2. Si nos referimos a el tiempo de solucion en el caso de        matrices llenas tienen un parecido predominante a N^3. La complejidad de solucion en el caso de matrices dispersas se parece a C.
  * Para matrices llemas se puede notar que para tamaños pequeños el tipo disminuye y luego aumenta de manera constante pareciendose a N^2(ensamblado)y N^3(solucion). En matrices dispersas es mas constante, teniendo variaciones pequeñas al variar el tamaño de la matriz.
  * En los casos Matriz llena (solucion y ensamblado) existe una gran dispersion desde N=0 hasta aprox N=200 donde comienza a ser mas consistente. Para    matrices dispersas en general se puede notar mas presicion en las corridas, entre 10 y 100 podria existir una pequeña dispersion de datos pero es        minimo.
 
* COMPLEJIDAD ALGORITMICA DE SOLVE

 * Llena

![PERFORMANCE](/SOLVE_LLENA.png)

 * Dispersa

![PERFORMANCE](/SOLVE_DISPERSA.png)

* Preguntas

  * Se puede notar que en el caso de la matriz dispersa los tiempos de solucion bajan considerablemente, pero los de ensamblado es similar, esto se debe    a que se utiliza la matriz llena para generar la matriz dispersa con el comando csr_matrix. 
  * La complejidad asintotica de ensamblado para la matriz llena y dispersa predominaria N^2. Si nos referimos a el tiempo de solucion en el caso de        matrices llenas tienen un parecido predominante a N^3. La complejidad de solucion en el caso de matrices dispersas se parece a C.
  * Para matrices llemas se puede notar que para tamaños pequeños el tipo disminuye y luego aumenta de manera constante pareciendose a N^2(ensamblado)y    N^3(solucion). En matrices dispersas es mas constante, teniendo variaciones pequeñas al variar el tamaño de la matriz.
  * En los casos Matriz llena (solucion y ensamblado) existe una gran dispersion desde N=0 hasta aprox N=100 donde comienza a ser mas consistente. Para    matrices dispersas en general se puede notar mas presicion en las corridas, entre 10 y 100 podria existir una pequeña dispersion de datos pero es        minimo.

* COMPLE ALGORITMICA DE INV

 * Llena
 
![PERFORMANCE](/INV_LLENA.png)

 * Dispersa

![PERFORMANCE](/INV_DISPERSA.png)

* Preguntas 
 
   * Se puede notar que en el caso de la matriz dispersa los tiempos de solucion bajan ligeramente, logrando mas que nada unos resultados mas parejos       pero los de ensamblado es similar, esto se debe al comando csr_matrix. 
   * La complejidad asintotica de ensamblado para la matriz llena y dispersa predominaria N^2. Si nos referimos a el tiempo de solucion en el caso de       matrices llenas tienen un parecido predominante a N^2 para N<500 y N^3 cuando N>500.  La complejidad de solucion en el caso de matrices dispersas se     parece a N en general.
   * Para matrices llemas se puede notar que para tamaños pequeños el tipo disminuye y luego aumenta de manera constante pareciendose a N^2(ensamblado)y     N^3(solucion). En matrices dispersas es mas constante, teniendo variaciones pequeñas al variar el tamaño de la matriz.
   * En los casos Matriz llena (solucion y ensamblado) existe una gran dispersion desde N=0 hasta aprox N=500 donde comienza a ser mas consistente. Para     matrices dispersas en general se puede notar una dispersion considerable hasta llegar a un Nv= 10, luego de esto se mantiene una dispersion muy         baja.
