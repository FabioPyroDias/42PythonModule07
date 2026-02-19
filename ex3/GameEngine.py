from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine():
    def __init__(self):
        self.turns = 0
        self.strategy = None
        self.factory = None
        self.total_damage = 0
        self.cards_created = 0
        self.battlefield = []
        self.hand = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            raise ValueError("Engine must be configured")
        self.turns += 1
        self.cards_created = 3
        if not self.hand:
            deck = self.factory.create_themed_deck(self.cards_created)
            for card_type, cards in deck.items():
                for card in cards:
                    self.hand.append(card)
        print(f"Hand: {[card.name for card in self.hand]}")
        print()
        turn = self.strategy.execute_turn(self.hand, self.battlefield)
        print("Turn execution:")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        self.total_damage += turn["damage_dealt"]
        print(f"Actions: {turn}")
        return turn

    def get_engine_status(self) -> dict:
        strategy_name = None
        if self.strategy is not None:
            strategy_name = self.strategy.get_strategy_name()
        return {
            "turns_simulated": self.turns,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
