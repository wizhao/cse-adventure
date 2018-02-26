# methods handling operations in Atlantis

import random
import hub

app = None

shark = False
triton = False
krabbyPatty = False
shipwreck = False

def run(a):
    # called by main
    global app
    app = a
    if (app.has_item('Oxygen Tank')):
        app.update_console('You put on your oxygen tank and admire the vibrant blue water and magestic city.\n')
        start()
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank', tag='r')
        hub.run(app)

def start():
    # starting point
    if (app.has_item('Oxygen Tank')):
        app.update_console('You can either visit the coral reef, the city of Atlantis, or the Marinara Trench. Where would you like to go?\n')
        app.update_buttons([('Coral Reef', op1), ('City of Atlantis', op2), ('Marinara Trench', op3), ('Return to Hub', lambda: hub.run(app))])
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op1():
    # option 1
    if (app.has_item('Oxygen Tank')):
        if (not shark):
            app.update_console('You see a shark in the coral reef. Do you want to fight it?\n')
            app.update_buttons([('Fight', op1_1), ('Back', start)])
        else:
            app.update_console('There\'s nothing left in the coral reef to see\n')
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op1_1():
    # option 1: suboption 1
    global shark
    if (app.has_item('Oxygen Tank')):
        if (app.get_items('weapon') != []):
            chance = random.randint(0,1)
            if (chance == 0):
                app.update_console('You successfully kill the shark with your ' + random.choice(app.get_items('weapon')) + '. You get nothing.\n')
                shark = True
            else:
                app.update_console('The shark bites you. (-1 Life)\n', tag='r')
                app.add_life(-1)
        else:
            chance = random.randint(0,9)
            if (chance == 9):
                app.update_console('You successfully punch the shark to death. You get nothing.\n')
                shark = True
            else:
                app.update_console('The shark bites you. (-1 Life)\n', tag='r')
                app.add_life(-1)
                app.update_buttons([('Back', op1)])
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op2():
    # option 2
    if (app.has_item('Oxygen Tank')):
        app.update_console('You enter the marvellous city of Atlantis and see two buildings that stand out to you: a grandiose gilded castle and a fast food restaurant. Where do you visit?\n')
        app.update_buttons([('Gilded Castle', op2_1), ('Fast Food Place', op2_2), ('Back', start)])
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op2_1():
    # option 2: suboption 1
    global triton
    if (app.has_item('Oxygen Tank')):
        if (not triton):
            app.update_console('You travel through the diamond-encrusted doorway and find a merman sitting on a throne with a shiny crown placed neatly on his head. You walk up to the merman and he tells you to kneel before him. He tells you his name is King Triton and that he is in need of a dolphin translator to speak with the wildlife. He offers a grand prize of his trident if you succed in bringing it to him.\n')
            if (app.has_item('Dolphin Translator')):
                app.update_buttons([('Give Dolphin Translator', op2_1_1), ('Back', op2)])
            else:
                app.update_buttons([('Back', op2)])
        else:
            app.update_console('King Triton once again thanks you for his gift\n')
            app.update_buttons([('Back', op2)])
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op2_1_1():
    # option 2: suboption 1 suboption 1
    global triton
    if (app.has_item('Oxygen Tank')):
        app.update_console('Triton thanks you for your generous gift and returns to you his trident.')
        app.remove_item('Dolphin Translator')
        app.add_item('Trident')
        triton = True
        app.update_buttons([('Back', op2)])
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op2_2():
    # option 2: suboption 2
    global krabbyPatty
    if (app.has_item('Oxygen Tank')):
        if (not krabbyPatty):
            app.update_console('A crab walking on his hind legs walks up to you and says: "Ahoy, laddy! Welcome to the Krusty Krab! Err... Unfortunately, our fry cook, Spongebob, is out for today, and our restaurant is really busy. Do you think you could make a Krabby Patty for us? I\'ll pay ya with my daughter Pearl\'s nice seashell necklace!"\n')
            app.update_buttons([('Sure!', op2_2_1), ('Back', op2)])
        else:
            app.update_console('You see their regular fry cook, Spongebob, has arrived, and he says to you, "Good morning! Isn\'t it the best day ever!"\n')
            app.update_buttons([('Back', start)])
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op2_2_1():
    # option 2: suboption 2 suboption 1
    if (app.has_item('Oxygen Tank')):
        app.update_console('Mr. Krabs hands you the Krabby Patty secret formula, but it\'s written in code! You\'re going to have to decipher it. The paper reads:')
        app.update_console('Uif tfdsfu gpsnvmb jt dsbc')
        app.update_console('The note also provides a hint: Caeser. What is the secret ingredient?\n')
        app.update_buttons([('Parsley', op2_2_1_1), ('Squirrel', op2_2_1_2), ('Seastar', op2_2_1_3), ('Crab', op2_2_1_4), ('Back', op2_2)])
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op2_2_1_1():
    # option 2: suboption 2 suboption 1 suboption 1
    if (app.has_item('Oxygen Tank')):
        app.update_console('You show the burger to Mr. Krabs. He takes a bite and says: "That\'s not the secret formula! Yer fired! (-1 Life)\n', tag='r')
        app.add_life(-1)
        app.update_buttons([('Back', op2_2)])
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op2_2_1_2():
    # option 2: suboption 2 suboption 1 suboption 2
    if (app.has_item('Oxygen Tank')):
        app.update_console('You show the burger to Mr. Krabs. He takes a bite and says: "That\'s not the secret formula! Yer fired! (-1 Life)\n', tag='r')
        app.add_life(-1)
        app.update_buttons([('Back', op2_2)])
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op2_2_1_3():
    # option 2: suboption 2 suboption 1 suboption 3
    if (app.has_item('Oxygen Tank')):
        app.update_console('You show the burger to Mr. Krabs. He takes a bite and says: "That\'s not the secret formula! Yer fired! (-1 Life)\n', tag='r')
        app.add_life(-1)
        app.update_buttons([('Back', op2_2)])
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op2_2_1_4():
    # option 2: suboption 2 suboption 1 suboption 4
    global krabbyPatty
    if (app.has_item('Oxygen Tank')):
        app.update_console('You show the burger to Mr. Krabs. He takes a bite and says: "Great job, lad! You made a perfect Krabby Patty! Here\'s a nice seashell necklace fer ya!\n', tag='g')
        app.add_item('Seashell Necklace')
        krabbyPatty = True
        app.update_buttons([('Back', op2)])
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op3():
    # option 3
    global shipwreck
    if (app.has_item('Oxygen Tank')):
        if (not shipwreck):
            app.update_console('You see a group of undersea scientists surrounding the very deep part of the ocean. "We know that there\'s a power crystal down there in an abandoned shipwreck, but we have no way to get it! We need some sort of deep-sea diving device," one says. You decide you want to go get the power crystal yourself.\n')
            if (app.has_item('Deep-sea Diving Device')):
                app.update_buttons([('Use Deep-sea Diving Device', op3_1), ('Back', start)])
            else:
                app.update_buttons([('Back', start)])
        else:
            app.update_console('There is nothing left in the trench.')
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)

def op3_1():
    # option: 3 suboption 1
    global shipwreck
    if (app.has_item('Oxygen Tank')):
        app.update_console('You put on your deep-sea diving device, travel all the way down to the bottom of the ocean, and enter the abandoned shipwreck. Stuck between the floorboards, you find a power crystal and put it in your backpack. However, your deep-sea diving device is used up, so you must throw it away.', tag='g')
        app.remove_item('Deep-sea Diving Device')
        app.add_item('Blue Crystal')
        shipwreck = True
        app.update_buttons([('Back', start)])
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank. (-2 Lives)', tag='r')
        app.add_life(-2)
        hub.run(app)
