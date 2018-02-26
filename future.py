# methods handling operations in Future

import hub
import random

app = None

mayor = False
scientists = False
criminal = False
door = False
hospital = False

def run(a):
    # called by main
    global app
    app = a
    app.update_console('You step into the futuristic landscape with awe as hovercars fly past your head.\n')
    start()

def start():
    # starting point
    app.update_console('You enter the busy city and see what appear to be a city hall, a research department, and a hospital wing. Which area you do inspect?\n')
    app.update_buttons([('City Hall', op1), ('Tech Research Department', op2), ('Hospital Wing', op3), ('Return to Hub', lambda: hub.run(app))])

def op1():
    # option 1
    global mayor
    if (not mayor):
        app.update_console('The mayor of the city greets you with a polite handshake. You converse and he starts to complain about the food in the future. He says he would give anything to taste food that isn\'t a bland soup like their food.\n')
        if (app.get_items('food') != [] and app.get_items('food') != ['Soylent']):
            app.update_buttons([('Give Some Food', op1_1), ('Back', start)])
        else:
            app.update_buttons([('Back', start)])
    else:
        app.update_console('Mayor Jeffery thanks you for your delicious snack\n')
        app.update_buttons([('Back', start)])

def op1_1():
    # option 1: suboption 1
    global mayor
    food = random.choice(app.get_items('food'))
    while (food == 'Soylent'):
        food = random.choice(app.get_item('food'))
    app.remove_item(food)
    app.update_console('The mayor tastes your ' + food + ' and his eyes light up. He thanks you immensely for your gratitude. He gives you a trendy parka as a reward.\n', tag='g')
    app.add_item('Parka')
    mayor = True
    app.update_buttons([('Back', start)])

def op2():
    # option 2
    app.update_console('The research building has a grand facility where you can see a group of scientists discussing their work, and suspicious door\n')
    app.update_buttons([('Talk to Scientists', op2_1), ('Door', op2_2), ('Back', start)])

def op2_1():
    # option 2 suboption 1
    global scientists
    if (not scientists):
        app.update_console('The scientists show you their new invention: a device that lets you go to the bottom of the ocean, withstanding all the immense pressure. In order to get yourself one of these, you must make a donation to their weapons department. Or... you could just steal it...\n')
        if (app.get_items('weapon') != []):
            app.update_buttons([('Give Weapon', op2_1_1), ('Steal Device', op2_1_2), ('Back', op2)])
        else:
            app.update_buttons([('Steal Device', op2_1_2), ('Back', op2)])
    else:
        app.update_console('The scientists have nothing more for you.\n')
        app.update_buttons([('Back', op2)])

def op2_1_1():
    # option 2 suboption 1 suboption 1
    global scientists
    weapon = random.choice(app.get_items('weapon'))
    app.remove_item(weapon)
    app.update_console('The scientists thank you kindly for your donation of a ' + weapon + ' and give you a copy of the deep-sea device\n', tag='g')
    app.add_item('Deep-sea Diving Device')
    scientists = True
    app.update_buttons([('Back', op2)])

def op2_1_2():
    # option 2 suboption 1 suboption 2
    global scientists
    global criminal
    chance = random.randint(0, 9)
    if (criminal):
        app.update_console('The scientists recognize you by your earlier encounter and call over the security drones again. They take you back to the federal prison cell.', tag='r')
        app.update_console('Since you apparently haven\'t learned your lesson, you have to escape again.\n')
        app.update_buttons([('Escape', op2_1_2_1)])
    elif (chance < 7):
        app.update_console('The scientists catch you trying to steal a device and yell "SECURITY!" Two massive drones fly from the air, grab you, and bring you to the federal prison.', tag='r')
        app.update_console('Now that you\'re in prison, you\'ll have to try to escape.\n')
        app.update_buttons([('Escape', op2_1_2_1)])
        criminal = True
    else:
        app.update_console('You sneakily grab one of the devices from a storage unit and escape without fail.\n', tag='g')
        app.update_buttons([('Back', op2)])
        app.add_item('Deep-sea Diving Device')
        scientists = True

def op2_1_2_1():
    # option 2 suboption 1 suboption 2 suboption 1
    chance = random.randint(0,1)
    if (chance == 0):
        app.update_console('You fail to escape from prison and are attacked by guards. (-1 Life)\n', tag='r')
        app.add_life(-1)
        app.update_buttons([('Escape', op2_1_2_1)])
    else:
        app.update_console('You successfully break out of your jail cell and sneak past your captors.\n',tag="g")
        app.update_buttons([('Back', op2)])

def op2_2():
    # option 2 suboption 2
    global door
    if (not door):
        app.update_console('You try to open the suspicious door, but it appears to be locked.\n')
        if (app.has_item('Key')):
            app.update_buttons([('Use Key', op2_2_1), ('Back', op2)])
        else:
            app.update_buttons([('Back', op2)])
    else:
        app.update_console('The closet is empty.\n')
        app.update_buttons([('Back', op2)])

def op2_2_1():
    # option 2 suboption 2 suboption 1
    global door
    app.update_console('You open the door and find a closet with a ray gun and a dolphin translator. You pick them up and store them in your backpack.\n', tag='g')
    app.add_item('Ray Gun')
    app.add_item('Dolphin Translator')
    app.add_item('Soylent')
    door = True
    app.update_buttons([('Back', op2)])

def op3():
    # option 3
    global hospital
    if (not hospital):
        app.update_console('You begin talking to one of the doctors in the medical research wing. She tells you that the research department is looking to perform tests on herbal medicine, but they can\'t seem to find it anywhere. They are offering a reward of a power crystal\n')
        if (app.has_item('Herbal Medicine')):
            app.update_buttons([('Give Herbal Medicine', op3_1), ('Back', start)])
        else:
            app.update_buttons([('Back', start)])
    else:
        app.update_console('The doctor smiles at you. She doesn\'t need anything else.\n')
        app.update_buttons([('Back', start)])

def op3_1():
    # option 3 suboption 1
    global hospital
    app.update_console('"Thank you so much for this! We\'re going to begin testing right away!" says the doctor. She grants you a power crystal.\n', tag='g')
    app.remove_item('Herbal Medicine')
    app.add_item('Orange Crystal')
    hospital = True
    app.update_buttons([('Back', start)])
