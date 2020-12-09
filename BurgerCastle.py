#Anthony Garrard
#chapter 6 activity

validOrders = ("burger", "fries", "salad", "soda", "milkshake")
itemDescriptions = ("Half-pound burger", "Large fries", "Side salad", "Diet root beer", "Chocolate shake")
order = []

print("Welcome to Burger Castle")
print("Menu:", validOrders)
print("Please enter each item in your order. Press 'Enter' or type 'quit on an empty line when done.")

while True:
    item = input("Enter item: ")
    if item in validOrders:
        order.append(item)
    elif item == "quit" or item == "":
        break
    else:
        print("Sorry, we don't sell", item)

print("\nOrder complete. You are having:")
for item in order:
    index = validOrders.index(item)
    description = itemDescriptions[index]
    print(description)

print("Thanks for visiting Burger Castle!")
