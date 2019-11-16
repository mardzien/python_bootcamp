"""

1. Stwórz klasę Postac - niech ma atrybuty: imie, zycie, sila
2. Stwórz klasę Przedmiot - niech ma atrybuty: bonus do ataku, bonus do obrony, nazwa, miejsce
3. Postac ma atrybut atak wyliczany na podstawie sily i bonusów od przedmiotów
4. Stwórz funkcję obsługującą grę
5. Powinna być na niej jakś plansza o wymiarach x, y
6. Na planszy mogą pojawić się przedmioty, czy inne postaci
7. Jak wejdziemy na pole z przedmiotem to go bierzemy o ile miejsce w ekwipunku pozwala
8 gdy trafimy na inną postać - walka

"""

import random

class Postac:
    def __init__(self, imie, zycie, sila):
        self.imie = imie
        self.zycie = zycie
        self.sila = sila
        self.ekwipunek = []

    @property
    def atak(self):
        base = self.sila + sum([x.bonus_ataku for x in self.ekwipunek])
        return int(base*random.random())

    def wez_przedmiot(self, item):
        self.ekwipunek.append(item)

    def obrazenia(self, sila):
        self.zycie -= sila

    @property
    def zyje(self):
        return self.zycie > 0

    def __str__(self):
        return f"{self.imie}, żyje={self.zyje}"

class Przedmiot:
    def __init__(self, nazwa, bonus_ataku, bonus_obrony, miejsce):
        self.nazwa = nazwa
        self.bonus_ataku = bonus_ataku
        self.bonus_obrony = bonus_obrony
        self.miejsce = miejsce

class Polozenie:
    def __init__(self, x, y, zasieg_x, zasieg_y):
        self.x = x
        self.y = y
        self.zasieg_x = zasieg_x
        self.zasieg_y = zasieg_y

    def __str__(self):
        return f"Pozycja x = {self.x}, y = {self.y}"

    def gora(self):
        self.y += 1
        if self.y > self.zasieg_y:
            print("Wypadłeś poza planszę")
            exit()

    def dol(self):
        self.y -= 1
        if self.y < 0:
            print("Wypadłeś poza planszę")
            exit()

    def prawo(self):
        self.x += 1
        if self.x > self.zasieg_x:
            print("Wypadłeś poza planszę")
            exit()

    def lewo(self):
        self.x -= 1
        if self.x < 0:
            print("Wypadłeś poza planszę")
            exit()

class Plansza:
    def __init__(self, gracz, bot, przedmiot, x = 10, y = 10):
        self.x = x
        self.y = y
        self.gracz = gracz
        self.bot = bot
        self.przedmiot = przedmiot
        self.polozenie_gracza = Polozenie(random.randint(1, 10), random.randint(1, 10), x, y)
        self.polozenie_bota = Polozenie(random.randint(1, 10), random.randint(1, 10), x, y)
        self.polozenie_przedmiotu = Polozenie(random.randint(1, 10), random.randint(1, 10), x, y)


def gra():
    hero1 = Postac("Superman", 200, 200)
    hero2 = Postac("Hulk", 200, 200)

    while not hero1.zyje and hero2.zyje:
        hero2.obrazenia(hero1.atak)
        if hero2.zyje:
            hero1.obrazenia(hero2.atak)
    print(hero1, hero2)

def plansza():
    x_1 = random.randint(1, 10)
    y_1 = random.randint(1, 10)

    x_2 = random.randint(1, 10)
    y_2 = random.randint(1, 10)

gra()