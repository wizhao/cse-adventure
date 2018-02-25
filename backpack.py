from item import Item

class Backpack(object):
    def __init__(self):
        self.itemLimit = 12
        portal_gun = Item('Portal Gun', None, 'tool',"portalGun.png",False,"You need that to get around, silly!")
        ray_gun = Item('Ray Gun', None, 'weapon')
        translator = Item('Dolphin Translator', None, 'tool')
        lettuce = Item('Lettuce', None, 'food')
        daniel = Item('Steamed Hams and Macaroni', None, 'food')
        icicle = Item('Icicle', None, 'tool')
        bone_shiv = Item('Bone Shiv', None, 'weapon')
        shotgun = Item('Sawed-off Shotgun', None, 'weapon')
        tactical_shotgun = Item('Purple Tactical Shotgun', None, 'weapon')
        trident = Item('Trident', None, 'weapon')
        crossbow = Item('Crossbow', None, 'weapon')
        key = Item('Key', 'It looks very complicated, and it\'s intricate almost to a microscopic level. Whoever left this in Dino World did not come from there.', 'tool')
        note = Item('Note', 'The note reads: "The password is 01000101" (Hint: Dino World)', 'tool')
        photo = Item('Jisoo Photo', None, 'tool')
        gravy = Item('Gravy', None, 'food')
        mms = Item('M&Ms', None, 'food')
        skis = Item('Skis', None, 'tool')
        parka = Item('Parka', None, 'tool')
        coal = Item('Coal', None, 'tool')
        human_meat = Item('Human Meat', None, 'food')
        skull = Item('Skull', None, 'important')
        uranium = Item('Uranium', None, 'important')
        grenade = Item('Grenades', None, 'important')
        necklace = Item('Seashell Necklace', None, 'important')
        device = Item('Deep-sea Diving Device', None, 'important')
        medicine = Item('Herbal Medicine', None, 'important')
        yellow_crystal = Item('Yellow Crystal', None, 'crystal')
        blue_crystal = Item('Blue Crystal', None, 'crystal')
        green_crystal = Item('Green Crystal', None, 'crystal')
        red_crystal = Item('Red Crystal', None, 'crystal')
        purple_crystal = Item('Purple Crystal', None, 'crystal')
        orange_crystal = Item('Orange Crystal', None, 'crystal')
        tank = Item('Oxygen Tank', None, 'tool')
        tendies = Item("Chicken Tendies","A 4-pack of chicken tenders. It reminds you of your past school lunches.","food","tendies.png")
        rifle = Item("Rifle","A wooden, bolt-action rifle. Battle-Scarred quality.","weapon","rifle.png")
        mre = Item("MRE","Meal, ready-to-eat. Doesn't taste very good, but at least it won't spoil.","food","mre.png")
        card = Item("ID Card","A government ID card, used for top-level access.","important","card.png")
        rock = Item("Rock","A mossy rock with some strange carvings on it.","important","rock.png")


        self.item_list = {portal_gun.name: portal_gun, ray_gun.name: ray_gun,
                            translator.name: translator, lettuce.name: lettuce,
                            daniel.name: daniel, icicle.name: icicle,
                            bone_shiv.name: bone_shiv, shotgun.name: shotgun,
                            tactical_shotgun.name: tactical_shotgun, trident.name:
                            trident, crossbow.name: crossbow, key.name: key, note.name:
                            note, photo.name: photo, gravy.name: gravy,
                            mms.name: mms, skis.name: skis,
                            parka.name: parka, coal.name: coal,
                            human_meat.name: human_meat, skull.name: skull, uranium.name: uranium,
                            grenade.name: grenade, necklace.name: necklace, device.name: device,
                            medicine.name: medicine, yellow_crystal.name: yellow_crystal,
                            blue_crystal.name: blue_crystal, green_crystal.name: green_crystal,
                            red_crystal.name: red_crystal, purple_crystal.name: purple_crystal,
                            orange_crystal.name: orange_crystal, tank.name: tank, tendies.name: tendies,
                            rifle.name: rifle, mre.name: mre}
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

    '''
    def list_items(self):
        for key, value in self.contents.iteritems():
            print key
    '''

    def has(self, name):
        if name in self.contents:
            return True
        return False

    def get_item(self,name):
        if name in self.contents:
            return self.contents[name]
        else:
            return Item()

#b = Backpack()
#b.add('key')
#b.add('armor')
#b.add('coal')
#b.add('crossbow')
#print b.get_items('weapon')
