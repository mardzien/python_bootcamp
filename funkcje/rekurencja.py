import pytest

def silnia(liczba):
    if liczba < 0:
        raise ValueError("Argument musi być większy niż 0.")
    if liczba == 0:
        return 1
    return liczba*silnia(liczba-1)

silnia(5)

def test_silnia():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(2) == 2
    assert silnia(3) == 6

def test_silnia_argument_mniejszy_od_zera():
    with pytest.raises(ValueError) as e:
        silnia(-10)


lista = [10, 20, 30, 40, 50]

def rekuprint(lista):
    print(lista[0])
    if len(lista) > 1:
        rekuprint(lista[1:])