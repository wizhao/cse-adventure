from Tkinter import *
import os
from PIL import Image, ImageTk

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"
        
    def update_canvas(self,picname):
        picname = os.getcwd() + "\\assets\\" + picname
        self.pic_disp.create_image((0,0),image=ImageTk.PhotoImage(Image.open(picname)))
        
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.grid(row=0)

        self.pic_disp = Canvas(self, width=380, height=280)
        self.pic_disp.create_line(0, 0, 380, 280)
        self.pic_disp.create_line(0, 280, 380, 0, fill="red", dash=(4, 4))
        self.pic_disp.create_rectangle(50, 25, 150, 75, fill="blue")
        self.update_canvas("title.png")
        self.pic_disp.grid(row=1,column=1)
        
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello"
        self.hi_there["command"] = self.say_hi

        self.hi_there.grid(row=0, column=2)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
root = Tk()
root.resizable(width=False, height=False)
app = Application(master=root)

app.master.title("My Do-Nothing Application")
app.master.minsize(800, 600)


app.mainloop()
root.destroy()