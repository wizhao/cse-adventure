class Item(object):
#Item class

    def __init__(self, name=None, caption="Bottom Text", ilk="tool", picture="itemGeneric.png",droppable=True,reason=None):
        #initialize object in Item class
        self.name = name
        self.caption = caption
        self.ilk = ilk
        self.picture = picture
        self.droppable = droppable
