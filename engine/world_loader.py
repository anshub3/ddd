# engine/world_loader.py

import json
import os

WORLD_DIR = "data/world"
NPC_DIR = "data/npcs"


def load_world(game_state, filename: str):
    with open(os.path.join(WORLD_DIR, filename), "r") as f:
        game_state.world = json.load(f)


def load_npcs(game_state, filename: str):
    with open(os.path.join(NPC_DIR, filename), "r") as f:
        game_state.npcs = json.load(f)
