# Decorator


def counter(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"counter is:{count}")
        return func(*args, **kwargs)

    return inner

def logger(func):
    def closure(*args, **kwargs):
        print(f"logger is:{func.__name__}")
        return func(*args, **kwargs)

    return closure

@counter
@logger
def add(a, b):
    return a + b

@counter
@logger
def multiply(a, b):
    return a * b

# add = counter(add)
print(add(1,2))
print(add(1,2))

# multiply = counter(multiply)
print(multiply(1,2))