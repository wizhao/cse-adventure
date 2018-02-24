from backpack import Backpack
from  gui import Application
from Tkinter import *
import dinoWorld
import atlantis
import warWorld
import iceWorld
import future
import postApocWorld

b = Backpack()
lives = 5
count = 0

root = Tk()
root.resizable(width=False, height=False)
app = Application(master=root)

app.master.title("My Almost Do-Nothing Application")


app.mainloop()
root.destroy()

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
        
def start():
    global b
    global lives
    global count
    while (True):
        if (count == 0):
            print 'Welcome to Dimensions. At the start of our story, you wake up on a deserted planet in a world unlike your own. As you slowly regain consciousness, you realize that you are indeed on a different universe than you came from. You take out your portal gun and try to decipher the coordinates; however you can\'t seem to make out where you are. You notice in the distance a dimension hub. The hub may be able to take you home, if your universe is in range.\n\nYou walk into the dimension hub and gather information on your location. You find out your on an abandoned planet in dimension K33, but, unfortunately, you notice your home dimension is not within range. You do have a way of getting home using your portal gun, but its currently out of charge. Luckily, you notice 6 dimensions within range that each have a power crystal you need to recharge it. The only way to get home now is to find those six power crystals and make it home alive.\n\nYou will have to travel through six different universes and interact with the people and environment on each of them. You will have five lives to spare, and each mistake you make will take away one of those lives. Now, make us all proud and get back to your home.\n'
            print 'Choose the first world you want to visit:'
        else:
            print 'Choose a world to visit:'
        ans = select(['Dino World', 'Atlantis', 'War World', 'Ice World', 'Future World', 'Post-Apocalyptic World'])
        if (ans == 1):
            b, lives = dinoWorld.run(b, lives)
            b.list_items()
            print lives
        if (ans == 2):
            b, lives = atlantis.run(b, lives)
        if (ans == 3):
            b, lives = warWorld.run(b, lives)
        if (ans == 4):
            b, lives = iceWorld.run(b, lives)
        if (ans == 5):
            b, lives = future.run(b, lives)
        if (ans == 6):
            b, lives = postApocWorld.run(b, lives)
        count += 1
start()