from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.SpellCard import EffectType
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.__creatures = {
            "dragon": ("Fire Dragon", 5, Rarity.LEGENDARY.value,
                       7, 5),
            "goblin": ("Goblin Warrior", 2, Rarity.COMMON.value,
                       2, 1)
        }
        self.__spells = {
            "fireball": ("Fireball", 4, Rarity.UNCOMMON.value,
                         EffectType.DAMAGE.value)
        }
        self.__artifacts = {
            "mana_ring": ("Mana Crystal", 2, Rarity.COMMON.value,
                          5, "Permanent: +1 mana per turn")
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if (isinstance(name_or_power, str) and
                name_or_power in self.__creatures):
            (name, cost, rarity,
             attack, health) = self.__creatures[name_or_power]
            return CreatureCard(name, cost, rarity, attack, health)
        if isinstance(name_or_power, int):
            for key, value in self.__creatures.items():
                name, cost, rarity, attack, health = value
                if name_or_power == attack:
                    return (CreatureCard(name, cost, rarity,
                                         attack, health))
        if len(self.__creatures) == 0:
            return None
        (name, cost, rarity,
         attack, health) = random.choice(list(self.__creatures.values()))
        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power in self.__spells:
            (name, cost, rarity,
             effect) = self.__spells[name_or_power]
            return SpellCard(name, cost, rarity, effect)
        if isinstance(name_or_power, int):
            for key, value in self.__spells.items():
                name, cost, rarity, effect = value
                if cost == name_or_power:
                    return SpellCard(name, cost, rarity, effect)
        if len(self.__spells.keys()) == 0:
            return None
        (name, cost, rarity,
         effect) = random.choice(list(self.__spells.values()))
        return SpellCard(name, cost, rarity, effect)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if (isinstance(name_or_power, str) and
                name_or_power in self.__artifacts):
            (name, cost, rarity,
             durability, effect) = self.__artifacts[name_or_power]
            return (ArtifactCard(name, cost, rarity,
                                 durability, effect))
        if isinstance(name_or_power, int):
            for key, value in self.__artifacts.items():
                name, cost, rarity, durability, effect = value
                if cost == name_or_power:
                    return (ArtifactCard(name, cost, rarity,
                                         durability, effect))
        if len(self.__artifacts.keys()) == 0:
            return None
        (name, cost, rarity,
         durability, effect) = random.choice(list(self.__artifacts.values()))
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict:
        deck = {
            "creatures": [],
            "spells": [],
            "artifacts": []
        }
        for i in range(size):
            card_type = random.choice(list(deck.keys()))
            if card_type == "creatures":
                deck["creatures"].append(self.create_creature())
            elif card_type == "spells":
                deck["spells"].append(self.create_spell())
            elif card_type == "artifacts":
                deck["artifacts"].append(self.create_artifact())
        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": list(self.__creatures.keys()),
            "spells": list(self.__spells.keys()),
            "artifacts": list(self.__artifacts.keys())
        }
