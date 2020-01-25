# kawał denerwujący

#while True:
#    odp = input("Opowiedzieć Ci kawał denerwujący? ")
#    if odp.lower() == "nie":
#        break
i = 0
suma = 0
while True:
    x = input("Podaj liczbę lub wpisz \"k\", żeby zakończyć: ")
    if x == "k":
        break
    x = int(x)
    suma = suma + x
    i += 1
if i > 0:
    print("Średnia wynosi: ", suma/i)
else:
    print("Nie podano liczb")