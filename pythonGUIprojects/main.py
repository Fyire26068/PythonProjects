from tkinter import *
from PIL import Image, ImageTk
HEIGHT = 750
WIDTH=250

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack()
        self.createWidgits()

    def createWidgits(self):
        Label(text="my favorite Images").place(x=5, y=5)

def main():
    root = Tk()
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    app = App(root)
    root.mainloop()


main()