import json
from dm.llm import generate
from dm.prompt import DM_SYSTEM_PROMPT


class DungeonMaster:
    def __init__(self, game_state, model="phi3"):
        self.game = game_state
        self.model = model

    def _world_context(self):
        return f"""
WORLD DATA (authoritative):
{json.dumps(self.game.world, indent=2)}

NPC DATA (authoritative):
{json.dumps(self.game.npcs, indent=2)}
"""

    def _compose_prompt(self, content: str) -> str:
        """
        Combines system rules + dynamic content.
        """
        return f"""
{DM_SYSTEM_PROMPT}

{self._world_context()}

{content}
"""

    def introduce_scene(self):
        content = """
SYSTEM INSTRUCTION:
Describe the opening scene using ONLY the world and NPC data.
The player has not taken any action yet.
"""
        prompt = self._compose_prompt(content)
        return generate(self.model, prompt, temperature=0.2)

    def narrate_resolution(self, resolution: dict):
        content = f"""
SYSTEM-RESOLVED ACTION (authoritative):
{json.dumps(resolution, indent=2)}

Narrate what happens based ONLY on the above result.
If success is false, describe failure.
If success is true, describe success.
Do NOT invent mechanics or facts.
"""
        prompt = self._compose_prompt(content)
        return generate(self.model, prompt, temperature=0.4)
