#Iterator VS Iterable
r = range(2,10)

for i in r:
    print(i)
for i in r:
    print(i)

print("__iter__" in dir(r))
print("__next__" in dir(r))
print(list(r))
print(list(r))

iter_list = iter(r)
for i in iter_list:
    print(i)

print(list(iter_list))

for i in iter_list:
    print(i)

print("__iter__" in dir(iter_list))
print("__next__" in dir(iter_list))
