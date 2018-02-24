from Tkinter import *
import os
from PIL import Image, ImageTk
from backpack import Backpack


class Application(Frame):
    def createWidgets(self):
        title = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\assets\\titleBanner.png").convert("RGBA").resize((800,100)))
        titleBanner = Label(width=800,height=100,image=title)
        titleBanner.asset = title
        titleBanner.grid(row=0,column=0,columnspan=2)

        '''Items Section'''
        self.itemFrame = Frame(height=250,width=400,padx=5,pady=5)
        self.itemContainer = Frame(self.itemFrame,bd=2,relief=SUNKEN)
        self.itemContainer.pack(fill=BOTH,expand=1)
        Label(self.itemContainer,text="Items").pack(fill=X)


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
        self.pic_disp = Label(self.pic_container,bd=2,relief=SUNKEN,compound=TOP,textvariable=self.caption,image=ImageTk.PhotoImage(Image.open(os.getcwd() + "\\assets\\title.png")))
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

    def update_items(self):
        self.itemList.delete(0, END)
        for item in self.b.contents:
            self.itemList.insert(END, self.b.contents[item].name)

    def onselect(self,evt):
        if not self.lost:
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            self.update_console('You selected the %s' % (value))
            self.show_item(self.b.get_item(value))
            self.dropgun.grid_forget()
            self.dropgun.grid(row=5,column=0,sticky=E,padx=5,pady=5)

    def deselect_item(self,evt):
        self.update_canvas(self.currentLocation)
        self.dropgun.grid_forget()

    def drop_item(self):
        self.update_console("You dropped the %s and sent it to the hub." % (self.itemList.get(ACTIVE)))
        self.b.put_in_storage(self.itemList.get(ACTIVE))
        self.itemList.delete(ACTIVE)
        self.dropgun.grid_forget()
        self.update_canvas(self.currentLocation)

    def callback(self,evt):
        self.output.see(END)
        self.output.edit_modified(0)

    def update_console(self,message,nl=True,tag=""):
        self.output.config(state="normal")
        prefix = ""
        if nl:
            prefix += "\n>"
        self.output.insert(END,prefix + message,(tag,"wrap"))
        self.output.config(state="disabled")

    def update_canvas(self, picinfo):
        picname = os.getcwd() + "\\assets\\" + picinfo[0]
        photo = ImageTk.PhotoImage(Image.open(picname))
        self.pic_disp.config(image=photo)
        self.pic_disp.currentImage = photo
        self.caption.set(picinfo[1])

    def show_item(self,item):
        picinfo = ("Items\\" + item.picture, item.caption)
        self.update_canvas(picinfo)

    def update_buttons(self, buttonList):
        self.wipe_buttons()
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
        self.update_console("You lose! Game over.",tag="r")
        self.itemList.config(state="disabled")
        self.wipe_buttons()
        self.lost = True

    def get_b(self):
        return self.b

    def set_b(self, b):
        self.b = b
        self.update_items()



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.lost = False
        self.lives = IntVar()
        self.lives.set(5)
        self.caption = StringVar()
        self.currentLocation = ("title.png","Bottom Text")
        self.caption.set(self.currentLocation[1])
        self.grid()
        self.pack_propagate(0)
        self.createWidgets()
        self.b = Backpack()
'''
    def op1(self):
        print "Option 1"
        self.b.add("Portal Gun")
        self.update_items()

    def op2(self):
        print "Option 2"
        self.update_console(str(self.b.storage))

    def op3(self):
        print "Option 3"
        self.game_over()


#comment out everything below when not testing
root = Tk()
root.resizable(width=False, height=False)
app = Application(master=root)

app.master.title("My Almost Do-Nothing Application")

app.after(1000,app.update_buttons([("Option 1",app.op1) , ("Option 2",app.op2) , ("Option 3",app.game_over)]))
app.mainloop()
root.destroy()
'''
