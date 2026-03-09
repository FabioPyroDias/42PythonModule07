from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if name is None:
            raise ValueError("Name cannot be None")
        if len(name) == 0:
            raise ValueError("Name needs at least 1 character")
        self.name = name
        if cost < 0:
            raise ValueError("Cost cannot be negative")
        self.cost = cost
        if rarity is None:
            raise ValueError("Rarity cannot be None")
        if not (rarity == "Common" or rarity == "Uncommon" or rarity == "Rare"
                or rarity == "Legendary"):
            raise ValueError("Rarity needs to be Common, Uncommon, Rare "
                             "or Legendary")
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
