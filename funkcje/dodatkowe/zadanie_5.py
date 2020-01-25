"""

Napisz funkcję, która sprawdzi, czy napis jest pangramem - w j angielskim

"""

import string

napis = "The quick brown fox jumps over the lazy dog"

def is_pangram(napis, alfabet = string.ascii_lowercase):
    napis = set(napis.lower())
    napis.remove(" ")
    alfabet = set(alfabet)
    return napis == alfabet

def test_is_pangram():
    assert is_pangram("The quick brown fox jumps over the lazy dog") == True
    assert is_pangram("asdaa naaa") == False
    assert is_pangram("Śnij formę klech z wag bądź żółć pustyń", ) == True