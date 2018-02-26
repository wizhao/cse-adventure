# class handling Player methods and attributes

class Player(object):
    #Player class

    def __init__(self):
        #initialize object in Player class
        self.lives = 5
        self.chestOpened = False


    def set_lives(self, lives):
        #reset number of lives
        self.lives = lives

    def get_lives(self):
        #retrieve number of lives
        return self.lives
