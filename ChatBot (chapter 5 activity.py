#Anthony Garrard
#Chapter 5 Activity : Chatbot
#10/20

name = input("What is your name?\n")

print(str.format("Hi {}, nice to meet you. I am Chatbot-1024.", name))


sport = input("What is your favorite sport?\n")

if sport == "football":
    yards = int(input("I like football too. Can you tell me the length of a football field in yards?\n"))
    if yards < 100:
        print("No, too short.")
    elif yards >100:
        print("No, too long.")
    else:
        print("That's right!")
elif sport == "baseball":
    strikes = int(input("I play baseball every summer. How many 'strikes' does it take to get a batter out?\n"))
    if strikes == 3:
        print("Yes, 1, 2, 3 strikes you're out...")
    else:
        print("Actually, 3 strikes will get a batter out.")
elif sport == "basketball":
    team = input("The Harlem Globetrotters are the best. Do you know the name of the team they always beat?\n")
    if  team == "Washington Generals":
        print("Yes, those Generals can never catch a break.")
    else:
        print("I think it's the Washington Generals.")
else:
    print(str.format("That sounds cool; I've never played {}.", sport))

