from citadel.common.area import Area


class Drawbridge(Area):

    def __init__(self, name: str = "Drawbridge", terrain: str = "Forest", description: str = None):
        super().__init__(name, terrain=terrain, description=description)
