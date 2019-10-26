"""

Funkcja sprawdzająca, czy jest liczba pierwsza

"""
import unittest

def czy_jest_pierwsza(liczba):
    """Sprawdza, czy liczba jest liczbą pierwszą

    :param liczba:
    :return:
    """
    for i in range(2, liczba):
        czy_pierwsza = False
        if liczba % i == 0:
            return False
    return True

class TestCZyJestPierwsza(unittest.TestCase):

    def test_czy_jest_pierwsza_dla_liczby_pierwszej(self):
        self.assertEqual(czy_jest_pierwsza(11), True)
        self.assertEqual(czy_jest_pierwsza(7), True)
        self.assertEqual(czy_jest_pierwsza(17), True)