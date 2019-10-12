# To jest mój pierwszy program
# podstawowe typy numeryczne

x = 1	# x - zmienna, nazwa, referencja. 1 - obiekt, wartość, liczba
print(x)	# uzywam funkcji print do wypisania wartkosci, na ktora wskazuje referencja x
print(x+1)

# nazwy nie mogą zaczynać się od cyfry
# mogą składać się z liter, cyfr i znaków podkreślenia _
# poprawne nazwy to np: x, dziecko, wartosc_1
#niepoprawne nazwy to: 1zmienna, wartosc.1

#################################
#								#
#  Podstawowe typy numeryczne	#
#								#
#################################
#
# :iczby całkowite - integer - nazwa typu: int
int
# nawiacy po jakiejś nazwie to sposób na wywołanie, np. funkcji. Takie obiekty są callable
#
# podstawowe operatory
# + - * / ** pow // %
print(1 + 2)
print(3 - 1)
print(2 * 3)
print(5 / 2)
print(5 // 2)
print(9 % 7)
print(10 ** 2)
print(pow(10, 2))

##################################
# wartości boolowskie
# nazwa typu: bool
# False, True
# operatory logiczne
# and, or, not

# typ None
x = None

##################################
# operatory porównania
# ==, >, <, !=, >=, <=
# przykłady

x = 4
y = 12

print(x == y) # False
print(x < y) #False
print(x != y) #True

##################################
# Liczby zmienno-przecinkowe
# nazwa typu: float
# min = 1e-324
# max = 1e308

##################################
# liczby zespolone
# nazwa typu: complex

##################################
## zbadaj funkcję print

## Napisy -
# typ: str

"To jest napis"
x = "To \"jest\" napis\n" # \ to jest znak ucieczki
y = 'To też jest napis\n'
z = """ To jest
napis
wielolinijkowy
"""

print(x, y, z)


# co można robić z napisami
# napisy można łączyć

x = "Pierwszy napis"
y = "Drugi napis"

print (x + y)

# napisy można mnożyć przez liczbę

print ("#" * 40)

# napisy można formatować
template = "{} {} {}"
print(template.format(10, 20, 30))

x = 10
y = 20
z = 30

print(f"x = {x}, y = {y}, z = {z}, x + y = {x + y}")

pi = 3.1416
r = 7

print(f"""
normalnie {pi} x
szerokosc 10 {pi:10} x
szerokosc 10 {pi:<10} x
szerokosc 10 {pi:^10} x
zaokraglenie {pi:.2f} x
""")

# możemy przekształcać napisy

print(dir(""))

x = "ala ma kota"
print(x.title())


##########################
# Wyrażenia warunkowe

x = 1
y = 2

if x > y:
    print("Jedna odnoga programu")
elif x == y:
    print("Druga odnoga programu")
else:
    print("Pozostałe przypadki")












