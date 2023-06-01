import numpy as np
#arreglos, primero importaremos la bibloteca de numpy con el codigo anterior, y luego ejecutamos pip install numpy en la terminal
arreglo=np.array([3,4,12,4,7])

print(arreglo)
#con .ndim vemos cuantas dimensiones tiene el arreglo
print(arreglo.ndim)
#con len vemos la longitud del arreglo
largo=len(arreglo)
print(largo)
#con .shape vemos la dimension
print(arreglo.shape)
#cuando definimos [x:x] nos muestra algo desde un desde hasta un algo anterior  a la posicion que menciono
print(arreglo[1:3])
#cuando definimos [x:x:x] nos muestra de un desde hasta un algo con paso de
print(arreglo[1:3:2])
#cuando definimos [::x] no tiene un inicio ni un fin pero con un paso definido
print(arreglo[::2])
#cuando definimos[x::x] nos muestra un desde un numero hasta el fin con paso de algo
print(arreglo[2::1])

#para crear un arreglo automatico

arreglo2=[i for i in range(0,5)]
print(arreglo2) #crea un arreglo del 0 al 4

#para imprimir el largo del arreglo en sus posiciones
for i in range(len(arreglo)):
    print(f"arreglo en la posicion[{i}]= {arreglo[i]}")

#hay funciones como  para hacer un lista con solo 0 o 1
arreglo3=np.zeros(10)
print(arreglo3)
arreglo4=np.ones(10)
print(arreglo4)

#en la clonacion un arrego se puede igualar a otro y ambos estaran haciendo lo mismo
arreglo5=np.array([1,2,3])
arreglo6=arreglo5[:]
print(arreglo6)
arreglo5[0]=100
print(arreglo5)
print(arreglo6)

# en la copia, los arreglos no haran lo mismo, ya que es una copia del el otro
arreglo7=np.array([1,2,3])
arreglo8=arreglo5[:].copy()
print(arreglo8)
arreglo7[0]=100
print(arreglo7)
print(arreglo8)

#podemos hacer operaciones entre arreglos y estas se ejecutaran entre las mismas posicions que se encuentran en los arreglos respectivos.
#la funcion .sum() suma todos los numeros del arreglo
#la funcion .mean() calcula la mediana de la lista
#la funcion .min() entrega el valor minimo de la lista
#la funcion .max() entrega el valor maximo de la lista
