#Post-apocalyptic World
import random

b = None #stores backpack
lives = None #stores num of lives

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

#called by main
def run(backpack, life):
    global b
    global lives
    b = backpack #sets global backpack
    lives = life #sets num of lives
    print "You enter this fallow, dystopian world gasping for your breath as the dust invades your nostrils."
    start() #run game
    return b, lives #return the backpack and lives

#starting point
def start():
    print 'Within your field of view, you can see a massive glass dome, a group of off-road vehicles, and a gang of survivors. Which area do you visit first?'
    ans = select(['Thunderdome', 'Off-road Vehicles', 'Gang of Survivors', 'Return to Hub'])
    if (ans == 1):
        op1()
    if (ans == 2):
        op2()
    if (ans == 3):
        op3()
    if (ans == 4):
        pass

#option 1
def op1():
    global lives
    challenger = random.choice(['Jeff', 'Adithya the Almighty', 'Daniel the Dauntless', 'Con Hndenberg', 'Sidhu the Sadistic', 'Glasser the Graceful', 'Nelson the Nightmare'])
    print 'A man wearing a bucket as a helmet walks up to you and shouts: "WELCOME TO THE THUNDERDOME! Today you will face off against the next challenger: ' + challenger + '!"'
    print '\nTo fight, you will roll two six-sided dice to determine if you lose. A loss will make you lose a life, but a win will let you gain another. Winning also can get you other sweet rewards.'
    if (b.get_items('weapon') != []):
        print 'Since you have a weapon, you will need to roll higher than a 7 to win.'
        ans = select(["Play", "Back"])
        if (ans == 1):
            if (op1_1(7)):
                print 'Despite ' + challenger + '\'s brute force and dexterity, you are able to knock them down with your ' + random.choice(b.get_items('weapon')) + ' with grace. (+1 life)'
                loot = random.randint(0, 9)
                if (loot < 5):
                    if (not b.has('human meat')):
                        print 'For your victory, you recieve some human meat.'
                        b.add('human meat')
                if (loot == 6):
                    if (not b.has('crossbow')):
                        print 'For your victory, you recieve a crossbow!'
                        b.add('crossbow')
                lives+=1
            else:
                print challenger + ' runs at you full speed and clobbers you in the skull with a massive blow. (-1 life)'
                lives-=1
                check_lives()
            print 'You can always try your hand at the THUNDERDOME again.\n'
            op1()
        if (ans == 2):
            start()
    else:
        print 'Since you don\'t have a weapon, you will need to roll higher than a 9 to win.'
        ans = select(["Play", "Back"])
        if (ans == 1):
            if (op1_1(9)):
                print 'To the shock of the audience, you pummel down ' + challenger + ' with your bare fists. (+1 life)'
                loot = random.randint(0, 9)
                if (loot < 5):
                    if (not b.has('human meat')):
                        print 'For your victory, you recieve some human meat.'
                        b.add('human meat')
                if (loot == 6):
                    if (not b.has('crossbow')):
                        print 'For your victory, you recieve a crossbow!'
                        b.add('crossbow')
                lives+=1
            else:
                print challenger + ' takes advantage of your lack of protection and knocks you out in a single punch. (-1 life)'
                lives-=1
                check_lives()
            print 'You can always try your hand at the THUNDERDOME again.\n'
            op1()
        if (ans == 2):
            start()
        
#option 1: suboption 1
def op1_1(minRoll):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    total = roll1 + roll2
    print 'You rolled a ' + str(roll1) + ' and a ' + str(roll2) + ' for a total of ' + str(total) + '.'
    if (total > minRoll):
        return True
    else:
        return False
    
#option 1: suboption 2
def op1_2():
    pass
    
#option 2
def op2():
    pass

def op3():
    pass