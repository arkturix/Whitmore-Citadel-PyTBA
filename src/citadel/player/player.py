"""Player class"""
from .inventory import Inventory


class Player:

    def __init__(self):
        self.backpack = Inventory()
