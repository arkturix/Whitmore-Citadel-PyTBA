"""Common class for all treasure."""

class Treasure:

    def __init__(self, name: str, contents: list = []):
        self.name = name
        self.contents = contents
        if not self.contents:
            self._get_contents()

    def __str__(self):
        return self.name

    def _get_contents(self):
        """Generate the contents of the treasure"""
        pass

    def describe(self):
        """Describe the contents of the treasure"""
        pass

    def open(self):
        """Open the treasure container"""
        return self.contents

    def take(self):
        """Remove the treasure from the container"""
        yield self.contents
        self.contents = []
