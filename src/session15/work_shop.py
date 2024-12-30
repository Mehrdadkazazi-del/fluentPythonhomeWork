from src.session12.list_comprehension import list_


def find_common(list1, list2):
    list_ = []

    for item in list1:
        if item in list2:
            if item not in list_:
                list_.append(item)
    return list_

print(find_common([1,3,7], [7,2,12]))
print(find_common([1,1,12,7], [1,5,2]))
print(find_common([1,3,2,12], [3,2,2,23]))


def find_intersection(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))

print(find_intersection([1,3,7], [7,2,12]))
print(find_intersection([1,1,12,7], [1,5,2]))
print(find_intersection([1,3,2,12], [3,2,2,23]))