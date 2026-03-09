from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AgressiveStrategy
from ex3.GameEngine import GameEngine


if __name__ == "__main__":
    try:
        print()
        print("=== DataDeck Game Engine ===")
        print()
        print("Configuring Fantasy Card Game...")
        """ try: """
        factory = FantasyCardFactory()
        strategy = AgressiveStrategy()
        game = GameEngine()
        game.configure_engine(factory, strategy)
        print(f"Factory: {type(factory).__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Available  types: {factory.get_supported_types()}")
        print()
        print("Simulating aggressive turn...")
        game.simulate_turn()
        print()
        print("Game Report:")
        print(f"{game.get_engine_status()}")
        print()
        print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
    except ValueError as error:
        print(error)
    except ImportError as error:
        print("Somehow, ImportError appeared...")
        print(error)
    except TypeError as error:
        print("TypeError: Just read the trace and correct it...")
        print(error)