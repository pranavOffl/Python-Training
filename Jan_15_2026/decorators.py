# normal fun

def hello():
    print("Heyy pranav")

hello()
print()

# using function type decorator to wrap it

def decorator(func):
    def wrapper():
        print("start of decorator")
        func()
        print("end of decorator")
    return wrapper

@decorator
def hello():
    print("Heyy pranav")

hello()
print()

# with parameters

def adding(func):
    def wrapper(*args, **kwargs):
        print("start of decorator")
        func(*args, **kwargs)
        print("end of decorator")
    return wrapper

@adding
def add(a, b):
    print(a + b)

add(7, 3)
print("***********")

# passing argument to decorator

def solve(value):
    def adding(func):
        def wrapper(*args, **kwargs):
            print("start of decorator")
            res=0
            for i in range(value):
                res +=func(*args, **kwargs)
            print(res)
            print("end of decorator")
        return wrapper
    return adding

@solve(5)
def add(a, b):
    return a + b

add(7, 3)