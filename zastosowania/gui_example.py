import tkinter

def sumuj():
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
        w = a + b
        wynik.configure(text=f"Wynik : {w}")
    except ValueError:
        print("Niepoprawne użycie, liczby powinny być liczbami.")

root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="Liczba a")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="Liczba b")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()



add_button = tkinter.Button(master=root, text="Sumuj", command=sumuj)
add_button.pack()
wynik = tkinter.Label(master=root, text="-")
wynik.pack()
root.mainloop()

print("To się wykona dopiero po zakończeniu")