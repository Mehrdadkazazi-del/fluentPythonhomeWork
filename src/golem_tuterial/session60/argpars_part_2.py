import argparse

def say_hello(first_name, last_name):
    return f'Hello {first_name} {last_name}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Says hello to someone')
    parser.add_argument("-f", "--first", help='First name', type=str, required=True)
    parser.add_argument("-l", "--last", help='Last name', type=str, required=True)

    args = parser.parse_args()
    first_name = args.first
    last_name = args.last

    print(say_hello(first_name, last_name))