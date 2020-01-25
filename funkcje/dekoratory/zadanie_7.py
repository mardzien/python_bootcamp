
def bold(func):

    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"

    return wrapper

def italic(func):

    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"

    return wrapper


@italic
@bold
def foo(arg):
    return f"To jest {arg}"



print(foo("Kot"))