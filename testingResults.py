question = "What is your name?\n"
name = input(question)
print("Hello", name, "\n")
question2 = "Where do you live?\n"
question3 = "When is your birthday?\n"
question4 = "What is your Social Security Number?\n"
question5 = "What is your mother's maiden name?\n"
question6 = "What is the color of your first pet?\n"
question7 = "What is the CVC on the back of your credit card?\n"
question8 = "What is your email address?\n"
address = input(question2)
birthday = input(question3)
ssn = input(question4)
mname = input(question5)
pcolor = input(question6)
cvc = input(question7)
email = input(question8)
print("Name: " + name,
      "Address: " + address,"Birthday: " + birthday,"Social Security Number: " + ssn,
      "Mother's Maiden Name: " + mname,"First Pet's Color: " + pcolor,"CVC: " + cvc,
      "Email:" + email, sep = "\n")
print("Is this correct?")
confirm = input()
print(confirm, "Thank you")
      
