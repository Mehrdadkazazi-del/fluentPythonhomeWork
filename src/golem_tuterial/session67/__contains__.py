# یک عملگر در پایتون داریم به اسم in
# این عملگر برای همه ی iterable هاست
list_ = ["Mehrdad", "Ali", "Mohamad"]
print("Hamid" in list_)
print("Mehrdad" in list_)

language = "Python"
print("Py" in language)


# ما در اینجا __contain__ را پیاده سازی کردیم و سپس در زمان ساخت ابجکت داریم از in استفاده میکنیم.
class Book:
    def __init__(self, title):
        self.title = title

    def __contains__(self, item):
        return item in self.title


b = Book("Game of Thrones")
print("Thrones" in b)
