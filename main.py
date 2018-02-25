from gui import Application
from Tkinter import *
import dinoWorld
import atlantis
import warWorld
import iceWorld
import future
import postApocWorld
import hub


root = Tk()
root.resizable(width=False, height=False)
app = Application(master=root)

def intro():
    app.update_console('Welcome to Dimensions. At the start of our story, you wake up on a deserted planet in a world unlike your own. As you slowly regain consciousness, you realize that you are indeed on a different universe than you came from. You take out your portal gun and try to decipher the coordinates; however you can\'t seem to make out where you are. You notice in the distance a dimension hub. The hub may be able to take you home, if your universe is in range.\n\n')
    app.update_buttons([('Enter Hub', start)])

def start():
    app.update_console('You walk into the dimension hub and gather information on your location. You find out that you are on an abandoned planet in dimension K33, but, unfortunately, you notice your home dimension is not within range. You do have a way of getting home using your portal gun, but its currently out of charge. Luckily, you notice 6 dimensions within range that each have a power crystal you need to recharge it. The only way to get home now is to find those six power crystals and make it home alive.\n\nYou will have to travel through six different universes and interact with the people and environment on each of them. You will have five lives to spare, and each mistake you make will take away one of those lives. Now, make us all proud and get back to your home.\n')
    hub.run(app)
    '''
    app.update_console('Choose a world to visit:\n')
    app.update_buttons([('Atlantis', lambda: atlantis.run(app)), ('Future', lambda: future.run(app)), ("Post-Apocalyptic World", lambda: postApocWorld.run(app)), ("Dino World", lambda: dinoWorld.run(app)), ('War World', lambda: warWorld.run(app)), ('Ice World', lambda: iceWorld.run(app))])
    #app.consoleScrollbar.set(0)'''
    app.output.yview_moveto(0.25)

app.master.title("Dimensions")

app.after(0,intro)
app.mainloop()
root.destroy()
