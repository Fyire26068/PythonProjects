def getMenuChoice():
    options = ["Burger, Fries, Soda", "Chicken Salad, Iced Tea", "Pizza, Soda"]
    cost = [6.99, 10.50, 5.72]

    print("Your Menu Choices are: ")
    for i in range(len(options)):
        print(str.format("{} - ${:5.2f}  : {}", i+1, cost[i], options[i]))
        

    choice = askNumber("What will you have?\n",0,len(options)+1)

    order = options[choice-1]
    price = cost[choice-1]
    tax = 0.075
    total = (price * tax)+ price

    print(str.format("Ok, you have ordered ----- {}", order))
    print(str.format("Out the door you are looking at ----- ${:5.2f}", total))

def askNumber(question,low,high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response

def askYesNo(question):
    """Ask a yes or no question. and will only return yes or no"""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

running = "y"
while running == "y":
    getMenuChoice()
    running = askYesNo("Do you want to order more?\n")

