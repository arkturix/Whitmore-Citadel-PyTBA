from citadel.common.area import Area


class StartingArea(Area):

    def __init__(self, name: str = "Starting Area", terrain: str = "Meadow", description: str = None):
        super().__init__(name, terrain=terrain, description=description)
