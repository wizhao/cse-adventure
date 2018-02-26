# methods handling operations in War World

from Tkinter import *
import random
import hub

mainpic = "warWorld.png"
app = None
entered = False
digged = False
grenades = False
meal = False
saved = False
givenID = False
quested = False
rock = False
thug = False
traded = False

def run(a):
    # called by main
    global app
    app = a
    app.update_console('You step out of your portal into what appears to be a trench in a warzone. You hear the distinct sounds of gunfire nearby, and the occasional explosions of artillery shells.\n')
    start()

def start():
    # starting point
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
        app.update_console("You see the front lines ahead of you, the dugout behind you, and a faint outline of a city far back. Where do you go?\n")
        app.update_buttons( [ ("Front Lines",op1) , ("Military Dugout",op2) , ("City",op3) , ("Return to Hub",lambda: hub.run(app)) ])

def op1(msg="You move up to the gruesome front lines. Your shoes are soaked, the gunshots are deafening, and it smells horrible. Between the soldiers resting and firing, there is no joy to be seen anywhere. What do you do?\n"):
    # option 1
    app.change_location(("warWorld1.png","The gruesome front lines."),default=mainpic)
    if msg != "":
        app.update_console(msg)
    app.update_buttons([ ("Go Over the Top" , op1_1) , ("Talk to Soldier" , op1_2) , ("Dig Out Trenches" , op1_3) , ("Back",start) ])

def op1_1():
    # option 1: suboption 1
    if app.has_item("Rifle"):
        app.update_console("You try to join the war effort, climbing up and over the walls of the trench and brandishing your rifle.")
        app.update_console("Shortly after climbing, a shot from the other side hits you in the torso (-1 life). What were you thinking?\n",tag="r")
        app.add_life(-1)
        app.update_buttons([ ("Back", lambda: op1("You are now behind cover on the front lines. What do you do?")) ])
    else:
        app.update_console("You can't fight without your rifle!")
        op1()

def op1_2():
    # option 1: suboption 2
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
        app.update_console("The soldier sits idly, occasionally taking shifts on the front line with his comrades.\n")
    app.update_buttons([ ("Back",lambda: op1(msg="")) ])

def op1_3():
    # option 1: suboption 3
    global digged
    if not digged:
        if app.has_item("Shovel"):
            app.change_location(("warWorld1_3.png","The trenches are less agonizing to walk around now!"),default=mainpic)
            app.update_console("After some hard work, you manage to dig out most of the mud and slush in the trenches, exposing the more solid dirt underneath.\n",tag="g")
            digged = True
        else:
            app.update_console("You notice the thick mud in the trenches that soaks your feet. If only you had a shovel to clear it.\n")
    else:
        app.update_console("The trenches feel slightly more comfortable after your work.\n")
    app.update_buttons([ ("Back",lambda: op1(msg="")) ])

def op2(msg="You enter the military dugout. Military commanders crowd around a table, discussing tactics. What do you do?\n"):
    # option 2
    app.change_location(("warWorld2.png","Military commanders are discussing tactics."),default=mainpic)
    app.update_console(msg)
    app.update_buttons([ ("Look at Weapon Rack" , op2_1) , ("Talk to Official", op2_2) , ("Look at Map", op2_3) , ("Back" , start) ])

def op2_1():
    # option 2 suboption 1
    global grenades
    if not grenades:
        app.change_location(("warWorld2_1.png","Free grenades. What a steal!"),default=mainpic)
        app.update_console("You find a few grenades lying around near the bottom.")
        app.update_console("You carefully stash them, hoping the officers didn't notice.\n",tag="g")
        app.add_item("Grenades")
        grenades = True
    else:
        app.change_location(("warWorld2_1_1.png","There\'s nothing to take."),default=mainpic)
        app.update_console("There doesn't seem to be anything else insignificant enough to steal.\n")
    app.update_buttons([ ("Back", lambda: op2(msg="")) ])

