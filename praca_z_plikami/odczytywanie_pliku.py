



# contex manager
with open("nazwa_pliku.txt") as fh:
    print(fh.read())

with open("nazwa_pliku.txt") as fh:
    for line in fh.read().splitlines():
        print(line)

with open("text.txt", 'w') as fh:
    fh.write("Ala")