# engine/gameState.py

from typing import Dict, List


class GameState:
    """
    GameState holds EVERYTHING about the current D&D session:
    players, NPCs, world info, turn order, etc.
    """

    def __init__(self):
        # player_id -> character data
        self.players: Dict[str, dict] = {}

        # npc_id -> npc data
        self.npcs: Dict[str, dict] = {}

        # world state
        self.world = {
            "location": "starting_village",
            "time": "day",
            "weather": "clear"
        }

        # turn-based system
        self.turn_order: List[str] = []
        self.active_turn_index: int = 0

    # --------------------
    # PLAYER MANAGEMENT
    # --------------------

    def add_player(self, player_id: str, character_data: dict):
        """
        Add a player to the game.
        """
        self.players[player_id] = character_data

        if player_id not in self.turn_order:
            self.turn_order.append(player_id)

    def remove_player(self, player_id: str):
        """
        Remove a player from the game.
        """
        if player_id in self.players:
            del self.players[player_id]

        if player_id in self.turn_order:
            self.turn_order.remove(player_id)

    # --------------------
    # TURN SYSTEM
    # --------------------

    def get_active_player(self):
        """
        Returns whose turn it currently is.
        """
        if not self.turn_order:
            return None

        return self.turn_order[self.active_turn_index]

    def next_turn(self):
        """
        Move to the next player's turn.
        """
        if not self.turn_order:
            return None

        self.active_turn_index = (self.active_turn_index + 1) % len(self.turn_order)
        return self.get_active_player()

    # --------------------
    # DEBUG / DISPLAY
    # --------------------

    def summary(self):
        """
        Return a quick summary of the game state.
        """
        return {
            "players": list(self.players.keys()),
            "location": self.world["location"],
            "time": self.world["time"],
            "active_turn": self.get_active_player()
        }
    def set_turn_order(self, order):
     self.turn_order = order
     self.active_turn_index = 0
