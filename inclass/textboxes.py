from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        self.lbl = Label(self,text="Enter your username and password")
        self.lbl.grid(row=0, column=0, columnspan=3, sticky=N)

        self.lbl1 = Label(self, text="Username: ")
        self.lbl1.grid(row=1, sticky=W)

        self.lbl2 = Label(self, text="Password: ")
        self.lbl2.grid(row=2, sticky=W)

        self.btn = Button(self, text="Submit",height=1)
        self.btn.grid(row=3, sticky=W)
        self.btn["command"] = self.submit

        self.userText = Text(self, height=1)
        self.userText.grid(row=1, column=1, columnspan=2)

        self.passText = Text(self, height=1)
        self.passText.grid(row=2, column=1, columnspan=2)

        self.output = Text(self).grid(row=4, columnspan=3)

    def submit(self):
        self.username = self.userText.get()
        self.password = self.passText.get()




def main():

    root = Tk()
    root.title("textbox tester")
    root.geometry("500x300")
    root.attributes("-fullscreen", False)
    app = App(root)
    root.mainloop()

main()
