from ejercicio_funciones_6 import order_words

def test_order_words_correctly():
    assert order_words("Orange-Apple-Rambutan-Pineapple") == "Apple-Orange-Pineapple-Rambutan"

def test_order_repeated_words_correctly():
    assert order_words("Grape-Banana-Apple-Pineapple-Cherry-Grape-Apple") == "Apple-Apple-Banana-Cherry-Grape-Grape-Pineapple"

def test_oder_words():
    assert order_words("") == ("")