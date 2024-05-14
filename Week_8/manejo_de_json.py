# Creando el archivo JSON para trabajarlo

import json

pokemon = [
    {
        "name": {"english": "Pikachu"},
        "type": ["Electric"],
        "base": {
            "HP": 35,
            "Defense": 40,
            "Sp. Attack": 50,
            "Sp. Defense": 50,
            "Speed": 90

        }
    },
    {
        "name": {"english": "Charmander"},
        "type": ["Fire"],
        "base": {
            "HP": 39,
            "Attack": 52,
            "Defense": 43,
            "Sp. Attack": 60,
            "Sp. Defense": 50,
            "Speed": 65
        }
    },
    {
        "name": {"english": "Squirtle"},
        "type": ["Water"],
        "base": {
            "HP": 44,
            "Attack": 48,
            "Defense": 65,
            "Sp. Attack": 50,
            "Sp. Defense": 64,
            "Speed": 43
        }
    }
]

with open("pokemones.json", "w") as file: # json.dump() convierte la lista de Python en una cadena JSON y la escribe en el archivo especificado
    json.dump(pokemon, file, indent=2) # El argumento indent=2 indica que la salida JSON debe tener una sangría de 2 espacios para que sea más legible