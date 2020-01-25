"""

W GUI wprowadzamy: cena 1l paliwa, spalanie na 100km, dystans

"""

import tkinter

def spalanie():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        w = (a * b * c) / 100
        wynik.configure(text=f"Całkowity koszt paliwa: {w}")
    except ValueError:
        #print("Niepoprawne użycie, liczby powinny być liczbami.")
        wynik.configure(text=f"Niepoprawne użycie, liczby powinny być liczbami.")

root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="Cena 1 litra paliwa: ")
a_label.grid(row=1, column=1)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=1, column=2)

b_label = tkinter.Label(master=root, text="Spalanie na 100 km")
b_label.grid(row=2, column=1)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=2, column=2)

c_label = tkinter.Label(master=root, text="Dystans do przejechania")
c_label.grid(row=3, column=1)
c_entry = tkinter.Entry(master=root)
c_entry.grid(row=3, column=2)



add_button = tkinter.Button(master=root, text="Sumuj", command=spalanie)
add_button.grid(row=4, column=1)
wynik = tkinter.Label(master=root, text="-")
wynik.grid(row=4, column=2)
root.mainloop()