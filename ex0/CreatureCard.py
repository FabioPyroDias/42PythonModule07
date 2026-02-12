from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": "Creature", "attack": self.attack,
                     "health": self.health})
        return info

    def play(self, game_state: dict) -> dict:
        info = super().play(game_state)
        info.update({"effect": "Creature summoned to battlefield"})
        return info

    def attack_target(self, target) -> dict:
        return {"attacker": self.name, "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": target.health <= 0}
