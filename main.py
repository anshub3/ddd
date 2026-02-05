import ollama
import json

from engine.stats import Stats
from utils.character import Character
from engine.gameState import GameState
from engine.world_loader import load_world, load_npcs
from dm.dm import DungeonMaster

MODEL = "phi3"


def ai_scene_intro(game: GameState):
    """
    Strict world introduction.
    AI is NOT allowed to invent anything.
    """

    world = json.dumps(game.world, indent=2)
    npcs = json.dumps(game.npcs, indent=2)

    prompt = f"""
You are a Dungeon Master AI.

STRICT RULES:
- Use ONLY the information provided.
- Do NOT invent locations, paths, doors, shrines, enemies, or lore.
- Do NOT add NPC stats unless explicitly listed.
- Do NOT name the scene or add a title.
- Describe ONLY what the player can immediately observe.

WORLD DATA (authoritative):
{world}

NPC DATA (authoritative):
{npcs}

Write a short, grounded description (3–5 sentences).
"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.2}
    )

    return response["message"]["content"]


def ai_player_action(game: GameState, player_input: str):
    """
    React-only DM response.
    """

    world = json.dumps(game.world, indent=2)
    npcs = json.dumps(game.npcs, indent=2)

    prompt = f"""
You are a Dungeon Master AI.

STRICT RULES:
- React ONLY to the player action.
- Use ONLY provided world + NPC data.
- Do NOT invent new locations or NPCs.
- If an action is impossible, say so.
- End with a question asking what the player does next.

WORLD DATA:
{world}

NPC DATA:
{npcs}

PLAYER ACTION:
"{player_input}"
"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.3}
    )

    return response["message"]["content"]


# --------------------
# GAME SETUP
# --------------------

game = GameState()
dm = DungeonMaster(game)

stats1 = Stats(14, 16, 12, 10, 10, 11)
player = Character("Hero", stats1, 20)

game.add_player("player1", player)

load_world(game, "world.json")
load_npcs(game, "goblin.json")

# --------------------
# GAME START
# --------------------

print("\n[DM]:")
print(ai_scene_intro(game))

# --------------------
# MAIN LOOP
# --------------------

while True:
    user_input = input("\n> ")

    if user_input.lower() in ("exit", "quit"):
        print("\n[DM]: The world fades as your journey pauses.")
        break

    print("\n[DM]:")
    print(ai_player_action(game, user_input))
