###################
###################
# Funkcje przyjmujące dowolną ilość argumentów

dane = (1, 2, 3, 4, 5)

def sumator(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
    return sum(args)
sumator(1)
sumator(1, 10, 100)

sumator(*dane) ### * - wypakowuje elementy z danego kontenera

print(sumator(*dane))
print(sumator(1, 2, 3, 4, 5))

print(sumator(1, 2, 3, a=1, b=2))
