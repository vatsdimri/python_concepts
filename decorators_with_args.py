def plus_five(func):
    def wrapper(*args, **kwargs): # we can also pass keyword arguments into this
        c = func(*args, **kwargs)
        return c + 5
    return wrapper

@plus_five
def add(a, b):
    c = a+b
    print(f"sum of {a} and {b} is: {c}")
    return c

sum = add(2, 2)
print(f"sum + 5 is {sum}")
