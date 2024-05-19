print("Adivine el numero secreto")

while True:
    numero_secreto = int(input("Cual es el numero secreto? "))
    
    if numero_secreto == 8:
        print("Felicidades, adivinaste el numero secreto")
        break  
    else:
        print("Incorrecto, vuelva a intentarlo")