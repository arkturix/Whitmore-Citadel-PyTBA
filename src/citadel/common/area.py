"""Common class for all of the various areas (stages) of the game."""

class Area:

    def __init__(self, name, terrain=None, description=None):
        self.name = name
        self.terrain = terrain or "Desert"
        self.description = description or "!!! Missing description !!!"

    def __add__(self, add_desc):
        self.description += "\n" + add_desc

    def search(self):
        pass
    
    class Travel:

        def north(self):
            pass
        
        def east(self):
            pass

        def south(self):
            pass

        def west(self):
            pass
