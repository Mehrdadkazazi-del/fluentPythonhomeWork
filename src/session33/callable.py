class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def add(self, a, b):
        return a + b

    def __call__(self, *args, **kwargs):
        return type(self),id(self)

book1 = Book("Title", "Author")

print(book1.add(2,5))

#callable
print(callable(book1.add))
print(callable(book1.author))
print(callable(book1))
print(book1())
print(callable(book1))
