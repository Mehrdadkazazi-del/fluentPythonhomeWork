import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def phase(self):
        r = math.sqrt((self.real**2) + (self.imag**2))
        theta = math.atan2(self.imag, self.real)
        return r, theta

print(dir(Complex))