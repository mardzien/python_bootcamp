lista = [1, 2, 3, 5, 18, 33, 68, 98, 100, 102, 122]

parzyste = set(range(2, 101, 2))

print(len(set(lista) & parzyste))