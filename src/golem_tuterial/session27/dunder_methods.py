import math


class Complex:
    # dunder init
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return self.__class__(self.real, -self.imag)

    def phase(self):
        real = math.sqrt(self.real ** 2 + self.imag ** 2)
        theta = math.atan2(self.imag, self.real)
        return real, theta

    # c1 + c2
    def __add__(self, other):
        return self.__class__(self.real + other.real, self.imag + other.imag)

    # multiplication (ضربدر)
    def __mul__(self, scaler):
        return self.__class__(self.real * scaler, self.imag * scaler)

c1 = Complex(1, 1)
c2 = Complex(2, 1)

#dunder methods
# c1 + c2  -> c1.__add__(c2)
c3 = c1 + c2  #-> c3 = c1.__add__(c2)
print(c3.real, c3.imag)

#_______________________________________

c4 = c2 * 5
print(c4.real, c4.imag)
