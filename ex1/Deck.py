import random
from ex0 import Card


class Deck:
    def __init__(self):
        self.__cards = []

    def add_card(self, card: Card) -> None:
        if card is None:
            return
        self.__cards.append(card)

    def remove_card(self, card_name: str) -> None:
        if card_name is None or len(card_name) == 0 or len(self.__cards) == 0:
            return
        for card in self.__cards:
            if card.get_card_info()["name"] == card_name:
                self.__cards.remove(card_name)

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

    def draw_card(self) -> Card:
        if len(self.__cards) == 0:
            return None
        return self.__cards.pop(0)

    def get_deck_stats(self) -> dict:
        stats = {"total_cards": len(self.__cards), "creatures": 0,
                 "spells": 0, "artifacts": 0, "avg_cost": 0}
        if len(self.__cards) == 0:
            return stats
        type_creature = 0
        type_spell = 0
        type_artifact = 0
        cost = 0
        for card in self.__cards:
            card_info = card.get_card_info()
            cost += card_info["cost"]
            if card_info["type"] == "Creature":
                type_creature += 1
            elif card_info["type"] == "Spell":
                type_spell += 1
            else:
                type_artifact += 1
        stats["creatures"] = type_creature
        stats["spells"] = type_spell
        stats["artifacts"] = type_artifact
        stats["avg_cost"] = int(cost / len(self.__cards))
        return stats
