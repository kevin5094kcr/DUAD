# 2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
# a. Debe leer el archivo para importar los Pokémones existentes.
# b. Luego debe pedir la información del Pokémon a agregar.
# c. Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

def read_pokemones():
    with open("pokemones.json", "r") as file:  
        pokemones = json.load(file)# json.load lee los datos del archivo JSON y los carga en la variable 'pokemones'
    return pokemones # Retorna la lista de Pokémones


def add_pokemon(pokemones): # Función para agregar un nuevo Pokemon al archivo existente

    new_pokemon = {} # Crea un diccionario vacío para almacenar la información del nuevo Pokémon

    name = input("Ingrese el nombre del nuevo Pokémon: ")
    type = input("Ingrese el tipo del nuevo Pokémon: ")
    hp = int(input("Ingrese el HP del nuevo Pokémon: "))
    attack = int(input("Ingrese el Ataque del nuevo Pokémon: "))
    defense = int(input("Ingrese la Defensa del nuevo Pokémon: "))
    sp_attack = int(input("Ingrese el Ataque Especial del nuevo Pokémon: "))
    sp_defense = int(input("Ingrese la Defensa Especial del nuevo Pokémon: "))
    speed = int(input("Ingrese la Velocidad del nuevo Pokémon: "))

# Creando la estructura del nuevo pokemon
    new_pokemon["name"] = {"english": name}
    new_pokemon["type"] = [type]
    new_pokemon["base"] = {  
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
    }


    pokemones.append(new_pokemon)

    return pokemones


def save_pokemones(pokemones):
    with open("pokemons.json", "w") as file:
        json.dump(pokemones, file, indent=2)# El argumento indent=2 indica que la salida JSON debe tener una sangría de 2 espacios para que sea más legible


def main():

# Leer los Pokémones existentes del archivo
    existing_pokemones = read_pokemones()

# Agregar un nuevo Pokémon
    updated_pokemones = add_pokemon(existing_pokemones)

# Guardar la lista actualizada de Pokémones en el archivo
    save_pokemones(updated_pokemones)

    print("The new Pokemon has been successfully added. ")


if __name__ == "__main__":
    main() # Llama a la función principal para ejecutar el programa
