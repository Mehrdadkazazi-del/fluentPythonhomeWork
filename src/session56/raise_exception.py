#Precondition
#PostCondition

def say_hello(input_value : str):
    if input_value is None or input_value == '':
        print("please insert input value")
        raise ValueError("please insert input value", 404)
    else:
        print('Hello World!')

say_hello("")