#Dino World
from Tkinter import *
import random
import hub

lives = None
app = None

switches = False
chest = False
darkRoom = False
tRex = False
raptor = False
campfire = False
necklace = False

def run(a):
    global app
    global b
    app = a
    app.update_console('You enter the Dino World and are transported into a thick jungle filled with beautiful flora and fauna.')
    start()

def start():
    app.update_console('To your left you see a towering stone temple, in the distance, you see a sleeping T-Rex, and to your right, you see an abandoned campsite. Which way do you turn?\n')
    app.update_buttons([('Jungle Temple', op1), ('Sleeping T-Rex', op2), ('Abandoned Campsite', op3), ('Return to Hub', lambda: hub.run(app))])

def op1():
    app.update_console('You walk into the Jungle Temple and see eight switches on the wall in front of you. To the right of that wall is a staircase, and on the left side of the room is a dilapidated chest. Where do you choose to go?\n')
    app.update_buttons([ ('Switches', op1_1) , ('Chest', op1_2), ('Staircase', op1_3), ('Back', start)])

def op1_1():
    global switches
    def minigame ():
        def exit_puzzle():
            global switches
            code_in = str(var_1.get()) + str(var_2.get()) + str(var_3.get()) + str(var_4.get()) + str(var_5.get()) + str(var_6.get()) + str(var_7.get()) + str(var_8.get())
            if code_in == "01000101":
                app.update_console("A part of the wall retracts, revealing a bone shiv and some chicken tendies.",tag="g")
                app.add_item("Bone Shiv")
                app.add_item("Chicken Tendies")
                switches = True
                app.update_buttons( [ ("Back",op1)])
            else:
                app.update_console("Nothing happened.")
            game.destroy()
        game = Toplevel(width=800,height=100,padx=10,pady=10)
        game.title("Jungle Puzzle")
        switchArray = Frame(game)
        switchArray.pack(fill=X,expand=1)
        switch_1 = Frame(switchArray,bd=2,relief=SUNKEN,padx=20,pady=5)
        var_1 = IntVar()
        switch_1_disp = Label(switch_1,pady=5,font=("Fixedsys",16,"bold"),textvariable=var_1)
        switch_1_box = Checkbutton(switch_1,variable=var_1)
        switch_1_disp.pack()
        switch_1_box.pack()
        switch_1.pack(side=LEFT)

        switch_2 = Frame(switchArray,bd=2,relief=SUNKEN,padx=20,pady=5)
        var_2 = IntVar()
        switch_2_disp = Label(switch_2,pady=5,font=("Fixedsys",16,"bold"),textvariable=var_2)
        switch_2_box = Checkbutton(switch_2,variable=var_2)
        switch_2_disp.pack()
        switch_2_box.pack()
        switch_2.pack(side=LEFT)

        switch_3 = Frame(switchArray,bd=2,relief=SUNKEN,padx=20,pady=5)
        var_3 = IntVar()
        switch_3_disp = Label(switch_3,pady=5,font=("Fixedsys",16,"bold"),textvariable=var_3)
        switch_3_box = Checkbutton(switch_3,variable=var_3)
        switch_3_disp.pack()
        switch_3_box.pack()
        switch_3.pack(side=LEFT)

        switch_4 = Frame(switchArray,bd=2,relief=SUNKEN,padx=20,pady=5)
        var_4 = IntVar()
        switch_4_disp = Label(switch_4,pady=5,font=("Fixedsys",16,"bold"),textvariable=var_4)
        switch_4_box = Checkbutton(switch_4,variable=var_4)
        switch_4_disp.pack()
        switch_4_box.pack()
        switch_4.pack(side=LEFT)

        switch_5 = Frame(switchArray,bd=2,relief=SUNKEN,padx=20,pady=5)
        var_5 = IntVar()
        switch_5_disp = Label(switch_5,pady=5,font=("Fixedsys",16,"bold"),textvariable=var_5)
        switch_5_box = Checkbutton(switch_5,variable=var_5)
        switch_5_disp.pack()
        switch_5_box.pack()
        switch_5.pack(side=LEFT)

        switch_6 = Frame(switchArray,bd=2,relief=SUNKEN,padx=20,pady=5)
        var_6 = IntVar()
        switch_6_disp = Label(switch_6,pady=6,font=("Fixedsys",16,"bold"),textvariable=var_6)
        switch_6_box = Checkbutton(switch_6,variable=var_6)
        switch_6_disp.pack()
        switch_6_box.pack()
        switch_6.pack(side=LEFT)

        switch_7 = Frame(switchArray,bd=2,relief=SUNKEN,padx=20,pady=5)
        var_7 = IntVar()
        switch_7_disp = Label(switch_7,pady=5,font=("Fixedsys",16,"bold"),textvariable=var_7)
        switch_7_box = Checkbutton(switch_7,variable=var_7)
        switch_7_disp.pack()
        switch_7_box.pack()
        switch_7.pack(side=LEFT)

        switch_8 = Frame(switchArray,bd=2,relief=SUNKEN,padx=20,pady=5)
        var_8 = IntVar()
        switch_8_disp = Label(switch_8,pady=5,font=("Fixedsys",16,"bold"),textvariable=var_8)
        switch_8_box = Checkbutton(switch_8,variable=var_8)
        switch_8_disp.pack()
        switch_8_box.pack()
        switch_8.pack(side=LEFT)

        button_container = Frame(game,pady=10)
        Button(button_container,text="Done",command=exit_puzzle).pack()
        button_container.pack(side=BOTTOM)

        game.grab_set()

    if not switches:
        app.update_console("The eight switches seem to be placed in a random order. If only you had a code that could tell you the right order to put them in.")
        app.update_buttons([ ("Enter a Code", minigame) , ("Back", op1)])
    else:
        app.update_console("You have already collected the loot in the section under the switches.")
        app.update_buttons([ ("Back", op1) ])



    '''
    global switches
    #global b
    if (switches==False):
        print 'The eight switches seem to be placed in a random order. If only you had a code that could tell you the right order to put them in.'
        ans = raw_input('> ')
        print '\n'
        if (ans == '01000101'):
            print ('Correct combination! A part of the wall retracts and a bone shiv is dispensed!\n')
            app.add_item("Bone Shiv")
            switches = True
        else:
            print ('That combination does nothing.\n')
    else:
        print 'You have already seen the switches.\n'
    op1()
    '''

