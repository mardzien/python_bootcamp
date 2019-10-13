"""
plansza
"""
x = int(input("Podaj współrzędną x: "))
y = int(input("Podaj współrzędną y: "))

# ctrl alt l - formatuje kod zgodnie z PEBP

if x < 0 or x > 100 or y < 0 or y > 100:
    print("Jesteś poza planszą")
elif x > 90 and y > 90:
    print("Jesteś w prawym górnym rogu")
elif x > 90 and y < 10:
    print("Jesteś w prawym dolnym rogu")
elif x < 10 and y < 10:
    print("Jesteś w lewym dolnym rogu")
elif x < 10 and y > 90:
    print("Jesteś w lewym górnym rogu")
elif x > 90:
    print("Jesteś na prawej krawędzi")
elif x < 10:
    print("Jesteś na lewej krawędzi")
elif y > 90:
    print("Jesteś na górnej krawędzi")
elif y < 10:
    print("Jesteś na dolnej krawędzi")
else:
    print("Jestś w centrum")
