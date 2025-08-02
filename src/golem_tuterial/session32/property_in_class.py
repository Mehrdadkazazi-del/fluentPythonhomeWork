class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def set_author(self, author):
        if isinstance(author, str) and len(author) > 2:
            self._author = author
        else:
            print("invalid author")

    def get_author(self):
        return self._author

    # property
    author = property(fget=get_author, fset=set_author)


book1 = Book("George Martin", "Game of thrones")
# book1.set_author("G.Martin")

# print(book1.get_author())

book1.author = 100
print(book1.author)



