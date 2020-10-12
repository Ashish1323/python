class User():
    def sign_in(self):  
        print('logged in')
            
class Wizard(User):
    def __init__(self, name, power):
        self.name=name
        self.power=power
 
    def attacks(self):
        print(f'Attacking with Power of {self.power}')
        
    
class Archer(User):
    def __init__(self, name, arrows):
        self.name=name
        self.arrows=arrows
    
    def attack(self):
        print(f'Attacking with arrows: arrows left- {self.arrows}')     
    
    def run(self):
        return('ran really fast')
 
    
class Hybrid(Wizard, Archer): #Inherits from Wizard and User
    def __init__(self, name, power, arrows):
        Archer.__init__ (self, name, arrows)
        Wizard.__init__ (self, name, power)

hb1=Hybrid('borgie', 50, 100)   
print(hb1.attack())
print(hb1.attacks())
     
 
 
# wizard1= Wizard('Merlin', 50)
# archer1= Archer('Robin', 100)
    
# wizard1.attack()
# archer1.attack()   