from item import Item

class Backpack(object):
    def __init__(self):
        portal_gun = Item('portal gun')
        ray_gun = Item('ray gun')
        translator = Item('dolphin translator')
        lettuce = Item('lettuce')
        daniel = Item('steamed hams and macaroni')
        icicle = Item('icicle')
        bone_pick = Item('bone pick')
        grenade = Item('grenade')
        shotgun = Item('sawed-off shotgun')
        tactical_shotgun = Item('purple tactical shotgun')
        trident = Item('trident')
        crossbow = Item('crossbow')
        key = Item('key')
        note = Item('note w/ password')
        photo = Item('jisoo photo')
        gravy = Item('gravy')
        mms = Item('M&Ms')
        armor = Item('armor')
        skis = Item('skis')
        parkas = Item('parkas')
        coal = Item('coal')
        human_meat = Item('human meat')

b = Backpack()
human_meat = Item('human meat', 'yeet', 'long')
print human_meat.name, human_meat.description, human_meat.ilk, human_meat.subilk
