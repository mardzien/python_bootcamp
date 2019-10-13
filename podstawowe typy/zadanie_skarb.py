"""

zadanie ze znalezieniem skarbu

"""
import random

x_g = random.randint(1, 10)
y_g = random.randint(1, 10)

x_s = random.randint(1, 10)
y_s = random.randint(1, 10)

odleglosc_minimalna = abs(x_s - x_g) + abs(y_s - y_g)
liczba_ruchow = 0

while True:
    odleglosc_przed = abs(x_s - x_g) + abs(y_s - y_g)
    print(f"Jesteś na polu x = {x_g}, y = {y_g}")
    ruch = input("""Wpisz:
    a - żeby wykonać ruch w lewo
    d - żeby wykonać ruch w prawo
    w - żedy wykonać ruch w góre
    s - żeby wykonać ruch w dół
    : """)
    if ruch =="a":
        x_g -= 1
    elif ruch =="d":
        x_g += 1
    elif ruch == "w":
        y_g += 1
    elif ruch == "s":
        y_g -= 1
    else:
        print ("Błędna komenda")
    odleglosc_po = abs(x_s - x_g) + abs(y_s - y_g)

    if x_g > 10 or x_g < 0 or y_g < 0 or y_g > 10:
        print("Wypadłeś poza planszę")
        break

    if odleglosc_po < odleglosc_przed:
        print("Zbliżasz się do skarbu")
    else:
        print("Oddalasz się od skarbu")
    if x_g == x_s and y_g == y_s:
        print("Znalazłeś skarb!")
        break
    liczba_ruchow += 1
    if liczba_ruchow > 2 * odleglosc_minimalna:
        x_s = random.randint(1, 10)
        y_s = random.randint(1, 10)
        odleglosc_minimalna = abs(x_s - x_g) + abs(y_s - y_g)
        print("Jesteś gapa, skarb zmienił swoje położenie!")