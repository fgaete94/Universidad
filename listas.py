#listas
nombres = []

##nombres =["juan","pedro","maria"]
#posicion    0       1      2 
#            -3      -2     -1

#entonces si hago print con un numero entre [] me mostrara por pantalla lo que corresponde a esa posicion en la lista.

#funcion .append(), sirve para agregar algo al final de la lista
nombres.append(3)
print(nombres)
nombres.append("jose")
print(nombres)
apellidos=["letelier","sandoval"]
#con la funcion .extend() agregamos otra lista a la lista
nombres.extend(apellidos)
print(nombres)
#con la funcion .insert() agregamos algo en una posicion especifica
nombres.insert(5,"jaime")
print(nombres)
#con la funcion .remove() lo que hacemos es eliminar un elemento
nombres.remove(3)
print(nombres)
#con la funcion .pop() elimina el ultimo elemento en la lista, pero si le asigno una posicion () elimina el elemento en esa posicion
nombres.pop()
print(nombres)
nombres.pop(3)
print(nombres)
#con la funcion .reverse() revierte el orden de numeros
numeros=[1,2,3]
numeros.reverse()
print(numeros)
#con la funcion .sort() ordena numeros de menor a mayor.
num=[111,20,32]
num.sort()
print(num)

#la diferencia entre los arreglos y las listas, es que los arreglos son solo de un tipo de datos.
