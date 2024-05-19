# Intercambio del primer y el ultimo elemento de la lista. 
# Debe funcionar con listas de cualquier tamaño

my_list = [8, 4, 6, 2, 7]

# Almacena el valor del primer elemento en este caso 8, es util ya que se puede usar ese valor después
temp = my_list[0]

# Asigna el valor del último elemento al primer elemento
my_list[0] = my_list[-1]

# Asigna el valor almacenado (primer elemento original) al último elemento
my_list[-1] = temp

print(my_list)



