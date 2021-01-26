#simple GUI
#demonstratres creating a window
from tkinter import *


root = Tk()
root.title("Ant's GUI")
root.geometry("720x719")
root.resizable(0,0)
root.config(bg = "orange")

#create Frame to place widgets on
app = Frame(root)
app.grid()

#create labels
lbl = Label(app, text = "This is my Label", bg = "purple", fg = "white", font=("Comic Sans MS",  32))
lbl.grid()

#create some buttons
bttn1 = Button(app, text = "Do not Click Me", bg = "red")
bttn1.grid()
bttn2 = Button()
bttn2.grid()

for i in range(5):
    x = Button()
    x["text"] = "button " + str(i+1)
    x.grid()
bttn2.config(text= "this is another button")



#kick offf the window's event loop
root.mainloop()