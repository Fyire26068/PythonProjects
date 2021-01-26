# Anthony Garrard
# Game functions that can be used just about anywhere
#1/21


import time
import sys
import datetime
import random
import math
def slowText(text, speed=.03, sleeping=0.3):
#This is so you have the option to put in slower or faster text.
#The defaults are 0.03, and 0.3.
    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(sleeping)
    print()

def askYesNo(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def getNumber(question,high,low):
    """Gets a number and a range that it can be accepted in."""
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

class Player(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        self.lives = 3

class Score(object):

    def __init__(self):
        self.value = 0
        self.stepvalue = 10

    def addTo(self,itemid):
        for i in range(itemid):
            self.value += self.step

    def takeFrom(self, itemid):
        for i in range(itemid):
            self.value -= self.stepvalue



if __name__ == "__main__":
    print("You ran this module directly(and did not 'import' it).")
    input("\n\nPress the enter key to exit.")
