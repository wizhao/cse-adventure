#Dino World
import random


b = None
lives = None
switches = False
chest = False
darkRoom = False
tRex = False
raptor = False
campfire = False
necklace = False

#checks number of lives
def check_lives():
    global lives
    if (lives <= 0):
        print "YOU LOSE"
        exit()

#select and get_answer are temporary for string input
def select(options):
    print "\n"
    i = 1;
    for option in options: #print all options
        print str(i) + ') ' + option;
        i+=1;
    return get_answer(options)

def get_answer(options):
    answer = raw_input('> ') #get answer
    print "\n"
    isInt = True
    val = 0
    try:
        val = int(answer) #check if answer is an integer, set to int
    except ValueError:
        isInt = False
    if (isInt and val <= len(options) and val > 0):
        return val #return user's answer as a number
    else: #ask user for proper answer if not integer and within a range
        print 'Please enter a valid response (number 1-' + str(len(options)) + ')'
        return get_answer(options) #return next valid response

def run(backpack, life):
    global b
    global lives 
    b = backpack #sets global backpack
    lives = life #sets num of lives
    print '\nYou enter the Dino World and are transported into a thick jungle filled with beautiful flora and fauna.'
    start()
    return b, lives #return the backpack and lives
    
def start():
    print 'To your left you see a towering stone temple, in the distance, you see a sleeping T-Rex, and to your right, you see an abandoned campsite. Which way do you turn?'
    ans = select(['Jungle Temple', 'Sleeping T-Rex', 'Abandoned Campsite', 'Return to Hub'])
    if (ans == 1):
        op1()
    if (ans == 2):
        op2()
    if (ans == 3):
        op3()
    if (ans == 4):
        pass
        
def op1():
    print 'You walk into the Jungle Temple and see eight switches on the wall in front of you. To the right of that wall is a staircase, and on the left side of the room is a dilapidated chest. Where do you choose to go?'
    ans = select(['Switches', 'Dilapidated Chest', 'Staircase', 'Back'])
    if (ans == 1):
        op1_1()
    if (ans == 2):
        op1_2()
    if (ans == 3):
        op1_3()
    if (ans == 4):
        start()
        
def op1_1():
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
    
def op1_2():
    global chest
    if (chest==False):
        print 'The worn-down chest opens with a creaking sound, revealing: '
        loot = random.randint(0,3)
        if (loot == 0):
            print 'Steamed Hams and Macaroni!'
            b.add("steamed hams and macaroni")
        if (loot == 1):
            print 'M&Ms!'
            b.add("M&Ms")
        if (loot == 2):
            print 'Burger King Foot Lettuce!'
            b.add("lettuce")
        if (loot == 3):
            print 'Gravy!'
            b.add("gravy")
        print ""
        chest = True  
    else:
        print 'This chest has already been opened.\n'
    op1()
    
    
def op1_3():
    global lives
    global darkRoom
    if (darkRoom == False):
        print 'You descend the stairs and find a very dark room. You believe that there could be something useful in this room. You decide to search for a lightswitch. Do you...'
        ans = select(['Walk', 'Crawl', 'Hug the wall', 'Back'])
        if (ans == 1):
            print 'You try walking but unfortunately hit a few traps on the floor to the lightswitch. (-1 life)'
            lives-=1
            check_lives()
        if (ans == 2):
            print 'You try crawling but unfortunately hit a few traps on the floor to the lightswtich. (-1 life)'
            lives-=1
            check_lives()
        if (ans == 3):
            print 'You successfully make it to the other side of the room without getting hurt'
        if (ans == 4):
            op1()
        print 'You find the switch and see a futuristic-looking key on the ground. You pick up the key and put it in your backpack.\n'
        b.add('key')
        darkRoom = True
    else:
        print 'You decide there\'s nothing left for you downstairs\n'
    op1()

#change to short range weapon when functional
def op2():
    global tRex
    if (tRex == False):
        print 'You decide it would be a good idea to kill this sleeping dinosaur to get its skull.'
        if (b.get_items('weapon') != []):
            print 'You take out your ' + random.choice(b.get_items('weapon')) + ' and attack the dinosaur, killing it. You recieved its skull as a reward.'
            b.add('skull')
            tRex = True
        else:
            print 'However, you don\'t want to attack it without some sort of weapon.'
    start()
    
def op3():
    global necklace
    if (necklace == False):
        print 'At the abandoned campsite, you see a shaggy man with a wispy beard. The insane-looking man tells you that he has a power crystal to give you if you get him a **Seashell Necklace**. You decide to trust the man\'s word.'
    print 'Throughout the rest of the campsite, you see two tents and a campfire. What do you do?'
    ans = 0
    if (b.has('seashell necklace')):
        ans = select(['Search first tent', 'Search second tent', 'Search campfire', 'Back', 'Give necklace'])
    else:
        ans = select(['Search first tent', 'Search second tent', 'Search campfire', 'Back'])
    if (ans == 1):
        op3_1()
    if (ans == 2):
        op3_2()
    if (ans == 3):
        op3_3()
    if (ans == 4):
        start()
    if (ans == 5):
        op3_4()

def op3_1():
    print 'You find nothing in the first tent.'
    op3()
def op3_2():
    global lives
    global raptor
    if (raptor == False):
        print 'A baby raptor jumps out of the tent and starts attacking you.'
        if (b.get_items('weapon') != []):
            print 'You kill the raptor with your ' + random.choice(b.get_items('weapon')) + '.'
        else:
            chance = random.randint(0,1)
            if (chance == 0):
                print 'The raptor hits you with a devastating strike. (-1 life)'
                lives-=1
                check_lives()
            if (chance == 1):
                print 'Luckily, you are able to kill the raptor with your bare fists without a scratch.'
        raptor = True
    else:
        print 'The tent is now empty after the raptor left'
    op3()
    
def op3_3():
    global campfire
    if (campfire == False):
        print 'You find coal in the campfire'
        b.add('coal')
        campfire = True
    else:
        print 'You find nothing else in the campfire.'
    op3()
def op3_4():
    global necklace
    print 'You hand the seashell necklace over to the man, and, as he promised, he gifts you a green power crystal'
    b.add('green crystal')
    b.remove('seashell necklace')
    necklace = True
    op3()