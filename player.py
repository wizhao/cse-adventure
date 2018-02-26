class Player(object):
    #initialize object in Player class
    def __init__(self):
        self.lives = 5
        self.chestOpened = False

    #reset number of lives
    def set_lives(self, lives):
        self.lives = lives

    #retrieve number of lives
    def get_lives(self):
        return self.lives
