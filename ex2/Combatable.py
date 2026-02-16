from typing import Protocol


class Combatable(Protocol):
    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass
