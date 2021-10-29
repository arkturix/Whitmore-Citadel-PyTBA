"""Player class"""
from .inventory import Inventory


class Player:

    def __init__(self):
        self.backpack = Inventory()

    def travel(self, direction):
        pass

    def search_area(self):
        pass

    def equip(self, item):
        pass

    def attack(self, monster):
        pass
