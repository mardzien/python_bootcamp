macierz_A = [[1, 2], [2, 1]]
macierz_B = [[5, 2], [5, 1]]


lista = [9, 8, 7]

for index, element in enumerate(lista):
    print(index, element)

def dodaj_macierze (A, B, C = 0):
    macierz_wynikowa = []
    try:
        for index_wiersza, wiersz in enumerate(A):
            wiersz_tymczasowy = []
            for index_kolumny, element in enumerate(wiersz):
                if C == 0:
                    wiersz_tymczasowy.append(element + B[index_wiersza][index_kolumny])
                else:
                    wiersz_tymczasowy.append(element + B[index_wiersza][index_kolumny] + C[index_wiersza][index_kolumny])
            macierz_wynikowa.append(wiersz_tymczasowy)
        #print(macierz_wynikowa)
        return macierz_wynikowa
    except IndexError:
        print("Macierze mają różne rozmiary")


print(dodaj_macierze(macierz_A, macierz_B, macierz_B))