def op1_2():
    global chest
    if (chest==False):
        app.update_console( 'The worn-down chest opens with a creaking sound, revealing: ')
        loot = random.randint(0,3)
        if (loot == 0):
            app.update_console( 'Steamed Hams and Macaroni!\n', tag="g")
            app.add_item("Steamed Hams and Macaroni")
        if (loot == 1):
            app.update_console( 'M&Ms!\n', tag="g")
            app.add_item("M&Ms")
        if (loot == 2):
            app.update_console( 'Burger King Foot Lettuce!\n', tag="g")
            app.add_item("Lettuce")
        if (loot == 3):
            app.update_console( 'Gravy!\n', tag="g")
            app.add_item("Gravy")
        chest = True
        app.update_buttons([('Back', op1)])
    else:
        app.update_console('This chest has already been opened.\n')
        app.update_buttons([('Back', op1)])

def op1_3():
    global lives
    global darkRoom
    if (darkRoom == False):
        app.update_console( 'You descend the stairs and find a very dark room. You believe that there could be something useful in this room. You decide to search for a lightswitch. Do you...\n')
        app.update_buttons([('Walk', op1_3_1), ('Crawl', op1_3_2), ('Hug the wall', op1_3_3), ('Back', op1)])
    else:
        app.update_console( 'You decide there\'s nothing left for you downstairs\n')
        app.update_buttons([('Back', op1)])


def op1_3_1():
    global darkRoom
    app.update_console( 'You try walking but unfortunately hit a few traps on the floor to the lightswitch. (-1 life)', tag="r")
    app.add_life(-1)
    app.update_console( 'You find the switch and see a futuristic-looking key on the ground. You pick up the key and put it in your backpack.\n','g')
    app.add_item('Key')
    darkRoom = True

    app.update_buttons([('Back', op1)])

