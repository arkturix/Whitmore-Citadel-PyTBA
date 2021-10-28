"""Inventory class"""
from citadel.common import weapons, armors, potions
from citadel.common.exceptions import ItemNotInInventory, UnequippableItem


class Inventory:

    def __init__(self):
        starting_armor = armors.Cloth()
        starting_weapon = weapons.ShortSword()
        starting_potion = potions.Healing()
        # Contents is a dict with keys as items
        self.contents = {starting_armor: 1, starting_weapon: 1, starting_potion: 3}
        self.equipped = {
            'Armor': starting_armor,
            'Weapon': starting_weapon
        }

    def __add__(self, item):
        """Add item to inventory"""
        if self._inventory_contains(item):
            self.contents[item] += 1
        else:
            self.contents[item] = 1

    def __sub__(self, item):
        """Remove item from inventory"""
        if self._inventory_contains(item):
            if self.contents[item] > 1:
                self.contents[item] -= 1
            else:
                del self.contents[item]
        else:
            raise ItemNotInInventory(item)

    def _inventory_contains(self, item: object) -> bool:
        """Test if item is in inventory already"""
        return item in self.contents.keys()

    def equip_item(self, item):
        """Equip weapons or armor"""
        if item in [i['item'] for i in self.contents]:
            if type(item) is armors.Armor:
                self.equipped['Armor'] = item
            elif type(item) is weapons.Weapon:
                self.equipped['Weapon'] = item
            else:
                raise UnequippableItem(item)
        else:
            raise ItemNotInInventory(item)

