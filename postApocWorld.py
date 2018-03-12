# methods handling operations in Post-apocalyptic World

import hub
import random

app = None

jisoo = False
uranium = False
gang = False

def run(a):
    # called by main
    global app
    app = a
    app.update_console('You enter this fallow, dystopian world gasping for your breath as the dust invades your nostrils.\n')
    start()

def start():
    # starting point
    app.change_location(("postApocWorld.png","A dusty dystopia"))
    app.update_console('Within your field of view, you can see a massive metal dome, a group of off-road vehicles, and a gang of survivors. Which area do you visit first?\n')
    app.update_buttons([('Thunderdome', op1), ('Off-road Vehicles', op2), ('Gang of Survivors', op3), ('Return to Hub', lambda: hub.run(app))])

def op1():
    # option 1
    challenger = random.choice(['jeff', 'Adithya the Almighty', 'Daniel the Dauntless', 'Con Hndenberg', 'Sidhu the Sadistic', 'Glasser the Graceful', 'Nelson the Nightmare'])
    if (challenger == 'jeff'):
        app.change_location(("jeff.png","jeff"))
    if (challenger == 'Adithya the Almighty'):
        app.change_location(("adithya.png","Adithya the Almighty"))
    if (challenger == 'Daniel the Dauntless'):
        app.change_location(("daniel.png","Daniel the Dauntless"))
    if (challenger == 'Con Hndenberg'):
        app.change_location(("conH.png","Con Hndenberg"))
    if (challenger == 'Sidhu the Sadistic'):
        app.change_location(("sidhu.png","Sidhu the Sadistic"))
    if (challenger == 'Glasser the Graceful'):
        app.change_location(("glasser.png","Glasser the Graceful"))
    if (challenger == 'Nelson the Nightmare'):
        app.change_location(("nelson.png","Nelson the Nightmare"))
    app.update_console( 'A man wearing a bucket as a helmet walks up to you and shouts: "WELCOME TO THE THUNDERDOME! Today you will face off against the next challenger: ' + challenger + '!"\n')
    app.update_console( 'To fight, you will roll two six-sided dice to determine if you lose. A loss will make you lose a life, but a win will let you gain another. Winning also can get you other sweet rewards.')
    if (challenger == 'Daniel the Dauntless' and app.has_item('Jisoo Photo')):
        app.update_console('Daniel the Dauntless is distracted by your photo of Jisoo, so you only need higher than a 3 to win.\n')
        app.update_buttons([("Play", lambda: op1_1(3, challenger)), ("Back", start)])
    elif (app.get_items('weapon') != []):
        app.update_console( 'Since you have a weapon, you will need to roll higher than a 7 to win.\n')
        app.update_buttons([("Play", lambda: op1_1(7, challenger)), ("Back", start)])
    else:
        app.update_console( 'Since you don\'t have a weapon, you will need to roll higher than a 9 to win.\n')
        app.update_buttons([("Play", lambda: op1_1(9, challenger)), ("Back", start)])

def op1_1(minRoll, challenger):
    # option 1: suboption 1
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    total = roll1 + roll2
    app.update_console( 'You rolled a ' + str(roll1) + ' and a ' + str(roll2) + ' for a total of ' + str(total) + '.')
    if (minRoll == 7):
        if (total > minRoll):
            app.update_console( 'Despite ' + challenger + '\'s brute force and dexterity, you are able to knock them down with your ' + random.choice(app.get_items('weapon')) + ' with grace. (+1 life)', tag='g')
            loot = random.randint(0, 9)
            if (loot < 5):
                if (not app.has_item('Spam')):
                    app.update_console( 'For your victory, you recieve some Spam.', tag='g')
                    app.add_item('Spam')
            if (loot == 6):
                if (not app.has_item('Crossbow')):
                    app.update_console( 'For your victory, you recieve a crossbow!', tag='g')
                    app.add_item('Crossbow')
            app.add_life(1)
        else:
            app.update_console( challenger + ' runs at you full speed and clobbers you in the skull with a massive blow. (-1 life)', tag='r')
            app.add_life(-1)
    if (minRoll == 9):
        if (total > minRoll):
            app.update_console( 'To the shock of the audience, you pummel down ' + challenger + ' with your bare fists. (+1 life)', tag='g')
            loot = random.randint(0, 9)
            if (loot < 5):
                if (not app.has_item('Spam')):
                    app.update_console( 'For your victory, you recieve some Spam.', tag='g')
                    app.add_item('Spam')
            if (loot == 6):
                if (not app.has_item('Crossbow')):
                    app.update_console( 'For your victory, you recieve a crossbow!', tag='g')
                    app.add_item('Crossbow')
            app.add_life(1)
        else:
            app.update_console( challenger + ' takes advantage of your lack of protection and knocks you out in a single punch. (-1 life)', tag='r')
            app.add_life(-1)
    if (minRoll == 3):
        if (total > minRoll):
            app.update_console('Because of his distraction, you beat ' + challenger + ' with your bare hands. (+1 life)', tag='g')
            loot = random.randint(0, 9)
            if (loot < 5):
                if (not app.has_item('Spam')):
                    app.update_console( 'For your victory, you recieve some Spam.', tag='g')
                    app.add_item('Spam')
            if (loot == 6):
                if (not app.has_item('Crossbow')):
                    app.update_console( 'For your victory, you recieve a crossbow!', tag='g')
                    app.add_item('Crossbow')
            app.add_life(1)
        else:
            app.update_console(challenger + ', despite being distracted by Jisoo, ' + challenger + 'is able to knock you out. (-1 life)', tag='r')
            app.add_life(-1)
    app.update_console( 'You can always try your hand at the THUNDERDOME again.\n')
    app.update_buttons([('Back', start)])

