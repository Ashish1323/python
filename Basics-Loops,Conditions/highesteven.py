x=[]
def higheven(li):
    for n in li:
        if  n % 2 == 0: 
            x.append(n)

    return max(x)        
            


print(higheven([1,2,11,10,12,13]))