import random

class Critter(object):
    """this is the class that defines what a critter is"""
    def __init__(self):
        self.health = 100
        self.hunger = 0
        self.height = 0
        self.weight = random.randint(2,7)
        self.name = ""
        self.happy = 50

    def getHunger(self):
        return self.hunger
    def getHealth(self):
        return self.health
    def getWeight(self):
        return self.weight
    def getName(self):
        return self.name

    def setName(self, name):
        if len(name) > 4:
            if (name.contains("uck")) == False:
                self.name = name

    def setHeight(self, height):
        if height < 5 and height > 1:
            self.height = height



    def intro(self):
        print("hello my name is "+self.name)

    def feed(self, food):
        if food == "pizza":
            self.hunger -= 7
        elif food == "cheese burger":
            self.hunger -= 13
        elif food == "steak":
            self.hunger -= 18
        elif food == "corn":
            self.hunger -= 3
        elif food == "cheesecake":
            self.hunger -= 100
        else:
            self.hunger -= 5

    def hud(self):
        health = self.getHealth()
        if health > 80:
            print("Health: Great")
        elif health >60:
            print("Health: Good")
        elif health > 50:
            print("Health: Fair")
        elif health == 0:
            self.die()
        else:
            print("Health: Poor")
        hunger = self.getHunger()

        happy = self.getHappy()
        if happy > 50:
            print("Happy = Very Happy")
        elif happy > 35:
            print("Happy = Upset")
        else:
            print("Happy = Pissed")
            
    
    def passTime(self, hours):
        for i in range(hours):
            self.hunger += 2
            if self.hunger < 0:
                self.weight += 1
                self.happy += 10
                self.health -= 5
            if self.hunger >50:
                self.weight -= 1
                self.happy -= 10
                self.health -= 5
            self.happy -= 5

    

    def play(self,time):
        self.passTime(self, time)
        self.happy += 10*time
        if self.happy >100:
            self.happy = 100
        self.health

    def main():
        critter1 = Critter()
        critter1.name = "BOB"
        critter2 = Critter()
        critter2.name = "FRANK"

        critter1.intro()
        print(critter2.name)
