# game/dice.py

import random


def roll(sides: int) -> int:
    """
    Roll a single die with given number of sides.
    Example: roll(20) -> d20
    """
    return random.randint(1, sides)


def roll_multiple(count: int, sides: int) -> int:
    """
    Roll multiple dice and sum them.
    Example: 2d6
    """
    return sum(roll(sides) for _ in range(count))
