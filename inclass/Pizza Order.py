from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.nameLbl = Label(self, text="Name: ",height=1).grid(row=0, column=0)
        self.nameTxt = Text(self,height=1).grid(row=0,column=1,columnspan=1)

        self.phoneLbl = Label(self, text="Phone Number: ", height=1).grid(row=0, column=2)
        self.phoneTxt = Text(self,height=1).grid(row=0,column=3)

        self.addressLbl = Label(self, text="Address: ", height=1).grid(row=1,column=0)
        self.addressText = Text(self,height=1).grid(row=1,column=1,columnspan=2)

        self.type = StringVar()
        self.type.set(None)
        self.delLbl = Label(self, text="Delivery ").grid(row=2,column=0)
        self.carLbl = Label(self, text="Carry-Out ").grid(row=2,column=2)
        

def main():

    root = Tk()
    root.title("checkbox tester")
    root.geometry("1200x1200")
    root.attributes("-fullscreen", False)
    app = App(root)
    root.mainloop()


main()