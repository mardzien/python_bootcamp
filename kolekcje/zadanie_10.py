"""

W zadanym tekście zlicz wystąpienie każdego znaku

Nie używaj metody.count()

Dane przechowuj w słowniku
"""

napis = "ala ma kota, a kot ma alę"

liczniki = {}

for znak in napis:
    if znak != " ":
        liczniki[znak] = liczniki.get(znak,0) + 1
print(liczniki)