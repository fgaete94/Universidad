import numpy as np
#debemos crear una lista con 10 numeros aleatorios entre 1 al 100, luego copiar ese arreglo en otro y mostrar por pantalla el valor maximo, minimo,
#la suma de todos los valores, el promedio y el arreglo 2 completo.

arreglo=[]
for i in range (10):
    arreglo.append(np.random.randint(1,100))
print(arreglo)
arreglo2=arreglo[:].copy()


print("el numero mayor de el arreglo 2 es: ",arreglo2.max())
print("el numero menor del arreglo 2 es:",arreglo2.min())
print("la suma de todos los elementos del arreglo 2 es: ",arreglo2.sum())
print("la media del arreglo 2 es: ",arreglo2.mean())
print("los elementos del arreglo 2 son:")
print(arreglo2)