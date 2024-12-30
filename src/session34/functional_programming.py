# functional programming

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def square(number):
    return number ** 2


def map_(function, list_of_numbers):
    return [function(e) for e in list_of_numbers]


# print(map_(square, numbers))

# map function
print(list(map(square, numbers)))


# ----------------------------------------------------

def is_even(number):
    return number % 2 == 0


# ----------------------------------------------------
# filter function
print(list(filter(is_even, numbers)))

# ----------------------------------------------------
# lambda function
print(list(map(lambda num: num ** 2, numbers)))

print(list(filter(lambda num: num % 2 == 0, numbers)))

vector1 = [1, 3, 2, 7]
vector2 = [12, 4, 2, 3]

# lambda function with more than one input params
# ضرب داخلی دوتا بردار
print(sum(list(map(lambda x, y: x * y, vector1, vector2))))

# sorting
dictionary = {'Alireza': 19.5, 'Shahab': 17, 'Mahnaz': 20, 'Danial': 16, 'Ehsan': 15}
print(sorted(dictionary, key=lambda x: dictionary[x], reverse=True))

# workshop
# use list comprehension
print([x ** 2 for x in range(10) if x % 2 == 0])
# use functional programming
print(list(filter(lambda y: y % 2 == 0, map(lambda x: x ** 2, range(10)))))
