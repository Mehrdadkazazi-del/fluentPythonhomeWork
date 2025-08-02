import random
import string

list_ = [3, 2, 5, 4, 1, 9]

print(random.randint(0, 3))
print(random.choice(list_))
print(random.choices(list_, k=3))  # chioce with replacement (در این متد احتمال دارد عنصر تکراری برگرداند)
print(random.sample(list_, k=3))  # این نمونه گیری در آمار را انجام میدهد


def generate_password(length=8):
    print(string.digits)
    digits = string.digits
    upper_case_phrase = string.ascii_uppercase
    characters = string.ascii_letters
    passwords = random.choices(characters, k=length - 2)
    passwords.append(random.choice(upper_case_phrase))
    passwords.append(random.choice(digits))

    print(passwords)

    random.shuffle(passwords)

    print(passwords)
    return "".join(passwords)

print(f"password generated successfully : {generate_password(256)}")
