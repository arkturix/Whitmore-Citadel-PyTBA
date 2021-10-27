"""Common class for all of the various areas (stages)."""

class Area:

    def __init__(self, name: str, terrain: str = None, description: str = None):
        self.name = name
        self.terrain = terrain or "Desert"
        self.description = description or "!!! Missing description !!!"

    def __str__(self):
        return self.name

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
