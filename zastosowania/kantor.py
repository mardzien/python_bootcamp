import json

import requests

"""http://api.nbp.pl/api/exchangerates/tables/A?formt=json"""
"""Domena           sciezka                   query string"""
def wypisz_waluty(kursy):
    rates = kursy[0]['rates']
    for rate in rates:
        print(rate['code'])

def kurs_dla_waluty(kursy, waluta):
    rates = kursy[0]['rates']
    for rate in rates:
        if rate['code'] == waluta:
            return rate['mid']

data = requests.get("http://api.nbp.pl/api/exchangerates/tables/A?formt=json")

if data.status_code == 200:
    data = data.json()
    wypisz_waluty(data)

waluta = input("Dla jakiej waluty sprawdzic? ")
print(kurs_dla_waluty(data, waluta))