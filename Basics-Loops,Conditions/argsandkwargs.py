def loda(*args):
    return sum(args)

print(loda(1,3,4,6,9)) 


def kall(**kwargs):
    total=0
    for _ in kwargs.values():
        total+=_
    return total

print(kall(loda=1, bhos= 1))   


#Rule is params, *args, default parameter, **kwargs