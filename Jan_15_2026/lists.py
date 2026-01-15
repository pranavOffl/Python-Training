mylist = ["Heyy", 10, 6.7, True, 100, 10]

for num in mylist:
    print(num, end = ' ')

mylist.append(999)

print()
print(mylist)

for i in range(len(mylist)):
    print(mylist[i], end = ' ')

print()
print(mylist)