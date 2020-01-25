"""

Sprawdzanie, czy liczba jest doskonała

"""


def czy_doskonala(liczba):
    suma = 0
    for i in range(1, liczba):
        if liczba % i == 0:
            suma += i
    if suma == liczba:
        return True
    else:
        return False

def test_czy_doskonala():
    assert czy_doskonala(6) == True
    assert czy_doskonala(28) == True
    assert czy_doskonala(496) == True
    assert czy_doskonala(8128) == True
    assert czy_doskonala(29) == False