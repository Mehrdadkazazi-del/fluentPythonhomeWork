s1 = {1,2,3,4,1,2,3,4,3,4}
print(s1)

s2 = set()
s2.add(1)
s2.add(3.1)
s2.add(3.1)
s2.add(5)
s2.add(6)
s2.add(5)
s2.add(9.2)

print(s2)

#اجتماع
print(s1.union(s2))
#اشتراک
print(s1.intersection(s2))
#اختلاف
print(s1.difference(s2))