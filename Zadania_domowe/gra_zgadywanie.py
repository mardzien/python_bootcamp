import random
liczba = random.randint(1,20)
licznik = 1
while True:
   podaj = int(input("Podaj liczbę od 1 do 20: "))
   if podaj < 1 or podaj > 20:
       print("Liczba jest spoza zakresu.")
       licznik += 1
   elif podaj < liczba:
       print("Twoja liczba jest za mała.")
       licznik += 1
   elif podaj > liczba:
       print("Twoja liczba jest za duża.")
       licznik += 1
   else:
       print(f"Brawo, zgadłeś za {licznik} razem.")
       break