"""Common class for all of the various areas (stages)."""

class Area:

    def __init__(self, name: str, terrain: str = None, description: str = None):
        self.name = name
        self.terrain = terrain or "Desert"
        self.description = description or "!!! Missing description !!!"
        self.monsters = {}  # Dict keys will be monster objects and values will be qty
        self.treasure = None
        if self._monsters_appear():
            self._get_monsters()
        if self._treasure_appears():
            self._get_treasure()

    def __str__(self):
        return self.name

    def __add__(self, add_desc):
        self.description += "\n" + add_desc

    def search(self):
        """Search the area"""
        # TODO: Create hidden paths attributes
        self.treasure['hidden'] = False
        return self.treasure.describe()

    def _monsters_appear(self):
        """Determine if monsters appear on entering area"""
        pass

    def _get_monsters(self, monster_obj):
        """Generate a number of monsters"""
        pass

    def _treasure_appears(self):
        """Determine if treasure will appear"""
        pass

    def _get_treasure(self, treasure_obj):
        """Generate the treasure"""
        pass
