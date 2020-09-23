# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
nannu = Cat("nannu", 10)
monu = Cat("monu", 20)
shanu = Cat("shanu", 25)


# 2 Create a function that finds the oldest cat
def oldestcat(x, y, z):
    if x > y and x > z:
        return x
    elif y > z and y > z:
        return y
    else:
        return z


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print("The oldest cat is " +
      str(oldestcat(nannu.age, monu.age, shanu.age)) + " years old")
