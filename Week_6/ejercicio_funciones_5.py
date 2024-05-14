#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#a. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def count_uppercases_lowercases(input_str):
    # Iniciamos contador 
    upper_count = 0
    lower_count = 0
    
    # Contamos mayúsculas y minúsculas
    for char in input_str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    if upper_count == 1:
        upper_str = "upper case"
    else:
        upper_str = "upper cases"

    if lower_count == 1:
        lower_str = "lower case"
    else:
        lower_str = "lower cases"


    print(f"There's {upper_count} {upper_str} and {lower_count} {lower_str}")

count_uppercases_lowercases("Lyfter Community")

# Crear función de puros if e imprimir el mensaje correcto