from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def c(i):
    return i.capitalize()

print(list(map(c,my_pets)))
# output ['Sisi', 'Bibi', 'Titi', 'Carla']

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
x=sorted(my_numbers)
print(list(zip(my_strings,my_numbers)))

#output- [('a', 5), ('b', 4), ('c', 3), ('d', 2), ('e', 1)]

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def score(s):
    return s > 50
print(list(filter(score,scores)))    

#output [73, 65, 76, 100, 88]

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
meganumbers= my_numbers + scores
def ass(a,i):
    return a+i
print(reduce(ass,meganumbers,0))    

#output 456