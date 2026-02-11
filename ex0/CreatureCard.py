from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        pass

    def attack_target(self, target) -> dict:
        pass
