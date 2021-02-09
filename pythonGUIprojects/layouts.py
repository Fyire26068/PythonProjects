from tkinter import *
from PIL import Image, ImageTk
HEIGHT = 750
WIDTH=250

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill = BOTH,expand=1)
        self.createWidgits()

    def createWidgits(self):
        self.config(bg="DARKGREY")
        Label(text="my favorite Images", width=20).place(x=(WIDTH/2-70), y=5)
        # loaded images
        img1 = Image.open("Astralis_logo 200x200.png")
        img2 = Image.open("CSGO 200x200.png")
        img3 = Image.open("G2 200x200.png")

        #converted img to tk object
        logo1 = ImageTk.PhotoImage(img1)
        logo2 = ImageTk.PhotoImage(img2)
        logo3 = ImageTk.PhotoImage(img3)
        self.imglist = []

        imglbl1 = Label(self, image=logo1)
        imglbl1.image = logo1
        imglbl1.place(x=25,y=75)

        imglbl2 = Label(self, image=logo2)
        imglbl2.image = logo2
        imglbl2.place(x=25,y=300)

        imglbl3 = Label(self, image=logo3)
        imglbl3.image = logo3
        imglbl3.place(x=25,y=525)

    def changeimg(self):
        self.index +=1
        self.imglbl1.config(image=self.imglist[self.index])

def main():
    root = Tk()
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    app = App(root)
    root.mainloop()


main()