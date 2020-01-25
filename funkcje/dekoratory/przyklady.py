

def powitanie():
    print("Hello")

def be_awesome(name):
    print(f"Yo {name}. Be awesome!")

def nowa_funkcja(func):
    def wrapper(*args, **kwargs):
        print("To jest powitanie")
        result = func(*args, **kwargs)
        return result
    return wrapper

#powitanie()

#be_awesome("Gutek")

powitanie = nowa_funkcja(powitanie)
powitanie()