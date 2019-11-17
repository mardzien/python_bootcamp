from faker import Faker
fake = Faker("pl_PL")
from collections import defaultdict

#1. ponumeruj i wypisz linie
def numerator(nazwa_pliku):

    with open(nazwa_pliku, 'r') as fh:
        licznik = 1
        for line in fh.read().splitlines():
            print(f"({licznik}) {line}")
            licznik += 1

numerator("text.txt")
#2. zwróć liczbę linii w pliku
def zwroc_liczbe_linii(nazwa_pliku):
    with open(nazwa_pliku, 'r') as fh:
        licznik = 0
        for line in fh.read().splitlines():
            licznik += 1
    return licznik

print(zwroc_liczbe_linii("text.txt"))

#3. Korzystając z faker utwórz plik z losową treścią

def utworz_losowa_tresc(nazwa_pliku = "losowa.txt", n = 100000):
    text = fake.text(n)
    with open(nazwa_pliku, 'w') as fh:
        fh.write(text)

def zlicz_znaki(text):
    zliczenia = defaultdict(int)
    znaki = set(text)
    znaki = znaki - set([" ", "\n"])
    for znak in znaki:
        zliczenia[znak] = text.count(znak)
    return zliczenia

def czestotliwosc_liter(nazwa_pliku):
    with open(nazwa_pliku) as fh:
        text = fh.read().lower()
        zliczenia = zlicz_znaki(text)
    return zliczenia

#for litera, licznik in sorted(czestotliwosc_liter("fake.txt").items(), key=lambda x:x[1], reverse = True):
#    print(f"{litera}: {licznik}")

def czestotliwosc_slow(nazwa_pliku):
    slowa = defaultdict()
    with open(nazwa_pliku) as fh:
        text = fh.read().lower().split()
        for slowo in text:
            slowa[slowo] += 1
    return slowa

for slowo, licznik in sorted(czestotliwosc_slow("fake.txt").items(), key=lambda x: x[1], reverse = True):
    print(f"{slowo}: {licznik}")

utworz_losowa_tresc("fake.txt")