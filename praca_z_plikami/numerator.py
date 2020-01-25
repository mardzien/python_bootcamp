from collections import defaultdict

from faker import Faker
# 1. Napisz funkcję, która ponumeruje linie w pliku:

def ponumeruj(nazwa_pliku):
    with open(nazwa_pliku) as f:
        for count, line in enumerate(f, start=1):
            print(count, line.rstrip())

# 2. Napisz funkcję, która zwróci liczbę linii w pliku
def liczba_linii_1(plik):
    with open(plik) as f:
        # for c, line in enumerate(f, start=1):
        #     pass
        c = sum(1 for line in f)
    return c


def liczba_linii_2(plik):
    with open(plik) as f:
        # for c, line in enumerate(f, start=1):
        #     pass
        c = sum(1 for line in f)
    return c

# print(liczba_linii("numerator.py"))
# 3. Korzystając z faker utwórz plik z losowa treścią
def losowa_tresc(nazwa="losowa.txt", n=1000):
    faker = Faker("pl_PL")
    text = faker.text(n)
    with open(nazwa, 'w') as f:
        f.write(text)

losowa_tresc(n=100000)
# 4. Napisz funkcję, która zliczy częstotliwość występowania liter w pliku

def zlicz_znaki(text):
    zliczenia = defaultdict(int)
    znaki = set(text)
    znaki = znaki - set([" ", "\n"])
    for znak in znaki:
        zliczenia[znak] = text.count(znak)
    return zliczenia

def czestotliwosc_liter(plik):
    with open(plik) as f:
        text = f.read().lower()
        zliczenia = zlicz_znaki(text)
    return zliczenia

# for litera, licznik in sorted(czestotliwosc_liter("losowa.txt").items(), key=lambda x: x[1], reverse=True):
#     print(f"{litera}: {licznik}")

# 5. Napisz funkcję, która zliczy częstotliwość występowania słów w pliku
#    Wypisz w formacie słowo: ilosc  - posortuj od najczęsciej używanych do tych najrzadszych


def czestotliwosc_slow(plik):
    slowa = defaultdict(int)
    with open(plik) as f:
        text = f.read().lower()
        text = text.replace(".", "")
        text = text.split()
        for slowo in text:
            slowa[slowo] += 1

    return slowa

for slowo, licznik in sorted(czestotliwosc_slow("bible.txt").items(), key=lambda x: x[1], reverse=True)[:30]:
    print(f"{slowo}: {licznik}")

# with open("1000000_linii.txt", 'w') as f:
#     for i in range(1000000):
#         f.write(str(i))