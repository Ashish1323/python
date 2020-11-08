import random
import sys

randomno = random.randint(int(sys.argv[1]), int(sys.argv[2]))

abc = 2
while(abc):
    try:
        checker = int(input("guess the number!!"))
        if checker == randomno:
            print("you got it yooo!!!")
            break
        else:
            print('hey bozo, I said You Suck')

    except ValueError:
        print('please enter a number')
        continue
