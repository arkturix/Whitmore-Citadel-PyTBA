"""Common class for all of the monsters."""

class Monster:

    def __init__(self, name: str, level: int = 0, hit_points: int = 0, loot: list = []):
        self.name = name
        self.level = level
        self.hit_points = hit_points
        self.loot = loot
        self.attack_power = 0
        self.armor_class = 0

    def __str__(self):
        return self.name

    def __sub__(self, amount):
        """Remove hit points when subtracting from monster object"""
        remaining_hp = self.hit_points - amount
        self.hit_points = remaining_hp if remaining_hp >=0 else 0

    def attack(self):
        """Attack the player"""
        pass

    def loot_monster(self):
        """Get loot from the monster"""
        if self.hit_points != 0:
            return self.attack()
        if not self.loot:
            return "Nothing"
        else:
            return self.loot.pop()
