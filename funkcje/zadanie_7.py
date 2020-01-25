

lista = [1, 2, 3, 4, 5, 6, 7]

def przytnij(lista, start, stop):
    wynik = []
    czy_zliczac = False

    for element in lista:
        if not czy_zliczac and start(element):
            czy_zliczac = True
        if czy_zliczac == True:
            wynik.append(element)
            if stop(element):
                break
    return wynik


def test_przytnij():
    lista = [1, 2, 3, 4, 5, 6, 7]
    assert przytnij(
        lista,
        start = lambda x: x > 3,
        stop = lambda x: x == 6
    ) == [4, 5, 6]