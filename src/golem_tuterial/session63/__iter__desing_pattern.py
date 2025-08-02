from sympy.codegen.cnodes import static


class Range:

    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        result = self.start
        self.start = self.start + self.step
        return result

    def __iter__(self):
        return self

r = Range(1, 7, 2)

print("first loop")
for i in r:
    print(i)

l = [i ** 2 for i in r]
print(l)