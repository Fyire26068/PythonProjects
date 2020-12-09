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
       |  \\______|     |        |    |      \\__|
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


def slowText(text, speed=.03):
#This is so you have the option to put in slower or faster text. The default is 0.03
    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(speed)
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
          slowText(str.format("Please enter a number between {} and {}.", low, high-1))
    return(response)

def learn():
    """Displays the story of the game"""
    story = """ Some time ago, the darkness was cursed. The spirit world and the Other World
have been connected to your world by the darkness. Despite all this, you and your group are venturing into
a dangerous land to find a new home. Be prepared, be careful where you go, and beware of the darkness, unless
you can appease it.
    """
    slowText(story, 0.045)



def charSetup():
    """Sets the players class and starting money"""
    pClass = ""
    classOptions = ["(1) Knight (Starts with: 1000 gold)", "(2) Wizard (Starts with 800 gold)", "(3) Bard (Starts with 400 gold)", "(4) Cultist (Starts with 300 gold)", "(5) Blacksmith (Starts with 500 gold)", "(6) Explanation of Choices"]
    while True:
        slowText("Choose a class.")
        choice = getNumber(classOptions, len(classOptions)+1, 1)
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
            slowText("The Knight is the best at fighting monsters.")
            slowText("The Wizard can fight demons and monsters.")
            slowText("The Bard can play music to get money and appease ghosts.")
            slowText("The cultist can appease all those in the dark (monsters, ghosts, demons).")
            slowText("The blacksmith can make weapons so he doesn't always have to buy them.")#I'll change this later

def moneySetup(pClass):
    if pClass == "Knight":
        money = 1000
        return money
    elif pClass == "Wizard":
        money = 800
        return money
    elif pClass == "Bard":
        money = 400
        return money
    elif pClass == "Cultist":
        money = 300
        return money
    elif pClass == "Blacksmith":
        money = 500
        return money


def nameSetup():
    """Sets the player name and party member names"""
    name = getInput("What is your name?", 2, 15)
    party.append(name)
    partySize = getNumber("How many are in your group? ", 8, 3)
    for i in range(1, partySize):
        name = getInput(str.format("What is party member {}'s name?", i+1), 2, 15)
        party.append(name)
    for i in range(0, len(party)):
      slowText(str.format("{} {}", i+1, party[i]))
    return party

def getInput(question, minLength, maxLength):
    while True:
        slowText(question)
        pInput = input()
        if len(pInput) >= minLength and len(pInput) <= maxLength:
            return pInput
        elif len(pInput) < minLength:
            slowText(str.format("Input must be at least {} characters.", minLength))
        elif len(pInput) > maxLength:
            slowText(str.format("Input must be shorter than {} characters.", maxLength+1))


def StartScreen():
    """ Displays the start menu with 3 options, start, learn, exit"""
    while True:
        oBanner = """THE UNNAMED ROUTE\n-------------------"""
        print(oBanner)
        startOptions = ["(1) Travel the Trail", " (2) Learn about the Trail", " (3) End"]
        startOptions[0:3]
        choice = getNumber(startOptions, len(startOptions)+1, 1)
        while True:
            if int(choice) == 1:#Play
                play()
                break
            elif int(choice) == 2:#Learn about trail
                slowText("Story: ")
                learn()
                break
            elif int(choice) == 3:#quit
                slowText("Quit")
                break
        if int(choice) == 3:#checks if the user quit before restarting the start screen
            break

def play():
    """Player chooses class, names of party, and game starts"""
    pClass = charSetup()
    party = nameSetup()
    money = moneySetup(pClass)
    
def startMonth()
    pass
    
def shop(money, food, arrows, clothes, parts, horses):
    bill = 0 
    items = ["Food", "Arrows", "Clothes", "Cart Parts", "Horses", "Check Out"]
    spentOnItems = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, bill]
    slowText("Before leaving CITYNAMEHERE you should buy some supplies for your journey.")
    slowText(str.format("you have {} gold pieces to spend on supplies.", money))
    slowText("Remember, you can buy supplies along the way.")
    input(slowText("Press Enter to Continue\n"))
    while True:
        for
    #I'm closing this n


#Universal Variables
party = []
#game startup
LogoScreen()
input()#stop to check def
StartScreen()
input()#stop to check def
