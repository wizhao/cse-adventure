#Dino World
import random

b = None
switches = False
chest = False
darkRoom = False

#select and get_answer are temporary for string input
def select(options):
    print "\n"
    i = 1;
    for option in options:
        print str(i) + ') ' + option;
        i+=1;
    return get_answer(options)

def get_answer(options):
    answer = raw_input('> ')
    print "\n"
    isInt = True
    val = 0
    try:
        val = int(answer)
    except ValueError:
        isInt = False
    if (isInt and val <= len(options) and val > 0):
        return val
    else:
        print 'Please enter a valid response (number 1-' + str(len(options)) + ')'
        return get_answer(options)

def run(backpack):
    global b
    b = backpack
    print '\nYou enter the Dino World and are transported into a thick jungle filled with beautiful flora and fauna.'
    start()
    return b
    
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
            print ('Correct combination! You have recieved a bone pick!')
            b.add("bone pick")
            switches = True
        else:
            print ('Sorry, that combination is incorrect')
    else:
        print 'You have already seen the switches.'
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
        chest = True  
    else:
        print 'This chest has already been opened.'
    op1()
    
    
def op1_3():
    if (darkRoom == False):
        print 'You descend the stairs and find a very dark room. You believe that there could be something useful in this room. You decide to search for a lightswitch. Do you...'
        ans = select(['Walk', 'Crawl', 'Hug the wall', 'Back'])
        if (ans == 1):
            op1_3_1()
        if (ans == 2):
            op1_3_2()
        if (ans == 3):
            op1_3_3()
        if (ans == 4):
            op1()
    pass
    
def op1_3_1():
    pass

def op1_3_2():
    pass

def op1_3_3():
    pass
    
def op2():
    pass
    
def op3():
    pass
