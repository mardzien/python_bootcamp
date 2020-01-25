

#with open('plik.csv', 'r') as plikcsv:
#
#    dane = plikcsv.readlines()
#    slownik = {}
#    lista = []
#    for i, linia in enumerate(dane):
#        znaki = linia.replace("\n", "").split(",")
#        for j in range(len(znaki)):
#            lista[j].append(znaki)




def parse_line(raw_line):
    #tu będą wartości linii (także headerów) - jako lista znaków
    value_list = []

    #lecimy po wartościach w ramach pojedynczej linii z pliku
    for val in raw_line:
        #czyścimy z spacji (to możę być zbędne, ale zostawiam)
        raw_line.replace (" ", "")

        # jak nie jest specjalnym znakiem to dodajemy do listy wartości
        if not "," in val and not "\n" in val:
            value_list.append(val)

    return value_list

# w tej funkcji wyciągamy z linii listę wartośći i tworzymy z niej dicty do których potem będziemy pakować wartości
def parse_headers(first_raw_line):
    #dict na listy wartośći
    header_dict = {}

    #dict na mapowanie indexów na nazwy
    header_to_name_dict = {}

    #wyciągamy headery
    value_list = parse_line(first_raw_line)

    idx = 0
    for val in value_list:
        #robimy (póki co)puste słowniki dla każdego headera
        header_dict[idx] = []

        #tu wsadzamy mapowanie indexów na literki (przyda się potem, żeby zamiast 0 było A, zamiast 1 B itd.
        header_to_name_dict[idx] = val
        idx += 1

    return header_dict, header_to_name_dict


def parse_values(file):
    values_lists = []
    idx = 1
    while idx <= len(file) - 1:
        values = parse_line(file[idx])
        if values:
            values_lists.append(values)
            idx += 1
    return values_lists


def put_values_to_dicts(header_dict, val_list):
    idx = 0
    # lecimy po listach wartości z kolejnych wierszy
    for list in val_list:
        dict_idx = 0
        # i potem dla każdej takiej listy lecimy po jej wartościach i pakujemy je do tych odpowiednich dictów
        # w sęsie - wyciągamy z nich listę i doczepiamy tę wartość
        for val in list:
            list = header_dict[dict_idx]
            list.append(val)
            dict_idx += 1
        idx += 1


def main():
    with open('plik.csv', 'r') as plikcsv:

        f = plikcsv.readlines()

        head_dict, head_to_name_dict = parse_headers(f[0])
        print(head_to_name_dict)

        val_lists = parse_values(f)
        print(val_lists)

        put_values_to_dicts(head_dict, val_lists)
        print(head_dict)

if __name__ == "__main__":
    main()