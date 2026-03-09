from abc import abstractmethod
from typing import Protocol


class Rankable(Protocol):
    @abstractmethod
    def calculate_rating(self) -> None:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        pass
