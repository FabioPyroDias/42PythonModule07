from ex0 import Card
from enum import Enum


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": "Spell", "effect": self.effect_type})
        return info

    def resolve_effect(self, targets: list) -> dict:
        pass
