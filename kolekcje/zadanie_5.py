"""

Policz samogłoski w podanym napisie

samogłoski: a, e, i, o, u, y

"""

napis = input("Wpisz jakiś tekst: ").lower()

samogloski = "aeiou"

i = 0

for litera in napis:
    for samogloska in samogloski:
        if litera == samogloska:
            i += 1

print(f"Liczba samogłosek w tekście to: {i}")