#3. Cree una función que retorne la suma de todos los números de una lista.
    #1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    #2. [4, 6, 2, 29] → 41

def sum_list(lista):
    suma = 0
    for number in lista:
        suma += number
    return suma

my_list = [1, 2, 3, 4, 5]
result = sum_list(my_list)

print(" The sum of the elements of the list is:", result)

# Cambiar nombres a variables de sum y list 
# Googlear que hace sum y list

# sum:
# La función sum se utiliza para sumar todos los elementos de una lista o de un iterable.
# Puede tomar un iterable de números como argumento y devuelve la suma total de esos números.
# Si se le pasa una lista vacía, devuelve 0.

# list:
# La función list se utiliza para crear una lista a partir de otro iterable (como una cadena, una tupla, un conjunto o un rango).
# Puede tomar un iterable como argumento y devuelve una lista que contiene los elementos de ese iterable, en el mismo orden.