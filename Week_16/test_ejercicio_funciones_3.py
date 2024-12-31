from ejercicio_funciones_3 import sum_list

def test_sum_list_of_all_positive_numbers():
    assert sum_list([5, 8, 10, 11]) == 34

def test_sum_list_of_all_negative_numbers():
    assert sum_list([-5, -8, -10, -11]) == -34

def test_sum_empty_list():
    assert sum_list([]) == 0

    