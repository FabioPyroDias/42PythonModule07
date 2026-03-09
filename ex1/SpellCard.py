from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
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
        if effect_type is None:
            raise ValueError("effect_type needs cannot be None")
        if not (effect_type == "damage" or effect_type == "heal"
                or effect_type == "buff" or effect_type == "debuff"):
            raise ValueError("effect_type needs to be 'damage', 'heal', "
                             "'buff' or 'debuff'")
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        info = {"card_played": self.name, "mana_used": self.cost}
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
        if not targets:
            return {"No targets for spell effect"}
        for target in targets:
            if not isinstance(target, CreatureCard):
                raise ValueError("Target list should only contain "
                                 "Creature Cards")
        if self.effect_type == EffectType.DAMAGE.value:
            for target in targets:
                target.health -= self.cost
        elif self.effect_type == EffectType.HEAL.value:
            for target in targets:
                target.health += self.cost
        elif self.effect_type == EffectType.BUFF.value:
            for target in targets:
                target.attack += self.cost
        elif self.effect_type == EffectType.DEBUFF.value:
            for target in targets:
                target.attack -= self.cost
                if target.attack < 0:
                    target.attack = 0
        return {"targets": targets, "effect": self.effect_type,
                "value": self.cost}
