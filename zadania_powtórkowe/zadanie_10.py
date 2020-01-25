
liczba_1 = int(input("Podaj pierwszą liczbę: "))
liczba_2 = int(input("Podaj drugą liczbę: "))

dzialanie = input("Podaj działanie: ")

if dzialanie == "+":
    wynik = liczba_1 + liczba_2
elif dzialanie == "-":
    wynik = liczba_1 - liczba_2
elif dzialanie == "*":
    wynik = liczba_1 * liczba_2
elif dzialanie == "/":
    wynik = liczba_1 / liczba_2
else:
    wynik = "nieokreślony"
    print("Błędny znak działania")

print(f"Wynik działania to: {wynik}")