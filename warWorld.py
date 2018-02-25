#War World
from Tkinter import *
import random
import hub

mainpic = "warWorld\\warWorld.png"
app = None
entered = False
digged = False
grenades = False

#called by main
def run(a):
    global app
    app = a
    app.update_console('You step out of your portal into what appears to be a trench in a warzone. You hear the distinct sounds of gunfire nearby, and the occasional explosions of artillery shells.\n')
    start()

#starting point
def start():
    global entered
    app.change_location(("warWorld.png","A grim landscape in the midst of war."))
    if not entered:
        app.update_console("Shortly after stepping foot in the trench, a military officer notices you and approaches you:\n\"What are you doing here, private? Get back to the front lines, where you're supposed to be!\"")
        app.update_console("Hastily, you follow orders, trying to avoid trouble, and make your way to the front lines.")
        app.update_console("You find a rifle along the way.",tag="g")
        app.add_item("Rifle")
        entered = True
        op1()
    else:
        app.update_console("You see the front lines ahead of you, the dugout behind you, and a faint outline of a city far back. Where do you go?")
        app.update_buttons( [ ("Front Lines",op1) , ("Military Dugout",op2) , ("City",op3) , ("Return to Hub",lambda: hub.run(app)) ])



#option 1
def op1(msg="You move up to the gruesome front lines. Your shoes are soaked, the gunshots are deafening, and it smells horrible. Between the soldiers resting and firing, there is no joy to be seen anywhere. What do you do?\n"):
    app.change_location(("warWorld1.png","The gruesome front lines."),default=mainpic)
    if msg != "":
        app.update_console(msg)
    app.update_buttons([ ("Go Over the Top" , op1_1) , ("Talk to Soldier" , op1_2) , ("Dig Out Trenches" , op1_3) , ("Back",start) ])

#option 1: suboption 1
def op1_1():
    if app.has_item("Rifle"):
        app.change_location(("warWorld1_1.png","What are you doing?"),default=mainpic)
        app.update_console("You try to join the war effort, climbing up and over the walls of the trench and brandishing your rifle.")
        app.update_console("Shortly after climbing, a shot from the other side hits you in the torso (-1 life). What were you thinking?\n",tag="r")
        app.add_life(-1)
        app.update_buttons([ ("Back", lambda: op1("You are now behind cover on the front lines. What do you do?")) ])
    else:
        app.update_console("You can't fight without your rifle!")
        op1()

#option 1: suboption 2
def op1_2():
    app.change_location(("warWorld1_2.png","A soldier suffers on the front lines."),default=mainpic)
    global digged
    global meal
    if not digged:
        app.update_console("The soldier says he can't feel his feet from the trench conditions.")
    elif not meal:
        app.update_console("The soldier thanks you for clearing out the trench. His feet feel better already!")
        app.update_console("You recieve an MRE from the soldier.",tag="g")
        app.add_item("MRE")
        meal = True
    else:
        app.update_console("The soldier sits idly, occasionally taking shifts on the front line with his comrades.")
    app.update_buttons([ ("Back",lambda: op1(msg="")) ])


#option 1: suboption 3
def op1_3():
    global digged
    if not digged:
        if app.has_item("Shovel"):
            app.change_location(("op1_3()","The trenches are less agonizing to walk around now!"),default=mainpic)
            app.update_console("After some hard work, you manage to dig out most of the mud and slush in the trenches, exposing the more solid dirt underneath.\n",tag="g")
            digged = True
        else:
            app.update_console("You notice the thick mud in the trenches that soaks your feet. If only you had a shovel to clear it.\n")
    else:
        app.update_console("The trenches feel slightly more comfortable after your work.\n")
    app.update_buttons([ ("Back",lambda: op1(msg="")) ])

#option 2
def op2(msg="You enter the military dugout. Military commanders crowd around a table, discussing tactics. What do you do?\n"):
    app.change_location(("warWorld2.png","Military commanders are discussing tactics."),default=mainpic)
    app.update_console(msg)
    app.update_buttons([ ("Look at Weapon Rack" , op2_1) , ("Talk to Official", op2_2) , ("Look at Map", op2_3) , ("Back" , start) ])

def op2_1():
    global grenades
    if not grenades:
        app.update_console("You find a few grenades lying around near the bottom.")
        app.update_console("You carefully stash them, hoping the officers didn't notice.\n",tag="g")
        app.add_item('Grenades')
    else:
        app.update_console("There doesn't seem to be anything insignificant enough to steal.\n")
    app.update_buttons([ ("Back", op2)])

def op2_2():
    pass

def op2_3():
    pass

#option 3
def op3():
    pass
