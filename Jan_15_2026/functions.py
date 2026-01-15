def fun():
    print("hello")

fun()

def fun2(num): # parameter
    print(num)

fun2(7) # argument

# *args and **kwargs

def fun3(*args):
    print(args)
    print(args[0], args[2])

fun3(1, 5.6, "hey", "hru", "???")

def fun4(**kwargs):
    print(kwargs)
    print(kwargs['age'])
    print(kwargs['city'])

fun4(age = 18, city = "noida")
