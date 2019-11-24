

lista = [3, 1, 2]

#lista.sort()
print(sorted(lista))


def lacz(a, b):
    wynik = b + a
    return wynik[::-1]

print(lacz("mama", "tata"))


slownik = {'a': 1}
print(slownik.get('k'))