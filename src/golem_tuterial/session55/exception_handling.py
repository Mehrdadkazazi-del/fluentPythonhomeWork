def division(a, b):
    return a / b


def run_method():
    print(division(5, 2))
    try:
        print(division(5, 0))
    except Exception as e:
        print("Division by zero", e)
        raise ZeroDivisionError

    try:
        print(division(5, "A"))
    except Exception as e:
        print("Unsupported ", e)


print(division(10, 2))
