

dzien_tygodnia = 1
suma = 0

while dzien_tygodnia <=7:
    temp = int(input(f"Podaj temperaturę w {dzien_tygodnia} dzień tygodnia: "))
    suma = suma + temp
    dzien_tygodnia += 1

print(f"Średnia temperatura w tym tygodniu to: {suma / dzien_tygodnia}")