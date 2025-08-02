symbols = '!@#$%^&*()'
beyond_ascii = [ord(symbol) for symbol in symbols]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 40, map(ord,symbols)))
print(beyond_ascii)