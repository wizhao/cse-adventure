#Dino World
b = None
done = None

def select(options):
    i = 1;
    for option in options:
        print str(i) + ') ' + option;
        i+=1;
    return get_answer(options)

def get_answer(options):
    answer = raw_input('> ')
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

def run(backpack, d):
    global b
    global done
    b = backpack
    done = d
    print '\nYou enter the Dino World and are transported into a thick jungle filled with beautiful flora and fauna.'
    start()
    return b, done
    
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
    return
        
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
    return
        
def op1_1():
    global done
    global b
    if (done==True):
        print 'The eight switches seem to be placed in a random order. If only you had a code that could tell you the right order to put them in.'
        ans = raw_input('> ')
        if (ans == '01000101'):
            print ('Correct combination! You have recieved a bone pick!')
            b.add("bone pick")
            done = True
        else:
            print ('Sorry, that combination is incorrect')
    else:
        print 'You have already seen the switches.'
    op1()
    return
    
def op1_2():
    pass
    
def op1_3():
    pass
    
def op2():
    pass
    
def op3():
    pass
