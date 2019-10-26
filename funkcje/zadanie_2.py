"""

Funkcja zwracająca zbiór wszystkich znaków występujących więcej niż x razy, gdzie x jest podawaną zmienną

"""

### Użycie 2 słowników

def wiecej_niz(napis, liczba_znakow):
    liczniki = {}
    wynik = set()
    for znak in napis:
        liczniki[znak] = liczniki.get(znak, 0) + 1

    for znak in liczniki:
        if liczniki[znak] > liczba_znakow:
            wynik.add(znak)
    return wynik

### użycie metody count

def wiecej_niz_2(napis, liczba_znakow):
    wynik = set()
    for znak in set(napis):
        if napis.count(znak) > liczba_znakow:
            wynik.add(znak)
    return wynik

### wyrażenie warunkowe w 1 linii

def wiecej_niz_3(napis, liczba_znakow):
    wynik = set()
    {wynik.add(znak) for znak in set(napis) if napis.count(znak) > liczba_znakow}
    return wynik

print(wiecej_niz_3("ala ma kota, a kot ma alę", 3))

def test_czy_wiecej_niz_dla_pustego():
    assert wiecej_niz_3('', 3) == set()

def test_czy_wiecej_niz():
    assert wiecej_niz_3("Ala ma kota a kot ma alę", 3) == {'a', ' '}