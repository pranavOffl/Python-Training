# List Comprehension

nums = [1, 2, 3, 4, 5]

squares = [x*x for x in nums]
print(squares)

# Set Comprehension

s = {x*x for x in [1, 2, 2, 3, 4]}
print(s)

# Dict Comprehension

nums = [1, 2, 3]

d = {x: x*x for x in nums}
print(d)
