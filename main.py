from engine.stats import Stats
from utils.character import Character
from engine.gameState import GameState
from engine.world_loader import load_world, load_npcs
from dm.dm import DungeonMaster
from engine.intent import parse_intent
from engine.resolution import resolve_intent

# --------------------
# GAME SETUP
# --------------------

game = GameState()
dm = DungeonMaster(game, model="phi3")

stats = Stats(14, 16, 12, 10, 10, 11)
player = Character("Hero", stats, 20)
game.add_player("player1", player)

load_world(game, "world.json")
load_npcs(game, "goblin.json")

# --------------------
# GAME START
# --------------------

print("\n[DM]:")
print(dm.introduce_scene())

# --------------------
# MAIN LOOP
# --------------------

while True:
    user_input = input("\n> ")

    if user_input.lower() in ("exit", "quit"):
        print("\n[DM]: The world fades as your journey pauses.")
        break

    intent = parse_intent(user_input)
    resolution = resolve_intent(intent, player)

    print("\n[DM]:")
    print(dm.narrate_resolution(resolution))
