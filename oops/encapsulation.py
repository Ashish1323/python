class aj:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def encapsule(self):
        return (f'Hello {self.name}, Your Age is {self.age}')


x=aj("andrie", 100)
print(x.encapsule())            