def op1_3_2():
    global darkRoom
    global lives
    app.update_console( 'You try crawling but unfortunately hit a few traps on the floor to the lightswtich. (-1 life)', tag="r")
    app.add_life(-1)
    app.update_console( 'You find the switch and see a futuristic-looking key on the ground. You pick up the key and put it in your backpack.\n', tag='g')
    app.add_item('Key')
    darkRoom = True
    app.update_buttons([('Back', op1)])

def op1_3_3():
    global darkRoom
    app.update_console( 'You successfully make it to the other side of the room without getting hurt', tag="g")
    app.update_console( 'You find the switch and see a futuristic-looking key on the ground. You pick up the key and put it in your backpack.\n', tag='g')
    app.add_item('Key')
    darkRoom = True
    app.update_buttons([('Back', op1)])

#change to short range weapon when functional
def op2():
    global tRex
    if (tRex == False):
        app.update_console( 'You decide it would be a good idea to kill this sleeping dinosaur to get its skull.')
        if (app.get_items('weapon') != []):
            app.update_buttons([('Attack', op2_1), ('Back', start)])
        else:
            app.update_console( 'However, you don\'t want to attack it without some sort of weapon.\n')
            app.update_buttons([('Back', start)])
    else:
        app.update_console('You have already killed the T-Rex')
        app.update_buttons([('Back', start)])

def op2_1():
    global tRex
    app.update_console( 'You take out your ' + random.choice(app.get_items('weapon')) + ' and attack the dinosaur, killing it. You recieved its skull as a reward.\n', tag='g')
    app.add_item('Skull')
    tRex = True

def op3():
    global necklace
    if (necklace == False):
        app.update_console( 'At the abandoned campsite, you see a shaggy man with a wispy beard. The insane-looking man tells you that he has a power crystal to give you if you get him a seashell necklace. You decide to trust the man\'s word.')
    app.update_console( 'Throughout the rest of the campsite, you see two tents and a campfire. What do you do?\n')
    if (app.has_item('Seashell Necklace')):
        app.update_buttons([('Search first tent', op3_1), ('Search second tent', op3_2), ('Search campfire', op3_3), ('Back', start), ('Give necklace', op3_4)])
    else:
        app.update_buttons([('Search first tent', op3_1), ('Search second tent', op3_2), ('Search campfire', op3_3), ('Back', start)])

def op3_1():
    app.update_console( 'You find nothing in the first tent.\n')
    app.update_buttons([('Back', op3)])
def op3_2():
    global lives
    global raptor
    if (raptor == False):
        app.update_console( 'A baby raptor jumps out of the tent and starts attacking you!',tag="r")
        if (app.get_items('weapon') != []):
            app.update_console( 'You kill the raptor with your ' + random.choice(app.get_items('weapon')) + '.')
        else:
            chance = random.randint(0,1)
            if (chance == 0):
                app.update_console( 'The raptor hits you with a devastating strike. (-1 life)\n', tag='r')
                app.add_life(-1)
            if (chance == 1):
                app.update_console( 'Luckily, you are able to kill the raptor with your bare fists without a scratch.\n')
        raptor = True
    else:
        app.update_console( 'The tent is now empty after the raptor left\n')
    app.update_buttons([('Back', op3)])

def op3_3():
    global campfire
    if (campfire == False):
        app.update_console( 'You find coal in the campfire!\n',tag="g")
        app.add_item('Coal')
        campfire = True
    else:
        app.update_console( 'You find nothing else in the campfire.\n')
    app.update_buttons([('Back', op3)])
def op3_4():
    global necklace
    app.update_console( 'You hand the seashell necklace over to the man, and, as he promised, he gifts you a green power crystal.\n', tag='g')
    app.remove_item('Seashell Necklace')
    app.add_item('Green Crystal')
    necklace = True
    app.update_buttons([('Back', op3)])
