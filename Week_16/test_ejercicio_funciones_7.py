from ejercicio_funciones_7 import is_prime

def test_if_numbers_are_prime():
    primes = [num for num in [1, 4, 6, 7, 13, 9, 67] if is_prime(num)]
    assert primes == [7, 13, 67]

def test_if_numbers_are_prime():
    primes = [num for num in [1, 4, 6, 9,] if is_prime(num)]
    assert primes == []





