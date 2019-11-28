alfabet_dalekopisu = {1: "E", 2: "\n", 3: "A", 4: " ", 5: "S", 6: "I", 7: "U", 8: "", 9: "D", 10: "R",
            11: "J", 12: "N", 13: "F", 14: "C", 15: "K", 16: "T", 17: "Z", 18: "L", 19: "W", 20: "H",
            21: "Y", 22: "P", 23: "Q", 24: "O", 25: "B", 26: "G", 27: " ", 28: "M", 29: "X", 30: "V",
            31: ""}

def konwerter(bin_code):
    wynik = 0
    i = 4
    for znak in bin_code:
        if znak == "1":
            wynik += 2 ** i
        i -= 1
    return wynik
def main():
    with open('d.txt', 'r') as plik:
        lista_bin = []
        lista_dec = []
        szyfr = plik.read()
        lista_bin = szyfr.split(" ")
        for i in range(len(lista_bin)):
            lista_dec.append(konwerter(lista_bin[i]))

        napis = ""
        for i in range(len(lista_dec)):
            napis += alfabet_dalekopisu.get(lista_dec[i])
        print(napis)

main()