from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 type: str, damage: int, defense: int, health: int,
                 combat_type: str, mana: int):
        super().__init__(name, cost, rarity)
        self.type = type
        self.damage = damage
        self.defense = defense
        self.health = health
        self.combat_type = combat_type
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        info = super().play(None)
        info.update({"effect": "Elite unit summoned to battlefield"})
        return info

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": self.type, "damage": self.damage,
                     "defense": self.defense, "health": self.health})
        return info

    def is_playable(self, available_mana: int) -> bool:
        return super().is_playable()

    def attack(self, target) -> dict:
        return {"attacker": self.name, "target": target.name,
                "damage": self.damage, "combat_type": self.combat_type}

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = self.defense - incoming_damage
        if damage_taken < 0:
            self.health += damage_taken
        alive = True
        if self.health <= 0:
            alive = False
        return {"defender": self.name, "damage_taken": incoming_damage,
                "damage_blocked": self.damage, "still_alive": alive}

    def get_combat_stats(self) -> dict:
        pass

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        target_names = [target.name for target in targets]
        return {"caster": self.name, "spell": spell_name,
                "targets": target_names, "mana_used": 4}

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> dict:
        pass
