"""Player class"""
from .inventory import Inventory


class Player:

    def __init__(self):
        self.level = 1
        self.hp = 10
        self.backpack = Inventory()

    def __add__(self, amount: int):
        """Add to players hit points"""
        self.hp += amount

    def __sub__(self, amount: int):
        """Subtract from players hit points"""
        self.hp -= amount

    def level_up(self):
        """Increase level and hit points when leveling up"""
        

    def travel(self, direction):
        """Travel in a given direction"""
        pass

    def search_area(self):
        """Search the area for treasure and paths"""
        pass

    def equip(self, item):
        """Equip armor or weapon from inventory"""
        pass

    def attack(self, monster):
        """Attack a monster"""
        pass
