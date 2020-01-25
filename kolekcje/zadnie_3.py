"""

Napisanie tabliczki mnożenia 1 - 10

"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("      ", end='')
for i in lista:
    print(f"{i:5}", end="")
print()
print()

for i in lista:
    print(i, end = '     ')
    for j in lista:
        print(f"{i*j:5}", end='')
    print()

for index, element in enumerate(lista):
    print(index, element)


lista1 = [10, 20, 30, 40]
lista2 = ["a", "b", "c", "d"]

for index, element in enumerate(lista1):
    print(lista2[index]*element)

macierz_a  = [
    [1, 2, 3],
    [4, 5, 6]
]

macierz_b  = [
    [5, 6, 7],
    [8, 9, 10]
]

wynik = []

for row_index, row in enumerate(macierz_a):
    #print(index, row)
    row_wynikowy = []
    for col_index, col in enumerate(row):
        row_wynikowy.append(col + macierz_b[row_index][col_index])
        #print(f"macierz_a wiersz: {row_index} kolumna: {col_index}", col)
        #print(f"macierz_b wiersz: {row_index} kolumna: {col_index}", macierz_b[row_index][col_index])
    wynik.append(row_wynikowy)
wynik = []
i = 0

while i < len(macierz_a):
    wiersz_a = macierz_a[i]
    wiersz_b = macierz_b[i]
    j = 0
    while j < len(wiersz_a):
        col_z_a = wiersz_a[j]
        col_z_b = wiersz_b[j]
        row.append(col_z_a + col_z_b)
        j += 1
    wynik.append(row)
    i += 1
print(wynik)


expected = [
    [6, 8, 10],
    [12, 14, 16]
]

print(wynik)





# assert == expected