def op2():
    # option 2
    app.change_location(("postApocWorld2.png","Nice rides"))
    app.update_console('Upon entering the area, you see three vehicles: an off-road jeep, a monster truck, and a formula one racer. Which vehicle to you check?\n')
    app.update_buttons([('Jeep', op2_1), ('Monster Truck', op2_2), ('Formula One Racer', op2_3), ('Back', start)])

def op2_1():
    # option 2 suboption 1
    global jisoo
    if (not jisoo):
        app.change_location(("postApocWorld2_1jisoo.png","Cute"))
        app.update_console('You find a photo of a Korean Popstar and a french fry under the seat\n')
        app.add_item('Jisoo Photo')
        app.add_item('Fry')
        jisoo = True
    else:
        app.change_location(("postApocWorld2_1.png","Nothing left"))
        app.update_console('Nothing left to see here\n')
    app.update_buttons([('Back', op2)])

def op2_2():
    # option 2 suboption 2
    app.change_location(("postApocWorld2_2.png","Oooh a knife!"))
    app.update_console('You see a sleeping man decked out in chainmail armor asleep with a knife in his hands. Do you attempt to steal the knife?\n')
    app.update_buttons([('Steal', op2_2_1), ('Back', op2)])

def op2_2_1():
    # option 2 suboption 2 suboption 1
    app.update_console('The man wakes up before you can grab the knife out of his hands. He stabs you with it and falls back asleep. (-1 Life)\n', tag='r')
    app.add_life(-1)
    app.update_buttons([('Back', op2_2)])

def op2_3():
    # option 2 suboption 3
    global uranium
    if (not uranium):
        app.change_location(("postApocWorld2_3map.png","Map to somewhere???"))
        app.update_console('You find a map to a distant location marked with an X on it. You know that you won\'t be able to make it that far without some food for the trip, so you must have some food before continuing.\n')
        if (app.get_items('food') != []):
            app.update_buttons([('Eat food', op2_3_1), ('Back', op2)])
        else:
            app.update_buttons([('Back', op2)])
    else:
        app.update_console('You already got the uranium')
        app.update_buttons([('Back', op2)])

def op2_3_1():
    # option 2 suboption 3 suboption 1
    global uranium
    app.change_location(("postApocWorld2_3_1.png","Uranium...I'll take."))
    food = random.choice(app.get_items('food'))
    app.update_console('You eat your ' + food + ' and begin your trek')
    app.remove_item(food)
    app.update_console('You make your way to the point on the map, and once you get there, you see a vat of uranium. You decide this uranium is useful, so you take it with you for later.\n', tag='g')
    app.add_item('Uranium')
    uranium = True
    app.update_buttons([('Back', op2)])

def op3():
    # option 3
    global gang
    if (not gang):
        app.change_location(("postApocWorld3.png","A bunch of riff-raffs and hoodlums"))
        app.update_console('You walk up to the gang members and one of them starts speaking to you. "If ya wanna to be a part of our gang, yer gonna have to get yerself a skull of a dead predator." You see that they all have something around their necks: a power crystal.\n')
        if (app.has_item('Skull')):
            app.update_buttons([('Give Skull', op3_1), ('Back', start)])
        else:
            app.update_console("You have to go find the skull of another predator for them.")
            app.update_buttons([('Back', start)])
    else:
        app.update_console('You do NOT want to go back to that angry gang.\n')
        app.update_buttons([('Back', start)])

def op3_1():
    # option 3 suboption 1
    global gang
    app.change_location(("postApocWorld3_1.png", "Don't wanna get on this guy's bad side...."))
    app.update_console('"Wow, that\'s one impressive skull." says the gang leader. You hand him the skull and he returns to you a pendant. You take the crystal from the pendant and run away.\n')
    app.remove_item('Skull')
    app.add_item('Yellow Crystal')
    gang = True
    app.update_buttons([('Back', start)])
