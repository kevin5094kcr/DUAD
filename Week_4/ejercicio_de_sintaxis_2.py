nombre = input("Cual es su nombre? ")
apellido = input("Cual es su apellido? ")
edad = int(input("Cual es su edad? " ))

if edad == 0 or edad < 3 :
    print("Eres un bebé")
elif 3 <= edad <= 11:
    print("Eres un niño")
elif 12 <= edad <= 15:
    print("Eres un preadolescente")
elif 16 <= edad <= 18:
    print("Eres un adolescente")
elif 19 <= edad <= 29:
    print("Eres un adulto joven")
elif 30 <= edad <= 59:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")