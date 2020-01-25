

def parse_line(line):
    line.replace(" ","").replace('\\n', '')
    splited_list = line.split(",")
    return splited_list


def get_list(lines):
    l = []
    for line in lines:
        parsed_line = parse_line(line)
        l.append(parsed_line)
        print(parsed_line)
    return l

def check_h_number(l_of_l):
    return len(l_of_l[0])

# def list_of_columns(l_of_l):
#     list = []
#     number_of_rows = len(l_of_l)
#     number_of_columns = len(l_of_l[0])
#     for row in range(number_of_rows):
#         for col in range(number_of_columns):
#             list[col, row] = l_of_l[row, col]
#     return list


def main():

    with open('plik.csv', 'r') as plikcsv:

        f = plikcsv.readlines()
        print(f)
        parse_line(f[0])
        print(get_list(f))

main()