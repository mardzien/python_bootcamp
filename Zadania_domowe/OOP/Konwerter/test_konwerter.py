import pytest
from konwerter import Konwerter

def test_int_to_roman():
    assert Konwerter().int_to_roman(1) == "I"
    assert Konwerter().int_to_roman(4) == "IV"
    assert Konwerter().int_to_roman(3999) == "MMMCMXCIX"


def test_roman_to_int():
    assert Konwerter().roman_to_int("MMMCMXCIX") == 3999
    assert Konwerter().roman_to_int("IV") == 4
    assert Konwerter().roman_to_int("II") == 2