"""Common class for all armor"""
import random


class Armor:

    def __init__(self, name: str, level: int = 1, armor_class: int = 1):
        self.name = name
        self.level = level
        self.armor_class = armor_class

    def __str__(self):
        return self.name


class Cloth(Armor):

    def __init__(self, name="Cloth Armor"):
        super().__init__(name=name, armor_class=random.randint(1,5))
    

class Leather(Armor):

    def __init__(self, name="Leather Armor", level=5):
        self.level = random.randint(level-2, level+2)
        self.armor_class = self.level + random.randint(-2, 2)
        super().__init__(name, self.level, self.armor_class)


class Scale(Armor):

    def __init__(self, name="Scale Armor", level=10):
        self.level = random.randint(level-3, level+3)
        self.armor_class = self.level + random.randint(-3, 3)
        super().__init__(name, self.level, self.armor_class)


class Plate(Armor):

    def __init__(self, name="Plate Armor", level=15):
        self.level = random.randint(level-5, 20)
        self.armor_class = random.randint(self.level, 20)
        super().__init__(name, self.level, self.armor_class)
