from src.session57.Exception import BookNotFound


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author


class BookCatalog:
    def __init__(self):
        self.books = list()

    def add(self, book):
        self.books.append(book)

    def search_by_title(self, name):
        for book in self.books:
            if book.name == name:
                return book
        else:
            raise BookNotFound


book1 = Book("Game of thrones", "Martin")
book2 = Book("Harry Potter", "Rolling")

bookList = BookCatalog()
bookList.add(book1)
bookList.add(book2)

print(bookList.search_by_title("Game of thrones"))
print(bookList.search_by_title("Harry Potter"))
# print(bookList.search_by_title("Witcher"))
