from ejercicio_funciones_4 import reverse_str

def test_reverse_string():
    assert reverse_str("Hola soy Goku") == "ukoG yos aloH"

def test_reverse_string_with_special_characters():
    assert reverse_str("¡¡Hola!! Como estas?? ") == " ??satse omoC !!aloH¡¡"

def test_reverse_empty():
    assert reverse_str("") == ""