# resolution.py


from engine.intent import ActionIntent


def resolve_intent(intent: ActionIntent, character):
    """
    Resolves an intent using game rules.
    Returns a structured result.
    """

    if intent.type == "ability_check":
        roll = character.ability_check(intent.ability)

        # Temporary static difficulty (we'll improve later)
        difficulty = 12
        success = roll >= difficulty

        return {
            "type": "ability_check",
            "ability": intent.ability,
            "roll": roll,
            "difficulty": difficulty,
            "success": success,
            "description": intent.description
        }

    if intent.type == "attack":
        return {
            "type": "attack",
            "note": "Combat system not implemented yet."
        }

    return {
        "type": "unknown",
        "note": "The action could not be interpreted."
    }
