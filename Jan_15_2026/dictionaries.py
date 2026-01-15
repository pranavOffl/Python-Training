mydict = {
    1 : "hey", 
    4.5 : 10,
    False : 7.999,
    (6, 7) : 90,
    "one" : "two",
    frozenset({8}) : None,
}

print(mydict, type(mydict))

for num in mydict:
    print(num)

for num in mydict.values():
    print(num)

for num in mydict.keys():
    print(num)

for k, v in mydict.items():
    print(k, v)

mydict["one"] = 5

for k, v in mydict.items():
    print(k, v)

mydict["two"] = 67