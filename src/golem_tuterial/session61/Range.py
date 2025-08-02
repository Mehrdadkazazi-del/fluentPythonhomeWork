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

r = Range(2, 7, 1)
print(next(r))
