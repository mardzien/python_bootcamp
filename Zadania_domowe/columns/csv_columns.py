import csv


with open('plik.csv', 'r') as plikcsv:
    dane = plikcsv.read()
    slownik = {}
    lista = []
    wiersz = []
    licznik_kolumn = 0
    licznik_wierszy = 0
    for element in dane:
        if element == ",":
            licznik_kolumn += 1
        elif element == " ":
            continue
        elif element == None:
            continue
        elif element == "\n":
            licznik_kolumn = 0
            licznik_wierszy += 1
            wiersz = []
            continue
        else:
            wiersz.append(element)
            continue
        lista.append(wiersz)

klucze = lista[0]

slownik.fromkeys(lista[0], lista[1:])
print(slownik)
indeksy = lista[0]
wartosci = lista[1:]
print(lista)
print(indeksy)
print(wartosci)