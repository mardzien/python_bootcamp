"""
1. Utwórz listę
2. W pętli while wypisz wszystkie elementy listy (print). Skorzystaj z len
3. zrób to samo bez len - obsługa wyjątków w pytonie
try:
    coś tam
except:
    coś jak jest wyjątek
"""



lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
i = 0

while i < len(lista):
    print(lista[i])
    i += 1

i = 0

while True:
    try:
        print(lista[i])
    except IndexError:
        break
    i += 1
