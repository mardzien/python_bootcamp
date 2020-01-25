

def max_of_two(a, b):
    if a > b:
        return a

def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))

def maksimum(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(maksimum(1, 2, 3))