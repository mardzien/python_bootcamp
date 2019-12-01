from collections import namedtuple

Samochod = namedtuple("Samochod", ["rocznik", "silnik", "max_predkosc"])

audi = Samochod(rocznik=2010, silnik="diesel", max_predkosc=220)

print(audi)