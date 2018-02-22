class Item(object):
    def __init__(self, name=None, description=None, ilk=None, subilk=None):
        self.name = name
        self.description = description
        self.ilk = ilk
        self.subilk = subilk

# pencil = Item('pencil', 'used to write stuff', 'utensil', 'lead-based')
# print pencil.description
