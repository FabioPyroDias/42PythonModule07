from ex3.GameStrategy import GameStrategy


class AgressiveStrategy(GameStrategy):
    def execute_turn(self, hand, battlefield) -> dict:
        pass

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets) -> list:
        pass
