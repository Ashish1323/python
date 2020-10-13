from functools import reduce

myl=[1,2,3]
def a(acc,item):
    return acc+item

print(reduce(a,myl,0))   

#output 6