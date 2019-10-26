lista = [9, 1, 6, 8, 4, 3, 2, 0]

minimum = 9


def sortuj(lista):
    for i in range(len(lista)):
        index_min = i
        for j in range(i, len(lista)):
            if lista[j] < lista[index_min]:
                index_min = j
        lista[index_min], lista[i] = lista[i], lista[index_min]
    return lista

sortuj(lista)

assert lista == [0,1,2,3,4,6,8,9]