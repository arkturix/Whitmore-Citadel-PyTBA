"""Battle class"""
from citadel.player.player import Player


class Battle:

    def __init__(self, player: Player, enemies: dict) -> None:
        self.p = player
        self.enemies = enemies
        self._round = 0

    @property
    def round(self):
        return self._round

    def fight(self):
        """Manage fight between player and enemies"""
        pass
