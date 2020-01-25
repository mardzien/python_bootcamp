"""
Zapytaj użytkownika o :
miasto_a, miasto_b, odległość między miastami,
koszt paliwa, spalanie/ 100 km.
Oblicz koszt podróży pomiędzy tymi miastami
Wyświetl sformatowaną odpowiedź


"""

miasto_a = input("Podaj nazwę miasta a: ").capitalize()
miasto_b = input("Podaj nazwę miasta b: ").capitalize()
odleglosc = float(input(f"Podaj odległość między {miasto_a} - {miasto_b}: "))
koszt_paliwa = float(input("Podaj cenę paliwa za litr: "))
spalanie = float(input("Podaj spalanie pojazdu na 100km: "))

koszt_podrozy = odleglosc * koszt_paliwa * spalanie / 100

print(f"Koszt podróży z {miasto_a} do {miasto_b} to: {koszt_podrozy} złotych")