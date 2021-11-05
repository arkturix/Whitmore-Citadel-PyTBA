from citadel.common.area import Area


class Stables(Area):

    def __init__(self, name: str = "Stables", terrain: str = "Castle", description: str = None):
        super().__init__(name, terrain=terrain, description=description)
