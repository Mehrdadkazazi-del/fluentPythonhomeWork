class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def __call__(self, x):
        return self.a * (x ** 2) + self.b * x + self.c

qobj = Quadratic(3, 4, 1)

print(qobj(1))
print(qobj(2))


# closure
def quadratic(a, b, c):
    def inner(x):
        return a * x ** 2 + b * x + c

    return inner

q = quadratic(3, 4, 1)
print(q(1))
print(q(2))