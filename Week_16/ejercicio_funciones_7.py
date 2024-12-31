# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#a. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#b. Tip 1: Investigue la lógica matemática para averiguar si un numero es primo, y conviértela a código. No busque el código, eso no ayudaría.
#c. Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.

def is_prime(num): 
    print(f"Checking if {num} is prime")
    if num == 1 or num == 0:
        return False
    else: 
        dividers = range(2, num)
        for divider in dividers:
            if num % divider == 0:
                return False
        return True

numbers = [1, 4, 6, 7, 13, 9, 67]

prime_numbers = []

for num in numbers:
    if is_prime(num):
        prime_numbers.append(num)

print("Prime numbers are:", prime_numbers)
