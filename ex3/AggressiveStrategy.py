from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class AgressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        max_mana = 10
        available_mana = max_mana
        damage = 0
        creatures = []
        cards_played = []
        for card in hand:
            if isinstance(card, CreatureCard):
                creatures.append(card)
        if len(creatures) > 0:
            current_creature = 0
            while current_creature < len(creatures) - 1:
                if (creatures[current_creature].cost >
                        creatures[current_creature + 1].cost):
                    temp = creatures[current_creature]
                    creatures[current_creature] = (
                        creatures[current_creature + 1])
                    creatures[current_creature + 1] = temp
                    current_creature -= 1
                    if current_creature < 0:
                        current_creature = 0
                else:
                    current_creature += 1
            current_creature = 0
            cards_to_be_removed = []
            while current_creature < len(creatures):
                if creatures[current_creature].is_playable(available_mana):
                    available_mana -= (
                        creatures[current_creature].get_card_info()["cost"])
                    cards_to_be_removed.append(current_creature)
                    damage += (
                        creatures[current_creature].get_card_info()["attack"])
                current_creature += 1
            removed_card_index = len(cards_to_be_removed) - 1
            while removed_card_index >= 0:
                cards_played.append(
                    creatures.pop(
                        cards_to_be_removed[removed_card_index]).name)
                removed_card_index -= 1
        spells = []
        for card in hand:
            if (isinstance(card, SpellCard) and
                    card.get_card_info()["effect"] == "damage"):
                spells.append(card)
        if len(spells) > 0:
            current_spell = 0
            while current_spell < len(spells) - 1:
                if spells[current_spell].cost > spells[current_spell + 1].cost:
                    temp = spells[current_spell]
                    spells[current_spell] = spells[current_spell + 1]
                    spells[current_spell + 1] = temp
                    current_spell -= 1
                    if current_spell < 0:
                        current_spell = 0
                else:
                    current_spell += 1
        current_spell = 0
        spells_to_be_removed = []
        spells_played = []
        while current_spell < len(spells):
            if spells[current_spell].is_playable(available_mana):
                available_mana -= spells[current_spell].get_card_info()["cost"]
                spells_to_be_removed.append(current_spell)
                damage += spells[current_spell].get_card_info()["cost"]
            current_spell += 1
        removed_card_index = len(spells_to_be_removed) - 1
        while removed_card_index >= 0:
            spells_played.append(
                spells.pop(spells_to_be_removed[removed_card_index]).name)
            removed_card_index -= 1
        current_spell = 0
        while current_spell < len(spells_played):
            cards_played.append(spells_played[current_spell])
            current_spell += 1
        artifacts = []
        for card in hand:
            if isinstance(card, ArtifactCard):
                artifacts.append(card)
        if len(artifacts) > 0:
            current_artifacts = 0
            while current_artifacts < len(artifacts) - 1:
                if (artifacts[current_artifacts].cost >
                        artifacts[current_artifacts + 1].cost):
                    temp = artifacts[current_artifacts]
                    artifacts[current_artifacts] = (
                        artifacts[current_artifacts + 1])
                    artifacts[current_artifacts + 1] = temp
                    current_artifacts -= 1
                    if current_artifacts < 0:
                        current_artifacts = 0
                else:
                    current_artifacts += 1
        current_artifacts = 0
        artifacts_to_be_removed = []
        artifacts_played = []
        while current_artifacts < len(artifacts):
            if artifacts[current_artifacts].is_playable(available_mana):
                available_mana -= (
                    artifacts[current_artifacts].get_card_info()["cost"])
                artifacts_to_be_removed.append(current_artifacts)
                damage += artifacts[current_artifacts].get_card_info()["cost"]
            current_artifacts += 1
        removed_card_index = len(artifacts_to_be_removed) - 1
        while removed_card_index >= 0:
            artifacts_played.append(artifacts.pop(
                artifacts_to_be_removed[removed_card_index]).name)
            removed_card_index -= 1
        current_artifacts = 0
        while current_artifacts < len(artifacts_played):
            cards_played.append(artifacts_played[current_artifacts])
            current_artifacts += 1
        return {
            "cards_played": cards_played,
            "mana_used": max_mana - available_mana,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        targets = []
        current_target = 0
        for target in available_targets:
            if isinstance(target, CreatureCard):
                targets.append(target)
        while current_target < len(targets) - 1:
            if targets[current_target].cost > targets[current_target + 1].cost:
                temp = targets[current_target]
                targets[current_target] = targets[current_target + 1]
                targets[current_target + 1] = temp
                current_target -= 1
                if current_target < 0:
                    current_target = 0
            else:
                current_target += 1
        targets.append("Enemy Player")
        return targets
