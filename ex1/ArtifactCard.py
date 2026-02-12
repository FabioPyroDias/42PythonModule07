from ex0 import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": "Artifact", "durability": self.durability,
                    "effect": self.effect})
        return info

    def activate_ability(self) -> dict:
        pass
