class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #method
    def price(self):
        return 254000


book1 = Book("George Martin", "Game of thrones", 1000)

print(book1.title , getattr(book1, 'title'))
print(getattr(book1, 'x',None))

book2 = Book("JK Rolling", "Harry Potter", 100)
setattr(book2, 'isbn', 125478)

print(getattr(book2, 'isbn', None))

print(getattr(book1, 'price')())
print(getattr(Book, 'price')(book1))