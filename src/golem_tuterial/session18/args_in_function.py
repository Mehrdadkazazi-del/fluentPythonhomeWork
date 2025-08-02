# بررسی آرگومان های ورودی یک تابع
def student_info(first_name, last_name, age=24, city = "Tehran"):
    return f"first_name = {first_name}, lastName = {last_name}, age = {age}, city = {city}"


print(student_info("John", "Smith", "23", "Tehran"))

#use tuple and unpacking for input functions
person_ = ("Mehrdad", "Kazazi", 32, "Tehran")
print(student_info(*person_))

#use dictionary and unpacking for input functions
person_dict_ = {"first_name":"Mehrdad", "last_name":"Kazazi", "age":23, "city":"Tehran"}
print(student_info(**person_dict_))

def student_info(name, *args):
    print(name, *args)

student_info("John", "Smith", "23", "Tehran")


def student_info(name, **kwargs):
    print(name)
    for key, value in kwargs.items():
        print(f"key = {key}, value = {value}")

student_info("John", first_name="John", last_name="Smith", age=24, city="Tehran", avg=19.6)
