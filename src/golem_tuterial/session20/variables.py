a = 5

def function(n):
    global a
    print("a value before modify is: ", a)
    a = 2
    print("a value modified to: ",a)
    print("a value after modify is: ", a)
    print("input value is: ",n)

function(10)
print("a value out of function is: ",a)