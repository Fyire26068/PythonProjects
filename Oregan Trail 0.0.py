# OREGON TRAIL PROJECT
# Anthony Garrard // Caleb Keller
# started 11/20
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
    # Logo and copyright


def slowText(text, speed=.03, sleeping=0.3):
    # This is so you have the option to put in slower or faster text.
    # The defaults are 0.03, and 0.3.
    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(sleeping)
    print()


def getNumber(question, high, low):
    """Gets a number and a range that it can be accepted in."""
    response = None
    while True:
        slowText(question)
        response = input()
        if response.isnumeric() and int(response) in range(low, high):
            response = int(response)
            break
        else:
            slowText(str.format("Please enter a number between {} and {}.", low, high-1))
    return response


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
    classOptions = ["(1) Knight (Starts with: 1000 gold)\n", "(2) Wizard (Starts with 800 gold)\n",
                    "(3) Bard (Starts with 400 gold)\n", "(4) Cultist (Starts with 300 gold)\n",
                    "(5) Blacksmith (Starts with 500 gold)\n", "(6) Explanation of Choices\n"]
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
            # Tells user what each class does
            slowText("The Knight is the best at fighting monsters.")
            slowText("The Wizard can fight demons and monsters.")
            slowText("The Bard can play music to get money and appease ghosts.")
            slowText("The cultist can appease all those in the dark (monsters, ghosts, demons).")
            slowText("The blacksmith can make weapons so he doesn't always have to buy them.")


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
        choice = getNumber(startOptions, len(startOptions)+1, 1)
        while True:
            if int(choice) == 1:  # Play
                play()
                break
            elif int(choice) == 2:  # Learn about trail
                learn()
                break
            elif int(choice) == 3:  # quit
                slowText("Quit", 0.015)
                break
        if int(choice) == 3:  # checks if the user quit before restarting the start screen
            break


def play():
    """Player chooses class, names of party, and game starts"""
    pClass = charSetup()
    party = nameSetup()
    money = moneySetup(pClass)
    slowText("Before leaving STARTINGCITYNAMEHERE you should buy some supplies for your journey.")
    money = shop(money, food, arrows, clothes, parts, horses, len(party))
    distance = turn(0)
    while distance < 42000:
        distance = turn(distance)



def turn(distance):
    """the main part of the game"""
    slowText(str.format("You have traveled {} miles towards your goal."))
    if distance == 0:
        slowText("You are ready to depart from STARTINGCITYNAMEHERE.")
        pace = setPace()
        if pace == 1:
            distance += 200
        elif pace == 2:
            distance += 300
        elif pace == 3:
            distance += 400
        return distance
    else:
        slowText("Yet another day furthering your journey.")
        pace = setPace()
        if pace == 1:
            distance += 200
        elif pace == 2:
            distance += 300
        elif pace == 3:
            distance += 400
        return distance

def setPace():
    """sets the pace for a turn"""
    slowText("""(1) Slow
    (2) Regular
    (3) Fast""")
    pace = getNumber("What would you like your pace to be?", 3, 1)
    return pace
def startMonth():
    pass