def op2_2():
    # option 2 suboption 2
    global saved
    global givenID
    if not saved:
        app.update_console("The officer yells at you for disobeying orders, and commands you to leave the dugout.\n")
    elif saved and not givenID:
        app.update_console("You ask for a SuperLieutenant Chalmers in the crowd. The same officer who yelled at you before looks at you, infuriated.\n")
        app.update_console("\"If you\'re back here again one more--\"")
        app.update_console("The lost girl you saved runs out from behind you and embraces her father, finally reunited. Superlieutenant Chalmers is speechless.\n")
        app.update_console("\"But how did you-- That city--\"")
        app.update_console("After he calms down, you tell him all about your portal gun, your quest, and why you're here.")
        app.update_console("SuperLieutenant Chalmers tells you about a secret meeting room in the city, where top secret government research is being done.")
        app.update_console("He gives you an ID card that allows entrance as well as the location of the room.\n",tag="g")
        app.add_item("ID Card")
        givenID = True
    else:
        app.update_console("SuperLieutenant Chalmers warmly greets you, and wishes you good luck on your journey.\n")
    app.update_buttons([ ("Back",lambda: op2(msg="")) ])

def op2_3():
    # option 2 suboption 3
    def journey():
        def trek(has_weapon):
            global saved
            if not has_weapon:
                if random.randint(1,10) > 9:
                    app.update_console("Luckily, you find the lost girl on the first day!\n",tag="g")
                    saved = True
                else:
                    app.update_console("After several days of sneaking very carefully to avoid being seen, you couldn\'t find the lost girl.\n")
            else:
                app.update_console("You search the occupied city very quickly, and in one day you find the lost girl.",tag="g")
                saved = True
            removedFood = app.get_items("food")[random.randint(0,len(app.get_items("food"))-1 ) ]
            app.update_console("You ate your " + removedFood + " on the journey.")
            app.remove_item(removedFood)
            if random.randint(1,10) > 5:
                app.update_console("On your way back, a soldier spots you and fires at you just as you're about to escape. Luckily, he missed, and you jump through the portal unscathed.")
            else:
                if has_weapon:
                    fight = "In a heated battle, you finally disable the soldier with your " + app.b.get_items("weapon")[random.randint(0,len(app.b.get_items("weapon"))-1)] + " and get away."
                else:
                    fight = "In a heated fistfight, you finally disable the soldier and get away."
                app.update_console("On your way back, a soldier spots you and lunges at you. " + fight,tag="r")
                app.add_life( -1 if has_weapon else -2)
                app.update_console("(" + ("-1" if has_weapon else "-2") + " life)",tag="r")
            if saved:
                app.update_buttons([ ("Talk to Official" , op2_2) ])
            else:
                app.update_buttons([ ("Back" , lambda: op2(msg="")) ])
        if len(app.get_items("food")) > 0:
            if len(app.get_items("weapon")) <= 0:
                app.update_console("You have no weapon. Are you still sure you want to go?")
                app.update_buttons([ ("YOLO", lambda: trek(False)) , ("Nah", lambda:op2(msg="")) ])
            else:
                trek(True)
        else:
            app.update_console("You have no food. You won't be able to last long enough behind enemy lines.")
            app.update_buttons([ ("Back" , lambda: op2(msg="")) ])

    global saved
    global quested
    app.change_location(("warWorld2_3.png","A map of the current encampment."),default=mainpic)
    choices = []
    app.update_console("You see a map showing the surroundings. There's a city that looks like it was recently captured by the enemy.")
    if quested and not saved:
        app.update_console("That's the city that SuperLieutenant Chalmers lost his daughter in!")
        app.update_console("Your portal gun can bypass enemy lines, but it will still be a long and dangerous trek. You should bring some food with you and some form of weapon.\n")
        choices.append( ("Go!",journey) )
    choices.append( ("Back", lambda: op2(msg="")) )
    app.update_buttons(choices)

