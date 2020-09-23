class ashish: #class declaration
    sex="6ka" #class object attribute!!
    def __init__(self,name): #constructor
        self.name=name #attribute

    def loda(self): #function
        return print( self.name +" is loda")      
x=ashish("raju") #calling class

print(x.loda())