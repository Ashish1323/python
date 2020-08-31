is_magician=input("are you a magician??")
is_expert=input("are you an expert??")

if is_magician == "yes" or  is_magician == "y":
    is_magician= True
else:
    is_magician=False

if is_expert == "yes" or is_expert == "y":
    is_expert= True
else:
    is_expert=False

if is_magician and is_expert:
    print("You are a master!!")
elif is_magician:
    print("atleast you are getting there!!")
else:
    print("grow up man!!")



