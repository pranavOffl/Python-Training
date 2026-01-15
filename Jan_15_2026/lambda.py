x = lambda a, b, c : a + b + c
print(x(5, 5, 10))

# Map - Transform each element (Many -> Many)

nums = [1, 2, 3, 4]

def square(x):
    return x * x

result = list(map(square, nums))
print(result)

result = list(map(lambda x : x * x, nums))
print(result)

# filter() – Select elements (Many -> Fewer)

nums = [1, 2, 3, 4, 5]

def is_even(x):
    return x % 2 == 0

result = list(filter(is_even, nums))
print(result)

result = list(filter(lambda x : x % 2 == 0, nums))
print(result)

# reduce() – Combine into one value (Many -> One)

from functools import reduce

nums = [1, 2, 3, 4]

def add(a, b):
    return a + b

result = reduce(add, nums)
print(result)

result = reduce(lambda a, b : a + b, nums)
print(result)

