from citadel.common.area import Area


class Tower(Area):

    def __init__(self, name: str = "Tower", terrain: str = "Castle", description: str = None):
        super().__init__(name, terrain=terrain, description=description)
