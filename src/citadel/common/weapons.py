"""Common class for all Weapons"""
import random


class Weapon:

    def __init__(self, name: str, level: int = 1, attack_power: int = 1):
        self.name = name
        self.level = level
        self.attack_power = attack_power

    def __str__(self):
        return self.name


class ShortSword(Weapon):

    def __init__(self, name="Short Sword"):
        super().__init__(name, attack_power=random.randint(1,5))


class LongSword(Weapon):

    def __init__(self, name="Long Sword", level=5):
        level = random.randint(level-2, level+2)
        attack_power = level + random.randint(-2, 2)
        super().__init__(name, level=level, attack_power=attack_power)


class TwoHandedSword(Weapon):

    def __init__(self, name="Two-handed Sword", level=10):
        level = random.randint(level-3, level+3)
        attack_power = level + random.randint(-3, 3)
        super().__init__(name, level=level, attack_power=attack_power)


class Claymore(Weapon):

    def __init__(self, name="Claymore", level=15):
        level = random.randint(level, 20)
        attack_power = random.randint(level, 20)
        super().__init__(name, level=level, attack_power=attack_power)


class DragonsBane(Weapon):

    def __init__(self, name="Dragons' Bane Sword", level=20, attack_power=20):
        super().__init__(name, level=level, attack_power=attack_power)
