
#

try:
    1/0
    tutajcosrobimy
except ZeroDivisionError:
    print("Dzieliłeś przez zero- wstydź się!")
except NameError:
    print("Tego jeszcze nie zdefiniowałeś")
finally:
    print("To się wykona zawsze")


odp = input("Wpisz x by rzucić wyjątek: ")

if odp == "x":
        raise Exception("To jest mój wyjątek. X powoduje wyjątek")