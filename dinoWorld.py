#Dino World
import random
import hub

b = None
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
    b = app.get_b()
    app.update_console('You enter the Dino World and are transported into a thick jungle filled with beautiful flora and fauna.')
    start()
    app.set_b(b)
    
def start():
    app.update_console('To your left you see a towering stone temple, in the distance, you see a sleeping T-Rex, and to your right, you see an abandoned campsite. Which way do you turn?')
    app.update_buttons([('Jungle Temple', op1), ('Sleeping T-Rex', op2), ('Abandoned Campsite', op3), ('Return to Hub', lambda: hub.run(app))])
        
def op1():
    app.update_console('You walk into the Jungle Temple and see eight switches on the wall in front of you. To the right of that wall is a staircase, and on the left side of the room is a dilapidated chest. Where do you choose to go?')
    app.update_buttons([('Switches', op1_1), ('Chest', op1_2), ('Staircase', op1_3), ('Back', start)])
        
def op1_1():
    pass
    '''
    global switches
    #global b
    if (switches==False):
        print 'The eight switches seem to be placed in a random order. If only you had a code that could tell you the right order to put them in.'
        ans = raw_input('> ')
        print '\n'
        if (ans == '01000101'):
            print ('Correct combination! A part of the wall retracts and a bone shiv is dispensed!\n')
            b.add("bone shiv")
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
            b.add("steamed hams and macaroni")
        if (loot == 1):
            app.update_console( 'M&Ms!\n', tag="g")
            b.add("M&Ms")
        if (loot == 2):
            app.update_console( 'Burger King Foot Lettuce!\n', tag="g")
            b.add("lettuce")
        if (loot == 3):
            app.update_console( 'Gravy!\n', tag="g")
            b.add("gravy")
        chest = True  
    else:
        app.update_console('This chest has already been opened.\n')
    op1()
    
    
def op1_3():
    global lives
    global darkRoom
    if (darkRoom == False):
        app.update_console( 'You descend the stairs and find a very dark room. You believe that there could be something useful in this room. You decide to search for a lightswitch. Do you...')
        app.update_buttons([('Walk', op1_3_1), ('Crawl', op1_3_2), ('Hug the wall', op1_3_3), ('Back', op1)])
    else:
        app.update_console( 'You decide there\'s nothing left for you downstairs\n')
    

def op1_3_1():
    global darkRoom
    app.update_console( 'You try walking but unfortunately hit a few traps on the floor to the lightswitch. (-1 life)', tag="r")
    #lives-=1
    app.update_console( 'You find the switch and see a futuristic-looking key on the ground. You pick up the key and put it in your backpack.\n','g')
    b.add('key')
    darkRoom = True
    op1()
    
def op1_3_2():
    global darkRoom
    app.update_console( 'You try crawling but unfortunately hit a few traps on the floor to the lightswtich. (-1 life)', tag="r")
    #lives-=1
    app.update_console( 'You find the switch and see a futuristic-looking key on the ground. You pick up the key and put it in your backpack.\n', tag='g')
    b.add('key')
    darkRoom = True
    op1()
    
def op1_3_3():
    global darkRoom
    app.update_console( 'You successfully make it to the other side of the room without getting hurt', tag="g")
    app.update_console( 'You find the switch and see a futuristic-looking key on the ground. You pick up the key and put it in your backpack.\n', tag='g')
    b.add('key')
    darkRoom = True
    op1()
        
#change to short range weapon when functional
def op2():
    global tRex
    if (tRex == False):
        app.update_console( 'You decide it would be a good idea to kill this sleeping dinosaur to get its skull.')
        if (b.get_items('weapon') != []):
            app.update_console( 'You take out your ' + random.choice(b.get_items('weapon')) + ' and attack the dinosaur, killing it. You recieved its skull as a reward.', tag='g')
            b.add('skull')
            tRex = True
        else:
            app.update_console( 'However, you don\'t want to attack it without some sort of weapon.')
    start()
    
def op3():
    global necklace
    if (necklace == False):
        app.update_console( 'At the abandoned campsite, you see a shaggy man with a wispy beard. The insane-looking man tells you that he has a power crystal to give you if you get him a **Seashell Necklace**. You decide to trust the man\'s word.')
    app.update_console( 'Throughout the rest of the campsite, you see two tents and a campfire. What do you do?')
    if (b.has('seashell necklace')):
        app.update_buttons([('Search first tent', op3_1), ('Search second tent', op3_2), ('Search campfire', op3_3), ('Back', op3), ('Give necklace', op3_4)])
    else:
        app.update_buttons([('Search first tent', op3_1), ('Search second tent', op3_2), ('Search campfire', op3_3), ('Back', op3), ('Give necklace', op3_4)])

def op3_1():
    app.update_console( 'You find nothing in the first tent.')
    op3()
def op3_2():
    global lives
    global raptor
    if (raptor == False):
        app.update_console( 'A baby raptor jumps out of the tent and starts attacking you.')
        if (b.get_items('weapon') != []):
            app.update_console( 'You kill the raptor with your ' + random.choice(b.get_items('weapon')) + '.')
        else:
            chance = random.randint(0,1)
            if (chance == 0):
                app.update_console( 'The raptor hits you with a devastating strike. (-1 life)', tag='r')
                #lives-=1
            if (chance == 1):
                app.update_console( 'Luckily, you are able to kill the raptor with your bare fists without a scratch.')
        raptor = True
    else:
        app.update_console( 'The tent is now empty after the raptor left')
    op3()
    
def op3_3():
    global campfire
    if (campfire == False):
        app.update_console( 'You find coal in the campfire')
        b.add('coal')
        campfire = True
    else:
        app.update_console( 'You find nothing else in the campfire.')
    op3()
def op3_4():
    global necklace
    app.update_console( 'You hand the seashell necklace over to the man, and, as he promised, he gifts you a green power crystal')
    b.add('green crystal')
    b.remove('seashell necklace')
    necklace = True
    op3()