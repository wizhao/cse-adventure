#Ice World
b = None #stores backpack
lives = None #stores num of lives

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
    print "ice world description"
    start() #run game
    return b, lives #return the backpack and lives

#starting point
def start():
    pass

#option 1
def op1():
    pass

#option 1: suboption 1
def op1_1():
    pass
    
#option 1: suboption 2
def op1_2():
    pass
    
#option 2
def op2():
    pass