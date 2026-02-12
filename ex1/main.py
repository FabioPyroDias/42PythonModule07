from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.SpellCard import EffectType
from ex1.Deck import Deck


if __name__ == "__main__":
    print()
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5,
                               Rarity.LEGENDARY.value, 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3,
                            Rarity.COMMON.value, EffectType.DAMAGE.value))
    deck.add_card(ArtifactCard("Mana Crystal", 2,
                               Rarity.COMMON.value, 5,
                               "Permanent: +1 mana per turn"))
    print(f"Deck stats: {deck.get_deck_stats()}")
