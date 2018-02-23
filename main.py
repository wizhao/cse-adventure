from backpack import Backpack
from player import Player
import dinoWorld
import atlantis
import warWorld
import iceWorld
import future
import postApocWorld

class Main():
    def __init__(self):
        self.b = Backpack();
        self.p = Player();
        self.chest = False;
        self.start()
    def select(self, options):
        i = 1;
        for option in options:
            print str(i) + ') ' + option;
            i+=1;
        return self.get_answer(options)
    
    def get_answer(self, options):
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
            return self.get_answer(options)
            
    def start(self):
        print 'Welcome to Dimensions. At the start of our story, you wake up on a deserted planet in a world unlike your own. As you slowly regain consciousness, you realize that you are indeed on a different universe than you came from. You take out your portal gun and try to decipher the coordinates; however you can\xe2\x80\x99t seem to make out where you are. You notice in the distance a dimension hub. The hub may be able to take you home, if your universe is in range.\n\nYou walk into the dimension hub and gather information on your location. You find out your on an abandoned planet in dimension K33, but, unfortunately, you notice your home dimension is not within range. You do have a way of getting home using your portal gun, but its currently out of charge. Luckily, you notice 6 dimensions within range that each have a power crystal you need to recharge it. The only way to get home now is to find those six power crystals and make it home alive.\n\nYou will have to travel through six different universes and interact with the people and environment on each of them. You will have five lives to spare, and each mistake you make will take away one of those lives. Now, make us all proud and get back to your home.\n'
        print 'Choose the first world you want to visit:'
        ans = self.select(['Dino World', 'Atlantis', 'War World', 'Ice World', 'Future World', 'Post-Apocalyptic World'])
        if (ans == 1):
            dinoWorld.run()
        if (ans == 2):
            atlantis.run()
        if (ans == 3):
            warWorld.run()
        if (ans == 4):
            iceWorld.run()
        if (ans == 5):
            future.run()
        if (ans == 6):
            postApocWorld.run()
    
    def hub(self):
        print 'Choose a world to visit:'
        ans = self.select(['Dino World', 'Atlantis', 'War World', 'Ice World', 'Future World', 'Post-Apocalyptic World'])
        if (ans == 1):
            dinoWorld.run()
        if (ans == 2):
            atlantis.run()
        if (ans == 3):
            warWorld.run()
        if (ans == 4):
            iceWorld.run()
        if (ans == 5):
            future.run()
        if (ans == 6):
            postApocWorld.run()
    
    def set_chest(self, val):
        self.chest = val
        
    def get_chest(self):
        return self.chest
