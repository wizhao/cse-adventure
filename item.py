class Item(object):
    def __init__(self, name=None, caption="Bottom Text", ilk=None, subilk=None, picture="itemGeneric.png",droppable=True):
        self.name = name
        self.caption = caption
        self.ilk = ilk
        self.subilk = subilk
        self.picture = picture
        self.droppable = droppable

# pencil = Item('pencil', 'used to write stuff', 'utensil', 'lead-based')
# print pencil.description
