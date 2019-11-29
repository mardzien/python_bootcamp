alfabet_dalekopisu = {1: "E", 2: "\n", 3: "A", 4: " ", 5: "S", 6: "I", 7: "U", 8: "", 9: "D", 10: "R",
            11: "J", 12: "N", 13: "F", 14: "C", 15: "K", 16: "T", 17: "Z", 18: "L", 19: "W", 20: "H",
            21: "Y", 22: "P", 23: "Q", 24: "O", 25: "B", 26: "G", 27: " ", 28: "M", 29: "X", 30: "V",
            31: ""}

def bin_to_dec(bin_code):
    wynik = 0
    i = 4
    for znak in bin_code:
        if znak == "1":
            wynik += 2 ** i
        i -= 1
    return wynik

def dec_to_bin(dec):
    wynik = ""
    odpowiedniki = [16, 8, 4, 2, 1]
    ### liczba od 32 do 1
    for i in range(len(odpowiedniki)):
        if dec > odpowiedniki[i]:
            wynik += "1"
            dec -= odpowiedniki[i]
        else:
            wynik += "0"
    return wynik



def bit_to_text():
    with open('d.txt', 'r') as plik:
        lista_dec = []
        szyfr = plik.read()
        lista_bin = szyfr.split(" ")
        for i in range(len(lista_bin)):
            lista_dec.append(bin_to_dec(lista_bin[i]))

        napis = ""
        for i in range(len(lista_dec)):
            napis += alfabet_dalekopisu.get(lista_dec[i])
        return napis

napis = bit_to_text()
print(napis)

def text_to_bit(napis):
    lista_dec = []
    lista_bin = []
    for znak in napis:
        for i in range(1, 31):
            if znak == alfabet_dalekopisu[i]:
                lista_dec.append(i)
    for i in range(len(lista_dec)):
        lista_bin.append(dec_to_bin(lista_dec[i]))
    return lista_bin

print(text_to_bit(napis))