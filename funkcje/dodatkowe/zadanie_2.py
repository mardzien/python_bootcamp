



def suma(dane):
    sum = 0
    if isinstance(dane, dict):
        dane = dane.values()
    for element in dane:
        if isinstance(element, int):
            sum += element
        elif isinstance(element, str):
            try:
                sum += int(element)
            except ValueError:
                pass
    return sum


def test_suma():
    assert suma([1, 2, 3]) == 6
    assert suma([1, 2, 3, "4"]) == 10
    assert suma([1, 2, 3, "a"]) == 6
    assert suma({'a': 10, 'b': 20}) == 30
    assert suma({'a': '10', 'b': 'xx'}) == 10