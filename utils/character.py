# utils/character.py

from engine.stats import Stats
from game.dice import roll


class Character:
    def __init__(self, name: str, stats: Stats, hp: int):
        self.name = name
        self.stats = stats
        self.max_hp = hp
        self.current_hp = hp
        self.armor_class = 10 + self.stats.dex_mod
        self.dead = False

    def ability_check(self, ability: str) -> int:
        d20 = roll(20)

        if ability == "str":
            return d20 + self.stats.str_mod
        if ability == "dex":
            return d20 + self.stats.dex_mod
        if ability == "con":
            return d20 + self.stats.con_mod
        if ability == "int":
            return d20 + self.stats.int_mod
        if ability == "wis":
            return d20 + self.stats.wis_mod
        if ability == "cha":
            return d20 + self.stats.cha_mod

        raise ValueError("Invalid ability")

    # REPLACE take_damage
    def take_damage(self, damage: int):
        self.current_hp -= damage
        if self.current_hp <= 0:
            self.current_hp = 0
            self.dead = True


    def is_alive(self):
     return not self.dead

