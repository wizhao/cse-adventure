from item import Item

class Backpack(object):
    def __init__(self):
        portal_gun = Item('portal gun', None, 'weapon')
        ray_gun = Item('ray gun', None, 'weapon')
        translator = Item('dolphin translator', None, 'tool')
        lettuce = Item('lettuce', None, 'food')
        daniel = Item('steamed hams and macaroni', None, 'food')
        icicle = Item('icicle', None, 'tool')
        bone_pick = Item('bone pick', None, 'tool')
        grenade = Item('grenade', None, 'weapon')
        shotgun = Item('sawed-off shotgun', None, 'weapon')
        tactical_shotgun = Item('purple tactical shotgun', None, 'weapon')
        trident = Item('trident', None, 'weapon')
        crossbow = Item('crossbow', None, 'weapon', 'long-range')
        key = Item('key', None, 'tool')
        note = Item('note w/ password', None, 'tool')
        photo = Item('jisoo photo', None, 'tool')
        gravy = Item('gravy', None, 'food')
        mms = Item('M&Ms', None, 'food')
        armor = Item('armor', None, 'weapon')
        skis = Item('skis', None, 'tool')
        parkas = Item('parkas', None, 'tool')
        coal = Item('coal', None, 'tool')
        human_meat = Item('human meat', None, 'food')

        self.item_list = {portal_gun.name: portal_gun, ray_gun.name: ray_gun,
                            translator.name: translator, lettuce.name: lettuce,
                            daniel.name: daniel, icicle.name: icicle,
                            bone_pick.name: bone_pick, grenade.name: grenade,
                            shotgun.name: shotgun, tactical_shotgun.name:
                            tactical_shotgun, trident.name: trident,
                            crossbow.name: crossbow, key.name: key, note.name:
                            note, photo.name: photo, gravy.name: gravy,
                            mms.name: mms, armor.name: armor, skis.name: skis,
                            parkas.name: parkas, coal.name: coal,
                            human_meat.name: human_meat}
        self.contents = {}

    def add(self, name):
        self.contents[name] = self.item_list[name]

    def remove(self, name):
        self.contents.pop(name)

    def get_items(self, type):
        names = []
        for key, value in self.contents.iteritems():
            if value.ilk == 'weapon':
                names.append(key)
        return names

b = Backpack()
b.add('key')
b.add('armor')
b.add('coal')
b.add('crossbow')
print b.get_items('weapon')
