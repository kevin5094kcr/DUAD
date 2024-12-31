from Bubble_Sort_1 import bubble_sort

def test_small_list():
    list = [15, 8, 9]
    bubble_sort(list)
    assert list == [8, 9, 15]


def test_large_list():
    lista = list(range(115, 0, -50))
    bubble_sort(lista)
    
    result = sorted(list(range(115, 0, -50)))
    assert lista ==  result


def test_empty_list():
    lista = [] 
    bubble_sort(lista) 
    assert lista == []  
