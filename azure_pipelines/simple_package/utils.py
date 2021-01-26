# simple module to test azure CI/CD with testing

def add_ints(x, y):
    return x + y

def divide_ints(x, y):
    # divide by zero error
    if y == 0:
        raise ZeroDivisionError
    return x / y 