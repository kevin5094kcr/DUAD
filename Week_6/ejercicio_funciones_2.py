# 2. Experimente con el concepto de scope:

#a. Intente accesar a una variable definida dentro de una función desde afuera.

def my_first_function():
    inside_local = 29
    print("Inside the function, inside_local has a value of:",  inside_local)

my_first_function()

#print("Outside of the function, inside_local has a value of:",  inside_local)
# Al imprimir este print dará un error por esta fuera del Scope de inside_local

#b. Intente accesar a una variable global desde una función y cambiar su valor

my_global_variable = 40

def change_value():
    global my_global_variable
    my_global_variable = 45
    print("Inside the function, my_global_variable has a value of:", my_global_variable)

change_value()

print("Outside of the function, my_global_variable has a value of:", my_global_variable)