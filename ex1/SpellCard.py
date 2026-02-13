from ex0.Card import Card
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
        info = super().play(None)
        if self.effect_type == EffectType.DAMAGE.value:
            info.update({"effect": f"Deal {self.cost} damage to target"})
        elif self.effect_type == EffectType.HEAL.value:
            info.update({"effect": f"Heal {self.cost} health to target"})
        elif self.effect_type == EffectType.BUFF.value:
            info.update({"effect": f"Buff {self.cost} damage to target"})
        elif self.effect_type == EffectType.DEBUFF.value:
            info.update({"effect": f"Debuff {self.cost} damage to target"})
        return info

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": "Spell", "effect": self.effect_type})
        return info

    def resolve_effect(self, targets: list) -> dict:
        return {"targets": targets, "effect": self.effect_type,
                "value": self.cost}
