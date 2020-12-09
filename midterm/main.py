#trivia challenge
#trivia game that read a plain text file
#Anthony Garrard
#12/7/20

#import time
import sys
from datetime import datetime

#func
def openFile(fileName, mode):
    """open and return a open file"""
    try:
        file = open("assets/test/"+fileName,mode)
    except IOError as e:
        print("Unable to open the file", fileName, "Ending program. \n", e)
        try:
            file = open("assets/errors/errorsLog.txt","a+")
            time = datetime.now()
            errorTime = time.strftime("%m/%d/%Y %H:%<:%S")
            file.write(str(e)+" "+str(errorTime)+"\n")
            input("\n\nPress the enter key to exit.")
            sys.exit()

        except:
            sys.exit()
    else:
        return file

def getName():
    """Gets the name of person taking the test"""
    try:
        time = datetime.now()
        testTime = time.strftime("%m/%d %H:%M")
        while True:
            name = input("Enter your name : ")

            if(len(name)>2) and (" " in name):
                name = name.title()
                return name, time

            else:
                print("Not a valid name")

    except:
        print("something went wrong while getting the name")
            

def nextLine(file):
    try:
        line = file.readline()
        line = line.replace("/","\n")
        return line
    except:
        print("Could not read line")
        sys.exit


def nextQuestion(file):
    """Return the contents of the next question"""
    category = nextLine(file)
    question = nextLine(file)
    answers = []
    for i in range(4):
        answers.append(nextLine(file))
    correct = nextLine(file)
    if correct:
        correct = correct[0]

    explanation = nextLine(file)
    return category, question, answers, correct, explanation

def welcome(title, name, testTime):
    """Welcome the player"""
    print("Welcome "+name+" to your Mid Term\n")
    print("your tester is" +title)

def createReportCard(name,score,totalQuestions):
    card = open("assets\\ReportCards\\"+name+".txt"  ,"w")
    card.write("Name = "+name+"\n")
    card.write("Number Correct = "+str(score)+"\n")
    percentage = score/totalQuestions*100
    card.write("Percentage Correct = " +"%"+str(percentage)+"\n")
    if percentage >= 90:
        card.write("Letter Grade = A")
    elif percentage >= 80:
        card.write("Letter Grade = B")
    elif percentage >= 70:
        card.write("Letter Grade = C")
    elif percentage >= 60:
        card.write("Letter Grade = D")
    else:
        card.write("Letter Grade = F")


def main():
    file = openFile("CounterStrikeGlobalTrivia.txt", "r")#needs to change to match
    title = nextLine(file)
    name, testTime = getName()
    welcome(title,name,testTime)
    score = 0
    totalQuestions = 0
    category, question, answers, correct, explanation = nextQuestion(file)
    while category:
        totalQuestions += 1
        print(category)
        print(question)
        for i in range(len(answers)):
            print(str.format("\t{}:  {}", i+1, answers[i]))
        #get answer
        answer = input("What is your answer?\n")
        #check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score +=1
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        category, question, answers, correct, explanation = nextQuestion(file)
    file.close()
    print("That was the last question!")
    print("You're final score is", score)
    createReportCard(name, score, totalQuestions)
main()
