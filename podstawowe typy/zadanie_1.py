"""
korzystając ze zmiennych oblicz

1. Pole prostokąta o wymiarach 7x14
2. Pole trójkąta, gdzie podstawa to 2, a wysokość to 4
3. Objętość kuli o promieniu 6

wynik wypisz przy pomocy funkcji print

"""
### podpunkt 1
a = 7
b = 14

pole_prostakata = a * b
print(pole_prostakata)

### podpunkt 2

a = 2
h = 4

pole_trojkata = 1/2* a * h
print(pole_trojkata)

### podpunkt 3
import math
r = 6
pi = 3.14

objetosc_kuli = 4/3 * math.pi * r**3
print(objetosc_kuli)