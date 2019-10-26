

def nazwa_funkcji(): # definicja funkcji
    pass

nazwa_funkcji # obiekt funkcji

nazwa_funkcji() # wywołanie funkcji

def powitanie(imie):
    return f"Hello {imie.upper()}"

poczatek = powitanie("Jakieś imię")
print(poczatek)

def operacje(a, b, op = 3):
    print(a + b, op)

operacje(1, 2)
operacje(1, 2, 4)