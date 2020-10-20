mylist = [c for c in "Yoooooo!"]
print(mylist)
mylist1 = [x**2 for x in range(0, 12)]
print(mylist1)
mylist2 = [x**2 for x in range(0, 12) if (x % 2 != 0)]
print(mylist2)

# not so good practise as it takes away code readablility!!
