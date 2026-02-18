from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AgressiveStrategy


if __name__ == "__main__":
    print()
    print("=== DataDeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    fantasy_card_factory = FantasyCardFactory()
    print("Strategy: AggressiveStrategy")
    aggresive_strategy = AgressiveStrategy()
    print(f"Available types: {fantasy_card_factory.get_supported_types()}")
    print()
    print("Simulating aggressive turn...")
    deck = list(fantasy_card_factory.create_themed_deck(3).values())
    hand = []
    for cards in deck:
        for card in cards:
            hand.append(card)
    hand_info = []
    for card in hand:
        hand_info.append(f"{card.name} ({card.cost})")
    print(f"Hand: {hand_info}")
    print()
    print("Turn execution:")
    print(f"Strategy: {aggresive_strategy.get_strategy_name()}")




"""
Actions: {'cards_played': ['Goblin Warrior', 'Lightning Bolt'],
'mana_used': 5, 'targets_attacked': ['Enemy Player'],
'damage_dealt': 8}
Game Report:
{'turns_simulated': 1, 'strategy_used': 'AggressiveStrategy',
'total_damage': 8, 'cards_created': 3}
Abstract Factory + Strategy Pattern: Maximum flexibility achieved! """