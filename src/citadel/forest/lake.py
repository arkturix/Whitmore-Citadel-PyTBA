from citadel.common.area import Area


class Lake(Area):

    def __init__(self, name: str = "Hidden Lake", terrain: str = "Forest", description: str = None):
        super().__init__(name, terrain=terrain, description=description)
