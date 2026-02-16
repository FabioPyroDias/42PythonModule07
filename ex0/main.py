from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    print()
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()
    print("CreatureCard Info:")
    fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, "Creature", 7, 5)
    print(fire_dragon.get_card_info())
    print()
    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(6)}")
    print(f"Play result: {fire_dragon.play(None)}")
    print()
    goblin_warrior = CreatureCard("Goblin Warrior", 2,
                                  Rarity.COMMON.value, "Creature", 2, 1)
    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")
    print()
    print("Testing insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(3)}")
    print()
    print("Abstract pattern successfully demonstrated!")
