import math


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return self.__class__(self.real, -self.imag)

    def phase(self):
        real = math.sqrt(self.real ** 2 + self.imag ** 2)
        theta = math.atan2(self.imag, self.real)
        return real, theta

    # this is same to toString method in java
    def __str__(self):
        print("__str__ called")
        if self.real > 0:
            return f"{self.real}+{self.imag}i"
        return f"{self.real}+{self.imag}i"

    # this is toString for developers
    def __repr__(self):
        print("__repr__ called")
        return f"{self.__class__.__name__}({self.real},{self.imag})"


c1 = Complex(1, 2)
print(c1)
