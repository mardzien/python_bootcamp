


lista = [1, 2, 3, [4, 5, [6]]]

def splaszcz(lista):
    lista_plaska = []
    for element in lista:
        if isinstance(element, lista):
            for e in splaszcz(element):
                lista_plaska.append(e)
        else:
            lista_plaska.append(element)
    return lista_plaska



def test_splaszcz_pusta_lista():
    assert splaszcz([]) == []

def test_splaszcz_plaska_lista():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]

def test_splaszcz():
    assert splaszcz([1, 2, 3, [4, 5, [6]]]) == [1, 2, 3, 4, 5, 6]