from tkinter import *


HEIGHT = 200
WIDTH = 200
TITLE = "new program"
BACKGROUND = "darkgray"
FONT = "San_Serif"



class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):
        pass


def main():
    root = Tk()
    root.geometry(str.format("{}x{}",WIDTH,HEIGHT))
    root.title(TITLE)
    root.config(bg = BACKGROUND)
    app = App(root)
    root.mainloop()

main()
