"""

funkcja licząca znaki pomiędzy określonymi znakami- domyślnie <>

"""


def policz_znaki (napis, sep1 = '<', sep2 = '>'):
    licz = False
    licznik = 0
    poziom = 0
    for znak in napis:
        if znak == sep1:
            poziom += 1
        elif znak == sep2:
            poziom -= 1
        elif poziom:
            licznik += poziom

    return licznik


def test_policz_znaki_pusty_napis():
    assert policz_znaki("") == 0

def test_policz_znaki_dodatkowe_nawiasy():
    assert policz_znaki('', '[', ']') == 0

def test_policz_znaki_1_poziom_zaglebienia():
    assert policz_znaki('Ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('<aa><bb>')

def test_policz_dla_x_poziomu_zaglebienia():
    assert policz_znaki('<a<<<a>>>>') == 5