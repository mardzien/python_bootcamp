def add_matrices(macierz_a, macierz_b):
    macierz_c = []
    wiersz_wynikowy = []
    for index_w, wiersz in enumerate(macierz_a):
        for index_k, kolumna in enumerate(wiersz):
            wiersz_wynikowy.append(kolumna + macierz_b[index_w][index_k])
    macierz_c.append(wiersz_wynikowy)
    return macierz_c

def sub_matrices(macierz_a, macierz_b):
    macierz_c = []
    wiersz_wynikowy = []
    for index_w, wiersz in enumerate(macierz_a):
        for index_k, kolumna in enumerate(wiersz):
            wiersz_wynikowy.append(kolumna * macierz_b[index_w][index_k])
    macierz_c.append(wiersz_wynikowy)
    return macierz_c


if __name__ == "__main__":
    print(__file__)
    print(dir())
    print(globals())
    print(__name__)
    print("XXXXXXX")