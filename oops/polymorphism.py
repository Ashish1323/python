class a:
    def __init__(self,a,b):
        self.a=a;
        self.b=b
    def defi(self):
        return (self.a,self.b)

class b:
    def __init__(self,a,b):
        self.a=a;
        self.b=b
    def defi(self):
        return (self.a,self.b)


c=a(10,20)
d=b(20,10)

for _ in [c,d]:
    print(_.defi())