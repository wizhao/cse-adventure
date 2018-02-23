#Ice World
b = None #stores backpack

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

#called by main
def run(backpack):
    global b
    b = backpack #sets global backpack
    print "ice world description"
    start() #run game
    return b #return the backpack

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