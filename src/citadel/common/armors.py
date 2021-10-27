"""Common class for all armor"""

class Armor:

    def __init__(self, name: str, level: int = 1, armor_class: int = 1):
        self.name = name
        self.level = level
        self.armor_class = armor_class

    def __str__(self):
        return self.name
