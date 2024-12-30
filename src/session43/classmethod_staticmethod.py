# types of methods in class:
#    class method - instance method - static method

class Dollar:
    def __init__(self, amount):
        self.amount = amount

    # instance method
    def increase(self, amount):
        print(self)
        self.amount += amount
        return self.amount

    @classmethod
    def from_string(cls, amount):
        print(cls)
        return cls(int(amount))

    @staticmethod
    def to_rial(amount):
        return amount * 80_000

dollar1 = Dollar(100)
dollar2 = Dollar(200)

print(dollar1.increase(10))  # instance method

dollar3 = Dollar.from_string(10) # class method
print(dollar3)

dollar4 = Dollar.to_rial(100)
print(dollar4)