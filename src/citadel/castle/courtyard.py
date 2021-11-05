from citadel.common.area import Area


class Courtyard(Area):

    def __init__(self, name: str = "Courtyard", terrain: str = "Castle", description: str = None):
        super().__init__(name, terrain=terrain, description=description)
