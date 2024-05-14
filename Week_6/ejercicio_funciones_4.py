# 4. Cree una función que le de la vuelta a un string y lo retorne.
#a. Esto ya lo hicimos en iterables.
#b. “Hola mundo” → “odnum aloH”

def reverse_str(original_str):
    reversed_str = original_str[::-1] # El slicing [::-1] nos permite tomar el str desde el principio a final, con un paso de -1 nos invierte el orden de los caracteres.
    return reversed_str

original_str = "Hola soy Goku"
reversed_str = reverse_str(original_str)

print("Original string:", original_str)
print("Reversed string:", reversed_str)

