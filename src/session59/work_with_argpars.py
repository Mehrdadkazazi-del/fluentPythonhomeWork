import argparse


def say_hello(arg):
    if arg:
        return f"hello {arg}"
    else:
        return "please insert argument"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program show hello to client with input name")
    parser.add_argument("name", nargs="?", default="unknown", help="input name", type=str)

    args = parser.parse_args()

    print(say_hello(args.name))
