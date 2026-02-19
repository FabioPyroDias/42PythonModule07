from typing import Protocol


class Rankable(Protocol):
    def calculate_rating(self) -> None:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_rank_info(self) -> dict:
        pass
