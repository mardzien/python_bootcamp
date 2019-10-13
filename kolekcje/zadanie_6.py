"""

Napisz program zliczający liczbę znaków pomiędzy nawiasami "< >"

"""


napis = " Ala <ma kota>, a kot ma alę"

licznik = 0
czy_zliczac = False
for znak in napis:
    if znak == ">":
        czy_zliczac = False
    if czy_zliczac:
        licznik += 1
    if znak == "<":
        czy_zliczac = True


print(f"Liczba znaków pimiędzy nawiasami to : {licznik}")