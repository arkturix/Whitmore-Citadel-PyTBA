from citadel.common.area import Area


class Grotto(Area):

    def __init__(self, name: str = "Grotto", terrain: str = "Cave", description: str = None):
        super().__init__(name, terrain=terrain, description=description)
