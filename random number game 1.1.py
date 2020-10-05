# Anthony Garrard
#9/29/20
#guess my number v 1.1

import random

theNum = random.randint(1,10) #creating the number
#print(theNum)
win = False

print("Welcome to Guess My Number!")
print("\nI'm thinking of a number between 1 and 10")
print("\nYou have three guesses.")

#guess1
guess = int(input("Pick a number between 1 and 10: \n"))

if (guess == theNum) :
         win = True
elif guess > theNum:
    print("You need to guess lower")
    guess = int(input("Pick a number between 1 and 10: \n"))
else:
    print("You need to guess higher")
    guess = int(input("Pick a number between 1 and 10: \n"))

#guess 2

if (guess == theNum) and (not win):
     win = True
elif win:
    pass
elif guess > theNum:
     print("You need to guess lower")
     guess = int(input("Pick a number between 1 and 10: \n"))
else:
     print("You need to guess higher")
     guess = int(input("Pick a number between 1 and 10: \n"))

#guess3

if (guess == theNum) and (not win):
     win = True
elif win:
    pass
else:
        print("You did not guess the number")
        print("The number was :", theNum)

if win:
    print("You guessed the number!")

input()
