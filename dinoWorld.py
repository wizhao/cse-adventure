from main import Main
#Dino World
def run():
    print '\nYou enter the Dino World and are transported into a thick jungle filled with beautiful flora and fauna.'
    start()
    
def start():
    print 'To your left you see a towering stone temple, in the distance, you see a sleeping T-Rex, and to your right, you see an abandoned campsite. Which way do you turn?'
    ans = Main.select(['Jungle Temple', 'Sleeping T-Rex', 'Abandoned Campsite', 'Return to Hub'])
    if (ans == 1):
        op1()
    if (ans == 2):
        op2()
    if (ans == 3):
        op3()
    if (ans == 4):
        Main.hub()
def op1():
    print 'You walk into the Jungle Temple and see eight switches on the wall in front of you. To the right of that wall is a staircase, and on the left side of the room is a dilapidated chest. Where do you choose to go?'
    ans = Main.select(Main, ['Switches', 'Dilapidated Chest', 'Staircase', 'Back'])
    if (ans == 1):
        op1_1()
    if (ans == 2):
        op1_2()
    if (ans == 3):
        op1_3()
    if (ans == 4):
        op1()
def op1_1():
    print 'The eight switches seem to be placed in a random order. If only you had a code that could tell you the right order to put them in.'
    ans = raw_input('> ')
    if (ans == '01000101'):
        print ('Correct combination! You have recieved a bone pick!')
        #Main.add("bone pick")
    else:
        print ('Sorry, that combination is incorrect')
    op1()
def op1_2():
    if (Main.get_chest() == False):
        print 'You go to the worn-down chest to open it. It makes a creaking sound and reveals to you: '
        Main.set_chest(True)
    else:
        print 'test'
        
def op1_3():
    pass
def op2():
    pass
def op3():
    pass
