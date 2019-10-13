###
### Dzisiaj poznamy tuple, zbiory, listy, słowniki

# tworzenie listy
lista = [] #pusta lista
lista1 = [1, 2, 3]
lista2 = [1, "2", "a", 3]
lista3 = [1, "2", ["a", 3]]

# funkcja tworząca listę: list

lista = list() # pusta lista

# lista ma swoje metody
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

print(dir(lista))
print(help(lista.append))

print("lista przed append:", lista)

lista.append(10)

print("lista po append: ", lista)

print(lista.pop())
print("lista po pop:", lista)

### index - zwraca indeks

lista = [1, 2, 3, 4, 5, 6]
index = lista.index(4)
print("Indeks 4 to: ", index)

### reverse - odwrócenie kolejności w liście

lista.reverse()
print("Odwrócona lista: ", lista)

### sort - sortowanie listy

lista.sort()
print("Posortowana lista:", lista)

# slicing - wybieranie

lista = [10, 20, 30, 40, 1, 2, 3, 4, 50, 60, 70]
print(lista[4:])
print(lista[:4])
print(lista[3:7])
# [start:stop:step]
print(lista[::2])
print(lista[1::2])

######
# tupla: tuple
# z listy mogę zrobić tuplę
moja_tupla = (1, 2, 3, 4, 5, 6)
print(moja_tupla)


################
# set - zbiór

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

### suma
print(A | B)
# różnica
print(A - B)
print(B - A)
#koniunkcja
print(A & B)
# różnica symetrycna
print (A ^ B)