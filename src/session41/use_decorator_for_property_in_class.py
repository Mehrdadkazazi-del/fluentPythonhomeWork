class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title


book1 = Book("Game of thrones", "George Martin")
print(book1.author)
print(book1.title)
book1.author = "Mehrdad"
book1.title = "Friends"
print(book1.title)
print(book1.author)
print(book1.__dict__)
