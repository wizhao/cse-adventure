class Player(object):
    def __init__(self):
        self.lives = 5
        self.chestOpened = False
    
    def set_lives(self, lives):
        self.lives = lives
    
    def get_lives(self):
        return self.lives
        
    