def shop(money, food, arrows, clothes, parts, horses, partySize):
    bill = 0
    inventory = []
    items = ["Horses", "Food", "Clothes", "Arrows", "Cart Parts", "Check Out"]
    spentOnItems = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, bill]
    slowText(str.format("You have {} gold pieces to spend on supplies.", money))
    slowText("Remember, you can buy supplies along the way.")
    slowText("Press Enter to Continue")
    input()
    slowText("Welcome to the NAMESHOPHERE shop!")
    slowText("Here are the things you can buy: ")
    while True:
        spentOnItems[len(spentOnItems)-1] = bill
        print()
        for i in range(len(items)-1):
            slowText(str.format("{}.        {:20}   {:.2f} Gold", i+1, items[i], spentOnItems[i]), 0.02, 0)
        slowText("6.        Checkout")
        slowText(str.format("Total Bill so far:        {:.2f} Gold", bill), 0.02)
        slowText(str.format("Total funds available:    {:.2f} Gold", money-bill), 0.02)
        choice = getNumber("What would you like to buy?", 7, 1)
        if choice == 1:
            bill -= spentOnItems[0]
            horses = 0
            spentOnItems[0] = 0.00
            slowText("For a group your size, I'd reccommend at least 3 horses")
            slowText("I charge 40 gold for a horse")
            answer = getNumber("How many horses do you want?", partySize+1, 0)
            cost = int(answer) * 40
            horses = answer
            bill += cost
            spentOnItems[0] = cost
        elif choice == 2:
            bill -= spentOnItems[1]
            food = 0
            spentOnItems[1] = 0.00
            slowText(str.format("""I reccommend you take at least 40 rations for each person in your party.
            I see that you have {} party members. My price is 1 gold per ration.""", partySize))
            answer = getNumber("How many rations of food do you want?", 50*partySize, 0)
            cost = int(answer)
            food = answer
            bill += cost
            spentOnItems[1] = cost
        elif choice == 3:
            bill -= spentOnItems[2]
            clothes = 0
            spentOnItems[2] = 0.00
            slowText("""You'll need warm clothing when your quest takes you to the mountains.
            I recommend taking at least 2 sets of clothes per person. Each set is 10 gold.""")
            answer = getNumber("How many sets of clothes do you want?", partySize*3, 0)
            cost = int(answer) * 10
            clothes = answer
            bill += cost
            spentOnItems[2] = cost
        elif choice == 4:
            bill -= spentOnItems[3]
            arrows = 0
            spentOnItems[3] = 0.00
            slowText("""I sell arrows in quivers of 20 arrows. Each quiver is 2 gold.""")
            answer = getNumber("How many quiver's do you want?", 150, 0)
            cost = int(answer) * 2
            arrows = answer
            bill += cost
            spentOnItems[3] = cost
        elif choice == 5:
            bill -= spentOnItems[4]
            partsBill = 0
            parts[0] = 0
            parts[1] = 0
            parts[2] = 0
            spentOnItems[4] = 0.00
            slowText("""It's a good idea to have a few spare parts for your carriage.
            """)
            partsList = ["carriage wheel", "carriage axle", "horse lead"]
            partsCost = [0, 0, 0, partsBill]
            while True:
                partsCost[len(partsCost)-1] = partsBill
                slowText("Here is a list of cart parts you can purchase :")
                for i in range(len(partsList)):
                    slowText(str.format("{}.    {:20}       {:.2f} gold", i+1, partsList[i], partsCost[i]))
                slowText("4.    Continue to Shop")
                print(str.format("Parts Bill so far:        {:.2f} gold", partsBill))
                slowText(str.format("Total funds available: {:.2f} gold", money-bill))
                item = getNumber("what Item would you like to buy?", 5, 1)
                if item == 1:
                    partsBill -= partsCost[0]
                    partsCost[0] = 0
                    answer = getNumber("How many carrige wheels do you want?", 4, 0)
                    for i in range(answer):
                        inventory.append("Cart Wheel")
                    partsCost[0] = 10*answer
                    partsBill += partsCost[0]
                elif item == 2:
                    partsBill -= partsCost[1]
                    partsCost[1] = 0
                    answer = getNumber("How many carrige axels do you want?", 4, 0)
                    for i in range(answer):
                        inventory.append("Carrige Axle")
                    partsCost[1] = 10*answer
                    partsBill += partsCost[1]
                elif item == 3:
                    partsBill -= partsCost[2]
                    partsCost[2] = 0
                    answer = getNumber("I charge 1 gold for each horse lead. How many horse Leads did you want?", 10, 0)
                    for i in range(answer):
                        inventory.append("Horse Lead")
                    partsCost[2] = answer
                    partsBill += partsCost[2]
                elif item == 4:
                    bill += partsBill
                    spentOnItems[4] = partsBill
                    break
        elif choice == 6:
            newMoney = money -  bill
            return newMoney
        else:
            slowText("Choose a valid option between 1 and 6")
            input()


        input()


# Universal Variables
money = 1000
food = 0
arrows = 0
clothes = 0
parts = [0, 0, 0]
partySize = 3
horses = 0
party = []
distance = 0
#shop(money, food, arrows, clothes, parts, horses, partySize)
# game startup
LogoScreen()
input()  # top to check def
StartScreen()
input()  # stop to check def
play()

slowText("Great Job!, you reached the jewel filled city of DWARFCITYNAMEHERE. \nYou now are amongst many riches and opportunitys.")