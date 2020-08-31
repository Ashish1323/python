#unordered pair of unique items is known as sets
aset={1,2,3,45,5}

print(aset)
print(1 in aset) #to check in set
#to add add() clear() for clearing copy() for copying 

mylist=list(aset)
#also vice versa can be done

abset={1,2,3,4,5}
asset={4,5,6,7,8,9}

#difference
print(abset.difference(asset))

#discard =removes the element from set
abset.discard(5)
print(abset)

#difference update update the difference
abset.difference_update(asset)
print(abset)


abset={1,2,3,4,5}
#intersection
print(abset.intersection(asset))

#disjoint means overlapping
print(abset.isdisjoint(asset))

#union
print(abset.union(asset))