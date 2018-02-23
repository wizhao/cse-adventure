from item import Item

class Backpack(object):
    def __init__(self):
        portal_gun = Item('portal gun', None, 'tool')
        ray_gun = Item('ray gun', None, 'weapon', 'long')
        translator = Item('dolphin translator', None, 'tool')
        lettuce = Item('lettuce', None, 'food')
        daniel = Item('steamed hams and macaroni', None, 'food')
        icicle = Item('icicle', None, 'tool')
        bone_pick = Item('bone pick', None, 'weapon', 'short')
        shotgun = Item('sawed-off shotgun', None, 'weapon', 'short')
        tactical_shotgun = Item('purple tactical shotgun', None, 'weapon', 'short')
        trident = Item('trident', None, 'weapon', 'short')
        crossbow = Item('crossbow', None, 'weapon', 'long')
        key = Item('key', 'It looks very complicated, and it\'s intricate almost to a microscopic level. Whoever left this in Dino World did not come from there.', 'tool')
        note = Item('note w/ password', 'The note reads: "The password is 01000101" (Hint: Dino World)', 'tool')
        photo = Item('jisoo photo', None, 'tool')
        gravy = Item('gravy', None, 'food')
        mms = Item('M&Ms', None, 'food')
        armor = Item('armor', None, 'tool')
        skis = Item('skis', None, 'tool')
        parka = Item('parka', None, 'tool')
        coal = Item('coal', None, 'tool')
        human_meat = Item('human meat', None, 'food')
        skull = Item('skull', None, 'important')
        uranium = Item('uranium', None, 'important')
        bomb = Item('bomb', None, 'important')
        necklace = Item('seashell necklace', None, 'important')
        device = Item('deep-sea diving device', None, 'important')
        medicine = Item('herbal medicine', None, 'important')
        yellow_crystal = Item('yellow crystal', None, 'crystal')
        blue_crystal = Item('blue crystal', None, 'crystal')
        green_crystal = Item('green crystal', None, 'crystal')
        red_crystal = Item('red crystal', None, 'crystal')
        purple_crystal = Item('purple crystal', None, 'crystal')
        orange_crystal = Item('orange crystal', None, 'crystal')
        

        self.item_list = {portal_gun.name: portal_gun, ray_gun.name: ray_gun,
                            translator.name: translator, lettuce.name: lettuce,
                            daniel.name: daniel, icicle.name: icicle,
                            bone_pick.name: bone_pick, shotgun.name: shotgun,
                            tactical_shotgun.name: tactical_shotgun, trident.name:
                            trident, crossbow.name: crossbow, key.name: key, note.name:
                            note, photo.name: photo, gravy.name: gravy,
                            mms.name: mms, armor.name: armor, skis.name: skis,
                            parka.name: parka, coal.name: coal,
                            human_meat.name: human_meat, skull.name: skull, uranium.name: uranium,
                            bomb.name: bomb, necklace.name: necklace, device.name: device,
                            medicine.name: medicine, yellow_crystal.name: yellow_crystal,
                            blue_crystal.name: blue_crystal, green_crystal.name: green_crystal,
                            red_crystal.name: red_crystal, purple_crystal.name: purple_crystal, 
                            orange_crystal.name: orange_crystal}
        self.contents = {}
        self.storage = {}

    def add(self, name):
        self.contents[name] = self.item_list[name]
        
    def remove(self, name):
        self.contents.pop(name)

    def put_in_storage(self, name):
        if name in self.contents:
            self.contents.pop(name)
            self.storage[name] = self.item_list[name]
        
    def get_from_storage(self, name):
        if name in self.storage:
            self.storage.pop(name)
            self.contents[name] = self.item_list[name]

    def get_items(self, category):
        names = []
        for key, value in self.contents.iteritems():
            if value.ilk == category:
                names.append(key)
        return names
    '''
    def get_items(self, category, subcategory):
        names = []
        for key, value in self.contents.iteritems():
            if value.ilk == category and value.subilk == subcategory:
                names.append(key)
        return names
    '''
    def list_items(self):
        for key, value in self.contents.iteritems():
            print key
            
    def has(self, name):
        if name in self.contents:
            return True
        else:
            return False

#b = Backpack()
#b.add('key')
#b.add('armor')
#b.add('coal')
#b.add('crossbow')
#print b.get_items('weapon')
