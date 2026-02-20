from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 card_id: str, damage: int, defense: int, health: int,
                 base_rating: int):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.damage = damage
        self.defense = defense
        self.health = health
        self.base_rating = base_rating
        self.rating = base_rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        return super().play(game_state)

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"card_id": self.card_id, "damage": self.damage,
                     "defense": self.defense, "health": self.health})
        return info

    def is_playable(self, available_mana: int) -> bool:
        return super().is_playable(available_mana)

    def attack(self, target) -> dict:
        damage_blocked = target.defend(self.damage)["damage_blocked"]
        final_damage = self.damage - damage_blocked
        if final_damage < 0:
            final_damage = 0
        return {"attacker": self.name, "target": target.name,
                "damage_dealt": final_damage,
                "combat_resolved": target.health <= 0}

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = self.defense - incoming_damage
        if damage_taken < 0:
            self.health += damage_taken
        alive = True
        if self.health <= 0:
            alive = False
        return {"defender": self.name, "damage_taken": incoming_damage,
                "damage_blocked": self.damage, "still_alive": alive}

    def get_combat_stats(self) -> dict:
        return {"attack": self.damage, "defense": self.defense,
                "health": self.health}

    def calculate_rating(self) -> int:
        rating_per_match = 16
        self.rating = (self.base_rating +
                       ((self.wins - self.losses) * rating_per_match))
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins = wins

    def update_losses(self, losses: int) -> None:
        self.losses = losses

    def get_rank_info(self) -> dict:
        return {"card_id": self.card_id,
                "interfaces": ["Card", "Combatable", "Rankable"],
                "rating": self.rating,
                "wins": self.wins, "losses": self.losses}
