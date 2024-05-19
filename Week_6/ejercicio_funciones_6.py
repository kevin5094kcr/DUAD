#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#a. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#b. Ejemplo: “python-variable-función-computadora-monitor” → “computadora-función-monitor-python-variable”

def order_words(input_str):
    word_list = input_str.split("-")
    sorted_list = sorted(word_list)
    result_str = "-".join(sorted_list)
    return result_str

input_str = "python-variable-función-computadora-monitor"
ordered_str = order_words(input_str)

print("Ordered string:", ordered_str)