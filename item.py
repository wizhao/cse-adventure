class Item(object):
    def __init__(self, name=None, caption="Bottom Text", ilk="tool", picture="itemGeneric.png",droppable=True,reason=None):
        self.name = name
        self.caption = caption
        self.ilk = ilk
        self.picture = picture
        self.droppable = droppable

# pencil = Item('pencil', 'used to write stuff', 'utensil', 'lead-based')
# print pencil.description
