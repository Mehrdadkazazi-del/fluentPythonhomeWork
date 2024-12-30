list_ = [1,2,3,4,5,6,7,8,9]
iterable_List = iter(list_)
while True:
    try:
        item = next(iterable_List)
        print(item)
    except StopIteration:
        break