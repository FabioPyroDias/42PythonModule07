from ex3.GameStrategy import GameStrategy


class AgressiveStrategy(GameStrategy):
    def execute_turn(self, hand, battlefield):
        return super().execute_turn(hand, battlefield)

    def get_strategy_name(self):
        return super().get_strategy_name()

    def prioritize_targets(self, available_targets):
        return super().prioritize_targets(available_targets)
