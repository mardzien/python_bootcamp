"""

Napisz funkcje, które:
- policzy pole kwadratu
- policzy pole prostokąta
- policzy pole trójkąta
- policzy pole koła
- pozwoli na dodanie 2 macierzy o jednakowych wymiarach

"""

def licz_pole_kwadratu(a):
    pole = a * a
    return pole

def licz_pole_prostokata(a, b):
    pole = a * b
    return pole

def licz_pole_trojkata(a, h):
    pole = (a * h)/ 2
    return pole

def licz_pole_koła(r):
    Pi = 3.14
    pole = Pi * r**2
    return pole

def dodaj_macierze(macierz_a, macierz_b):
    macierz_c = []
    wiersz_wynikowy = []
    for index_w, wiersz in enumerate(macierz_a):
        for index_k, kolumna in enumerate(wiersz):
            wiersz_wynikowy.append(kolumna + macierz_b[index_w][index_k])
    macierz_c.append(wiersz_wynikowy)
    return macierz_c

def dodaj_macierze_with_zip(m1, m2):
    wynik = []
    for row_m1, row_m2 in zip(m1, m2):
        row = []
        for col_m1, col_m2 in zip(row_m1, row_m2):
            row.append(col_m1 + col_m2)
        wynik.append(row)
    return wynik

print(dodaj_macierze([[1, 2], [3, 4]], [[5, 6], [7, 8]]))

def test_czy_liczy_pole_kwadratu():
    assert licz_pole_kwadratu(4) == 16

def test_czy_liczy_pole_prostokata():
    assert licz_pole_prostokata(4, 5) == 20

def test_czy_liczy_pole_trojkata():
    assert licz_pole_trojkata(4, 4) == 8.0

def test_czy_liczy_pole_kola():
    assert licz_pole_koła(4) == 3.14 * 4**2
