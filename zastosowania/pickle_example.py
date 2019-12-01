import pickle

f_name = "employees.pickle"

class Employee:

    def __init__(self, imie, nazwisko, rok, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok = rok
        self.pensja = pensja

    def report(self, id_):
        return f"- [{id_}] {self.imie} {self.nazwisko} - rok: {self.rok}, pensja: {self.pensja} PLN"


try:
    with open(f_name, 'rb') as f:
        employees = pickle.load(f)

except FileNotFoundError:
    employees = []

sciezka = input("Co chcesz zrobić? [d - dodaj, w - wypisz]")

if sciezka == "d":
    print("Dodaje...")
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    rok = input("Rok: ")
    pensja = input("Pensja: ")
    e = Employee(imie, nazwisko, rok, pensja)

    employees.append(e)

    with open(f_name, 'wb') as f:
        pickle.dump(employees, f)

elif sciezka == "w":
    print("Wypisuję...")
    for id_, e in enumerate(employees, start=1):
        print(e.report(id_))
