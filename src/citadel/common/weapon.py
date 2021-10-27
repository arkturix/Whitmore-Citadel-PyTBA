"""Common class for all Weapons"""

class Weapon:

    def __init__(self, name: str, level: int = 1, attack_power: int = 1):
        self.name = name
        self.level = level
        self.attack_power = attack_power

    def __str__(self):
        return self.name
