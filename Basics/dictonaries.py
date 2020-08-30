#keyword is dict

loda={"a":2,"b":23}

#get the value from the key
print(loda["a"])


#print items in dict
print(loda.items())

#print keyss in dict
print(loda.keys())

#print values in dict
print(loda.values())

#clear() clear the dict
#copy() to copy the dict

#updating the exisiting thing
loda.update({"a":69})
print(loda)

#updating the non exisiting thing hence creating the one
loda.update({"a2":69})
print(loda)

