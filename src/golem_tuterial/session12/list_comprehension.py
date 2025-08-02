# [0,1,2,3,4,5]

list_ = []
for i in range(6):
    list_.append(i)
print(list_)

#list comprehension
list_ = [i for i in range(6)] # {i | i <= 6}
print(list_)

# "hello"
list_ = []
for c in "hello":
    list_.append(c)
print(list_)

#list comprehension
list_ = [c for c in "hello"]
print(list_)

list_ = []
for i in range(10):
    list_.append(i ** 2)
print(list_)

#list comprehension
list_ = [i ** 2 for i in range(10)]
print(list_)

list_ = []
for i in range(10):
    if i % 2 == 0:
        list_.append(i)
print(list_)

#list comprehension
list_ = [i for i in range(10) if i % 2 == 0]
print(list_)