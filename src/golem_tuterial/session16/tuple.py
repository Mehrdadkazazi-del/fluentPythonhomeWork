def divider():
    print("-----------------------------------------")

def compute_add_sub(a,b):
    return a+b , a-b

print(compute_add_sub(2,3))
print(type(compute_add_sub(2,3)))
# tuple = (5, -1)

divider()

list_ = [1,2,3]
tuple_ = (1,2,3)

print(type(list_))
print(type(tuple_))

divider()

list_[0] = 3
print(list_)

# tuple is immutable
#tuple_[0]= 3  # this is wrong
#print(tuple_)

divider()

print(len(list_))
print(len(tuple_))

record_ = "Iran",2021,11,14
print(record_)

# unpacking
country, year, month, day = record_
print(country, year, month, day)
print(country)
print(year)

divider()

country, *_ , day = record_
print(country)
print(_)
print(day)

divider()
#swapping
x = 25
y = 12

#traditional
t = y
y = x
x = t
print(x)
print(y)
# swapping using by unpacking
x = 25
y = 12

y , x = x , y

print(x)
print(y)