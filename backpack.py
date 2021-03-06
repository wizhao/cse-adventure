# class handling Backpack methods and attributes

from item import Item

class Backpack(object):
    # Backpack class

    def __init__(self):
        # initialize object in backpack class
        self.itemLimit = 12
        ray_gun = Item('Ray Gun', 'Revive me!', 'weapon',"raygun.png")
        translator = Item('Dolphin Translator', 'Used to speak with your undersea mammal friends', 'tool',"translator.png")
        lettuce = Item('Lettuce', 'Number 15, Burger King Foot Lettuce. The last thing you want in your Burger King burger is someone\'s foot fungus, but apparently, it might be what you get.', 'food',"lettuce.png")
        daniel = Item('Steamed Hams and Macaroni', 'At this time of year, at this time day, in this part of the country, localized entirely inside your kitchen', 'food',"daniel.png")
        bone_pick = Item('Bone Pick', 'I am a dwarf, and I\'m digging a hole.', 'tool',"pick.png")
        trident = Item('Trident', 'From the hands of Triton himself, it glows with St. Elmo\'s fire', 'weapon',"trident.png")
        crossbow = Item('Crossbow', 'The layman\'s sniper rifle', 'weapon',"crossbow.png")
        key = Item('Key', 'It looks very complicated, and it\'s intricate almost to a microscopic level. Whoever left this in Dino World did not come from there.', 'tool',"key.png")
        photo = Item('Jisoo Photo', 'A photo of a beautiful Korean Popstar', 'tool',"jisoo.png")
        gravy = Item('Gravy', 'Cookin\' with your mom in the kitchen, makin\' blueberry muffins.', 'food',"gravy.png")
        mms = Item('M&Ms', 'Uhh...summa lumma dooma lama you assumin\' imma human', 'food',"mms.png")
        parka = Item('Parka', 'Protects you from the cold frost', 'tool',"parka.png")
        coal = Item('Coal', 'It might do something if you believe in it', 'tool',"coal.png")
        spam = Item('Spam', 'Nothing satisfies you more than the meat of your fallen brethren', 'food',"spam.png")
        skull = Item('Skull', 'A massive T-Rex skull, good for decorating your car', 'important',"skull.png")
        uranium = Item('Uranium', 'A green glowy stick', 'important',"uranium.png")
        grenade = Item('Grenades', 'Kablam!', 'important',"grenades.png")
        necklace = Item('Seashell Necklace', 'Makes the wearer instantly beautiful', 'important',"necklace.png")
        device = Item('Deep-sea Diving Device', 'Helps get to those tough to reach places!', 'important',"device.png")
        medicine = Item('Herbal Medicine', 'Good for the heart and soul' , 'important',"medicine.png")
        yellow_crystal = Item('Yellow Crystal', 'Powers your portal gun. From the Post Apocalyptic World' , 'crystal', 'yellow.png')
        blue_crystal = Item('Blue Crystal', 'Powers your portal gun. From Atlantis.', 'crystal', 'blue.png')
        green_crystal = Item('Green Crystal', 'Powers your portal gun. From the Dino World.', 'crystal', 'green.png')
        red_crystal = Item('Red Crystal', 'Powers your portal gun. From the War World', 'crystal', 'red.png')
        purple_crystal = Item('Purple Crystal', 'Powers your portal gun. From Ice World', 'crystal', 'purple.png')
        orange_crystal = Item('Orange Crystal', 'Powers your portal gun. From the future.', 'crystal', 'orange.png')
        tank = Item('Oxygen Tank', 'Lets you breathe underwater', 'tool', 'tank.png')
        tendies = Item("Chicken Tendies","A 4-pack of chicken tenders. It reminds you of your past school lunches.","food","tendies.png")
        rifle = Item("Rifle","A wooden, bolt-action rifle. Battle-Scarred quality.","weapon","rifle.png")
        mre = Item("MRE","Meal, ready-to-eat. Doesn't taste very good, but at least it won't spoil.","food","mre.png")
        shovel = Item("Shovel","A foldable shovel.","tool","shovel.png")
        card = Item("ID Card","A government ID card, used for top-level access.","tool","card.png")
        rock = Item("Rock","A mossy rock with some strange carvings on it. It says 01000101.","tool","rock.png")
        cube = Item("Ice Cube","A frozen block of Mystic Water. Tastes funny.","tool","cube.png")
        spear = Item("Ceremonial Spear","A decorated Inuit weapon, destined to kill 'The Lurker,' according to myth.","weapon","spear.png")
        fruit = Item("Fruit","A strange fruit, picked from a strange tree. Strange.","food","fruit.png")
        fry = Item("Fry", "Yum, seat fries", "food", "fry.png")
        sfs = Item("Shark Fin Soup", 'Cruel, but delicious', "food", "sfs.png")
        soylent = Item('Soylent', 'A day\'s meal in one cup', 'food', 'soylent.png')


        self.item_list = {ray_gun.name: ray_gun,
                            translator.name: translator, lettuce.name: lettuce,
                            daniel.name: daniel,
                            bone_pick.name: bone_pick, trident.name:
                            trident, crossbow.name: crossbow, key.name: key, photo.name: photo, gravy.name: gravy,
                            mms.name: mms,
                            parka.name: parka, coal.name: coal,
                            spam.name: spam, skull.name: skull, uranium.name: uranium,
                            grenade.name: grenade, necklace.name: necklace, device.name: device,
                            medicine.name: medicine, yellow_crystal.name: yellow_crystal,
                            blue_crystal.name: blue_crystal, green_crystal.name: green_crystal,
                            red_crystal.name: red_crystal, purple_crystal.name: purple_crystal,
                            orange_crystal.name: orange_crystal, tank.name: tank, tendies.name: tendies,
                            rifle.name: rifle, mre.name: mre, shovel.name: shovel, card.name: card,
                            rock.name: rock, cube.name: cube, spear.name: spear, fruit.name: fruit,
                            fry.name: fry, sfs.name: sfs, soylent.name: soylent}
        self.contents = {}
        self.storage = {}

    def add(self, name):
        # add item to backpack
        self.contents[name] = self.item_list[name]

    def remove(self, name):
        # remove item from backpack
        self.contents.pop(name)

    def add_to_storage(self,name):
        self.storage[name] = self.item_list[name]

    def put_in_storage(self, name):
        # put item from backpack in storage
        if name in self.contents:
            self.contents.pop(name)
            self.storage[name] = self.item_list[name]

    def get_from_storage(self, name):
        # get item from storage
        if name in self.storage:
            self.storage.pop(name)
            self.contents[name] = self.item_list[name]

    def get_items(self, category):
        # get lsit of items from backpack based on category
        names = []
        for key, value in self.contents.iteritems():
            if value.ilk == category:
                names.append(key)
        return names

    def get_items_storage(self, category):
        # get lsit of items from storage based on category
        names = []
        for key, value in self.storage.iteritems():
            if value.ilk == category:
                names.append(key)
        return names

    def has(self, name):
        # checks if item is in backpack
        if name in self.contents:
            return True
        return False

    def get_item(self,name):
        # get specific item from backpack
        if name in self.contents:
            return self.contents[name]
        else:
            return Item()
