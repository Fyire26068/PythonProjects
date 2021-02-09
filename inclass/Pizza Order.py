from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.nameLbl = Label(self, text="Name: ",height=1).grid(row=0, column=0)
        self.nameTxt = Text(self,height=1).grid(row=0,column=1,columnspan=1, sticky=W)

        self.phoneLbl = Label(self, text="Phone Number: ", height=1).grid(row=0, column=3)
        self.phoneTxt = Text(self,height=1).grid(row=0,column=4,sticky=W)

        self.addressLbl = Label(self, text="Address: ", height=1).grid(row=1,column=0)
        self.addressText = Text(self,height=1).grid(row=1,column=1,columnspan=3,sticky=W)

        self.typeOrder = StringVar()
        self.typeOrder.set(None)

        self.delRad = Radiobutton(self, text="Delivery ", value="Delivery", variable=self.typeOrder,
                                  command=self.update).grid(row=2, column=0,columnspan=1,sticky=W)
        self.carRad = Radiobutton(self,text="Carry-Out ", value="Carry-Out", variable=self.typeOrder,
                                  command=self.update).grid(row=2, column=2,columnspan=1,sticky=W)

        self.orderTitle = Label(self, text="Order", height=1).grid(row=3,column=0, columnspan=5)

        self.crustTitle = Label(self, text="Crust",height=1).grid(row=4,column=0,sticky=W)
        self.crustType = StringVar()
        self.crustType.set(None)
        self.handtossedRad = Radiobutton(self, text="Hand-Tossed", value="Hand-Tossed", variable=self.crustType,
                                         command=self.update).grid(row=5,column=0, sticky=W)
        self.thincrustRad = Radiobutton(self, text="Thin Crust", value="Thin Crust", variable=self.crustType,
                                        command=self.update).grid(row=5,column=1, sticky=W)
        self.pancrustRad = Radiobutton(self, text="Pan", value="Pan", variable=self.crustType,
                                       command=self.update,width=2).grid(row=5,column=2, sticky=W)
        self.brookcrustRad = Radiobutton(self, text="Brooklyn-Style", value="Brookyln-Style", variable=self.crustType,
                                         command=self.update).grid(row=5,column=3, sticky=W)
        self.glutencrustRad = Radiobutton(self, text="Gluten-Free", value="Gluten-Free", variable=self.crustType,
                                          command=self.update).grid(row=5,column=4, sticky=W)

        self.sizeTitle = Label(self, text="Size",height=1).grid(row=6,column=0,sticky=W)
        self.sizeVar = StringVar()
        self.sizeVar.set(None)
        self.xlargeRad = Radiobutton(self, text="Extra-Large", value="XL", variable=self.sizeVar,
                                     command=self.update).grid(row=7,column=0, sticky=W)
        self.largeRad = Radiobutton(self, text="Large", value="L", variable=self.sizeVar,
                                     command=self.update).grid(row=7, column=1, sticky=W)
        self.medRad = Radiobutton(self, text="Medium", value="M", variable=self.sizeVar,
                                     command=self.update).grid(row=7, column=2, sticky=W)
        self.smallRad = Radiobutton(self, text="Small", value="S", variable=self.sizeVar,
                                     command=self.update).grid(row=7, column=3, sticky=W)

        self.sauceTitle = Label(self, text="Sauce", height=1).grid(row=8,column=0,sticky=W)
        self.sauceVar = StringVar()
        self.sauceVar.set(None)
        self.marinaraRad = Radiobutton(self, text="Marinara Sauce", value="Marinara Sauce", variable=self.sauceVar,
                                       command=self.update).grid(row=9,column=0,sticky=W)
        self.alfredoRad = Radiobutton(self, text="Alfredo Sauce", value="Alfredo Sauce", variable=self.sauceVar,
                                       command=self.update).grid(row=9, column=1, sticky=W)
        self.bbqRad = Radiobutton(self, text="BBQ Sauce", value="BBQ Sauce", variable=self.sauceVar,
                                       command=self.update).grid(row=9, column=2, sticky=W)
        self.garlicRad = Radiobutton(self, text="Garlic Parmesan", value="Garlic Parmesan", variable=self.sauceVar,
                                       command=self.update).grid(row=9, column=3, sticky=W)
        self.ranchRad = Radiobutton(self, text="Ranch", value="Ranch", variable=self.sauceVar,
                                       command=self.update).grid(row=9, column=4, sticky=W)

        self.toppingTitle = Label(self, text="Toppings", height=1).grid(row=10, column=0, sticky=W)
        self.pep = BooleanVar()
        self.greenpep = BooleanVar()
        self.parasi = BooleanVar()
        self.ham = BooleanVar()
        self.onion = BooleanVar()
        self.redpep = BooleanVar()
        self.prov = BooleanVar()
        self.bolive = BooleanVar()
        self.bpep = BooleanVar()
        self.spinach = BooleanVar()
        self.mush = BooleanVar()
        self.jpep = BooleanVar()
        self.phil = BooleanVar()
        self.sau = BooleanVar()
        self.ched = BooleanVar()
        self.pine = BooleanVar()
        self.beef = BooleanVar()
        self.tom = BooleanVar()

        self.boolsvars = [self.pep,self.greenpep,self.parasi,self.ham,self.onion,self.redpep,self.prov,self.bolive,
                          self.bpep,self.spinach,self.mush,self.jpep,self.phil,self.sau,self.ched,self.pine,self.beef,self.tom]

        self.toppings = ["Pepporoni","Green Pepper","Parmasean Asiago","Ham","Onion","Red Peppers","Provolone","Black Olives",
                        "Banana Peppers", "Spinach","Mushrooms","Jalapenos","Philly Steak","Sausage","Chedder","Pineapple","Beef","Diced Tomatoes"]
        for i in range(17):
            for c in range(2):
                self.createCB(self.toppings[i], self.boolsvars[i],int((i/3)+11), c)


    def update(self):
        self.name = StringVar()
        self.name = self.nameTxt.get()
        self.phone = StringVar()
        self.phone = self.phoneTxt.get()
        self.address = StringVar()
        self.address = self.addressText.get()

        self.resultstxt.delete(0.0,END)
        self.resultstxt.insert(0.0,self.name, self.phone, self.address)

    def createCB(self, words, ischecked,r,c):
        Checkbutton(self, text=words, variable=ischecked).grid(row=r+11,column=c,sticky=W)



def main():

    root = Tk()
    root.title("checkbox tester")
    root.geometry("1200x1200")
    root.attributes("-fullscreen", False)
    app = App(root)
    root.mainloop()


main()