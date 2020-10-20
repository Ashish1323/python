def decorator(func):  # declaring decoratorsss
    def wrapfunc():
        print("__________________")
        print("")
        func()
        print("__________________")

    return wrapfunc


@decorator  # decorator syntax!!
def yoo():
    print("chup hoja lode")


yoo()

# output
# __________________
# chup hoja lode
# __________________
