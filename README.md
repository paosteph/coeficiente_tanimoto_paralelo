# coeficiente_tanimoto_paralelo
Cálculo del ceoficiente Tanimoto mediante hilos en Python y en C

El presente proyecto fue desarrollado para la materia de Computación Distribuida de la carrera de Ingenieria de Sistemas de la EPN, Quito - Ecuador

El propósito de este ha sido disminuir los tiempos de ejecución al tratar de calcular el coeficiente tanimoto de 12422 fórmulas químicas, cada una con el resto de ellas.

El código ha sido implementado en los lenguajes de programación Python y C.

REQUISITOS:

* Python https://www.python.org/downloads/

Windows:

  * CodeBlocks http://www.codeblocks.org/downloads
  * Ademas se debe configurar la biblioteca OpenMP que permite realizar la paralelización en C. 
  
Linux:

  * No es necesario instalar OpenMP pues esta ya es parte del compilador GCC, mas bien se debe verificar que esta configurado.
 
 CODIGO:
 
 Se debe ejecutar el archivo .c o .py junto con el archivo ZINC_chemicals.tsv en la misma carpeta
 
 Posteriormente se habrá escrito un archivo de aproximadamante 2.5Gb, que corresponden a las etiquetas de los dos compuestos comparados y su coeficiente tanimoto
 
 Compare tiempos de ejecución de ambos códigos.
