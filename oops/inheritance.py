class User():
    def ab(self):
        return "sign in"

class baba(User): #inheritance!!
    pass

x=baba()
print(x.ab())

print(isinstance(x,User))