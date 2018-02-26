# methods handling operations in Ice World
from Tkinter import *
import random
import hub

app = None
traded = False
rescued = False
climbed = False
located = False
mined = False
opened = False

def run(a):
    # called by main
    global app
    app = a
    if (app.has_item('Parka')):
        app.update_console('You step into the howling winds of the Ice World, your feet sinking into the snow. Your parka protects you from the cold.\n')
        start()
    else:
        app.update_console('The fierce winds ruthlessly force you immediately back to the hub, threatening hypothermia.\n', tag='r')
        hub.run(app)

def checkParka():
    # checks if parka is in backpack
    if app.has_item("Parka"):
        pass
    else:
        app.update_console("Without your parka, you scramble to get away from the cold.\n(-2 life)")
        app.add_life(-2)
        hub.run(app)

def start():
    # starting point
    checkParka()
    app.change_location(("iceWorld.png","A frozen wasteland."))
    app.update_console("You see the glow of an Inuit Village, the towering outline of a mountain, and a pack of sabertooth tigers. What do you do?\n")
    app.update_buttons([ ("Village",op1) , ("Mountain",op2) , ("Sabertooth Tigers",op3) , ("Return to Hub", lambda: hub.run(app)) ])

def op1(msg="You approach a small Inuit Village. You pick up power crystal readings somewhere by the village, but you don't know where.\n"):
    # option 1
    checkParka()
    app.change_location(("iceWorld1.png","It's a small iglooville."))
    app.update_console(msg)
    app.update_buttons([ ("Visit Medicine Man",op1_1) , ("Visit Chief",op1_2) , ("Ice Cave",op1_3) , ("Back",start) ])

def op1_1(msg="The medicine man greets you, and asks a favor: he needs some mystic water, but the only source is at the top of the mountain, and he's too frail."):
    # option 1: suboption 1
    checkParka()
    app.change_location(("iceWorld1_1.png","There's lots of exotic medicines. How'd he get them?"))
    def make_trade():
        global traded
        if app.has_item("Ice Cube") and not traded:
            app.update_console("You hand him the ice cube, and he gives you a selection of his finest herbal medicines as a reward.\n",tag="g")
            app.remove_item("Ice Cube")
            app.add_item("Herbal Medicine")
            traded = True
        elif traded:
            app.update_console("The Medicine Man doesn't need any more Mystic Water, at least for now.\n")
        else:
            app.update_console("You don't have any Mystic Water on you!\n",tag="r")
        app.update_buttons([ ("Back",lambda: op1_1(msg="")) ])
    if not traded:
        app.update_console(msg)
    app.update_buttons([ ("Trade Mystic Water", make_trade) , ("Back" ,lambda: op1(msg="")) ])

def op1_2():
    # option 1: suboption 2
    checkParka()
    global rescued
    global climbed
    global located
    global opened
    app.change_location(("iceWorld1_2.png","The leader's home."))
    app.update_console("You step into the chief's igloo.")
    if opened:
        app.update_console("The Chief greets you with respect.")
    elif rescued and climbed:
        app.update_console("You have earned the Chief's trust and proved your might.\n")
        app.update_console("He tells you of the location of the sacred cave, and bestows upon you a ceremonial spear. To kill The Lurker.\n",tag="g")
        app.add_item("Ceremonial Spear")
        located = True
    elif rescued:
        app.update_console("The Chief heard from the hunters about your heroic feat and have earned his trust, but when you ask for the location of the cave he says that you have to show that you are worthy by climbing the mountain.\n")
    elif climbed:
        app.update_console("You tell the Chief that you climbed the mountain, but the Chief still does not trust you.\n")
    else:
        app.update_console("You ask the Chief about the ice cave, but he does not tell you. He doesn't trust you.\n")
    app.update_buttons([ ("Back",lambda: op1(msg="")) ])


