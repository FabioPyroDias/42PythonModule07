from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = 0
        self.health = 0
        if attack <= 0:
            raise ValueError("Attack needs to be positive (> 0)")
        self.attack = attack
        if health <= 0:
            raise ValueError("Health needs to be positive (> 0)")
        self.health = health

    def play(self, game_state: dict) -> dict:
        info = {"card_played": self.name, "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"}
        return info

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": "Creature", "attack": self.attack,
                     "health": self.health})
        return info

    def attack_target(self, target: "CreatureCard") -> dict:
        if not target:
            raise ValueError("Target not defined")
        target.health -= self.attack
        return {"attacker": self.name, "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": target.health <= 0}
