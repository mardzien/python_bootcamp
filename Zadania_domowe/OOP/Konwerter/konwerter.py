class Konwerter:
    def __init__(self):
        ### wypisanie wszystkich kombinacji 2-kowych i ich wartości
        self.num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        self.rom = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

    def int_to_roman(self, liczba):
        #inicjalizacja zmiennej wynik
        wynik = ""
        # i - numer przedstawiający ostatni element listy wartości
        i = 12

        while liczba:
            ## sprawdzam, czy liczba dzieli się _ przez kolejne wartości zaczynając od największej
            div = liczba // self.num[i]
            # jeśli tak to div będzie miało wartość od 1 do 3. Gdzie w alfabecie rzymskim mogą być max 3 takie same znaki odok siebie.
            # dalej nadpisujemy wartość liczby, teraz będzie równa reszcie z dzielenia przez kolejne wartości z listy.
            liczba = liczba % self.num[i]

            while div:
                # sydłużamy napis o kolejne wartości z listy self.rom
                wynik += self.rom[i]
                div -= 1
            i -= 1
        return wynik

    def roman_to_int(self, rzymska):

        """
        słownik klucz - symbol z liczb rzymskich, wartość - odpowiednik w liczbach arabskich

        XCVII
        kolejne wartości: 10, 100, 5, 1, 1
        reprezentacja liczbowa: 96 = -10 + 100 + 5 + 1 + 1
        dodajemy kolejne wartości jeśli każda kolejna cyfra ma reprezentację mniejszą bądź równą od poprzedniej
        jeśli wieksza wartość jest poprzedzona przez mniejszą - wówczas odejmujemy od wynuku tą mniejszą wartość
        """

        wartosci = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        wynik = 0
        i = 0

        while i < len(rzymska):

            ### przypisujemy wartość ze słownika do w1
            w1 = wartosci.get(rzymska[i])

            if i + 1 < len(rzymska):

                ### przypisujemy kolejną wartość, którą potem będziemy porównywać z poprzednią
                w2 = wartosci.get(rzymska[i + 1])

                if w1 >= w2:
                    ### jeśli kolejna liczba jest mniejsza od poprzedniej, to dodajemy ją do wyniku i zwiększamy i o 1
                    wynik += w1
                    i += 1

                else:
                    ### tutaj odejmujemy mniejszą wartość, dodajemy większą i zwiększamy i o 2
                    wynik = wynik + w2 - w1
                    i += 2
            else:
                ### dodajemy ostatnią liczbę do wyniku, zwiększamy i i wychodzimy z pętlii
                wynik += w1
                i += 1
        return wynik

    def cel_to_farh(self, cel):

        return cel * 1.8 + 32

    def farh_to_cel(self, farh):

        return (farh - 32) / 1.8





print(Konwerter().int_to_roman(399))
print(Konwerter().int_to_roman(999))

print(Konwerter().roman_to_int("CCCXCIX"))
print(Konwerter().roman_to_int("CMXCIX"))

print(Konwerter().cel_to_farh(100))
print(Konwerter().farh_to_cel(212))