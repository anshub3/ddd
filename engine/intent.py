# engine/intent.py


from dataclasses import dataclass
from typing import Optional


@dataclass
class ActionIntent:
    """
    Structured representation of what the player wants to do.
    """
    type: str                   # e.g. "ability_check", "attack", "observe"
    ability: Optional[str]      # str, dex, wis, etc.
    description: str            # cleaned natural-language intent



def parse_intent(player_input: str) -> ActionIntent:
    """
    Converts raw player input into a structured ActionIntent.
    This is deliberately simple and deterministic.
    """

    text = player_input.lower()

    # ---- Stealth / Sneak ----
    if any(word in text for word in ["sneak", "stealth", "hide", "creep"]):
        return ActionIntent(
            type="ability_check",
            ability="dex",
            description="attempt to move stealthily"
        )

    # ---- Perception / Observe ----
    if any(word in text for word in ["look", "observe", "inspect", "search", "listen"]):
        return ActionIntent(
            type="ability_check",
            ability="wis",
            description="attempt to observe surroundings"
        )

    # ---- Strength / Force ----
    if any(word in text for word in ["push", "break", "force", "lift"]):
        return ActionIntent(
            type="ability_check",
            ability="str",
            description="attempt to use physical strength"
        )

    # ---- Attack (placeholder for later combat system) ----
    if any(word in text for word in ["attack", "hit", "strike", "stab"]):
        return ActionIntent(
            type="attack",
            ability="str",
            description="attempt to attack"
        )

    # ---- Fallback ----
    return ActionIntent(
        type="unknown",
        ability=None,
        description=player_input
    )
