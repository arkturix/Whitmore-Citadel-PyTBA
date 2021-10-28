"""Common potions classes"""


class Potion:
    """Base class for potions"""

    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

    def __hash__(self) -> int:
        return hash((self.name, self.level))

    def __eq__(self, o: object) -> bool:
        return (self.name, self.level) == (o.name, o.level)

    def __str__(self) -> str:
        return self.name


class Healing(Potion):

    def __init__(self, name: str = "Healing Potion", level: int = 5):
        super().__init__(name, level)


class LargeHealing(Potion):

    def __init__(self, name: str = "Large Healing Potion", level: int = 10):
        super().__init__(name, level)


class GreaterHealing(Potion):

    def __init__(self, name: str = "Greater Healing Potion", level: int = 15):
        super().__init__(name, level)


class MassiveHealing(Potion):

    def __init__(self, name: str = "Massive Healing Potion", level: int = 20):
        super().__init__(name, level)
