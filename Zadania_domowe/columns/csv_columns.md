
Napisz funkcję columns, która przyjmie obiekt pliku i zwróci słownik, który będzie napował nagłówki kolumn na listy ich wartości

Przykład - jeśli mamy plik CSV (`plik.csv`) o następującej treści

A,B
0,2
1,4

Wtedy wywołanie naszej funkcji powinno dać taki efekt

	>>> columns(open('plik.csv'))
	{'A': ['0', '1'], 'B': ['2', '4']}


Dodatkowo:

1. Upewnij się, że kolejność kluczy w słowniku jest taka sama jak kolejność kolumn w pliku CSV

2. Dodaj opcjonalną możliwość podania własnych nagłówków. Domyślnie pierwszy wiersz brany jest jako nagłówek.

	>>> columns(open('my_file.csv'), headers=['header1', 'header2'])
	{'header1': ['A', '0', '1'], 'header2': ['B', '2', '4']}

3. Zadba o obsługę sytuacji, w której plik csv ma różną liczbę kolumn w różnych wierszach. Brakujące dane powinny być oznaczane domyślnie jako None, ale powinna być możlwość ustawienia czegoś innego

file.csv:

	h1,h2
	1,2
	3,4
	5

	>>> columns(open('file.csv'), missing='0')
	{'h1': ['1', '3', '5'], 'h2': ['2', '4', '0']}
	>>> columns(open('file.csv'))
	{'h1': ['1', '3', '5'], 'h2': ['2', '4', None]}

