# Ejemplo numero 1 con range

# Lista que almacena los números ingresados
numbers = []

# Pide al usuario que ingrese 10 números y agregarlos a la lista
for i in range(10):
    number = int(input("Ingrese un número: "))
    numbers.append(number)

# Imprime todos los números ingresados
print("Los números ingresados fueron:", numbers)

# Encuentra el número más alto en la lista
max_number = numbers[0]  # Asignar el primer número como el máximo inicialmente

for num in numbers:
    if num > max_number:
        max_number = num

# Imprime el número más alto
print("El número más alto fue:", max_number)