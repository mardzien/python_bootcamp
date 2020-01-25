"""

W zadanej liście zmień ze sobą miejscami element największy i najmniejszy

"""


lista = [6, 2, 1, 9, 12, 18]
print("Lista przed zamianą: ", lista)

i = sum(lista) / len(lista)
j = sum(lista) / len(lista)

for el in lista:
    if el < i:
        i = el
        index_min = lista.index(el)

    if el > j:
        j = el
        index_max = lista.index(el)

lista[index_min] = j
lista[index_max] = i

print("Lista po zamianie:   ", lista)

i_min_v = 0
i_max_v = 0

for i, v in enumerate(lista):
    if v < lista[i_min_v]:
        i_min_v = i
    if v > lista[i_max_v]:
        i_max_v = i

temp = lista[i_min_v] # wartość minimalna
lista[i_min_v] = lista[i_max_v]
lista[i_max_v] = temp

print("Lista po 2 zmianach: ", lista)