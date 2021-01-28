from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        self.titlelbl = Label(self, text="What do you like?")
        self.titlelbl.grid(row=0, column=0, columnspan=3, sticky=N)

        self.selectlbl = Label(self, text="Select all that Apply")
        self.selectlbl.grid(row=1,column=0, columnspan=2,sticky=W)

        self.likesPizza = BooleanVar()
        Checkbutton(self, text="Pizza",
                variable=self.likesPizza,
                command = self.update
                ).grid(row=2, column=0, sticky=W)

        self.likesTacos = BooleanVar()
        Checkbutton(self, text="Tacos",
                variable=self.likesTacos,
                command=self.update
                ).grid(row=3, column=0, sticky=W)

        self.likesHotdogs = BooleanVar()
        Checkbutton(self, text="Hot Dogs",
                 variable=self.likesHotdogs,
                 command=self.update
                ).grid(row=4, column=0, sticky=W)

        self.worstFood = StringVar()
        self.worstFood.set(None)
        Radiobutton(self,
                    text="Yams",
                    value="Yams",
                    variable=self.worstFood,
                    command=self.update
                    ).grid(row=5,column=0, sticky=W)
        Radiobutton(self,
                    text="Beets",
                    value="Beets",
                    variable=self.worstFood,
                    command=self.update
                    ).grid(row=6, column=0, sticky=W)
        Radiobutton(self,
                    text="Eggs",
                    value="Eggs",
                    variable=self.worstFood,
                    command=self.update
                    ).grid(row=7, column=0, sticky=W)






        self.resultstxt = Text(self, width=40, height=5, wrap=WORD)
        self.resultstxt.grid(row=8,column=0,columnspan=3)


    def update(self):
        likes = ""
        if self.likesPizza.get():
            likes += "You like Pizza\n"

        if self.likesTacos.get():
            likes += "You like Tacos\n"

        if self.likesHotdogs.get():
            likes += "You like Hot Dogs\n"

        likes += "your least favorite food is " +self.worstFood.get()

        self.resultstxt.delete(0.0,END)
        self.resultstxt.insert(0.0,likes)


def main():

    root = Tk()
    root.title("checkbox tester")
    root.geometry("300x300")
    root.attributes("-fullscreen", False)
    app = App(root)
    root.mainloop()

main()
