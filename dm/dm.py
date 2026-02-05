# dm/dm.py

class DungeonMaster:
    def __init__(self, game_state):
        self.game_state = game_state

    def narrate(self, text: str):
        """
        Simple placeholder DM narration.
        Later we can replace this with AI (Ollama / OpenAI).
        """
        print(f"\n[DM]: {text}\n")

    def describe_world(self):
        world = self.game_state.world
        return f"You are in {world['location']}. It is {world['time']}."
