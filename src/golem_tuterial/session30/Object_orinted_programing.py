class Book:
    uniqNumber = 0

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.__class__.uniqNumber += 1

    #method
    def price(self):
        return 254000


book1 = Book("George Martin", "Game of thrones", 1000)
print(book1.__dict__)
print(book1.price())
print(book1.title)
print(book1.uniqNumber)
print(dir(book1))
book2 = Book("JK Rolling", "Harry Potter", 100)
print(book2.__dict__)
print(book2.price())
print(book2.title)
print(book2.uniqNumber)
print(dir(book2))