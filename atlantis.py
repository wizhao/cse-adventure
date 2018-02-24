#Atlantis
import hub

b = None #stores backpack
lives = None #stores num of lives
app = None

#called by main
def run(a):
    global app
    global b
    app = a
    b = app.get_b()
    app.update_console('description')
    start()
    app.set_b(b)

#starting point
def start():
    pass

#option 1
def op1():
    pass

#option 1: suboption 1
def op1_1():
    pass
    
#option 1: suboption 2
def op1_2():
    pass
    
#option 2
def op2():
    pass