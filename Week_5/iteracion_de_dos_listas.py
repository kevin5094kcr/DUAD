first_list = ['Muchas', 'a', 'principiantes', 'programacion', 'cuesta', 'aprender', 'que', 'algo', 'a', 'que', 'cerebro', 'que']
second_list = ['veces', 'los', 'en', 'les', 'mucho', 'ya', 'es', 'nuevo', 'lo', 'su', 'tiene', 'acostumbrarse']

# Itera sobre los elementos de ambas listas al mismo tiempo
for first, second in zip(first_list, second_list): # La funcion zip se usa para iterar dos elementos de dos listas al mismo tiempo
    # La funcion zip solo va funcionar cuando las listas tengan la misma cantidad de elementos, si una tiene menos que otra no va funcionar y van a faltar datos por imprimirse
    # Imprimir los elementos de ambas listas
    print(first, second)
