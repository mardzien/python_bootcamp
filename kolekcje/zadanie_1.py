"""
Napisz program obliczający  sredbu a warti sc z podanych przez użytkownika liczb.
Liczby przyjmuj z wykorzystanie pętli while i funkcji input
pozwól na podanie maksymalnie 10 liczb
wydrukuj informację o minimalnej i maksymalnej wartości

pamiętaj o funkcjach len, max, min, sum
"""
i = 0 #licznik
k = 0
lista = []

print("Wpisz liczbę lub 'k', aby zakończyć")

while len(lista) < 10:
    k = input(f"Podaj {i + 1} liczbę: ")
    if k == "k":
        break
    try:
        lista.append(int(k))
        i = i + 1
    except:
        print("Wpisuj liczby!")



w_min = min(lista)
w_max = max(lista)
srednia = sum(lista) / len(lista)

print(f"Wartość minimalna to: {w_min}, maksymalna to: {w_max}, a średnia z podanych liczb to: {srednia}")