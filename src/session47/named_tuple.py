import collections

#tuple
# country = ("Iran", "Tehran", 85_000_000)
# print(type(country))
# print(country[0])
from src.session16.tuple import country


class Country:
    def __init__(self, country, capital, population):
        self.country = country
        self.capital = capital
        self.population = population

# c1 = Country("Iran", "Tehran", 85_000_000)
# print(c1.country)

#namedTuple

Country = collections.namedtuple("country",['country','capital','population'])
c1 = Country("Iran", "Tehran", 85_000_000)
c2 = Country("Iran", "Tehran", 85_000_000)

print(c1[0])
print(c1.country)
print(c1.capital)
print(c1.population)
print(c1)

# unpacking
_, capital, pop = c1
print(capital, pop)
c3 = c1._replace(capital="Esfahan")
print(c3.capital, c3.population)
print(id(c1))
print(id(c2))
print(id(c3))

