def power(base, exponent, /):
    return base ** exponent


# ما در ورودی متد از / استفاده کنیم فقط از طریق positional دیگه میتونه استفاده بشه
# positional arguments
print(power(2, 3))


# keyword
#  الان چون / توی ورودی متد دادیم دیگه این حالتی پارامتر پاس دادن خطا میخوره
# print(power(base = 2, exponent= 3))

def func(a, b, *args, d):
    print(a, b, d)


func(1, 2, 3, d=4)


def func(a, b, *args, d, **kwargs):
    print(a, b, args, d, kwargs)

# positional , keyword با هم
func(1, 2, 3, 4, 5, d=12, e=15, f=7)
