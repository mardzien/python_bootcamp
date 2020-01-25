import csv

dane=[["A", "B", "C", "D"], [1, 2, 3, 4], [5, 6, 7, 8]]


with open("dane.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(dane)
