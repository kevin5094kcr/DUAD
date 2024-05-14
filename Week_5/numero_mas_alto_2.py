# Ejemplo numero 2 con el contador 

# Inicializa el contador de números ingresados
count = 0

# Lista que almacena los números ingresados
numbers = []

# Pide al usuario que ingrese 10 números y agregarlos a la lista
while count < 10:
    number = int(input("Ingrese un número: "))
    numbers.append(number)
    count += 1

# Imprime todos los números ingresados
print("Los números ingresados fueron:", numbers)

# Encuentra el número más alto en la lista
max_number = numbers[0]  # Asignar el primer número como el máximo inicialmente

for num in numbers:
    if num > max_number:
        max_number = num

# Imprime el número más alto
print("El número más alto fue:", max_number)