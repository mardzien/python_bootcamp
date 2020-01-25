"""
Napisz program zliczający wystąpienia liczb:
dodatnich i ujemnych
parzystych i nieparzystych
w zadanej liście

dodatnich: <x>
ujemnych: <x>
parzystych: <x>
nieparzystych: <x>
"""
lista = [1, 2, 3, 4, -1, -2, -3, -4, -6]
x = 0
y = 0
z = 0
e = 0

for el in lista:
    if el > 0:
        x += 1
    else:
        y += 1


    if el % 2 == 0:
        z += 1
    else:
        e += 1

print(f"Liczba dodatnich: {x}, ujemnych {y}, parzystych {z}, nieparzystych, {e}")