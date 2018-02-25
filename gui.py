from Tkinter import *
import os
from PIL import Image, ImageTk
from backpack import Backpack


class Application(Frame):
    def createWidgets(self):
        title = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\assets\\misc\\titleBanner3.png").convert("RGBA").resize((800,100)))
        titleBanner = Label(width=800,height=100,image=title)
        titleBanner.asset = title
        titleBanner.grid(row=0,column=0,columnspan=2)

        '''Items Section'''
        self.itemFrame = Frame(height=250,width=400,padx=5,pady=5)
        self.itemContainer = Frame(self.itemFrame,bd=2,relief=SUNKEN)
        self.itemContainer.pack(fill=BOTH,expand=1)
        Label(self.itemContainer,textvariable=self.itemCount,font=("Arial",14)).pack(fill=X)


        self.itemScrollbar = Scrollbar(self.itemContainer)

        self.itemList = Listbox(self.itemContainer,yscrollcommand=self.itemScrollbar.set,activestyle="none")

        '''#test values
        for i in range(4):
            for x in ["A","DI","TH","YA",""]:
                self.itemList.insert(END,x)
        '''

        self.itemScrollbar.config(command=self.itemList.yview)
        self.itemScrollbar.pack(side=RIGHT,fill=Y)
        self.itemList.pack(side=LEFT,fill=BOTH,expand=1)
        self.itemList.bind('<<ListboxSelect>>', self.onselect)
        self.itemList.bind('<FocusOut>',self.deselect_item)

        self.itemFrame.grid(row=2,column=1,sticky=N+S+E+W)

        '''Console Section'''
        self.outputFrame = Frame(height=300,width=400,padx=5,pady=5)
        self.outputContainer = Frame(self.outputFrame,bd=2,relief=SUNKEN)
        self.outputContainer.pack(fill=BOTH,expand=1)

        self.consoleScrollbar = Scrollbar(self.outputContainer)
        self.consoleScrollbar.pack(side=RIGHT, fill=Y)

        self.output = Text(self.outputContainer,bd=0,width=50,height=19,yscrollcommand=self.consoleScrollbar.set,state="disabled")
        self.consoleScrollbar.config(command=self.output.yview)
        self.output.tag_config("g",foreground="darkgreen")
        self.output.tag_config("r",foreground="red")
        self.output.tag_config("wrap",wrap=WORD)
        self.output.pack()
        self.output.bind('<<Modified>>', self.callback)

        '''#test inputs
        self.update_console("Welcome to Osu")
        self.update_console("Welcome to Osu x2")
        self.update_console("Welcome to Osu x3 ")
        self.update_console("KILLING SPREE",nl=False,tag="g")
        self.update_console("You died",tag="r")
        for i in range(20):
            if i%2 == 0:
                self.update_console("Merry",tag="g")
            else:
                self.update_console("Crissmass",tag="r")
        self.update_console("What the frick did you just flipping say abotu me, you little witch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Qauaeda, and I have over 300 confirmed kills. I am trianed in orilla woarfare and I'm the to pscniper in the entire US frarmed forces. Ypu are nothing to me but jsut anot er target. I will wipe you the frick out with prescision the lies of which ash never been see nbefore on thies Earth, mark my frickning words.")
        self.update_console("anogiabgabrgergh928293r9238749y9rhgdlgdqwertyuiopasdfghjklzxcvbnm",tag="g")
        #end test inputs'''

        self.outputFrame.grid(row=1,column=0,sticky=N+S+E+W)

        '''Picture Section'''
        self.pic_container = Frame(height=300,width=400,padx=5,pady=5)
        self.pic_disp = Label(self.pic_container,bd=2,relief=SUNKEN,compound=TOP,wraplength=390,textvariable=self.caption,image=ImageTk.PhotoImage(Image.open(os.getcwd() + "\\assets\\misc\\title.png")))
        self.update_canvas(self.currentLocation)
        self.pic_disp.pack(fill=BOTH)
        self.pic_container.grid(row=1,column=1,sticky=N+S+E+W)

        '''Buttons Section'''
        self.buttonFrame = Frame(height=250,width=400,bd=2,padx=5,pady=5)
        self.dropgun = Button(self.buttonFrame,text="Drop Selected Item",command=self.drop_item)


        self.option0 = Button(self.buttonFrame,text="")
        self.option1 = Button(self.buttonFrame,text="")
        self.option2 = Button(self.buttonFrame,text="")
        self.option3 = Button(self.buttonFrame,text="")
        self.option4 = Button(self.buttonFrame,text="")
        self.option5 = Button(self.buttonFrame,text="")
        self.option6 = Button(self.buttonFrame,text="")
        self.option7 = Button(self.buttonFrame,text="")
        self.option8 = Button(self.buttonFrame,text="")
        self.option9 = Button(self.buttonFrame,text="")
        self.buttonList = [self.option0,self.option1,self.option2,self.option3,self.option4,self.option5,self.option6,self.option7,self.option8,self.option9]
        for buton in self.buttonList:
            buton.grid_forget()

        self.buttonFrame.columnconfigure(0,minsize=195,weight=1)
        self.buttonFrame.columnconfigure(1,minsize=195,weight=1)

        self.buttonFrame.grid(row=2,sticky=N+S+E+W)

        '''Toolbar Section'''
        self.toolbar = Frame(width=800,height=50,bd=2,bg="lightgray")
        self.toolbar.grid(row=3,columnspan=2,sticky=N+S+E+W)

        self.QUIT = Button(self.toolbar)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.confirm_quit

        self.QUIT.pack(side=LEFT)

        Label(self.toolbar,text="Lives: ",bg="lightgray").pack(side=LEFT)
        self.lifecount = Label(self.toolbar,textvariable=self.lives,bg="lightgray")
        self.lifecount.pack(side=LEFT)

        self.hi_there = Button(self.toolbar)
        self.hi_there["text"] = "Hello"
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack(side=RIGHT)



    def say_hi(self):
        print "hi there, everyone!"

    def confirm_quit(self):
        if self.lost:
            self.quit()
        else:
            cquit = Toplevel(width=400,height=100)
            cquit.title("Confirm Quit")
            mes = Message(cquit, width=400,text="Are you sure you want to quit? We LITERALLY don't have a save feature.")
            mes.pack()

            button_container = Frame(cquit,pady=5)
            button_container.pack(side=BOTTOM)
            confirm = Button(button_container,text="Yea, your game sucks",fg="white",bg="red",command=self.quit)
            cancel = Button(button_container,text="Nah im good",command=cquit.destroy)
            confirm.pack(side=LEFT,padx=5)
            cancel.pack(side=LEFT,padx=5)
            cquit.grab_set()

    def update_items(self):
        self.itemList.delete(0, END)
        for item in self.b.contents:
            self.itemList.insert(END, self.b.contents[item].name + " (" + self.b.contents[item].ilk + ")")
        self.update_itemCount()

    def onselect(self,evt):
        if not self.lost:
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            self.update_console('You selected the %s' % (value))
            self.show_item(self.b.get_item(" ".join(value.split(" ")[:-1])))
            self.dropgun.grid_forget()
            self.dropgun.grid(row=5,column=0,sticky=E,padx=5,pady=5)

    def deselect_item(self,evt):
        self.update_canvas(self.currentLocation)
        self.dropgun.grid_forget()

    def drop_item(self):
        self.update_console("You dropped the %s and sent it to the hub." % (" ".join(self.itemList.get(ACTIVE).split(" ")[:-1])))
        self.b.put_in_storage(" ".join(self.itemList.get(ACTIVE).split(" ")[:-1]))
        self.itemList.delete(ACTIVE)
        self.dropgun.grid_forget()
        self.update_canvas(self.currentLocation)
        self.update_itemCount()

    def pull_out(self):
        pullout = Toplevel(width=400,height=300,padx=10,pady=10)
        pullout.title("Withdraw Items")
        Label(pullout,text="Select the items you wish to bring to your backpack:").pack(fill=X,expand=1)
        list_container = Frame(pullout)
        list_container.pack(fill=X,expand=1)
        scrollbar = Scrollbar(list_container)
        scrollbar.pack(side=RIGHT,fill=Y)
        stored = Listbox(list_container,selectmode=EXTENDED,yscrollcommand=scrollbar.set)

        for i in self.b.storage:
            stored.insert(END,str(self.b.storage[i].name + " (" + self.b.storage[i].ilk + ")"))
        stored.pack(side=LEFT, fill=X, expand=1)
        scrollbar.config(command=stored.yview)

        def withdraw():
            amt = map(int, stored.curselection())
            if len(amt) + len(self.b.contents) <= self.b.itemLimit:
                for i in amt:
                    itemname = " ".join(stored.get(i).split(" ")[:-1])
                    self.b.get_from_storage(itemname)
                    self.update_console("Retrieved the " + itemname,tag="g")
                self.update_items()
                pullout.destroy()
            else:
                notif = Toplevel(width=400)
                notif.title("TMI")
                Message(notif,aspect=500,text="You selected too many items. They won't fit in your backpack.").pack(side=TOP,fill=X,expand=1)
                Button(notif,text="Ok",command=notif.destroy).pack(side=TOP,padx=10,pady=10)
                notif.grab_set()

        button_container = Frame(pullout,pady=5,height=50)
        button_container.pack(side=BOTTOM)
        confirm = Button(button_container,text="Confirm",command= withdraw,padx=5)
        back = Button(button_container,text="Back",command=pullout.destroy,padx=5)
        confirm.pack(side=LEFT)
        back.pack(side=LEFT)

        pullout.grab_set()



    def callback(self,evt):
        self.output.see(END)
        self.output.edit_modified(0)

    def update_console(self,message,nl=True,tag=""):
        if not self.lost and len(message) > 0:
            self.output.config(state="normal")
            prefix = ""
            if nl:
                prefix += "\n>"
            self.output.insert(END,prefix + message,(tag,"wrap"))
            self.output.config(state="disabled")

    def change_location(self, picinfo,default="misc\\landscapeGeneric.png"):
        self.currentLocation = picinfo
        self.update_canvas(picinfo,backup=default)

    def update_canvas(self, picinfo,backup=""):
        picname = os.getcwd() + "\\assets\\" + picinfo[0]
        try:
            photo = ImageTk.PhotoImage(Image.open(picname))
        except IOError:
            try:
                photo = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\assets\\" + backup))
            except IOError:
                photo = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\assets\\misc\\landscapeGeneric.png"))
        self.pic_disp.config(image=photo)
        self.pic_disp.currentImage = photo
        self.caption.set(picinfo[1])

    def show_item(self,item):
        picinfo = ("Items\\" + item.picture, item.caption)
        self.update_canvas(picinfo,backup="Items\\itemGeneric.png")

    def update_buttons(self, buttonList):
        self.wipe_buttons()
        if not self.lost:
            for i in range(len(buttonList)):
                self.buttonList[i].config(text=buttonList[i][0],command=buttonList[i][1])
                r = int(i / 2.0)
                c = 0 if i % 2 == 0 else 1
                stick = E if c == 0 else W
                self.buttonList[i].grid(row=r,column=c,padx=5,pady=5,sticky=stick)

    def wipe_buttons(self):
        for buton in self.buttonList:
            buton.grid_forget()

    def add_life(self,amt=1):
        newcount = self.lives.get() + amt
        self.lives.set(newcount)
        if self.lives.get() <= 0:
            self.game_over()
        elif self.lives.get() == 1:
            self.lifecount.config(foreground="red")
        else:
            self.lifecount.config(foreground="black")

    def game_over(self,mes=""):
        if len(mes) > 0:
            self.update_console(mes)
        self.change_location(("misc\\gameOver.png","You get nothing. You lose! Good day sir!"))
        self.itemList.config(state="disabled")
        self.wipe_buttons()
        self.update_console("You lose! Game over.",tag="r")
        self.lost = True

    '''
    def get_b(self):
        return self.b

    def set_b(self, b):
        self.b = b
        self.update_items()
    '''

    def update_itemCount(self):
        self.itemCount.set("Backpack (" + str(len(self.b.contents)) + "/" + str(self.b.itemLimit) + ")")

    def add_item(self,name):
        if len(self.b.contents) < self.b.itemLimit and name not in self.b.storage:
            self.b.add(name)
            self.update_items()
            self.update_itemCount()
        elif name in self.b.storage:
            self.update_console("You already have this item!", tag='r')
            self.update_console("You can retrieve it from the hub.")
        elif len(self.b.contents) >= self.b.itemLimit:
            self.update_console("You do not have enough space in your backpack.",tag="r")
            self.update_console("It was sent to your storage in the hub.")
            self.b.put_in_storage(name)
        else:
            self.update_console("Oops! Something unexpected happened.",tag="r")
            self.update_console("Tell the bois if you see this.")


    def remove_item(self,name):
        self.b.remove(name)
        self.update_itemCount()

    def get_items(self,category):
        return self.b.get_items(category)

    def has_item(self,name):
        return self.b.has(name)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.b = Backpack()
        self.lost = False
        self.lives = IntVar()
        self.lives.set(5)
        self.itemCount = StringVar()
        self.itemCount.set("Backpack (0/" + str(self.b.itemLimit) + ")")
        self.caption = StringVar()
        self.currentLocation = ("misc\\title.png","A strange, desolate, world.")
        self.caption.set(self.currentLocation[1])
        self.grid()
        self.pack_propagate(0)
        self.createWidgets()

    def op1(self):
        print "Option 1"
        self.add_item("Portal Gun")
        self.add_item("Purple Tactical Shotgun")
        self.add_item("Lettuce")
        self.add_item("Jisoo Photo")

        self.update_items()

    def op2(self):
        print "Option 2"
        self.update_console(str(self.b.storage))
        self.add_item("Steamed Hams and Macaroni")

    def op3(self):
        print "Option 3"
        self.pull_out()

'''
#comment out everything below when not testing
root = Tk()
root.resizable(width=False, height=False)
app = Application(master=root)

app.master.title("My Almost Do-Nothing Application")

app.after(1000,app.update_buttons([("Option 1",app.op1) , ("Option 2",app.op2) , ("Option 3",app.op3)]))
app.mainloop()
root.destroy()
'''
