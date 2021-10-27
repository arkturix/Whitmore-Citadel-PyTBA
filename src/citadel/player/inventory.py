"""Inventory class"""
from citadel.common import weapons, armors
from src.citadel.common.armors import Armor
from src.citadel.common.weapons import Weapon

class Inventory:

    def __init__(self):
        starting_armor = armors.Cloth()
        starting_weapon = weapons.Weapon()  # TODO: Finish weapons class
        self.contents = [starting_armor]
        self.equipped = {
            'Armor': starting_armor,
            'Weapon': starting_weapon
        }

    def __add__(self, item):
        self.contents.append(item)

    def __sub__(self, item):
        if item in self.contents:
            self.contents.pop(item)
        else:
            pass  # TODO: Figure out what to do with trying to remove items that aren't in inventory

    def equip_item(self, item):
        if item in self.contents:
            if type(item) is Armor:
                self.equipped['Armor'] = item
            elif type(item) is Weapon:
                self.equipped['Weapon'] = item
            else:
                pass  # TODO: Handle attempt to equip item that is not equippable
        else:
            pass  # TODO: Handle attempt to equip item that is not in inventory

