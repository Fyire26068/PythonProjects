# Anthony Garrard
#9/29/20
#guess my number v 1.1

import random
#setting variables
diDiff = 1
diMax = 11
diTrys = 3

print("Welcome to Guess My Number!")


#asking for difficulty
question = input("What Difficulty would you like Easy, Medium, or Hard?\n")

if question == " M" or question == " m" or question.startswith("M") or question.startswith("m") : #medium difficulty
    diDiff = 2
    diMax = 50
    diTrys = 5
elif question == " H" or question == " h" or question.startswith("H") or question.startswith("h") : #hard difficulty
    diDiff = 3
    diMax = 100
    diTrys = 10
else: #easy difficulty
    diDiff = 1
    diMax = 10
    diTrys = 3


theNum = random.randint(1,diMax) #creating the number
#print(theNum)


win = False

print(str.format("\nI'm thinking of a number between 1 and {0}", diMax))
print(str.format("\nYou have {0} guesses.", diTrys))

#guess1
guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))

if (guess == theNum) :
         win = True
elif guess > theNum:
    print("You need to guess lower")
    guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
else:
    print("You need to guess higher")
    guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))

#guess 2

if (guess == theNum) and (not win):
     win = True
elif win:
    pass
elif guess > theNum:
     print("You need to guess lower")
     guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
else:
     print("You need to guess higher")
     guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))

#guess 3
if diDiff == 2 or diDiff ==3:
    if (guess == theNum) and (not win):
        win = True
    elif win:
        pass
    elif guess > theNum:
         print("You need to guess lower")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
    else:
         print("You need to guess higher")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
else:
    pass

#guess 4
if diDiff == 2 or diDiff == 3:
    if (guess == theNum) and (not win):
        win = True
    elif win:
        pass
    elif guess > theNum:
         print("You need to guess lower")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
    else:
         print("You need to guess higher")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
else:
    pass
         
#guess 5
if diDiff == 3:
    if (guess == theNum) and (not win):
        win = True
    elif win:
        pass
    elif guess > theNum:
         print("You need to guess lower")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
    else:
         print("You need to guess higher")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
else:
    pass

#guess 6
if diDiff == 3:
    if (guess == theNum) and (not win):
        win = True
    elif win:
        pass
    elif guess > theNum:
         print("You need to guess lower")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
    else:
         print("You need to guess higher")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
else:
    pass

#guess 7
if diDiff == 3:
    if (guess == theNum) and (not win):
        win = True
    elif win:
        pass
    elif guess > theNum:
         print("You need to guess lower")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
    else:
         print("You need to guess higher")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
else:
    pass

#guess 8
if diDiff == 3:
    if (guess == theNum) and (not win):
        win = True
    elif win:
        pass
    elif guess > theNum:
         print("You need to guess lower")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
    else:
         print("You need to guess higher")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
else:
    pass

#guess 9
if diDiff == 3:
    if (guess == theNum) and (not win):
        win = True
    elif win:
        pass
    elif guess > theNum:
         print("You need to guess lower")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
    else:
         print("You need to guess higher")
         guess = int(input(str.format("Pick a number between 1 and {0}: \n", diMax)))
else:
    pass

#last guess (3, 5, 10)

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
