from sympy import isprime

def sum_params(firstParam: int, secondParam:int) -> int:
    return firstParam + secondParam


print(type(sum_params))
print(id(sum_params))
print(sum_params(2,3))

def say_hello():
    print("Hello")

say_hello()
result_ = say_hello()
print(result_)

def say_welcome(name : str) -> str:
    return f"Hello {name}"

result_ = say_welcome("John")
print(result_)

def is_prime(number : int) -> int:
    if isprime(number):
        print(f"{number} is a natural number")
    else:
        print(f"{number} is not a natural number")

    # if check_natural_number(number):
    #     print(f"{number} is a natural number")
    # else:
    #     print(f"{number} is not a natural number")

def check_natural_number(number) -> bool:
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

is_prime(5)