#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.


def main():
    current_number = 0 # Se crea la variable current number y se inicializa en cero

    while True:
        print(f"Current number: {current_number}")
        print("Menu:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. Division")
        print("5. Borrar resultado")
        print("6. Salir")
        
        choice = input("Seleccione una opción: ")

        if choice == "1":
            try: 
                number = float(input("Ingrese el numero a sumar: "))
                current_number += number
            except ValueError:
                print("Error: Ingrese un numero valido.")

        elif choice == "2":
            try:
                number = float(input("Ingrese el numero a restar: "))
                current_number -= number
            except ValueError:
                print("Error: Ingrese un numero valido.")

        elif choice == "3":
            try: 
                number = float(input("Ingrese el numero a multiplicar: "))
                choice *= number
            except ValueError:
                print("Error: Ingrese numero valido.")

        elif choice == "4":
            try:
                number = float(input("Ingrese el numero a dividir: " ))
                if number == 0:
                    print("Error: No se puede dividir por cero.")
                else: 
                    current_number /= number
            except ValueError:
                print("Error: Ingrese numero valido.")

        elif choice == "5":
            current_number = 0
            print("Resultado borrado.")

        elif choice == "6":
            print("Saliendo de calculadora.")
            break

        else:
            print("Error: Opción no es valida")

if __name__ == "__main__":
    main()


