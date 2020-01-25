"""

Funkcja sprawdzająca, czy jest liczba pierwsza

"""


def czy_jest_pierwsza(liczba):
    """Sprawdza, czy liczba jest liczbą pierwszą

    >>> czy_jest_pierwsza(10)
    False
    >>> czy_jest_pierwsza(17)
    True

    :param liczba:
    :return:
    """
    for i in range(2, liczba):
        czy_pierwsza = False
        if liczba % i == 0:
            return False
    return True

