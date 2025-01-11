from ejercicio_funciones_5 import count_uppercases_lowercases, count_uppercases, count_lowercases

def test_count_uppercases_lowercases():
    assert count_uppercases_lowercases("Hello World") == "There's 2 upper cases and 8 lower cases"


def test_count_uppercases():
    assert count_uppercases("Hello World") == "There's 2 upper cases."

def test_count_lowercases():
    assert count_lowercases("Hello World") == "There's 8 lower cases."