from Tkinter import *
import os
from PIL import Image, ImageTk

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def update_canvas(self, picname):
        picname = os.getcwd() + "\\assets\\" + picname
        photo = ImageTk.PhotoImage(Image.open(picname))
        self.pic_disp.config(image=photo)
        self.pic_disp.currentImage = photo

    def createWidgets(self):
        '''Picture Section'''
        self.pic_disp = Label(bd=3,image=ImageTk.PhotoImage(Image.open(os.getcwd() + "\\assets\\title.png"),height=300,width=400))
        self.update_canvas("title.png")
        self.pic_disp.grid(row=0,column=1,sticky=NE)

        '''Toolbar Section'''
        self.toolbar = Frame(width=800,height=50,bd=2,bg="gray")
        self.toolbar.grid(row=2,columnspan=2,sticky=N+S+E+W)

        self.QUIT = Button(self.toolbar)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack(side=LEFT)


        self.hi_there = Button(self.toolbar)
        self.hi_there["text"] = "Hello"
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack(side=RIGHT)

        '''Items Section'''
        self.itemFrame = Frame(height=250,width=400,bd=2,bg="azure2",padx=20,pady=20)
        Label(self.itemFrame,text="Items").pack(fill=X)


        self.itemScrollbar = Scrollbar(self.itemFrame)
        self.itemScrollbar.pack(side=RIGHT,fill=Y)
        self.itemList = Listbox(self.itemFrame,yscrollcommand=self.itemScrollbar.set)
        for i in range(4):
            for x in ["A","DI","TH","YA",""]:
                self.itemList.insert(END,x)
        self.itemList.pack(side=LEFT,fill=BOTH)
        self.itemScrollbar.config(command=self.itemList.yview)


        self.itemFrame.grid(row=1,column=1,sticky=N+S+E+W)

        '''Console Section'''
        #self.output =

        '''Buttons Section'''
        self.buttonContainer = Frame(height=250,width=400,bd=2,bg="aquamarine1",padx=20,pady=20)
        

        self.buttonContainer.grid(row=1,sticky=N+S+E+W)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.pack_propagate(0)
        self.createWidgets()

root = Tk()
root.resizable(width=False, height=False)
app = Application(master=root)

app.master.title("My Do-Nothing Application")
#app.master.minsize(800, 600)


app.mainloop()
root.destroy()
