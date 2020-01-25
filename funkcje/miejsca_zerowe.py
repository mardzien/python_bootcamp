
import math


def delta(a, b, c):
    return b ** 2 - 4 * a * c

def rozwiazanie(a, b, c):
    miejsca_zerowe = []
    d = delta(a, b, c)
    if d == 0:
        x = -b/ (2 * a)
        miejsca_zerowe =[x]
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        miejsca_zerowe = [x1, x2]
    else:
        miejsca_zerowe = []
    return miejsca_zerowe


print(rozwiazanie(-1, -11, 12))
print(rozwiazanie(1, 4, 4))

def test_delta():
    assert delta(1, 1, 1) == -3

def test_brak_miejsc_zerowych():
    assert rozwiazanie(1, 1, 10) == []

def test_jedno_miejsce_zerowe():
    assert rozwiazanie(1, 4, 4) == [-2.0]

def test_dwa_miejsca_zerowe():
    assert rozwiazanie(-1, -11, 12) == [-12.0, 1.0]