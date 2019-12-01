import json

f_name = "employees.json"


class Employee:

    def __init__(self, imie, nazwisko, rok, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok = rok
        self.pensja = pensja

    def serialize(self):
        return {
            "imie": self.imie,
            "nazwisko": self.nazwisko,
            "rok": self.rok,
            "pensja": self.pensja
        }

    @staticmethod
    def deserialize(data):
        return Employee(**data)

    def report(self, id_):
        return f"- [{id_}] {self.imie} {self.nazwisko} - rok: {self.rok}, pensja: {self.pensja} PLN"


try:
    with open(f_name) as f:
        employees = json.load(f)
        employees = [Employee.deserialize(data) for data in employees]

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

    employees.append(e.serialize())

    with open(f_name, 'w') as f:
        json.dump(employees, f, indent=4)

elif sciezka == "w":
    print("Wypisuję...")
    for id_, e in enumerate(employees, start=1):
        print(e.report(id_))
