from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self) -> None:
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards.update({card.get_card_info()["card_id"]: card})

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.matches_played += 1
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        card1_attack_info = card1.attack(card2)["damage_dealt"]
        card2_attack_info = card2.attack(card1)["damage_dealt"]
        if card1_attack_info >= card2_attack_info:
            card1.update_wins(card1.get_rank_info()["wins"] + 1)
            card2.update_losses(card2.get_rank_info()["losses"] + 1)
            return {"winner": card1.name, "loser": card2.name,
                    "winner_rating": card1.calculate_rating(),
                    "loser_rating": card2.calculate_rating()}
        else:
            card2.update_wins(card2.get_rank_info()["wins"] + 1)
            card1.update_losses(card1.get_rank_info()["losses"] + 1)
            return {"winner": card2.name, "loser": card1.name,
                    "winner_rating": card2.calculate_rating(),
                    "loser_rating": card1.calculate_rating()}

    def get_leaderboard(self) -> list:
        current_card = 0
        cards = list(self.cards.values())
        while current_card < len(cards) - 1:
            if (cards[current_card + 1].get_rank_info()["rating"] >
                    cards[current_card].get_rank_info()["rating"]):
                temp = cards[current_card]
                cards[current_card] = cards[current_card + 1]
                cards[current_card + 1] = temp
                current_card -= 1
                if current_card < 0:
                    current_card = 0
            else:
                current_card += 1
        return cards

    def generate_tournament_report(self) -> dict:
        average = 0
        if len(self.cards) != 0:
            for card in list(self.cards.values()):
                average += card.get_rank_info()["rating"]
            average = int(average / len(self.cards))
        return {"total_cards": len(self.cards),
                "matches_played": self.matches_played,
                "avg_rating": average, "plarform_status": "active"}
