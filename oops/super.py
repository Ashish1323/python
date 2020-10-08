class Baap():
    def __init__(self,email):
        self.email=email

class Beta(Baap):
    def __init__(self,name,email):
        super().__init__(email) #Super Class Bitch!!
        self.name=name

ayush=Beta("Ayush","ajmadarchod@gmail.com")
print(ayush.email)                