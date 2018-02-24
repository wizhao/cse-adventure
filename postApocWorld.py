#Post-apocalyptic World
import hub
import random

b = None #stores backpack
lives = None #stores num of lives
app = None

#called by main
def run(a):
    global app
    global b
    app = a
    app.update_console('You enter this fallow, dystopian world gasping for your breath as the dust invades your nostrils.\n')
    b = app.get_b()
    start()
    app.set_b(b)

#starting point
def start():
    app.update_console('Within your field of view, you can see a massive glass dome, a group of off-road vehicles, and a gang of survivors. Which area do you visit first?\n')
    app.update_buttons([('Thunderdome', op1), ('Off-road Vehicles', op2), ('Gang of Survivors', op3), ('Return to Hub', lambda: hub.run(app))])

#option 1
def op1():
    challenger = random.choice(['jeff', 'Adithya the Almighty', 'Daniel the Dauntless', 'Con Hndenberg', 'Sidhu the Sadistic', 'Glasser the Graceful', 'Nelson the Nightmare'])
    app.update_console( 'A man wearing a bucket as a helmet walks up to you and shouts: "WELCOME TO THE THUNDERDOME! Today you will face off against the next challenger: ' + challenger + '!"\n')
    app.update_console( 'To fight, you will roll two six-sided dice to determine if you lose. A loss will make you lose a life, but a win will let you gain another. Winning also can get you other sweet rewards.')
    if (b.get_items('weapon') != []):
        app.update_console( 'Since you have a weapon, you will need to roll higher than a 7 to win.')
        app.update_buttons([("Play", lambda: op1_1(7, challenger)), ("Back", start)])
    else:
        app.update_console( 'Since you don\'t have a weapon, you will need to roll higher than a 9 to win.')
        app.update_buttons([("Play", lambda: op1_1(9, challenger)), ("Back", start)])
        
#option 1: suboption 1
def op1_1(minRoll, challenger):
    global lives
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    total = roll1 + roll2
    app.update_console( 'You rolled a ' + str(roll1) + ' and a ' + str(roll2) + ' for a total of ' + str(total) + '.')
    if (minRoll == 7):
        if (total > minRoll):
            app.update_console( 'Despite ' + challenger + '\'s brute force and dexterity, you are able to knock them down with your ' + random.choice(b.get_items('weapon')) + ' with grace. (+1 life)', tag='g')
            loot = random.randint(0, 9)
            if (loot < 5):
                if (not b.has('Human Meat')):
                    app.update_console( 'For your victory, you recieve some human meat.', tag='g')
                    b.add('Human Meat')
            if (loot == 6):
                if (not b.has('Crossbow')):
                    app.update_console( 'For your victory, you recieve a crossbow!', tag='g')
                    b.add('Crossbow')
            app.add_life(1)
        else:
            app.update_console( challenger + ' runs at you full speed and clobbers you in the skull with a massive blow. (-1 life)', tag='r')
            app.add_life(-1)
    if (minRoll == 9):
        if (total > minRoll):
            app.update_console( 'To the shock of the audience, you pummel down ' + challenger + ' with your bare fists. (+1 life)', tag='g')
            loot = random.randint(0, 9)
            if (loot < 5):
                if (not b.has('Human Meat')):
                    app.update_console( 'For your victory, you recieve some human meat.', tag='g')
                    b.add('Human Meat')
            if (loot == 6):
                if (not b.has('Crossbow')):
                    app.update_console( 'For your victory, you recieve a crossbow!', tag='g')
                    b.add('Crossbow')
            app.add_life(1)
        else:
            app.update_console( challenger + ' takes advantage of your lack of protection and knocks you out in a single punch. (-1 life)', tag='r')
            app.add_life(-1)
    app.update_console( 'You can always try your hand at the THUNDERDOME again.\n')
    op1()
        
    
#option 1: suboption 2
def op1_2():
    pass
    
#option 2
def op2():
    pass

def op3():
    pass