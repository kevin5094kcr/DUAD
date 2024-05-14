#Tenemos dos ejemplos usando el bucle for y usando el range

my_first_string = ["Hola soy Goku"]
string = my_first_string[0]

# Itera sobre el string de derecha a izquierda
#for char in reversed(my_first_string[0]):
    #print(char)

for i in range(len(string) - 1, -1, -1):
    print(string[i])