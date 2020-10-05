name = input("What is your name?")

print(str.format("Hi {}, nice to meet you. I am Chatbot-1024."))


sport = input("What is your favorite sport?")

if sport == football:
    yards = int(input("I like football too. Can you tell me the length of a football field in yards?"))
    if yards < 100:
        print("No, too short.")
    elif yards >100:
        print("No, too long.")
    else:
        print("That's right!")
elif sport == baseball:
    strikes = int(input("I play baseball every summer. How many 'strikes' does it take to get a batter out?"))
    if strikes == 3:
        print("Yes, 1, 2, 3 strikes you're out...")
    else:
        print("Actually, 3 strikes will get a batter out.")
elif sport == basketball:
    pass
else:
    pass

