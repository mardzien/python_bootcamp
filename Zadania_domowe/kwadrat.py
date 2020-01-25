"""

Idealny kwadrat to każda liczba, która ma całkowity pierwiastek kwadratowy
4 jest doskonałym kwadratem, 5 nie. 9 jest doskonałym kwadratem, 10 nie. 100 jest, 1000 nie.. itd itd
Napisz funkcję, która to sprawdzi.

"""

import math

print(isinstance(1, str))

def kwadrat_doskonaly(a):

    if isinstance(a, str):
        raise TypeError("Tu jest napis zamiast liczby.")
    if a < 0:
        return False
    pierwiastek = math.sqrt(a)
    if pierwiastek.is_integer() == True:
        return True
    else:
        return False

print(kwadrat_doskonaly("as"))