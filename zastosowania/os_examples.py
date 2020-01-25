"""

Wylistuj wszystki pliki we wskazanym katalogu. Wynik zapisz w C:\\temp\\skan_<current_date>.txt

"""

import os
import datetime


def skan_folder(path):
    data = os.listdir(path)
    cur_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"skan_{cur_date}.txt"
    if "temp" not in os.listdir("C:\\"):
        os.mkdir("C:\\temp")
    with open(f"C:\\temp\\{filename}", 'w') as f:
        f.write("\n".join(data))
    print("Skończone, wyniki w: ", filename)


skan_folder("C:\\Program Files")