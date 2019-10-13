
wynik = []
for i in range(1, 101):
    wynik.append(i**3)

print(wynik)

wynik1 = [i**3 for i in range(1, 101)]
wynik2 = {i**3 for i in range(1, 101)}
wynik3 = (i**3 for i in range(1, 101))

print(wynik1)
print(wynik2)
print(wynik3)

wynik1 = [i**3 for i in range(1, 101) if i % 7 == 0]