def op1_3():
    # option 1: suboption 3
    checkParka()
    global located
    global opened
    if not located:
        app.update_console("You can't visit the cave because you don't know where it is.\n",tag="r")
    elif located and not app.has_item("Grenades"):
        app.change_location(("iceWorld1_3.png","The mysterious cave. There is something glowing."))
        app.update_console("You find the cave, but it is sealed shut. Is there a way to break it open?\n")
    elif not opened:
        app.change_location(("iceWorld1_3_1.png","Those nades sure did the trick!"))
        app.update_console("You find the cave, and throw some grenades at the entrance. It shatters the thick ice, revealing a purple power crystal.\n",tag="g")
        app.add_item("Purple Crystal")
        opened = True
    else:
        app.change_location(("iceWorld1_3_2.png","An empty cave."))
        app.update_console("There is nothing but an empty cave here.\n")
    app.update_buttons([ ("Back",lambda: op1(msg="")) ])

def op2():
    # option 2
    checkParka()
    app.update_console("You stand at the foot of a towering mountain. You realize that you will need a lot of food to get to the top.\n")
    app.update_buttons([ ("Climb",op2_1) , ("Back", start) ])

def op2_1():
    # option 2 section 1
    checkParka()
    global climbed
    def mine():
        global mined
        checkParka()
        if app.has_item("Bone Pick") and not mined:
            app.change_location(("iceWorld2_1_2.png","Looks like Minecraft."))
            app.update_console("You use your bone pick to mine out a block of the Mystic Water.\n",tag="g")
            app.add_item("Ice Cube")
            mined=True
        elif not app.has_item("Bone Pick"):
            app.change_location(("iceWorld2_1_3.png","Ice sure is hard to break."))
            app.update_console("You can't seem to tap into the frozen lake. You need a tool to help you out.\n",tag="r")
        elif mined:
            app.change_location(("iceWorld2_1_2.png","There's no more."))
            app.update_console("There's not enough of the lake left to mine.\n")
        app.update_buttons([ ("Come Down", leave) ])

    def leave():
        # leaves world
        eated = random.choice(app.get_items("food"))
        app.update_console("You've made it to the bottom. On your journey you ate your " + eated + ".")
        app.remove_item(eated)
        checkParka()
        app.update_buttons([('Back', op1)])

    if len(app.get_items("food")) > 0:
        app.update_console("After a long, arduous hike, you finally make it to the top of the mountain. There is a single tree and a frozen lake.")
        if not climbed:
            app.change_location(("iceWorld2_1.png","You did it!"))
            app.update_console("You pick the single fruit from the tree, and stash it.",tag="g")
            app.add_item("Fruit")
            climbed = True
        else:
            app.change_location("iceWorld2_1_1.png","You did it!")
        app.update_buttons([ ("Harvest Mystic Water",mine) , ("Come Down",leave) ])
    else:
        app.update_console("You don't have enough food for the journey.")
        app.update_buttons([ ("Back",op2) ])

def op3():
    # option 3
    checkParka()
    if not rescued:
        app.change_location(("iceWorld3.png","Wow, they're getting merk'd!"))
        app.update_console("You see a group of hunters fighting a pack of sabertooth tigers! You should go and help them if you have a weapon!\n")
        app.update_buttons([ ("Help",op3_1) , ("Back",start) ])
    else:
        app.change_location(("iceWorld3_2.png","The hunters greet you."))
        app.update_console("The notice you, but they're too preoccupied with hunting.\n")
        app.update_buttons([ ("Back", start) ])

def op3_1():
    # option 3 suboption 1
    checkParka()
    global rescued
    if len(app.get_items("weapon")) > 0:
        app.update_console("You run in and fight off the tigers with your " + random.choice(app.get_items("weapon")) + ".")
        if random.randint(1,3) == 1:
            app.update_console("One of the sabertooths got a good swipe on you (-1 life).\n",tag="r")
            app.add_life(-1)
        rescued = True
        app.update_buttons([ ("Continue",lambda: op1(msg="You help the hunters to the nearby village, where they are tended to.")) ])
    else:
        app.update_console("It'll be suicide going in without a weapon!\n")
        app.update_buttons([ ("Run",start) ])
