from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 damage: int, defense: int, health: int,
                 combat_type: str, mana: int):
        super().__init__(name, cost, rarity)
        if damage < 0:
            raise ValueError("Damage cannot be negative")
        self.damage = damage
        if defense < 0:
            raise ValueError("Defense cannot be negative")
        self.defense = defense
        if health <= 0:
            raise ValueError("Health needs to be positive (> 0)")
        self.health = health
        if combat_type is None:
            raise ValueError("combat_type cannot be None")
        if not (combat_type == "melee" or combat_type == "ranged"
                or combat_type == "magical"):
            raise ValueError("effect_type needs to be 'melee', 'ranged', "
                             "or 'magical'")
        self.combat_type = combat_type
        if mana < 0:
            raise ValueError("Mana cannot be negative")
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": "Elite unit summoned to battlefield"}

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": "Elite", "damage": self.damage,
                     "defense": self.defense, "health": self.health})
        return info

    def is_playable(self, available_mana: int) -> bool:
        return super().is_playable(available_mana)

    def attack(self, target) -> dict:
        if not isinstance(target, (CreatureCard, "EliteCard")):
            raise ValueError("Attack: target must be either CreatureCard"
                             "or EliteCard")
        return {"attacker": self.name, "target": target.name,
                "damage": self.damage, "combat_type": self.combat_type}

    def defend(self, incoming_damage: int) -> dict:
        if incoming_damage < 0:
            raise ValueError("Defend: incoming_damage cannot be negative")
        if incoming_damage >= 0:
            damage_taken = self.defense - incoming_damage
            if damage_taken < 0:
                self.health += damage_taken
        return {"defender": self.name, "damage_taken": incoming_damage,
                "damage_blocked": self.damage, "still_alive": self.health > 0}

    def get_combat_stats(self) -> dict:
        return {"attack": self.damage, "defense": self.defense,
                "health": self.health, "combat_type": self.combat_type}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if not spell_name:
            raise ValueError("Cast Spell: spell_name cannot be None")
        if not targets:
            raise ValueError("Cast Spell: targets cannot be None")
        if len(targets) == 0:
            raise ValueError("Cast Spell: targets cannot be empty")
        for target in targets:
            if not isinstance(target, (CreatureCard, "EliteCard")):
                raise ValueError("Cast Spell: targets must have either "
                                 "CreatureCards or EliteCards")
        target_names = [target.name for target in targets]
        for target in targets:
            self.attack(target)
        self.mana -= 4
        return {"caster": self.name, "spell": spell_name,
                "targets": target_names, "mana_used": 4}

    def channel_mana(self, amount: int) -> dict:
        if amount <= 0:
            raise ValueError("Channel Mana: amount needs to be "
                             "positive (> 0)")
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> dict:
        return {"mana": self.mana}
