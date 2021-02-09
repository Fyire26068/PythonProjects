from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.displayText = "0"
        self.value1 = DoubleVar
        self.value2 = DoubleVar
        self.operator = StringVar
        self.result = DoubleVar

        self.display = Label(self, text="0", font=("Courier", 44))
        self.display.grid(column=0, row=0, columnspan=4, sticky=E)




        self.add = Button(self, text="+", font=("Courier", 44), command=self.add)
        self.add.grid(column=3, row=4, sticky=E)

        self.sub = Button(self,text = "-", font=("Courier", 44), command = self.subtract)
        self.sub.grid(column=3, row=3, sticky=E)

        self.mult = Button(self, text="*", font=("Courier", 44), command= self.multiply)
        self.mult.grid(column=3, row=2, sticky=E)

        self.div = Button(self, text="/", font=("Courier", 44),  command= self.divide)
        self.div.grid(column=3, row=1, sticky=E)

        self.one = Button(self, text="1", font=("Courier", 44), command=self.numberOne)
        self.one.grid(column=0, row=3, sticky=E)

        self.two = Button(self, text="2", font=("Courier", 44), command=self.numberTwo)
        self.two.grid(column=1, row=3, sticky=E)

        self.three = Button(self, text="3", font=("Courier", 44), command=self.numberThree)
        self.three.grid(column=2, row=3, sticky=E)

        self.four = Button(self, text="4", font=("Courier", 44), command=self.numberFour)
        self.four.grid(column=0, row=2, sticky=E)

        self.five = Button(self, text="5", font=("Courier", 44), command=self.numberFive)
        self.five.grid(column=1, row=2, sticky=E)

        self.six = Button(self, text="6", font=("Courier", 44), command=self.numberSix)
        self.six.grid(column=2, row=2, sticky=E)

        self.seven = Button(self, text="7", font=("Courier", 44), command=self.numberSeven)
        self.seven.grid(column=0, row=1, sticky=E)

        self.eight = Button(self, text="8", font=("Courier", 44), command=self.numberEight)
        self.eight.grid(column=1, row=1, sticky=E)

        self.nine = Button(self, text="9", font=("Courier", 44), command=self.numberNine)
        self.nine.grid(column=2, row=1, sticky=E)

        self.zero = Button(self, text="0", font=("Courier", 44), command=self.numberZero)
        self.zero.grid(column=1, row=4, sticky=E)

        self.clear = Button(self, text="C", font=("Courier", 44))
        self.clear.grid(column=0, row=4, sticky=E)

        self.equal = Button(self, text="=", font=("Courier", 44))
        self.equal.grid(column=2, row=4, sticky=E)





    # NUMBER commands

    def numberOne(self):
        if self.displayText == "0":
            self.displayText = "1"
        else:
            self.displayText += "1"
        self.display["text"] = self.displayText

    def numberTwo(self):
        if self.displayText == "0":
            self.displayText = "2"
        else:
            self.displayText += "2"
        self.display["text"] = self.displayText

    def numberThree(self):
        if self.displayText == "0":
            self.displayText = "3"
        else:
            self.displayText += "3"
        self.display["text"] = self.displayText

    def numberFour(self):
        if self.displayText == "0":
            self.displayText = "4"
        else:
            self.displayText += "4"
        self.display["text"] = self.displayText

    def numberFive(self):
        if self.displayText == "0":
            self.displayText = "5"
        else:
            self.displayText += "5"
        self.display["text"] = self.displayText

    def numberSix(self):
        if self.displayText == "0":
            self.displayText = "6"
        else:
            self.displayText += "6"
        self.display["text"] = self.displayText

    def numberSeven(self):
        if self.displayText == "0":
            self.displayText = "7"
        else:
            self.displayText += "7"
        self.display["text"] = self.displayText

    def numberEight(self):
        if self.displayText == "0":
            self.displayText = "8"
        else:
            self.displayText += "8"
        self.display["text"] = self.displayText

    def numberNine(self):
        if self.displayText == "0":
            self.displayText = "9"
        else:
            self.displayText += "9"
        self.display["text"]=self.displayText


    def numberZero(self):
        if self.displayText == "0":
            self.displayText = "0"
        else:
            self.displayText += "0"
        self.display["text"] = self.displayText


    # Operator Commands

    def add(self):

        self.operator = '+'
        if not self.value1:
            self.value1 = float(self.displayText)
        else:
            self.value2 = float(self.displayText)

            self.result = self.value1 + self.value2
            self.display.config(text=str(self.result))
            self.update()

    def subtract(self):
        self.operator = '-'
        if self.value1 == 0:
            self.value1 = float(self.displayText)
        else:
            self.value2 = float(self.displayText)

            self.result = self.value1 - self.value2
            self.update()

    def multiply(self):
        self.operator = '*'
        if self.value1 == 0:
            self.value1 = float(self.displayText)
        else:
            self.value2 = float(self.displayText)

            self.result = self.value1 * self.value2
            self.update()

    def divide(self):
        self.operator = '/'
        if self.value1 == None:
            self.value1 = float(self.displayText)
        else:
            self.value2 = float(self.displayText)

            self.result = self.value1 / self.value2
            self.update

    def equals(self):
        if self.value1 == None:
            self.value1 = float(self.displayText)
        else:
            self.value2 = float(self.displayText)
            if self.operator == "+":
                self.result = self.value1 + self.value2

            elif self.operator == "-":
                self.result = self.value1 - self.value2
            elif self.operator == "*":
                self.result = self.value1 * self.value2
            elif self.operator == "/":
                self.result = self.value1 / self.value2
            self.operator = None
            self.value1 = self.result
            self.update





    def update(self):
        self.displayText = self.result
        self.display = self.displayText


def main():
    root = Tk()
    root.title("Calculator")
    root.geometry("350x500")
    root.attributes("-fullscreen", False)
    app = App(root)
    root.mainloop()

main()


