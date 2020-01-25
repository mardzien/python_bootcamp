"""

Funkcja sprawdzająca, czy jest liczba pierwsza

"""
import pytest

def czy_jest_pierwsza(liczba):

    for i in range(2, liczba):
        czy_pierwsza = False
        if liczba % i == 0:
            return False
    return True


    def test_czy_jest_pierwsza_dla_liczby_pierwszej():
        assert czy_jest_pierwsza(11) == True
        assert czy_jest_pierwsza(17) == True
        assert czy_jest_pierwsza(7) == True