def op3(msg="You arrive at the city. The people seem to be tense from the war going on.\n"):
    # option 3
    app.change_location(("warworld3.png","The city."))
    app.update_console(msg)
    choices = [ ("Dark Alleys" , op3_1) , ("Hospital" , op3_2) ]
    if givenID:
        choices.append (("Secret Meeting Room" , op3_3))
    choices.append (("Leave" , start))
    app.update_buttons(choices)

def op3_1(msg="There is a dark alley, with some trash bags near you. What do you do?"):
    # option 3 suboption 1
    def find_rock():
        global rock
        if not rock:
            app.change_location(("warworld3_1_1.png","You found a special rock."))
            app.update_console("You find a strange rock in the trash!\n",tag="g")
            app.add_item("Rock")
            rock = True
        else:
            app.change_location(("warworld3_1_2.png","Just trash."))
            app.update_console("There's nothing useful in the trash\n.")
        app.update_buttons([ ("Back", lambda: op3(msg="")) ])
    def explore():
        global thug
        if not thug:
            if len(app.get_items("weapon")) > 0:
                chance = 5
                message = "A thug ambushes you, but you fight back with your weapon."
            else:
                chance = 2
                message = "A thug ambushes you, but you fight back."
            app.update_console(message,tag="r")
            if random.randint(1,10) >= chance:
                app.update_console("You lost 1 life from the fight.",tag="r")
                app.add_life(-1)
            app.update_console("However, you find an oxygen tank and a shovel in the darkness.\n",tag="g")
            app.add_item("Oxygen Tank")
            app.add_item("Shovel")
            thug = True
        else:
            app.update_console("There's nothing in this alley.\n")
        app.update_buttons([ ("Back", lambda: op3_1(msg="")) ])
    app.change_location(("warworld3_1.png","A dark alley."))
    app.update_console(msg)
    app.update_buttons([ ("Search Trash",find_rock) , ("Explore the Alley",explore) , ("Back",lambda: op3(msg="")) ])

def op3_2():
    # option 3 suboption 2
    global quested
    global saved
    app.change_location(("warworld3_2.png","A busy hospital."))
    if not saved:
        app.update_console("When you enter the hospital, you hear a hysterical patient being calmed down by a nurse. You overhear that this is the wife of SuperLieutenant Chalmers, and that she was separated from her daughter in the city that was captured recently.\n")
        quested = True
    else:
        app.update_console("It's a busy hospital with a lot of commotion. Better not bother them.\n")
    app.update_buttons([ ("Leave" , lambda: op3(msg="")) ])

def op3_3():
    # option 3 suboption 3
    global traded
    def make_trade():
        global traded
        if app.has_item("Uranium"):
            app.update_console("You give the scientists the uranium, and in exchange, they give you the power crystal they had.\n",tag="g")
            app.remove_item("Uranium")
            app.add_item("Red Crystal")
            traded = True
        else:
            app.update_console("You don't have any uranium to give!\n")
        app.update_buttons([ ("Back", op3_3) ])
    app.change_location(("warworld3_3.png","A top-secret meeting room."))
    if app.has_item("ID Card") and not traded:
        app.update_console("You find the secret room, and use the ID Card to enter. Inside, the scientists were expecting you. They say that they need a sample of Uranium for their research.\n")
        app.update_buttons([ ("Trade Uranium",make_trade) , ("Leave", lambda: op3(msg="")) ])
    elif traded:
        app.update_console("The scientists are hard at work, conducting research with the uranium you gave.\n")
        app.update_buttons([ ("Leave", lambda: op3(msg="")) ])
    else:
        app.change_location(("warworld3_3_1.png","You forgot the key!"))
        app.update_console("You find the secret room, but you realize you don't have the ID Card on you.\n")
        app.update_buttons([ ("Leave", lambda: op3(msg="")) ])
