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


