# Anthony Garrard
#9/29/20
#guess my number v 1.0

import random

theNum = random.randint(1,10) #creating the number

win = False

print("Welcome to Guess My Number!")
print("\nI'm thinking of a number between 1 and 10")
print("\nYou have three guesses.")

#guess1
if not win: 
    guess = int(input("Pick a number between 1 and 10: \n"))


    if guess == theNum:
            print("You guessed the number first try, great job!")
            win = True
    elif guess > theNum:
        print("You need to guess lower")
    else:
        print("You need to guess higher")
else:
    pass

#guess 2
if  not win: 
    guess = int(input("Pick a number between 1 and 10: \n"))


    if guess == theNum:
        print("You guessed the number, great job!")
        win = True
    elif guess > theNum:
        print("You need to guess lower")
    else:
        print("You need to guess higher")
else:
    pass

#guess3
if not win:
    guess = int(input("Pick a number between 1 and 10 : \n"))

    if guess == theNum:
       print("You guessed the number, great job!")
       win = True
    else:
        print("You did not guess the number")
        print("The number was :", theNum)
else:
    pass
