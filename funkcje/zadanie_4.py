"""

"""


def formatuj(*args, **kwargs):
    napis = "\n".join(args)
    for keys, values in kwargs.items():
        napis = napis.replace("$"+keys, str(values))
    return napis

formatuj('koszt $cena PLN', 'kwota $cena brutto', cena = 10)

def test_formatuj():
    assert formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena = 10,
    ) == 'koszt 10 PLN\nkwota 10 brutto'