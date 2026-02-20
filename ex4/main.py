from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    print("")
    print("=== Datadeck Tournament Platform")
    tournament = TournamentPlatform()
    print()
    print("Registering Tournament Cards...")
    print()
    card1 = TournamentCard("Fire Dragon", 7, "Legendary",
                           "dragon_001", 7, 2, 5, 1200)
    card1_info = card1.get_rank_info()
    tournament.register_card(card1)
    print(f"{card1.name} (ID: {card1_info['card_id']}):")
    print(f"- Interfaces: {card1_info['interfaces']}")
    print(f"- Rating: {card1_info['rating']}")
    print(f"- Record: {card1_info['wins']}-{card1_info['losses']}")
    print()
    card2 = TournamentCard("Ice Wizard", 4, "Rare",
                           "wizard_001", 3, 1, 4, 1150)
    card2_info = card2.get_rank_info()
    tournament.register_card(card2)
    print(f"{card2.name} (ID: {card2_info['card_id']}):")
    print(f"- Interfaces: {card2_info['interfaces']}")
    print(f"- Rating: {card2_info['rating']}")
    print(f"- Record: {card2_info['wins']}-{card2_info['losses']}")
    print()
    print("Creating tournament match...")
    result = tournament.create_match(
        card1_info['card_id'], card2_info['card_id'])
    print(f"Match result: {result}")
    print()
    print("Tournament Leaderboard:")
    leaderboard = tournament.get_leaderboard()
    position = 0
    while position < len(leaderboard):
        card = leaderboard[position]
        card_info = card.get_rank_info()
        print(f"{position + 1}. {card.name} - Rating: {card_info['rating']} "
              f"({card_info['wins']}-{card_info['losses']})")
        position += 1
    print()
    print("Platform Report:")
    print(tournament.generate_tournament_report())
    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
