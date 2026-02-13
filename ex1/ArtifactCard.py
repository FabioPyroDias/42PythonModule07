from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        info = super().play(game_state)
        info.update({"effect": self.effect})
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
