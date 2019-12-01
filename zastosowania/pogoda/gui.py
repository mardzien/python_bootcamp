import tkinter
from pogoda import get_location_id, get_location_weather, prepare_weather_report

def get_weather():
    location_name = location_entry.get()
    location_id = get_location_id(location_name)
    weather = get_location_weather(location_id)
    report = prepare_weather_report(weather, location_name)
    result_label.configure(text=report)


root = tkinter.Tk()

location_entry = tkinter.Entry(master=root)
get_button = tkinter.Button(master=root, text="Pobierz", command=get_weather)
result_label = tkinter.Label(master=root, text="")

location_entry.pack()
get_button.pack()
result_label.pack()

root.mainloop()
# miasto_label = tkinter.Label(master=root, text="Podaj nazwę miasta: ")
# miasto_label.pack()
# miasto_entry = tkinter.Entry(master=root)
# miasto_entry.grid(row=1, column=2)
#
#
# add_button = tkinter.Button(master=root, text="Pobierz informacje o pogodzie", command=)
# add_button.grid(row=2, column=1)
# wynik = tkinter.Label(master=root, text="-")
# wynik.grid(row=2, column=2)
# root.mainloop()