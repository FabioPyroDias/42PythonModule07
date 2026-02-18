from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard


if __name__ == "__main__":
    print()
    print("=== DataDeck Ability System ===")
    print()
    print("EliteCard capabilities:")
    card_methods = ["play", "get_card_info", "is_playable"]
    print(f"- Card: {card_methods}")
    combatable_methods = ["attack", "defend", "get_combat_stats"]
    print(f"- Combatable: {combatable_methods}")
    magical_methods = ["cast_spell", "channel_mana", "get_magic_stats"]
    print(f"- Magical: {magical_methods}")
    print()
    print("Playing Arcane Warrior (Elite Card):")
    card = EliteCard("Arcane Warrior", 9, Rarity.LEGENDARY.value, "Elite",
                     5, 3, 10, "melee", 8)
    print()
    print("Combat phase:")
    enemy = CreatureCard("Enemy", 2, Rarity.COMMON.value, "Creature", 2, 8)
    print(f"Attack result: {card.attack(enemy)}")
    print(f"Defense result: {card.defend(enemy.attack)}")
    print()
    print("Magic phase:")
    enemy1 = CreatureCard("Enemy1", 2, Rarity.COMMON.value, "Creature", 2, 8)
    enemy2 = CreatureCard("Enemy2", 2, Rarity.COMMON.value, "Creature", 2, 8)
    print(f"Spell cast: {card.cast_spell('Fireball', [enemy1, enemy2])}")
    print(f"Mana channel: {card.channel_mana(3)}")
    print()
    print("Multiple interface implementation sucessful!")
