

while True:
    print("Zapętliłem się")
    break

i = 0

while i < 10:
    if i == 5:
        i += 1
        continue
    print(i, "Pętla")
    i += 1 # i = i + 1
