class Superlist(list):
    def __len__(self):
        return 69

super=Superlist()
super.append(5)
print(super)
print(issubclass(Superlist,list)) # checks class!!