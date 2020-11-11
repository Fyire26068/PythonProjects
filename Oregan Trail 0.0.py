#OREGON TRAIL PROJECT
#Anthony Garrard // Caleb Keller
#started 11/20
import time
import sys
def LogoScreen():
  """Displays Logo, Names, and copyright"""
  logo = """
                  _____________
                 |   ___    __/
                 |  |   |  |
                 |  |   |  |
                 |  |   |  |___________________
                 |  |___|          _________   |
                 |      ________  |_________|  |
        __       |     |        |     ______   |
       |  \______|     |        |    |      \\__|
       |   _________   |________|    |
       |  |_________|          ___   |
       |___________________   |   |  |
                           |  |   |  |
                           |  |   |  |
                         __|  |___|  |
                        \\____________| """
  names = "Anthony // Caleb"
  cright = "©Shuriken Studios"
  print(logo, names, cright, sep="\n")


def slowText(text):

    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(0.5)
    print()

def getNumber(question,high,low):
    responce = None
    while True:
      slowText(question)
      response = input()
      if response.isnumeric() and int(response) in range(low, high):
          response = int(response)
          break
      else:
          slowText("Please enter a valid number.")
    return(response)

def learn():
    """Displays the story of the game"""
    story = """ You are journeying far across the land to settle in an unexplored area.
You will have to fight through the various dangers along your path.
Beware of the dark, but remember its usefulness.
Be careful of the routes you choose.
Remember to get all the supplies you need.
    """
    slowText(story)
    StartScreen()

    ##for i in range
     #print()
    #input()
def charSetup():
    pClass = ""
    classOptions = ["(1) Knight (Starts with: $1000)", "(2) Wizard (Starts withg)", "(3) Bard ", "(4) Cultist ", "(5) Blacksmith ", "(6) Explanation of Choices"]
    slowText("Choose a class.")
    choice = getNumber(classOptions, len(classOptions)+1, 1)
    while True:
        if choice == 1:
            pClass = "Knight"
            slowText("You are a " + pClass)
            return pClass
        elif choice == 2:
            pClass = "Wizard"
            slowText("You are a " + pClass)
            return pClass
        elif choice == 3:
            pClass = "Bard"
            slowText("You are a " + pClass)
            break
        elif choice == 4:
            pClass = "Cultist"
            slowText("You are a " + pClass)
            return pClass
        elif choice == 5:
            pClass = "Blacksmith"
            slowText("You are a " + pClass)
            return pClass
        elif choice == 6:
            #Tells user what each class does
            slowText("The Knight is the best at fighting.")
            charSetup()

def nameSetup():
    pName1 = input("What is your name?")
    party.append(pName1)
    for i in range(1, 5):
        name = input(str.format("What is party member {}'s name?", i+1))
        party.append(name)
    x = 0
    for i in range(0, len(party)):
      x = x+1
      slowText(str.format("{} {}", x, party[i]))
    return party
def play():
    """Player chooses class, names of party, and game starts"""
    pClass = charSetup()
    nameSetup()
    

#were going to have to exit now...


def checkValue(rightValue, value):
    """Checks to see if the value is valid or not"""
    valueType = type

def StartScreen():
    """ Displays the start menu with 3 options, start, learn, exit"""
    oBanner = """THE UNNAMED ROUTE\n-------------------"""
    print(oBanner)
    startOptions = ["(1) Travel the Trail", " (2) Learn about the Trail", " (3) End"]
    startOptions[0:3]
    choice = getNumber(startOptions, len(startOptions)+1, 1)
    while True:##You can run this though the command prompt, it's easier.
        if int(choice) == 1:#Play
            slowText("Travel the Trail")
            play()
            break
        elif int(choice) == 2:#Learn about trail
            slowText("Learn the Trail")
            learn()
            break
        elif int(choice) == 3:#quit
            slowText("Quit")
            break


#Universal Variables
party = []
LogoScreen()
input()#stop to check def
StartScreen()
input()#stop to check def
