"""

Funkcja sprawdzająca, czy napis jest palindromem

"""

def is_palindrome(napis):
    napis = napis.lower()
    return napis == napis[::-1]

def czy_palindrom(napis):
    Flaga = True
    for element in napis:
        if element.lower() != element.lower():
            Flaga = False
    return Flaga

def test_czy_palindrom():
    assert czy_palindrom("ala") == True
    assert czy_palindrom("xddd") == False