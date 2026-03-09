from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError("Durability needs to be positive (> 0)")
        self.durability = durability
        if not effect:
            raise ValueError("Effect cannot be None")
        if len(effect) == 0:
            raise ValueError("Effect needs at least 1 character")
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        info = {"card_played": self.name, "mana_used": self.cost,
                "effect": self.effect}
        return info

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": "Artifact", "durability": self.durability,
                    "effect": self.effect})
        return info

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {"status": None}
        result = {
            "effect": self.effect,
            "durability": self.durability
        }
        self.durability -= 1
        return result
